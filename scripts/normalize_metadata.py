#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import re
from collections import defaultdict
from pathlib import Path

PLAYLIST = Path("IPTV-Playlist.m3u")
REPORT = Path("reports/metadata-normalization.md")
ATTR_RE = re.compile(r'([A-Za-z0-9_-]+)="([^"]*)"')
BACKUP_GROUPS = {"Backup", "Not Playing", "New Channels"}
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
MARKERS = re.compile(r"[ⓎⓈᴴᴰ🇹🇷]")
RES_RE = re.compile(r"\s*\(\d{3,4}[pi]\)", re.I)
BACKUP_RE = re.compile(r"\s*\[Backup\s*\d+\]", re.I)
GEO_RE = re.compile(r"\s*\[Geo-blocked\]", re.I)

def attrs(line):
    return dict(ATTR_RE.findall(line))

def replace_attr(meta, key, value):
    pattern = re.compile(rf'{re.escape(key)}="[^"]*"')
    if pattern.search(meta):
        return pattern.sub(f'{key}="{value}"', meta, count=1)
    return meta.replace("#EXTINF:-1 ", f'#EXTINF:-1 {key}="{value}" ', 1)

def split_extinf(line):
    pos = line.rfind('",')
    if pos < 0:
        raise ValueError(f"Malformed EXTINF line: {line}")
    return line[:pos + 1], line[pos + 2:]

def clean_markers(text):
    return re.sub(r"\s+", " ", MARKERS.sub("", text)).strip()

def base_name(text):
    text = clean_markers(text)
    text = BACKUP_RE.sub("", text)
    text = GEO_RE.sub("", text)
    text = RES_RE.sub("", text)
    return re.sub(r"\s+", " ", text).strip()

def generated_id(name, url):
    digest = hashlib.sha1((base_name(name).lower() + "|" + url).encode("utf-8")).hexdigest()[:12]
    return "local." + digest

def main():
    lines = PLAYLIST.read_text(encoding="utf-8-sig").replace("\r", "").splitlines()
    rows = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("#EXTINF:"):
            meta, name = split_extinf(lines[i])
            url = lines[i + 1].strip() if i + 1 < len(lines) and lines[i + 1].strip().startswith(("http://", "https://")) else ""
            rows.append({"index": i, "meta": meta, "name": name, "url": url})
            if url:
                i += 1
        i += 1

    # First pass: establish one canonical name per identity.
    by_id = defaultdict(list)
    for row in rows:
        a = attrs(row["meta"])
        cid = (a.get("tvg-id") or a.get("channel-id") or "").strip()
        if cid:
            by_id[cid].append(row)

    canonical = {}
    for cid, group in by_id.items():
        primary = next(
            (r for r in group if attrs(r["meta"]).get("group-title", "").strip() not in BACKUP_GROUPS
             and attrs(r["meta"]).get("tvg-name")),
            None,
        )
        candidate = base_name(attrs(primary["meta"]).get("tvg-name", "")) if primary else ""
        if not candidate:
            candidate = base_name(next((attrs(r["meta"]).get("tvg-name", "") for r in group if attrs(r["meta"]).get("tvg-name")), group[0]["name"]))
        canonical[cid] = OVERRIDES.get(cid, candidate) or "Channel"

    stats = {
        "generated_ids": 0, "channel_ids_fixed": 0, "tvg_names_normalized": 0,
        "display_names_normalized": 0, "backup_numbers_removed": 0,
        "numbers_added": 0, "duplicate_numbers_fixed": 0,
    }

    # Normalize identity/name fields.
    for row in rows:
        meta, name, url = row["meta"], row["name"], row["url"]
        a = attrs(meta)
        tvg_id = a.get("tvg-id", "").strip()
        channel_id = a.get("channel-id", "").strip()
        if not tvg_id and channel_id:
            tvg_id = channel_id
            meta = replace_attr(meta, "tvg-id", tvg_id)
        if not tvg_id:
            tvg_id = generated_id(name, url)
            meta = replace_attr(meta, "tvg-id", tvg_id)
            stats["generated_ids"] += 1
        if a.get("channel-id", "").strip() != tvg_id:
            meta = replace_attr(meta, "channel-id", tvg_id)
            stats["channel_ids_fixed"] += 1

        canon = canonical.get(tvg_id) or OVERRIDES.get(tvg_id) or base_name(a.get("tvg-name", "")) or base_name(name)
        if a.get("tvg-name", "").strip() != canon:
            meta = replace_attr(meta, "tvg-name", canon)
            stats["tvg_names_normalized"] += 1

        group = a.get("group-title", "").strip()
        if group == "Backup" and a.get("tvg-chno"):
            meta = re.sub(r'\s*tvg-chno="[^"]*"', "", meta)
            stats["backup_numbers_removed"] += 1

        cleaned = clean_markers(name)
        resolution = RES_RE.search(cleaned)
        backup = BACKUP_RE.search(cleaned)
        geo = " [Geo-blocked]" if GEO_RE.search(cleaned) else ""
        new_name = canon + (f" {resolution.group(0).strip()}" if resolution else "") + (f" {backup.group(0).strip()}" if backup else "") + geo
        if new_name != name:
            stats["display_names_normalized"] += 1

        row["meta"], row["name"] = meta, new_name

    # Second pass: preserve existing primary numbers, then fill gaps and fix collisions.
    used = set()
    for row in rows:
        a = attrs(row["meta"])
        group = a.get("group-title", "").strip()
        if group in BACKUP_GROUPS:
            continue
        n = a.get("tvg-chno", "").strip()
        if n and n.isdigit() and int(n) > 0 and int(n) not in used:
            used.add(int(n))

    next_no = 1
    for row in rows:
        a = attrs(row["meta"])
        group = a.get("group-title", "").strip()
        if group in BACKUP_GROUPS:
            continue
        n = a.get("tvg-chno", "").strip()
        valid = n.isdigit() and int(n) > 0
        if valid and int(n) not in used:
            used.add(int(n))
            continue
        if valid and sum(1 for r in rows[:row["index"] + 1] if attrs(r["meta"]).get("tvg-chno", "").strip() == n and attrs(r["meta"]).get("group-title", "").strip() not in BACKUP_GROUPS) > 1:
            pass
        while next_no in used:
            next_no += 1
        if not valid:
            stats["numbers_added"] += 1
        else:
            stats["duplicate_numbers_fixed"] += 1
        row["meta"] = replace_attr(row["meta"], "tvg-chno", str(next_no))
        used.add(next_no)
        next_no += 1

    for row in rows:
        lines[row["index"]] = f'{row["meta"]},{row["name"]}'

    PLAYLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        "# Playlist Metadata Normalization\n\n"
        f"- Entries processed: **{len(rows)}**\n"
        f"- Deterministic IDs generated: **{stats['generated_ids']}**\n"
        f"- channel-id/tvg-id identities synchronized: **{stats['channel_ids_fixed']}**\n"
        f"- tvg-name values normalized: **{stats['tvg_names_normalized']}**\n"
        f"- Display names normalized: **{stats['display_names_normalized']}**\n"
        f"- Backup channel numbers removed: **{stats['backup_numbers_removed']}**\n"
        f"- Missing primary channel numbers added: **{stats['numbers_added']}**\n"
        f"- Duplicate/invalid primary channel numbers repaired: **{stats['duplicate_numbers_fixed']}**\n",
        encoding="utf-8",
    )

if __name__ == "__main__":
    main()
