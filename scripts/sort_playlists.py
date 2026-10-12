#!/usr/bin/env python3
"""Sort maintained M3U playlists by canonical group order and A–Z channel name."""
from pathlib import Path
import re
import unicodedata

PLAYLISTS = (Path("IPTV-Playlist.m3u"), Path("BDIX-Playlist.m3u"))
CATEGORY_ORDER = [
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports", "Backup",
    "New Channels", "New Backup", "Not Playing",
]
RANK = {name: i for i, name in enumerate(CATEGORY_ORDER)}
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')


def natural_key(value):
    value = unicodedata.normalize("NFKD", str(value or "")).casefold().strip()
    return tuple(int(p) if p.isdigit() else p for p in re.split(r"(\d+)", value))


def record_key(record):
    info = record[0]
    attrs = dict(ATTR.findall(info))
    name = (attrs.get("tvg-name") or info.rsplit(",", 1)[-1]).strip()
    group = attrs.get("group-title", "").strip()
    url = next((x.strip() for x in record[1:] if x.strip().startswith(("http://", "https://"))), "")
    return (RANK.get(group, len(RANK)), natural_key(name), url.casefold())


def sort_playlist(path):
    if not path.is_file():
        print(f"SKIP {path}: file not present")
        return
    lines = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").splitlines()
    preamble, records, current = [], [], None
    for line in lines:
        if line.startswith("#EXTINF:"):
            if current is not None:
                records.append(current)
            current = [line]
        elif current is not None:
            current.append(line)
        else:
            preamble.append(line)
    if current is not None:
        records.append(current)
    records.sort(key=record_key)
    path.write_text("\n".join(preamble + [line for rec in records for line in rec]) + "\n", encoding="utf-8")
    print(f"SORTED {path}: {len(records)} records; canonical category order and A–Z within each category")


if __name__ == "__main__":
    for playlist in PLAYLISTS:
        sort_playlist(playlist)
