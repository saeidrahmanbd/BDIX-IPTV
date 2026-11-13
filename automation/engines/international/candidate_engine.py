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

def assert_international_rows_preserved(before: str, after: str,
                                        allowed_removed_identities: set[str] | tuple[str,...] = ()) -> None:
    """Preserve row order and metadata except group-title; only authorized IDs may be removed."""
    old_rows,new_rows=parse_rows(before),parse_rows(after)
    allowed={identity.strip().casefold() for identity in allowed_removed_identities}
    old_identity_counts={}
    for row in old_rows:
        identity=dict(ATTR_RE.findall(row.extinf)).get("tvg-id","").strip().casefold()
        old_identity_counts[identity]=old_identity_counts.get(identity,0)+1
    if any(old_identity_counts.get(identity,0)!=1 for identity in allowed):
        raise ValueError("removal identity must match exactly one existing International row")

    def stable_signature(row):
        return GROUP_RE.sub('group-title="__GROUP__"',row.extinf,count=1),row.url

    old_index=new_index=0
    removed_seen=set()
    while old_index < len(old_rows):
        old=old_rows[old_index]
        identity=dict(ATTR_RE.findall(old.extinf)).get("tvg-id","").strip().casefold()
        if identity in allowed:
            removed_seen.add(identity)
            old_index += 1
            continue
        if new_index >= len(new_rows) or stable_signature(old)!=stable_signature(new_rows[new_index]):
            raise ValueError(f"International candidate changed, removed or reordered an unauthorized row at index {old_index}")
        old_index += 1
        new_index += 1
    if new_index != len(new_rows):
        raise ValueError("International candidate added rows during maintenance")
    if removed_seen != allowed:
        raise ValueError("International candidate removal list does not match the removed rows")


def build_candidate(baseline_text: str, changes: list[GroupChange],
                    remove_identities: set[str] | tuple[str,...] = ()) -> str:
    """Apply group changes and policy-authorized removals; never edits files or publishes."""
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

    remove_set={identity.strip().casefold() for identity in remove_identities}
    if "" in remove_set:
        raise ValueError("removal identity is required")
    row_indexes_by_identity={}
    removed_indexes=set()
    protected_groups={"backup","backups","new channels","new backups","new backup","not playing","test"}
    for index,row in enumerate(rows):
        attrs=dict(ATTR_RE.findall(row.extinf))
        identity=(attrs.get("tvg-id") or "").strip().casefold()
        if identity:
            row_indexes_by_identity.setdefault(identity,[]).append(index)
        if identity in remove_set:
            if row.group.strip().casefold() in protected_groups:
                raise ValueError("Backup and discovery-queue rows are protected from automatic removal")
            removed_indexes.add(index)
    for identity in remove_set:
        if len(row_indexes_by_identity.get(identity,[])) != 1:
            raise ValueError("removal identity must match exactly one existing International row")
    if set(by_index).intersection(removed_indexes):
        raise ValueError("a row cannot be changed and removed in the same plan")
    if not by_index and not removed_indexes:
        return baseline_text

    output: list[str] = []
    extinf_index = 0
    skip_removed_row = False
    for line in baseline_text.splitlines(keepends=True):
        if line.lstrip().startswith("#EXTINF:"):
            current_index=extinf_index
            extinf_index += 1
            if current_index in removed_indexes:
                skip_removed_row=True
                continue
            skip_removed_row=False
            if current_index in by_index:
                ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
                body = line[:-len(ending)] if ending else line
                output.append(_replace_group(body, by_index[current_index]) + ending)
            else:
                output.append(line)
            continue
        if skip_removed_row:
            if line.strip() and not line.lstrip().startswith("#"):
                skip_removed_row=False
            continue
        output.append(line)
    candidate = "".join(output)
    assert_international_rows_preserved(baseline_text,candidate,remove_set)
    return candidate


def assert_international_existing_rows_preserved(before: str, after: str,
                                                  allowed_removed_identities: set[str] | tuple[str,...] = ()) -> None:
    """Preserve old rows in order; allow only policy-authorized removals and group-only changes."""
    old_rows,new_rows=parse_rows(before),parse_rows(after)
    allowed={identity.strip().casefold() for identity in allowed_removed_identities}
    old_identity_counts={}
    for row in old_rows:
        identity=dict(ATTR_RE.findall(row.extinf)).get("tvg-id","").strip().casefold()
        old_identity_counts[identity]=old_identity_counts.get(identity,0)+1
    if any(old_identity_counts.get(identity,0)!=1 for identity in allowed):
        raise ValueError("removal identity must match exactly one existing International row")

    def stable_signature(row):
        normalized=GROUP_RE.sub('group-title="__GROUP__"',row.extinf,count=1)
        return normalized,row.url

    old_index=0
    review_queues={"New Channels","New Backups"}
    old_urls={row.url for row in old_rows}
    new_urls=set()
    removed_seen=set()
    for row in new_rows:
        while old_index < len(old_rows):
            old_identity=dict(ATTR_RE.findall(old_rows[old_index].extinf)).get("tvg-id","").strip().casefold()
            if old_identity in allowed:
                removed_seen.add(old_identity)
                old_index += 1
            else:
                break
        if old_index < len(old_rows) and stable_signature(row)==stable_signature(old_rows[old_index]):
            old_index += 1
            continue
        if row.url in old_urls or row.url in new_urls:
            raise ValueError("International candidate duplicated or displaced an existing stream URL")
        if row.group.strip() not in review_queues:
            raise ValueError("International candidate added a row outside manual-review queues")
        new_urls.add(row.url)
    while old_index < len(old_rows):
        old_identity=dict(ATTR_RE.findall(old_rows[old_index].extinf)).get("tvg-id","").strip().casefold()
        if old_identity in allowed:
            removed_seen.add(old_identity)
            old_index += 1
        else:
            break
    if old_index != len(old_rows):
        raise ValueError("International candidate changed, removed or reordered an existing row")
    if removed_seen != allowed:
        raise ValueError("International candidate removal list does not match the removed rows")


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
