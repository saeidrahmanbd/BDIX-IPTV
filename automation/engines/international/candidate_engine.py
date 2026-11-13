"""International playlist candidate group mover; no deletion, file writes or publication."""
from __future__ import annotations
import re
from dataclasses import dataclass
from automation.core.playlist_contract import parse_rows, ATTR_RE
from automation.engines.iptv.candidate_engine import DiscoveryCandidate

GROUP_RE = re.compile(r'(\bgroup-title=")[^"]*(")')

@dataclass(frozen=True)
class GroupChange:
    row_index: int
    target_group: str
    reason: str

def _replace_group(extinf_line: str, target: str) -> str:
    if not GROUP_RE.search(extinf_line):
        raise ValueError("International row has no group-title attribute")
    return GROUP_RE.sub(lambda match: match.group(1) + target + match.group(2), extinf_line, count=1)

def assert_international_rows_preserved(before: str, after: str) -> None:
    old_rows, new_rows = parse_rows(before), parse_rows(after)
    if len(old_rows) != len(new_rows):
        raise ValueError("International candidate changed the number of stream rows")
    for index, (old, new) in enumerate(zip(old_rows, new_rows)):
        if old.url != new.url:
            raise ValueError(f"International stream row reordered or URL changed at row {index}")
        if old.channel_number != new.channel_number:
            raise ValueError(f"International channel number changed at row {index}")
        if _replace_group(old.extinf, new.group) != new.extinf:
            raise ValueError(f"International metadata changed beyond group-title at row {index}")

def build_candidate(baseline_text: str, changes: list[GroupChange]) -> str:
    """Apply explicit group-only changes by parsed row index; all stream rows remain present."""
    if not baseline_text.lstrip("\ufeff").startswith("#EXTM3U"):
        raise ValueError("baseline must have an #EXTM3U header")
    rows = parse_rows(baseline_text)
    by_index: dict[int, str] = {}
    for change in changes:
        if change.row_index < 0 or change.row_index >= len(rows):
            raise ValueError(f"row index out of range: {change.row_index}")
        if not change.target_group.strip() or '"' in change.target_group or "\n" in change.target_group or "\r" in change.target_group:
            raise ValueError("target group must be a non-empty single line")
        if change.row_index in by_index:
            raise ValueError(f"duplicate group change for row: {change.row_index}")
        by_index[change.row_index] = change.target_group.strip()
    if not by_index:
        return baseline_text

    output: list[str] = []
    extinf_index = 0
    for line in baseline_text.splitlines(keepends=True):
        if line.lstrip().startswith("#EXTINF:"):
            if extinf_index in by_index:
                ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
                body = line[:-len(ending)] if ending else line
                output.append(_replace_group(body, by_index[extinf_index]) + ending)
            else:
                output.append(line)
            extinf_index += 1
        else:
            output.append(line)
    candidate = "".join(output)
    assert_international_rows_preserved(baseline_text, candidate)
    return candidate


CATEGORY_ORDER = [
    "Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment",
    "Pakistani","International","Documentary & Wildlife","Kids","Religious","Sports",
    "Backup","New Channels","New Backups","Review",
]

def assert_international_existing_rows_preserved(before: str, after: str) -> None:
    """All prior rows must remain byte-identical and in the same relative order."""
    old_rows,new_rows=parse_rows(before),parse_rows(after)
    old_signatures=[(row.extinf,row.url) for row in old_rows]
    remaining={}
    for signature in old_signatures:
        remaining[signature]=remaining.get(signature,0)+1
    preserved=[]
    for row in new_rows:
        signature=(row.extinf,row.url)
        if remaining.get(signature,0):
            preserved.append(signature)
            remaining[signature]-=1
        else:
            group=dict(ATTR_RE.findall(row.extinf)).get("group-title","").strip()
            if group not in {"New Channels","New Backups"}:
                raise ValueError("International candidate added a row outside manual-review queues")
    if preserved != old_signatures or any(remaining.values()):
        raise ValueError("International candidate changed or reordered an existing row")

def append_discovery_candidates(playlist_text: str,
                                discoveries: list[DiscoveryCandidate]) -> str:
    """Insert new discovery rows into their queue blocks without rewriting existing rows."""
    if not discoveries:
        return playlist_text
    lines=playlist_text.replace("\r","").splitlines()
    seen_urls={row.url for row in parse_rows(playlist_text)}
    additions={"New Channels":[],"New Backups":[]}
    for item in discoveries:
        url=item.url.strip()
        extinf=item.extinf.strip()
        if not url.startswith(("http://","https://")):
            raise ValueError("discovery URL must be HTTP(S)")
        if not extinf.startswith("#EXTINF:") or "\n" in extinf or "\r" in extinf or "\n" in url or "\r" in url:
            raise ValueError("discovery record must be a valid single-line M3U pair")
        expected="New Backups" if item.backup else "New Channels"
        actual=dict(ATTR_RE.findall(extinf)).get("group-title","").strip()
        if actual != expected:
            raise ValueError(f"discovery row must be assigned to {expected}")
        if url in seen_urls:
            continue
        seen_urls.add(url)
        additions[expected].extend((extinf,url))

    rank={name:index for index,name in enumerate(CATEGORY_ORDER)}
    for group in ("New Channels","New Backups"):
        block=additions[group]
        if not block:
            continue
        matching=[i for i,line in enumerate(lines) if line.startswith("#EXTINF:") and dict(ATTR_RE.findall(line)).get("group-title","").strip()==group]
        if matching:
            last=matching[-1]
            insert_at=next((i for i in range(last+1,len(lines)) if lines[i].startswith("#EXTINF:")),len(lines))
        else:
            target_rank=rank[group]
            insert_at=next((i for i,line in enumerate(lines)
                            if line.startswith("#EXTINF:") and
                            rank.get(dict(ATTR_RE.findall(line)).get("group-title","").strip(),len(rank))>target_rank),len(lines))
        lines[insert_at:insert_at]=block
    candidate="\n".join(lines).rstrip()+"\n"
    assert_international_existing_rows_preserved(playlist_text,candidate)
    return candidate
