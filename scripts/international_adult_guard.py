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
    preamble, records, current = [], [], None
    for line in text.replace("\r\n", "\n").replace("\r", "\n").splitlines():
        if line.startswith("#EXTINF:"):
            if current is not None: records.append(current)
            current = [line]
        elif current is None: preamble.append(line)
        else: current.append(line)
    if current is not None: records.append(current)
    return preamble, records

def attrs(info: str):
    return dict(ATTR_RE.findall(info))

def group_of(record):
    return attrs(record[0]).get("group-title", "").strip()

def url_of(record):
    return next((line.strip() for line in record[1:] if line.strip().startswith(("http://", "https://"))), "")

def _digest(blocks):
    return hashlib.sha256(json.dumps(blocks, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()

def snapshot(playlist: Path = PLAYLIST, snapshot_path: Path = SNAPSHOT):
    if not playlist.is_file(): raise SystemExit(f"ERROR: missing playlist: {playlist}")
    _, records = parse_playlist(playlist.read_text(encoding="utf-8-sig"))
    adult = [r for r in records if group_of(r).casefold() == "adult"]
    data = {"version": 1, "count": len(adult), "sha256": _digest(adult), "blocks": adult}
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Adult snapshot saved: {len(adult)} exact records ({data['sha256']}).")
    return data

def _load(snapshot_path):
    try: data = json.loads(snapshot_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc: raise SystemExit(f"ERROR: Adult snapshot unreadable: {exc}") from exc
    blocks = data.get("blocks")
    if data.get("version") != 1 or not isinstance(blocks, list) or len(blocks) != data.get("count") or _digest(blocks) != data.get("sha256"):
        raise SystemExit("ERROR: Adult snapshot integrity check failed.")
    return blocks

def _registry(preamble):
    prefix = "#PLAYLIST-STUDIO-CATEGORIES:"
    for i, line in enumerate(preamble):
        if not line.startswith(prefix): continue
        try: categories = json.loads(line[len(prefix):])
        except ValueError as exc: raise SystemExit("ERROR: malformed category registry.") from exc
        if not isinstance(categories, list): raise SystemExit("ERROR: category registry must be a list.")
        categories = [x for x in categories if x != "Adult"]
        after = categories.index("Sports") + 1 if "Sports" in categories else len(categories)
        categories.insert(after, "Adult")
        preamble[i] = prefix + json.dumps(categories, ensure_ascii=False)
        break
    return preamble

def verify(playlist: Path = PLAYLIST, snapshot_path: Path = SNAPSHOT):
    saved = _load(snapshot_path)
    _, records = parse_playlist(playlist.read_text(encoding="utf-8-sig"))
    current = [r for r in records if group_of(r).casefold() == "adult"]
    if current != saved: raise SystemExit(f"ERROR: Adult records changed (expected {len(saved)}, found {len(current)}).")
    print(f"Adult preservation verified: {len(saved)} records unchanged.")
    return True

def restore(playlist: Path = PLAYLIST, snapshot_path: Path = SNAPSHOT):
    if not playlist.is_file(): raise SystemExit(f"ERROR: missing playlist: {playlist}")
    saved = _load(snapshot_path)
    preamble, records = parse_playlist(playlist.read_text(encoding="utf-8-sig"))
    saved_urls = {url_of(r).casefold() for r in saved if url_of(r)}
    retained = [r for r in records if group_of(r).casefold() != "adult" and url_of(r).casefold() not in saved_urls]
    insert = next((i for i,r in enumerate(retained) if group_of(r).casefold() in AFTER_ADULT), len(retained))
    retained[insert:insert] = saved
    playlist.write_text("\n".join(_registry(preamble) + [line for r in retained for line in r]) + "\n", encoding="utf-8")
    return verify(playlist, snapshot_path)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("snapshot", "restore", "verify"))
    parser.add_argument("--playlist", type=Path, default=PLAYLIST)
    parser.add_argument("--snapshot", type=Path, default=SNAPSHOT)
    args = parser.parse_args()
    if args.action == "snapshot": snapshot(args.playlist, args.snapshot)
    elif args.action == "restore": restore(args.playlist, args.snapshot)
    else: verify(args.playlist, args.snapshot)

if __name__ == "__main__": main()
