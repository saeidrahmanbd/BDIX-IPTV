#!/usr/bin/env python3
"""Conservatively augment the EPG mapping with verified iptv-org guide data."""
import csv
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

from fetch_iptv_org_epg import INACTIVE_GROUPS, load_explicit_epg_mappings, load_locked_epg_mappings

PLAYLIST = Path("IPTV-Playlist.m3u")
MAPPING = Path("reports/epg-channel-mapping.csv")
GUIDE = Path("/tmp/iptv-org-guide.xml")


def norm(value):
    value = str(value or "").casefold()
    value = re.sub(r"\b(?:\d{3,4}p|50fps|60fps)\b", " ", value)
    value = re.sub(r"\b(hd|sd|uhd|fhd|tv|channel)\b", " ", value)
    return re.sub(r"[^a-z0-9]+", "", value)


def parse_xmltv_time(value):
    """Parse common XMLTV timestamps, treating an omitted timezone as UTC."""
    match = re.match(r"^\s*(\d{14})(?:\s+([+-]\d{4}))?\s*$", str(value or ""))
    if not match:
        return None
    raw, offset = match.groups()
    try:
        if offset:
            return datetime.strptime(f"{raw} {offset}", "%Y%m%d%H%M%S %z").astimezone(timezone.utc)
        return datetime.strptime(raw, "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def playlist_channels():
    channels = []
    current = None
    for line in PLAYLIST.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("#EXTINF:"):
            attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', line))
            current = (
                attrs.get("tvg-id", "").strip(),
                attrs.get("tvg-name", "").strip() or line.rsplit(",", 1)[-1].strip(),
                attrs.get("group-title", "").strip(),
            )
        elif current and line.strip().startswith(("http://", "https://")):
            if current[0] and current[2].casefold() not in INACTIVE_GROUPS:
                channels.append(current)
            current = None
    return channels


def guide_data():
    """Return normalized display-name candidates and IDs with usable current/future titled programmes."""
    root = ET.parse(GUIDE).getroot()
    now = datetime.now(timezone.utc)
    lower = now - timedelta(hours=6)
    upper = now + timedelta(days=7)
    scheduled_ids = set()
    for programme in root.findall("programme"):
        channel_id = (programme.get("channel") or "").strip()
        if not channel_id or not any((title.text or "").strip() for title in programme.findall("title")):
            continue
        start = parse_xmltv_time(programme.get("start"))
        stop = parse_xmltv_time(programme.get("stop"))
        if start and stop and stop > start and stop > lower and start < upper:
            scheduled_ids.add(channel_id)

    names = {}
    for elem in root.findall("channel"):
        channel_id = (elem.attrib.get("id") or "").strip()
        if not channel_id:
            continue
        for display in elem.findall("display-name"):
            key = norm(display.text)
            if key:
                names.setdefault(key, set()).add(channel_id)
    return names, scheduled_ids


def append_verified_ids(row, candidate_ids):
    """Append verified source IDs only when the fetched guide has real current/future programmes."""
    existing = [value.strip() for value in (row.get("epg_id") or "").split("|") if value.strip()]
    additions = [value for value in dict.fromkeys(candidate_ids) if value and value not in existing]
    if not additions:
        return False
    row["epg_id"] = "|".join(existing + additions)
    marker = "iptv-org/epg verified current/future schedule"
    source = (row.get("source") or "").strip()
    if marker not in source:
        row["source"] = (source + " | " + marker).strip(" |")
    note = (row.get("note") or "").strip()
    if marker not in note:
        row["note"] = (note + " " + marker + "; exact ID or repository-approved alias.").strip()
    row["status"] = "MAPPED"
    return True


def main():
    if not GUIDE.is_file() or GUIDE.stat().st_size == 0:
        print("No build-time iptv-org guide; nothing to augment.")
        return

    channels = playlist_channels()
    names, scheduled_ids = guide_data()
    explicit_mappings = load_explicit_epg_mappings()
    locked_mappings = load_locked_epg_mappings()
    with MAPPING.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    by_id = {row.get("tvg_id", "").strip(): row for row in rows if row.get("tvg_id", "").strip()}
    explicit_added = 0
    exact_name_added = 0

    for tvg_id, name, group in channels:
        row = by_id.get(tvg_id)
        if row is None:
            continue

        # Exact playlist IDs or curated aliases/locks take priority over name matching.
        approved_ids = (
            locked_mappings[tvg_id]
            if tvg_id in locked_mappings
            else [tvg_id, *explicit_mappings.get(tvg_id, [])]
        )
        usable_ids = [source_id for source_id in dict.fromkeys(approved_ids) if source_id in scheduled_ids]
        if usable_ids:
            if append_verified_ids(row, usable_ids):
                explicit_added += len(usable_ids)
            continue

        # Never infer a domestic Bangladesh guide from a similarly named foreign service.
        if group.casefold() == "bangladesh" or (row.get("epg_id") or "").strip():
            continue
        key = norm(name)
        if not key:
            continue
        hits = sorted({source_id for source_id in names.get(key, set()) if source_id in scheduled_ids})
        if len(hits) != 1:
            continue
        if append_verified_ids(row, hits):
            exact_name_added += 1
            row["note"] = "Unique exact normalized display-name match with current/future schedules from iptv-org/epg."

    fieldnames = ["group", "channel", "tvg_id", "epg_id", "source", "status", "note"]
    with MAPPING.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"iptv-org verified IDs added: {explicit_added}; unique exact-name mappings added: {exact_name_added}")


if __name__ == "__main__":
    main()
