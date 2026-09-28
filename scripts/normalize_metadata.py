#!/usr/bin/env python3
from __future__ import annotations
import re
from collections import defaultdict
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/metadata-normalization.md")
OVERRIDES = {
    "MohonaTV.bd": "Mohona TV",
    "MyTV.bd": "My TV",
    "SonyEntertainmentTelevision": "Sony Entertainment TV",
    "YRFMusic.in": "YRF Music",
    "ZeeBollywood.in": "Zee Bollywood",
    "PowerTurkTV.tr": "PowerTürk TV",
    "RupasiBangla.in": "Ruposhi Bangla",
    "Enterr10Bangla.in": "Enterr 10 Bangla",
}
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
BACKUP_RE = re.compile(r"\s*\[Backup\s*\d+\]", re.I)
GEO_RE = re.compile(r"\s*\[Geo-blocked\]", re.I)
RES_RE = re.compile(r"\s*\(\d{3,4}[pi]\)", re.I)

def attrs(meta):
    return {k: v for k, v in ATTR_RE.findall(meta)}

def replace_attr(meta, key, value):
    pattern = re.compile(rf'{re.escape(key)}="[^"]*"')
    repl = f'{key}="{value}"'
    if pattern.search(meta):
        return pattern.sub(repl, meta, count=1)
    return meta.replace("#EXTINF:-1 ", f'#EXTINF:-1 {repl} ', 1)

def remove_attr(meta, key):
    return re.sub(rf'\s*{re.escape(key)}="[^"]*"', "", meta)

def split_extinf(line):
    pos = line.rfind('",')
    if pos < 0:
        raise ValueError(f"Malformed EXTINF line: {line}")
    return line[:pos + 1], line[pos + 2:]

def clean_markers(text):
    text = text.replace("ᴴᴰ", "").replace("Ⓨ", "").replace("Ⓢ", "").replace("🇹🇷", "")
    return re.sub(r"\s+", " ", text).strip()

def base_name(text):
    text = clean_markers(text)
    text = BACKUP_RE.sub("", text)
    text = GEO_RE.sub("", text)
    text = RES_RE.sub("", text)
    return re.sub(r"\s+", " ", text).strip()

def main():
    lines = PLAYLIST.read_text(encoding="utf-8-sig").splitlines()
    rows = []
    for index, line in enumerate(lines):
        if not line.startswith("#EXTINF:"):
            continue
        meta, name = split_extinf(line)
        a = attrs(meta)
        rows.append({"index": index, "meta": meta, "name": name,
                     "id": a.get("tvg-id", ""), "tvg_name": a.get("tvg-name", ""),
                     "group": a.get("group-title", "")})

    by_id = defaultdict(list)
    for row in rows:
        if row["id"]:
            by_id[row["id"]].append(row)

    canonical = {}
    for channel_id, group in by_id.items():
        primary = next((r for r in group if r["group"] not in {"Backup", "Not Playing"} and r["tvg_name"]), None)
        candidate = base_name(primary["tvg_name"]) if primary else ""
        if not candidate:
            candidate = base_name(next((r["tvg_name"] for r in group if r["tvg_name"]), group[0]["name"]))
        canonical[channel_id] = OVERRIDES.get(channel_id, candidate)

    stats = {"backup_channel_numbers_removed": 0, "missing_tvg_name_added": 0,
             "missing_channel_id_added": 0, "tvg_names_normalized": 0,
             "display_names_normalized": 0, "stray_markers_removed": 0}

    for row in rows:
        meta, name = row["meta"], row["name"]
        a = attrs(meta)
        canon = canonical.get(row["id"]) or base_name(a.get("tvg-name", "")) or base_name(name)

        if row["group"] == "Backup" and a.get("tvg-chno"):
            meta = remove_attr(meta, "tvg-chno")
            stats["backup_channel_numbers_removed"] += 1

        if not a.get("channel-id") and a.get("tvg-id"):
            meta = replace_attr(meta, "channel-id", a["tvg-id"])
            stats["missing_channel_id_added"] += 1

        if not a.get("tvg-name"):
            meta = replace_attr(meta, "tvg-name", canon)
            stats["missing_tvg_name_added"] += 1
        elif canon and a.get("tvg-name") != canon:
            meta = replace_attr(meta, "tvg-name", canon)
            stats["tvg_names_normalized"] += 1

        cleaned = clean_markers(name)
        if cleaned != name:
            stats["stray_markers_removed"] += 1

        resolution_match = re.search(r"\(\d{3,4}[pi]\)", cleaned, re.I)
        backup_match = re.search(r"\[Backup\s*\d+\]", cleaned, re.I)
        geo = " [Geo-blocked]" if re.search(r"\[Geo-blocked\]", cleaned, re.I) else ""
        resolution = resolution_match.group(0) if resolution_match else ""
        backup = backup_match.group(0) if backup_match else ""
        new_name = canon + (f" {resolution}" if resolution else "") + (f" {backup}" if backup else "") + geo

        if new_name != name:
            stats["display_names_normalized"] += 1

        lines[row["index"]] = f"{meta},{new_name}"

    PLAYLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        "# Playlist Metadata Normalization\n\n"
        f"- Entries processed: **{len(rows)}**\n"
        f"- Backup channel numbers removed: **{stats['backup_channel_numbers_removed']}**\n"
        f"- Missing tvg-name added: **{stats['missing_tvg_name_added']}**\n"
        f"- Missing channel-id added: **{stats['missing_channel_id_added']}**\n"
        f"- tvg-name values normalized: **{stats['tvg_names_normalized']}**\n"
        f"- Display names normalized: **{stats['display_names_normalized']}**\n"
        f"- Stray Unicode markers removed: **{stats['stray_markers_removed']}**\n"
        f"- Local IDs retained for separate EPG mapping work: **{sum(x['id'].startswith('local.') for x in rows)}**\n",
        encoding="utf-8",
    )

if __name__ == "__main__":
    main()
