#!/usr/bin/env python3
"""Add conservative EPG mappings from configured additional country feeds.

Only active Indian playlist entries are considered, and a mapping is added or
extended only when a normalized channel name has exactly one channel ID in a
source. Existing IDs are preserved and new provider IDs/source URLs are appended.
Strict identity locks are never modified. This keeps discovery conservative while
allowing additional feeds to improve already-mapped channels.
"""
import csv
import gzip
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
import xml.etree.ElementTree as ET
from pathlib import Path

from epg_coverage import EPG_LOCKS

PLAYLIST = Path("IPTV-Playlist.m3u")
MAPPING = Path("reports/epg-channel-mapping.csv")

# New sources supplied for this repair. US feeds are intentionally omitted here;
# they are useful for the generator but should not create India mappings.
SOURCES = [
    "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz",
    "https://iptv-epg.org/files/epg-in.xml.gz",
    "https://epg.lat/files/in.xml.gz",
    "https://www.free-epg.de/api/epg/in.xml.gz",
    "https://www.open-epg.com/files/india.xml.gz",
    # Provider feeds already consumed by the XMLTV generator; scan their
    # channel catalogues too so active playlist IDs can acquire exact mappings.
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/dishtv.xml",
    "https://m3u-edit.com/epg-source.php?file=india_dishtv.in.xml",
    "https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/airtel.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/jiotv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml",
    "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/zee5.xml",
    "https://avkb.short.gy/epg.xml.gz",
    "https://avkb.short.gy/jioepg.xml.gz",
    "https://avkb.short.gy/tsepg.xml.gz",
]

EXCLUDED_GROUPS = {"Backup", "Test", "Not Playing"}
INDIAN_GROUPS = {"Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment"}
GENERIC_NAME_KEYS = {
    "news", "movie", "movies", "music", "live", "entertainment", "kids",
    "sports", "star", "zee", "colors", "sony", "cinema", "world", "plus",
    "one", "two", "four", "today", "max", "now",
}


def norm(value):
    value = str(value or "").lower()
    value = re.sub(r"\b(hd|sd|uhd|fhd|tv|channel)\b", " ", value)
    return re.sub(r"[^a-z0-9]+", "", value)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "BDIX-IPTV-EPG/1.0"})
    with urllib.request.urlopen(req, timeout=60) as response:
        data = response.read()
    if data[:2] == b"\x1f\x8b" or url.endswith(".gz"):
        data = gzip.decompress(data)
    return data


def playlist_channels():
    channels = []
    current = None
    for line in PLAYLIST.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("#EXTINF:"):
            attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', line))
            current = {
                "tvg_id": attrs.get("tvg-id", "").strip(),
                "name": attrs.get("tvg-name", "").strip() or line.rsplit(",", 1)[-1].strip(),
                "group": attrs.get("group-title", "").strip(),
                "country": attrs.get("tvg-country", "").strip().upper(),
            }
        elif current and line.strip().startswith(("http://", "https://")):
            if current["tvg_id"] and current["group"] not in EXCLUDED_GROUPS:
                is_indian_identity = bool(re.search(r"\.in(?:@|$)", current["tvg_id"], re.I))
                if current["country"] == "IN" or current["group"] in INDIAN_GROUPS or is_indian_identity:
                    channels.append(current)
            current = None
    return channels


def source_channels(data):
    root = ET.fromstring(data)
    by_name = {}
    for channel in root.findall("channel"):
        cid = (channel.get("id") or "").strip()
        if not cid:
            continue
        names = []
        for display in channel.findall("display-name"):
            text = (display.text or "").strip()
            if text:
                names.append(text)
        for name in names:
            key = norm(name)
            if key:
                by_name.setdefault(key, set()).add(cid)
    return by_name


def apply_exact_source_matches(rows, channels, source_hits, locked_targets=None):
    """Append unique exact-name provider IDs and source URLs without replacing trusted mappings."""
    locked_targets = set(EPG_LOCKS) if locked_targets is None else set(locked_targets)
    by_id = {
        row.get("tvg_id", "").strip(): row
        for row in rows
        if row.get("tvg_id", "").strip()
    }
    added_ids = 0
    updated_channels = 0

    for channel in channels:
        target_id = str(channel.get("tvg_id", "")).strip()
        row = by_id.get(target_id)
        if row is None or target_id in locked_targets:
            continue
        key = norm(channel.get("name", ""))
        if not key or key in GENERIC_NAME_KEYS:
            continue

        matches = []
        for source, names in sorted(source_hits.items()):
            ids = sorted(names.get(key, set()))
            if len(ids) == 1:
                matches.append((source, ids[0]))

        discovered_ids = sorted({source_id for _, source_id in matches})
        if not discovered_ids or (len(discovered_ids) > 1 and len(key) < 5):
            continue

        existing_ids = [
            item.strip()
            for item in str(row.get("epg_id", "")).split("|")
            if item.strip()
        ]
        merged_ids = list(dict.fromkeys(existing_ids + discovered_ids))
        existing_sources = [
            item.strip()
            for item in str(row.get("source", "")).split("|")
            if item.strip()
        ]
        merged_id_set = set(merged_ids)
        new_sources = [
            source
            for source, source_id in matches
            if source_id in merged_id_set and source not in existing_sources
        ]
        merged_sources = list(dict.fromkeys(existing_sources + new_sources))

        new_id_count = len([source_id for source_id in discovered_ids if source_id not in existing_ids])
        if new_id_count == 0 and len(merged_sources) == len(existing_sources):
            continue

        row["epg_id"] = " | ".join(merged_ids)
        row["source"] = " | ".join(merged_sources)
        if not existing_ids and discovered_ids:
            row["status"] = "MAPPED_ID_ONLY"
        elif not row.get("status"):
            row["status"] = "MAPPED_ID_ONLY"
        note = (
            "Additional exact normalized-name provider IDs discovered; "
            "all distinct provider IDs retained for schedule merging."
        )
        old_note = str(row.get("note", "")).strip()
        if note not in old_note:
            row["note"] = (old_note + " " + note).strip()
        added_ids += new_id_count
        updated_channels += 1

    return rows, added_ids, updated_channels


def main():
    if not PLAYLIST.exists() or not MAPPING.exists():
        print("Additional EPG mapping skipped: playlist or mapping file is missing.")
        return

    channels = playlist_channels()
    with MAPPING.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))

    by_id = {row.get("tvg_id", "").strip(): row for row in rows if row.get("tvg_id", "").strip()}
    source_hits = {}
    with ThreadPoolExecutor(max_workers=min(8, len(SOURCES))) as pool:
        futures = {pool.submit(fetch, source): source for source in SOURCES}
        for future in as_completed(futures):
            source = futures[future]
            try:
                source_hits[source] = source_channels(future.result())
            except Exception as exc:
                print(f"Additional EPG source unavailable: {source} ({exc})")

    rows, added_ids, updated_channels = apply_exact_source_matches(
        rows,
        channels,
        source_hits,
    )

    fieldnames = ["group", "channel", "tvg_id", "epg_id", "source", "status", "note"]
    with MAPPING.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(
        f"Additional India EPG mappings updated: {updated_channels} channels; "
        f"{added_ids} new provider IDs."
    )


if __name__ == "__main__":
    main()
