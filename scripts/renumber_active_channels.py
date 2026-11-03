#!/usr/bin/env python3
"""Sort active IPTV groups and assign contiguous channel numbers without rewriting stream URLs.

Backup, Not Playing, New Channels and New Backup remain unnumbered. Their internal
order is preserved; only their category blocks are placed in canonical queue order.
"""
from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

CATEGORY_ORDER = [
    "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
    "Indian Entertainment", "Pakistani", "International",
    "Documentary & Wildlife", "Kids", "Religious", "Sports",
    "Not Playing", "New Channels", "New Backup", "Backup",
]
CATEGORY_RANK = {name: index for index, name in enumerate(CATEGORY_ORDER)}
REVIEW_GROUPS = {"Backup", "Not Playing", "New Channels", "New Backup"}
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')


def attrs(info: str) -> dict[str, str]:
    return dict(ATTR_RE.findall(info))


def natural_key(value: str):
    value = unicodedata.normalize("NFKD", str(value or "")).casefold().strip()
    return tuple(int(part) if part.isdigit() else part for part in re.split(r"(\d+)", value))


def display_name(record: list[str]) -> str:
    metadata = attrs(record[0])
    return metadata.get("tvg-name", "").strip() or record[0].rsplit(",", 1)[-1].strip()


def stream_url(record: list[str]) -> str:
    return next((line.strip() for line in record[1:] if line.strip().startswith(("http://", "https://"))), "")


def set_channel_number(info: str, number: int) -> str:
    replacement = f'tvg-chno="{number}"'
    if re.search(r'\s+tvg-chno="[^"]*"', info):
        return re.sub(r'\s+tvg-chno="[^"]*"', " " + replacement, info, count=1)
    match = re.search(r'\s+group-title="', info)
    if match:
        return info[:match.start()] + " " + replacement + info[match.start():]
    comma = info.find(",")
    if comma >= 0:
        return info[:comma] + " " + replacement + info[comma:]
    raise ValueError(f"Cannot insert tvg-chno into malformed EXTINF: {info[:120]}")


def remove_channel_number(info: str) -> str:
    return re.sub(r'\s+tvg-chno="[^"]*"', "", info, count=1)


def parse_records(text: str):
    lines = text.splitlines()
    preamble: list[str] = []
    records: list[list[str]] = []
    current: list[str] | None = None
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
    return preamble, records


def url_inventory(records: list[list[str]]) -> list[str]:
    return [url for url in (stream_url(record) for record in records) if url]


def normalize_playlist_text(text: str) -> tuple[str, int]:
    newline = "\r\n" if "\r\n" in text else "\n"
    had_final_newline = text.endswith(("\n", "\r"))
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    preamble, records = parse_records(normalized)
    original_urls = url_inventory(records)
    primary = []
    review = []
    for record in records:
        group = attrs(record[0]).get("group-title", "").strip()
        if group in REVIEW_GROUPS:
            review.append(record)
        else:
            if group not in CATEGORY_RANK:
                raise ValueError(f"Unknown IPTV category; refusing to reorder: {group!r}")
            primary.append(record)

    primary.sort(key=lambda record: (
        CATEGORY_RANK[attrs(record[0]).get("group-title", "").strip()],
        natural_key(display_name(record)),
        stream_url(record).casefold(),
    ))
    # Stable sort moves review queues into canonical block order but preserves
    # each queue's original record order for manual review.
    review.sort(key=lambda record: CATEGORY_RANK[attrs(record[0]).get("group-title", "").strip()])

    for number, record in enumerate(primary, start=1):
        record[0] = set_channel_number(record[0], number)
    for record in review:
        record[0] = remove_channel_number(record[0])

    ordered = primary + review
    if sorted(url_inventory(ordered)) != sorted(original_urls):
        raise ValueError("Stream URL inventory changed during primary ordering/numbering.")
    result = newline.join(preamble + [line for record in ordered for line in record])
    if had_final_newline:
        result += newline
    return result, len(primary)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("playlist", nargs="?", default="IPTV-Playlist.m3u")
    parser.add_argument("--check", action="store_true", help="fail if the playlist is not already canonical")
    args = parser.parse_args()
    path = Path(args.playlist)
    if not path.is_file():
        raise SystemExit(f"Playlist not found: {path}")
    before = path.read_text(encoding="utf-8-sig")
    after, count = normalize_playlist_text(before)
    if args.check:
        if after != before:
            raise SystemExit("Active playlist order/channel numbers are not canonical.")
        print(f"OK: {count} active channels are sorted and numbered contiguously.")
        return 0
    if after != before:
        path.write_text(after, encoding="utf-8", newline="")
        print(f"Normalized {count} active channels; stream URLs and review-queue order were preserved.")
    else:
        print(f"No changes needed: {count} active channels are already canonical.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
