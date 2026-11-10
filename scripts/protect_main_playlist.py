#!/usr/bin/env python3
"""Protect existing IPTV-Playlist.m3u rows from automated deletion or relocation.

Metadata and logo edits are allowed. Existing stream URLs must remain present,
retain their original group, and preserve their relative playlist order.
Newly discovered rows may be added without disturbing existing rows.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

def records(path: Path):
    result = []
    current = None
    for line in path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").splitlines():
        if line.startswith("#EXTINF:"):
            if current is not None:
                result.append(current)
            current = {"info": line, "url": ""}
        elif current is not None and line.strip().lower().startswith(("http://", "https://")) and not current["url"]:
            current["url"] = line.strip()
    if current is not None:
        result.append(current)
    return [r for r in result if r["url"]]

def group(info: str) -> str:
    import re
    match = re.search(r'\bgroup-title="([^"]*)"', info)
    return match.group(1) if match else ""

def snapshot(playlist: Path, state: Path):
    rows = [{"url": r["url"], "group": group(r["info"])} for r in records(playlist)]
    state.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Protected {len(rows)} existing IPTV stream rows.")

def verify(playlist: Path, state: Path):
    before = json.loads(state.read_text(encoding="utf-8"))
    after = records(playlist)
    cursor = 0
    errors = []
    for old in before:
        found = None
        for index in range(cursor, len(after)):
            if after[index]["url"] == old["url"]:
                found = index
                break
        if found is None:
            errors.append(f"Existing stream deleted or URL changed: {old['url']}")
            continue
        actual_group = group(after[found]["info"])
        if actual_group != old["group"]:
            errors.append(f"Existing stream moved from group {old['group']!r} to {actual_group!r}: {old['url']}")
        cursor = found + 1
    if errors:
        for error in errors:
            print(f"::error::{error}")
        raise SystemExit(f"IPTV-Playlist.m3u protection failed: {len(errors)} violation(s); refusing to publish.")
    print(f"IPTV protection passed: all {len(before)} existing stream rows retained in their original groups and relative order.")

def main():
    if len(sys.argv) != 4 or sys.argv[1] not in {"snapshot", "verify"}:
        raise SystemExit("Usage: protect_main_playlist.py snapshot|verify PLAYLIST STATE.json")
    action, playlist, state = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    snapshot(playlist, state) if action == "snapshot" else verify(playlist, state)

if __name__ == "__main__":
    main()
