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
    """Preserve every old stream in order; group-title-only changes are permitted."""
    old_rows,new_rows=parse_rows(before),parse_rows(after)

    def stable_signature(row):
        normalized=GROUP_RE.sub('group-title="__GROUP__"',row.extinf,count=1)
        return normalized,row.url

    old_index=0
    review_queues={"New Channels","New Backups"}
    old_urls={row.url for row in old_rows}
    new_urls=set()
    for row in new_rows:
        if old_index < len(old_rows) and stable_signature(row)==stable_signature(old_rows[old_index]):
            old_index += 1
            continue
        if row.url in old_urls or row.url in new_urls:
            raise ValueError("International candidate duplicated or displaced an existing stream URL")
        if row.group.strip() not in review_queues:
            raise ValueError("International candidate added a row outside manual-review queues")
        new_urls.add(row.url)
    if old_index != len(old_rows):
        raise ValueError("International candidate changed, removed or reordered an existing row")

def append_discovery_candidates(playlist_text: str,
                                discoveries: list[DiscoveryCandidate]) -> str:
    """Insert new discovery rows into their queue blocks without rewriting existing lines."""
    if not discoveries:
        return playlist_text
    newline="\r\n" if "\r\n" in playlist_text else "\n"
    lines=playlist_text.splitlines(keepends=True)
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
        additions[expected].extend((extinf+newline,url+newline))

    rank={name:index for index,name in enumerate(CATEGORY_ORDER)}
    for group in ("New Channels","New Backups"):
        block=additions[group]
        if not block:
            continue
        extinf_indexes=[
            i for i,line in enumerate(lines)
            if line.lstrip().startswith("#EXTINF:") and
            dict(ATTR_RE.findall(line.rstrip("\r\n"))).get("group-title","").strip()==group
        ]
        if extinf_indexes:
            last=extinf_indexes[-1]
            insert_at=next((i for i in range(last+1,len(lines))
                            if lines[i].lstrip().startswith("#EXTINF:")),len(lines))
        else:
            target_rank=rank[group]
            insert_at=next((i for i,line in enumerate(lines)
                            if line.lstrip().startswith("#EXTINF:") and
                            rank.get(dict(ATTR_RE.findall(line.rstrip("\r\n"))).get("group-title","").strip(),len(rank))>target_rank),len(lines))
        if insert_at==len(lines) and lines and not lines[-1].endswith(("\n","\r")):
            lines[-1]=lines[-1]+newline
        lines[insert_at:insert_at]=block
    candidate="".join(lines)
    assert_international_existing_rows_preserved(playlist_text,candidate)
    return candidate
