#!/usr/bin/env python3
"""Snapshot, restore and verify Adult-group rows in International-Playlist.m3u."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

PLAYLIST = Path("International-Playlist.m3u")
SNAPSHOT = Path("/tmp/bdix-iptv-international-adult.json")
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
AFTER_ADULT = {"review", "new channels", "new backups", "backup"}


def parse_playlist(text: str):
    preamble = []
    records = []
    current = None
    for line in text.replace("\r\n", "\n").replace("\r", "\n").splitlines():
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


def attrs(info: str):
    return dict(ATTR_RE.findall(info))


def group_of(record):
    return attrs(record[0]).get("group-title", "").strip()


def url_of(record):
    return next((line.strip() for line in record[1:] if line.strip().startswith(("http://", "https://"))), "")


def _serialized_digest(blocks):
    payload = json.dumps(blocks, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def snapshot(playlist: Path = PLAYLIST, snapshot_path: Path = SNAPSHOT):
    if not playlist.is_file():
        raise SystemExit(f"ERROR: missing playlist: {playlist}")
    _, records = parse_playlist(playlist.read_text(encoding="utf-8-sig"))
    adult = [record for record in records if group_of(record).casefold() == "adult"]
    data = {
        "version": 1,
        "count": len(adult),
        "sha256": _serialized_digest(adult),
        "blocks": adult,
    }
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Adult snapshot saved: {len(adult)} exact records ({data['sha256']}).")
    return data


def _load_snapshot(snapshot_path):
    try:
        data = json.loads(snapshot_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SystemExit(f"ERROR: Adult snapshot cannot be read: {exc}") from exc
    blocks = data.get("blocks")
    if data.get("version") != 1 or not isinstance(blocks, list):
        raise SystemExit("ERROR: unsupported or malformed Adult snapshot.")
    if len(blocks) != data.get("count") or _serialized_digest(blocks) != data.get("sha256"):
        raise SystemExit("ERROR: Adult snapshot integrity check failed.")
    return blocks


def _restore_category_registry(preamble):
    prefix = "#PLAYLIST-STUDIO-CATEGORIES:"
    for index, line in enumerate(preamble):
        if not line.startswith(prefix):
            continue
        try:
            categories = json.loads(line[len(prefix):])
        except ValueError as exc:
            raise SystemExit("ERROR: malformed Playlist Studio category registry.") from exc
        if not isinstance(categories, list):
            raise SystemExit("ERROR: Playlist Studio category registry must be a list.")
        categories = [value for value in categories if value != "Adult"]
        sports = categories.index("Sports") + 1 if "Sports" in categories else len(categories)
        categories.insert(sports, "Adult")
        preamble[index] = prefix + json.dumps(categories, ensure_ascii=False)
        break
    return preamble


def verify(playlist: Path = PLAYLIST, snapshot_path: Path = SNAPSHOT):
    saved = _load_snapshot(snapshot_path)
    _, records = parse_playlist(playlist.read_text(encoding="utf-8-sig"))
    current = [record for record in records if group_of(record).casefold() == "adult"]
    if current != saved:
        raise SystemExit(
            f"ERROR: Adult records differ from their snapshot (expected {len(saved)}, found {len(current)})."
        )
    print(f"Adult preservation verified: {len(saved)} records are unchanged.")
    return True


def restore(playlist: Path = PLAYLIST, snapshot_path: Path = SNAPSHOT):
    if not playlist.is_file():
        raise SystemExit(f"ERROR: missing playlist: {playlist}")
    saved = _load_snapshot(snapshot_path)
    preamble, records = parse_playlist(playlist.read_text(encoding="utf-8-sig"))
    saved_urls = {url_of(record).casefold() for record in saved if url_of(record)}
    retained = [
        record for record in records
        if group_of(record).casefold() != "adult"
        and url_of(record).casefold() not in saved_urls
    ]
    insert_at = next(
        (index for index, record in enumerate(retained) if group_of(record).casefold() in AFTER_ADULT),
        len(retained),
    )
    retained[insert_at:insert_at] = saved
    preamble = _restore_category_registry(preamble)
    playlist.write_text(
        "\n".join(preamble + [line for record in retained for line in record]) + "\n",
        encoding="utf-8",
    )
    return verify(playlist, snapshot_path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("snapshot", "restore", "verify"))
    parser.add_argument("--playlist", type=Path, default=PLAYLIST)
    parser.add_argument("--snapshot", type=Path, default=SNAPSHOT)
    args = parser.parse_args()
    if args.action == "snapshot":
        snapshot(args.playlist, args.snapshot)
    elif args.action == "restore":
        restore(args.playlist, args.snapshot)
    else:
        verify(args.playlist, args.snapshot)


if __name__ == "__main__":
    main()
