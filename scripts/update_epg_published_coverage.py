#!/usr/bin/env python3
"""Refresh public EPG coverage reports from the XMLTV artefact without refetching feeds."""
import csv
import hashlib
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAYLISTS = (
    ("IPTV-Playlist.m3u", "Main IPTV"),
    ("BDIX-Playlist.m3u", "BDIX"),
    ("International-Playlist.m3u", "International"),
)
GUIDE = ROOT / "epg" / "epg.xml"
FRESHNESS = ROOT / "reports" / "epg-publish-freshness.md"
MAPPING = ROOT / "reports" / "epg-channel-mapping.csv"
RAW_URL = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml"
INACTIVE_GROUPS = {"Backup", "Test", "Not Playing", "New Channels", "New Backup"}
PLACEHOLDERS = {
    "movie", "movies", "program", "programme", "entertainment", "live", "live tv",
    "tba", "to be announced", "unknown", "schedule", "telecast", "show", "music",
    "test", "testing", "coming soon", "no data", "no information", "no info", "n/a",
    "none", "no title", "no program", "no programs", "no programme", "no programmes",
    "no schedule", "no schedule available", "not available",
    "program not available", "programme not available",
}


def parse_time(value):
    match = re.match(r"^\s*(\d{14})(?:\s*([+-]\d{4}))?\s*$", str(value or ""))
    if not match:
        return None
    raw, offset = match.groups()
    try:
        parsed = datetime.strptime(raw, "%Y%m%d%H%M%S")
        if offset:
            sign = 1 if offset[0] == "+" else -1
            minutes = sign * (int(offset[1:3]) * 60 + int(offset[3:5]))
            return parsed.replace(tzinfo=timezone(timedelta(minutes=minutes))).astimezone(timezone.utc)
        return parsed.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def parse_playlist(path):
    rows = []
    current = None
    for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        if line.startswith("#EXTINF:"):
            attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', line))
            comma = line.find(",")
            current = {"attrs": attrs, "name": line[comma + 1:].strip() if comma >= 0 else attrs.get("tvg-name", "")}
        elif current and line.strip().startswith(("http://", "https://")):
            rows.append(current)
            current = None
    return rows


def usable_title(value):
    title = re.sub(r"\s+", " ", str(value or "")).strip()
    if not title or title.casefold() in PLACEHOLDERS:
        return False
    return not bool(re.fullmatch(r"(?:program|programme|show|movie)\s*@?\s*\d{1,2}(?::\d{2})?\s*(?:am|pm)?", title, re.I))


def main():
    if not GUIDE.is_file() or GUIDE.stat().st_size == 0:
        raise SystemExit("Cannot report EPG coverage: epg/epg.xml is missing or empty.")
    freshness_text = FRESHNESS.read_text(encoding="utf-8", errors="replace") if FRESHNESS.is_file() else ""
    if not re.search(r"(?im)^Status:\s*\*\*PASS\*\*\s*$", freshness_text):
        raise SystemExit("Cannot report a published guide: epg-publish-freshness.md is not PASS.")

    now = datetime.now(timezone.utc)
    lower, upper = now - timedelta(hours=6), now + timedelta(days=7)
    guide_channels, window_ids, live_ids = set(), set(), set()
    eligible_window = eligible_live = 0
    for _, elem in ET.iterparse(str(GUIDE), events=("end",)):
        if elem.tag == "channel":
            cid = (elem.get("id") or "").strip()
            if cid:
                guide_channels.add(cid)
            elem.clear()
        elif elem.tag == "programme":
            cid = (elem.get("channel") or "").strip()
            start, stop = parse_time(elem.get("start")), parse_time(elem.get("stop"))
            title = elem.find("title")
            valid = bool(cid and start and stop and stop > start and start <= upper and stop >= lower
                         and title is not None and usable_title(title.text))
            if valid:
                eligible_window += 1
                window_ids.add(cid)
                if stop >= now:
                    eligible_live += 1
                    live_ids.add(cid)
            elem.clear()

    mapping = {}
    if MAPPING.is_file():
        with MAPPING.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                tid = (row.get("tvg_id") or "").strip()
                if tid:
                    mapping[tid] = row
    mapped_ids = {tid for tid, row in mapping.items() if (row.get("epg_id") or "").strip()}
    active_ids, playlist_stats, missing_live = set(), {}, []
    for filename, label in PLAYLISTS:
        path = ROOT / filename
        records = parse_playlist(path)
        active_rows = []
        for record in records:
            attrs = record["attrs"]
            tid = (attrs.get("tvg-id") or "").strip()
            group = (attrs.get("group-title") or "").strip()
            if tid and group not in INACTIVE_GROUPS:
                active_rows.append((tid, group, record["name"]))
        ids = {row[0] for row in active_rows}
        active_ids.update(ids)
        present, scheduled, in_window = ids & guide_channels, ids & live_ids, ids & window_ids
        header = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()[0]
        header_ok = f'url-tvg="{RAW_URL}"' in header and f'x-tvg-url="{RAW_URL}"' in header
        playlist_stats[filename] = {
            "label": label, "entries": len(records), "ids": len(ids), "present": len(present),
            "scheduled": len(scheduled), "window": len(in_window), "mapped": len(ids & mapped_ids),
            "header_ok": header_ok,
        }
        missing_live.extend((group, name, tid, "NO_MAPPING" if tid not in mapped_ids else "NO_CURRENT_PROGRAMME")
                            for tid, group, name in active_rows if tid not in live_ids)

    reports = ROOT / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    source_fingerprints = [
        f"- {filename} SHA-256: **{hashlib.sha256((ROOT / filename).read_bytes()).hexdigest()}**"
        for filename, _label in PLAYLISTS
        if (ROOT / filename).is_file()
    ]
    ratio = lambda n, d: f"{n}/{d} ({round(100*n/d, 1) if d else 0}%)"
    lines = [
        "# EPG Coverage & Mapping Report", "",
        f"Generated: **{now.isoformat(timespec='seconds')}**", "",
        "## Status: PUBLISHED — FRESHNESS PASS", "",
        f"- Public XMLTV guide: [{RAW_URL}]({RAW_URL})",
        f"- XMLTV channel IDs published: **{len(guide_channels)}**",
        f"- Eligible programme rows in the common -6h/+7d window: **{eligible_window}**",
        f"- Eligible current/future programme rows: **{eligible_live}**",
        f"- Active playlist IDs with current/future programmes: **{ratio(len(active_ids & live_ids), len(active_ids))}**",
        f"- Active playlist IDs with in-window programmes: **{ratio(len(active_ids & window_ids), len(active_ids))}**",
        f"- IDs with source mappings in the retained mapping snapshot: **{len(mapped_ids)}**",
        "- Current guide coverage is calculated from the validated XMLTV file, not historical mapping percentages.",
        "", "## Coverage by Playlist", "",
        "| Playlist | Entries | Active IDs | IDs in guide | IDs with current/future programmes | IDs with in-window programmes | Mapped IDs | EPG header |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for filename, item in playlist_stats.items():
        lines.append(f"| {item['label']} ({filename}) | {item['entries']} | {item['ids']} | {item['present']} | {item['scheduled']} | {item['window']} | {item['mapped']} | {'OK' if item['header_ok'] else 'MISMATCH'} |")
    lines += [
        "", "## Source Usage", "",
        "- The EPG pipeline may use useful public or otherwise accessible feeds for discovery, mapping and schedule acquisition.",
        "- Sources are combined and deduplicated; current/future schedules and stronger channel identity matches are preferred.",
        "- Private credentials, session tokens and personalized feed URLs are never committed to the repository.",
        "- EPG.PW remains excluded by explicit project configuration; this is a source-selection rule, not a repository-wide rights-register gate.",
        "", "## Channels Without Current/Future Programmes", "",
        "| Group | Channel | Playlist ID | Status |", "|---|---|---|---|",
    ]
    for group, name, tid, status in sorted(missing_live, key=lambda x: (x[0], x[1].casefold(), x[2]))[:200]:
        lines.append(f"| {group} | {name} | {tid} | {status} |")
    if len(missing_live) > 200:
        lines.append(f"_Only the first 200 of {len(missing_live)} IDs are listed._")
    lines += [
        "", f"- Programme window: **{lower.isoformat(timespec='minutes')} to {upper.isoformat(timespec='minutes')}**",
        "- Freshness validation: **PASS**.", "", "## Source Playlist Fingerprints", "",
        *source_fingerprints, "",
    ]
    (reports / "epg-coverage.md").write_text("\n".join(lines), encoding="utf-8")

    audit = [
        "# EPG Audit — Published Playlists", "", f"Generated: **{now.isoformat(timespec='seconds')}**", "",
        "## Status: PUBLISHED — XMLTV freshness validation PASS", "",
        "| Playlist | Stream entries | Active IDs | IDs in guide | Current/future programme IDs | In-window programme IDs | Mapped IDs | EPG header |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for filename, item in playlist_stats.items():
        audit.append(f"| {item['label']} ({filename}) | {item['entries']} | {item['ids']} | {item['present']} | {item['scheduled']} | {item['window']} | {item['mapped']} | {'OK' if item['header_ok'] else 'MISMATCH'} |")
    audit += [
        "", f"XMLTV channels: **{len(guide_channels)}**; eligible in-window programme rows: **{eligible_window}**; current/future rows: **{eligible_live}**.",
        "", "## Source Playlist Fingerprints", "", *source_fingerprints, "",
    ]
    (reports / "epg-three-playlist-audit.md").write_text("\n".join(audit), encoding="utf-8")

    unmapped = [
        "# EPG Unmapped / Missing Programme Audit", "", f"Generated: **{now.isoformat(timespec='seconds')}**", "",
        "## Status: GUIDE PUBLISHED — MAPPING GAPS REPORTED", "",
        f"- Active playlist IDs without current/future programme rows: **{len(missing_live)}**",
        f"- IDs without source mapping: **{sum(s == 'NO_MAPPING' for _, _, _, s in missing_live)}**",
        f"- Mapped IDs without current/future programme rows: **{sum(s == 'NO_CURRENT_PROGRAMME' for _, _, _, s in missing_live)}**",
        "- No schedule is fabricated for missing channels.",
        "", "| Group | Channel | Playlist ID | Status |", "|---|---|---|---|",
    ]
    for group, name, tid, status in sorted(missing_live, key=lambda x: (x[0], x[1].casefold(), x[2]))[:200]:
        unmapped.append(f"| {group} | {name} | {tid} | {status} |")
    if len(missing_live) > 200:
        unmapped.append(f"_Only the first 200 of {len(missing_live)} IDs are listed._")
    unmapped += ["", "## Source Playlist Fingerprints", "", *source_fingerprints, ""]
    (reports / "epg-unmapped-audit.md").write_text("\n".join(unmapped), encoding="utf-8")

    timing = [
        "# EPG Timing Audit", "", f"Generated: **{now.isoformat(timespec='seconds')}**", "",
        "## Status: PASS — published XMLTV timing measured", "",
        f"- Valid current/future programme rows: **{eligible_live}**",
        f"- Valid programme rows in the -6h/+7d window: **{eligible_window}**",
        f"- Channel IDs with current/future programmes: **{len(live_ids)}**",
        f"- Channel IDs with in-window programmes: **{len(window_ids)}**",
        f"- Window bounds: **{lower.isoformat(timespec='minutes')} to {upper.isoformat(timespec='minutes')}**",
        "- Empty and placeholder titles are excluded from these report counts.", "",
    ]
    (reports / "epg-timing-audit.md").write_text("\n".join(timing), encoding="utf-8")
    print(f"Published-guide reports updated: {len(guide_channels)} channels, {eligible_window} in-window programme rows, {eligible_live} current/future rows.")


if __name__ == "__main__":
    main()
