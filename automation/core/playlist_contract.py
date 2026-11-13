"""Pure, side-effect-free playlist invariants for Automation V2."""
from __future__ import annotations
import re
from collections import Counter
from dataclasses import dataclass

ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')

@dataclass(frozen=True)
class PlaylistRow:
    url: str
    group: str
    channel_number: str
    extinf: str

def parse_rows(text: str) -> list[PlaylistRow]:
    rows = []
    current = None
    for raw in text.replace("\r", "").splitlines():
        line = raw.strip()
        if line.startswith("#EXTINF:"):
            if current is not None:
                raise ValueError("EXTINF record has no stream URL")
            current = line
        elif current is not None and line.startswith(("http://", "https://")):
            attrs = dict(ATTR_RE.findall(current))
            rows.append(PlaylistRow(line, attrs.get("group-title", ""), attrs.get("tvg-chno", ""), current))
            current = None
    if current is not None:
        raise ValueError("Final EXTINF record has no stream URL")
    return rows

def assert_iptv_existing_rows_preserved(before: str, after: str) -> None:
    """Reject loss, duplication, reordering, regrouping or renumbering of old rows."""
    old, new = parse_rows(before), parse_rows(after)
    old_urls = [r.url for r in old]
    old_counts, new_counts = Counter(old_urls), Counter(r.url for r in new)
    missing = old_counts - new_counts
    if missing:
        raise ValueError(f"Existing IPTV stream URL occurrences removed: {sum(missing.values())}")
    if [row.url for row in new[:len(old)]] != old_urls:
        raise ValueError("Existing IPTV rows were reordered or displaced; they must remain an unchanged prefix and new rows append only")
    for index, (old_row, new_row) in enumerate(zip(old, new[:len(old)]), 1):
        if old_row.group != new_row.group:
            raise ValueError(f"Existing IPTV group changed for stream occurrence {index}")
        if old_row.channel_number != new_row.channel_number:
            raise ValueError(f"Existing IPTV channel number changed for stream occurrence {index}")

def validate_discovery_queues(text: str) -> None:
    hidden = {"new channels", "new backups"}
    if any(row.group.casefold() in hidden for row in parse_rows(text)):
        raise ValueError("Discovery queue rows must be excluded from Xtream publication")
