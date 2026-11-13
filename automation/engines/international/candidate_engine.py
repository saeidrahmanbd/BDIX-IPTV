"""International playlist candidate group mover; no deletion, file writes or publication."""
from __future__ import annotations
import re
from dataclasses import dataclass
from automation.core.playlist_contract import parse_rows

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
        if not change.target_group.strip() or "\n" in change.target_group or "\r" in change.target_group:
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
