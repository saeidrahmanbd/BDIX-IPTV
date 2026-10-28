#!/usr/bin/env python3
"""Add conservative EPG mappings from configured additional country feeds.

Only active Indian playlist entries are considered, and a mapping is added only
when a normalized channel name has exactly one channel ID in a source. Existing
manual/verified mappings are never overwritten. This keeps new feeds as a
fallback/discovery layer instead of allowing fuzzy matches to replace trusted IDs.
"""
import csv
import gzip
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
MAPPING = Path("reports/epg-channel-mapping.csv")

# New sources supplied for this repair. US feeds are intentionally omitted here;
# they are useful for the generator but should not create India mappings.
SOURCES = [
    "https://epg.lat/files/in.xml.gz",
    "https://www.free-epg.de/api/epg/in.xml.gz",
    "https://www.open-epg.com/files/india.xml.gz",
]

EXCLUDED_GROUPS = {"Backup", "Test", "Not Playing"}
INDIAN_GROUPS = {"Indian Bangla", "Indian Movies", "Indian Music", "Indian Entertainment"}


def norm(value):
    value = str(value or "").lower()
    value = re.sub(r"\b(hd|sd|uhd|fhd|tv|channel)\b", " ", value)
    return re.sub(r"[^a-z0-9]+", "", value)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "BDIX-IPTV-EPG/1.0"})
    with urllib.request.urlopen(req, timeout=45) as response:
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
                if current["country"] == "IN" or current["group"] in INDIAN_GROUPS:
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


def main():
    if not PLAYLIST.exists() or not MAPPING.exists():
        print("Additional EPG mapping skipped: playlist or mapping file is missing.")
        return

    channels = playlist_channels()
    with MAPPING.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))

    by_id = {row.get("tvg_id", "").strip(): row for row in rows if row.get("tvg_id", "").strip()}
    source_hits = {}
    for source in SOURCES:
        try:
            names = source_channels(fetch(source))
        except Exception as exc:
            print(f"Additional EPG source unavailable: {source} ({exc})")
            continue
        source_hits[source] = names

    added = 0
    for channel in channels:
        row = by_id.get(channel["tvg_id"])
        if row is None or row.get("epg_id", "").strip():
            continue
        key = norm(channel["name"])
        if not key:
            continue

        matches = []
        for source, names in source_hits.items():
            ids = sorted(names.get(key, set()))
            if len(ids) == 1:
                matches.append((source, ids[0]))

        ids = sorted({cid for _, cid in matches})
        if len(ids) != 1:
            continue

        cid = ids[0]
        sources = [source for source, matched_id in matches if matched_id == cid]
        row["epg_id"] = cid
        row["source"] = ((row.get("source", "").strip(" |") + " | " + " | ".join(sources)).strip(" |"))
        row["status"] = "MAPPED_ID_ONLY"
        row["note"] = "Unique exact normalized-name match across newly added India XMLTV feeds."
        added += 1

    fieldnames = ["group", "channel", "tvg_id", "epg_id", "source", "status", "note"]
    with MAPPING.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Additional India EPG mappings added: {added}")


if __name__ == "__main__":
    main()
