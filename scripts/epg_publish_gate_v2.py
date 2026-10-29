#!/usr/bin/env python3
"""Publish gate for the playlist-aligned EPG.

Unlike the legacy gate, this does not reject valid programme text because of
language/script. It validates title presence, schedule intervals, conflicts,
placeholder density, and sensible retention against the previous guide.
"""
import re
import sys
import unicodedata
from datetime import datetime, timezone, timedelta
import xml.etree.ElementTree as ET
from pathlib import Path

OLD = Path("/tmp/bdix-epg-previous.xml")
NEW = Path("epg/epg.xml")
GENERIC = {"movie", "movies", "program", "programme", "entertainment", "live", "live tv", "tba", "to be announced", "unknown", "schedule", "telecast", "show", "music", "test", "testing", "coming soon", "no data", "no information", "no info", "n/a", "none", "no title", "no program", "no programs", "no programme", "no programmes", "no schedule", "no schedule available", "not available", "program not available", "programme not available"}
# Blank time slots labelled like "Program @ 5:00 AM" carry no programme information.
SLOT_PLACEHOLDER_RE = re.compile(r"^(program|programme|show|slot)\s*@\s*\d")


def parse(path):
    if not path.exists() or path.stat().st_size == 0:
        return set(), [], 0
    root = ET.parse(path).getroot()
    channels = {x.get("id") for x in root.findall("channel") if x.get("id")}
    programmes = []
    title_violations = 0
    for x in root.findall("programme"):
        channel = x.get("channel")
        start = x.get("start")
        stop = x.get("stop")
        title_elements = x.findall("title")
        title = (title_elements[0].text or "").strip() if title_elements else ""
        if not title_elements or not title:
            title_violations += 1
        if channel and start and stop and title:
            programmes.append((channel, start, stop, title))
    return channels, programmes, title_violations


def parse_time(value):
    value = (value or "").strip()
    if len(value) < 14:
        return None
    try:
        base = value[:14]
        suffix = value[14:].strip()
        if suffix:
            return datetime.strptime(f"{base} {suffix}", "%Y%m%d%H%M%S %z").astimezone(timezone.utc)
        return datetime.strptime(base, "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def overlap_count(programmes):
    by_channel = {}
    for channel, start, stop, _ in programmes:
        s, e = parse_time(start), parse_time(stop)
        if s is None or e is None or e <= s:
            continue
        by_channel.setdefault(channel, []).append((s, e))
    overlaps = 0
    for rows in by_channel.values():
        rows.sort()
        previous_stop = None
        for start, stop in rows:
            if previous_stop is not None and start < previous_stop:
                overlaps += 1
            if previous_stop is None or stop > previous_stop:
                previous_stop = stop
    return overlaps


def quality(path):
    channels, programmes, title_violations = parse(path)
    generic = sum(
        1 for _, _, _, title in programmes
        if title.strip().lower() in GENERIC or SLOT_PLACEHOLDER_RE.match(title.strip().lower())
    )
    now = datetime.now(timezone.utc)
    lower = now - timedelta(hours=6)
    upper = now + timedelta(days=7)
    window_programmes = []
    current_programmes = []
    for programme in programmes:
        start, stop = parse_time(programme[1]), parse_time(programme[2])
        if start is None or stop is None or stop <= start:
            continue
        if stop >= lower and start <= upper:
            window_programmes.append(programme)
        if start <= now < stop:
            current_programmes.append(programme)
    return {
        "channels": len(channels),
        "programmes": len(programmes),
        "window_channels": len({item[0] for item in window_programmes}),
        "window_programmes": len(window_programmes),
        "current_channels": len({item[0] for item in current_programmes}),
        "current_programmes": len(current_programmes),
        "overlaps": overlap_count(programmes),
        "generic": generic,
        "generic_ratio": generic / len(programmes) if programmes else 1.0,
        "title_violations": title_violations,
    }


new = quality(NEW)
if new["channels"] == 0 or new["programmes"] == 0:
    raise SystemExit("EPG gate BLOCK: generated guide has no usable channels/programmes")
if new["title_violations"]:
    raise SystemExit(f"EPG gate BLOCK: {new['title_violations']} programmes have missing/blank titles")
if new["overlaps"]:
    raise SystemExit(f"EPG gate BLOCK: generated guide contains {new['overlaps']} overlapping programme intervals")
if new["generic_ratio"] > 0.01:
    raise SystemExit(f"EPG gate BLOCK: placeholder-title ratio is {new['generic_ratio']:.3f}, above 0.010")

if OLD.exists():
    old = quality(OLD)
    if old["window_channels"] and new["window_channels"] < max(1, int(old["window_channels"] * 0.80)):
        raise SystemExit(
            "EPG gate BLOCK: usable current-window channel coverage regressed below 80%: "
            f"{old['window_channels']} -> {new['window_channels']}"
        )
    clean_volume_pass = (
        not old["window_programmes"]
        or new["window_programmes"] >= int(old["window_programmes"] * 0.85)
    )
    quality_override = (
        (not old["window_programmes"] or new["window_programmes"] >= int(old["window_programmes"] * 0.20))
        and new["window_channels"] >= max(1, int(old["window_channels"] * 0.85))
    )
    if not clean_volume_pass and not quality_override:
        raise SystemExit(
            "EPG gate BLOCK: current-window programme retention/quality failed: "
            f"{old['window_programmes']} -> {new['window_programmes']} programmes"
        )

print(
    "EPG gate PASS: multilingual guide accepted "
    f"(channels={new['channels']}, programmes={new['programmes']}, "
    f"window_channels={new['window_channels']}, window_programmes={new['window_programmes']}, "
    f"current_channels={new['current_channels']}, current_programmes={new['current_programmes']}, "
    f"overlaps={new['overlaps']}, generic ratio={new['generic_ratio']:.3f})"
)
sys.exit(0)
