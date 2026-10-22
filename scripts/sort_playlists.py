#!/usr/bin/env python3
"""Canonicalize and sort the selected playlist by category and natural A–Z name."""
from pathlib import Path
import re
import sys
import unicodedata

CATEGORY_ORDER = [
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
    "New Channels", "New Backup", "Backup", "Not Playing",
]
RANK = {name: index for index, name in enumerate(CATEGORY_ORDER)}
NON_NUMBERED = {"Backup", "Not Playing", "New Channels", "New Backup"}
ATTRIBUTE_ORDER = (
    "tvg-id", "tvg-name", "tvg-logo", "tvg-chno",
    "channel-id", "tvg-country", "tvg-language", "group-title",
)
ATTR = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')


def natural_key(value):
    value = unicodedata.normalize("NFKD", str(value or "")).casefold().strip()
    return tuple(int(part) if part.isdigit() else part for part in re.split(r"(\d+)", value))


def attrs(info):
    return dict(ATTR.findall(info))


def split_head_display(info):
    quoted = False
    for index, char in enumerate(info):
        if char == '"':
            quoted = not quoted
        elif char == "," and not quoted:
            return info[:index], info[index:]
    return info, ""


def canonical_extinf(info):
    head, display = split_head_display(info)
    duration = re.match(r"^#EXTINF:\S+", head)
    if not duration:
        return info
    matches = list(ATTR.finditer(head))
    if not matches:
        return info
    rank = {key: index for index, key in enumerate(ATTRIBUTE_ORDER)}
    pairs = [(match.group(1), match.group(2), index) for index, match in enumerate(matches)]
    pairs.sort(key=lambda item: (rank.get(item[0], len(rank)), item[2]))
    return duration.group(0) + " " + " ".join(f'{key}="{value}"' for key, value, _ in pairs) + display


def set_attr(info, key, value):
    pattern = re.compile(rf'{re.escape(key)}="[^"]*"')
    if pattern.search(info):
        return pattern.sub(f'{key}="{value}"', info, count=1)
    return re.sub(r"^(#EXTINF:\S+)", rf'\1 {key}="{value}"', info, count=1)


def remove_attr(info, key):
    return re.sub(rf'\s+{re.escape(key)}="[^"]*"', "", info, count=1)


def record_name(record):
    a = attrs(record[0])
    if a.get("tvg-name", "").strip():
        return a["tvg-name"].strip()
    _, display = split_head_display(record[0])
    return display.lstrip(",").strip()


def record_url(record):
    return next((line.strip() for line in record[1:] if line.strip().startswith(("http://", "https://"))), "")


def record_key(record):
    a = attrs(record[0])
    group = a.get("group-title", "").strip()
    return (RANK.get(group, len(RANK)), natural_key(record_name(record)), record_url(record).casefold())


def sort_playlist(path):
    if not path.is_file():
        raise SystemExit(f"Playlist not found: {path}")
    lines = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").splitlines()
    preamble, records = [], []
    current = None
    for line in lines:
        if line.startswith("#EXTINF:"):
            if current is not None:
                records.append(current)
            current = [line]
        elif current is None:
            preamble.append(line)
        else:
            current.append(line)
    if current is not None:
        records.append(current)

    records.sort(key=record_key)
    next_number = 1
    for record in records:
        record[0] = canonical_extinf(record[0])
        group = attrs(record[0]).get("group-title", "").strip()
        if path.name == "IPTV-Playlist.m3u":
            if group in NON_NUMBERED:
                record[0] = remove_attr(record[0], "tvg-chno")
            elif group not in {"Sports"}:
                record[0] = set_attr(record[0], "tvg-chno", str(next_number))
                next_number += 1
    path.write_text("\n".join(preamble + [line for record in records for line in record]) + "\n", encoding="utf-8")


paths = sys.argv[1:] or ["IPTV-Playlist.m3u", "BDIX-Playlist.m3u", "International-Playlist.m3u"]
for raw in paths:
    sort_playlist(Path(raw))
