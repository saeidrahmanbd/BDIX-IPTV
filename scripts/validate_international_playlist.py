#!/usr/bin/env python3
"""Validate International playlist structure, attribution, categories and local logo paths."""
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re

PLAYLIST = Path("International-Playlist.m3u")
LOGOS = Path("logos")
RAW_BASE = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/"
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
FIXED = ["Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment", "Pakistani"]
TAIL = ["Adult", "International", "Documentary & Wildlife", "Kids", "Religious", "Sports", "Backup"]
FORBIDDEN = {"new channels", "new backup", "not playing", "international movies", "international music", "test"}
ATTRIBUTION = [
    "#=================================",
    "# Developed by: SAEID RAHMAN",
    "# Facebook: https://www.facebook.com/saeid.rahman.sr",
    "# Email: saeidrahman.mkt@gmail.com",
    "#=================================",
]


def attrs(line):
    return dict(ATTR_RE.findall(line))


def main():
    if not PLAYLIST.is_file():
        raise SystemExit("International playlist is missing.")
    lines = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    if not lines or not lines[0].startswith("#EXTM3U"):
        raise SystemExit("Missing #EXTM3U as the first line.")
    if lines[1:1 + len(ATTRIBUTION)] != ATTRIBUTION:
        raise SystemExit("Required attribution block is missing or not immediately after #EXTM3U.")
    if sum(line == ATTRIBUTION[1] for line in lines) != 1:
        raise SystemExit("Attribution block must appear exactly once.")

    registries = [line for line in lines if line.startswith("#PLAYLIST-STUDIO-CATEGORIES:")]
    if len(registries) != 1:
        raise SystemExit(f"Expected one category registry; found {len(registries)}.")
    try:
        registry = json.loads(registries[0].split(":", 1)[1])
    except Exception as exc:
        raise SystemExit(f"Invalid category registry JSON: {exc}")
    if not isinstance(registry, list) or len(registry) != len(set(registry)):
        raise SystemExit("Category registry must be a JSON list of unique names.")

    blocks, current = [], None
    for line in lines:
        if line.startswith("#EXTINF:"):
            if current is not None:
                blocks.append(current)
            current = [line]
        elif current is not None:
            current.append(line)
    if current is not None:
        blocks.append(current)
    if not blocks:
        raise SystemExit("Playlist contains no channel entries.")

    urls, groups_seen, group_set = [], [], set()
    missing_logos, broken_logos = 0, []
    for block in blocks:
        info = block[0]
        a = attrs(info)
        name = (a.get("tvg-name") or info.rsplit(",", 1)[-1]).strip()
        group = a.get("group-title", "").strip()
        if group.casefold() in FORBIDDEN:
            raise SystemExit(f"Forbidden staging/test group remains: {group!r} ({name}).")
        if group and group not in group_set:
            group_set.add(group)
            groups_seen.append(group)

        stream_rows = [
            line.strip() for line in block[1:]
            if line.strip().startswith(("http://", "https://"))
        ]
        if len(stream_rows) != 1:
            raise SystemExit(f"Expected exactly one URL row for {name!r}; found {len(stream_rows)}.")
        urls.append(stream_rows[0].casefold())

        logo = a.get("tvg-logo", "").strip()
        if not logo:
            missing_logos += 1
            continue
        if logo.startswith(RAW_BASE):
            rel = unquote(urlsplit(logo).path.split("/main/logos/", 1)[-1]).lstrip("/")
            target = (LOGOS / rel).resolve()
        elif logo.startswith("logos/"):
            rel = unquote(logo.split("?", 1)[0].split("#", 1)[0])
            target = Path(rel).resolve()
        else:
            raise SystemExit(f"External or unsupported logo reference for {name!r}: {logo}")
        root = LOGOS.resolve()
        if root not in target.parents or not target.is_file():
            broken_logos.append((name, logo))

    duplicates = [url for url, count in Counter(urls).items() if count > 1]
    if duplicates:
        raise SystemExit(f"Duplicate stream URL records: {len(duplicates)}.")
    if broken_logos:
        sample = "; ".join(f"{name}: {path}" for name, path in broken_logos[:5])
        raise SystemExit(f"Broken local logo references: {len(broken_logos)}. Examples: {sample}")

    dynamic = sorted(group for group in group_set if group not in FIXED and group not in TAIL)
    expected_registry = FIXED + dynamic + TAIL
    if registry != expected_registry:
        raise SystemExit(f"Category registry mismatch. Expected {expected_registry}; got {registry}.")
    expected_present_order = [group for group in expected_registry if group in group_set]
    if groups_seen != expected_present_order:
        raise SystemExit(f"Playlist category order mismatch. Expected {expected_present_order}; got {groups_seen}.")

    print(
        f"International structure OK: {len(blocks)} entries, 0 duplicate URLs, "
        f"0 broken/external logo references, {missing_logos} entries without logos. "
        "Playback was not tested."
    )


if __name__ == "__main__":
    main()
