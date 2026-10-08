#!/usr/bin/env python3
"""Prevent publication of a materially degraded EPG while allowing a clean guide
to replace a larger but internally conflicting legacy guide."""
import sys
from datetime import datetime, timezone
import xml.etree.ElementTree as ET
from pathlib import Path

OLD = Path("/tmp/bdix-epg-previous.xml")
NEW = Path("epg/epg.xml")

GENERIC = {
    "movie", "program", "programme", "entertainment", "live", "live tv",
    "tba", "to be announced", "unknown", "schedule", "telecast", "show",
    "music", "test", "testing", "coming soon",
}

def parse(path):
    if not path.exists() or path.stat().st_size == 0:
        return set(), []
    root = ET.parse(path).getroot()
    channels = {x.get("id") for x in root.findall("channel") if x.get("id")}
    programmes = []
    for x in root.findall("programme"):
        channel = x.get("channel")
        start = x.get("start")
        stop = x.get("stop")
        title = (x.findtext("title") or "").strip()
        if channel and start and stop and title:
            programmes.append((channel, start, stop, title))
    return channels, programmes

def parse_xmltv_time(value):
    """Parse XMLTV timestamps consistently, including explicit timezone offsets."""
    value = (value or "").strip()
    if not value:
        return None
    try:
        if len(value) >= 19:
            base = value[:14]
            suffix = value[14:].strip()
            if suffix:
                return datetime.strptime(
                    f"{base} {suffix}", "%Y%m%d%H%M%S %z"
                ).astimezone(timezone.utc)
            return datetime.strptime(base, "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)
    except ValueError:
        return None
    return None

def overlap_count(programmes):
    by_channel = {}
    for p in programmes:
        start_dt = parse_xmltv_time(p[1])
        stop_dt = parse_xmltv_time(p[2])
        if start_dt is None or stop_dt is None or stop_dt <= start_dt:
            continue
        by_channel.setdefault(p[0], []).append((start_dt, stop_dt))
    overlaps = 0
    for rows in by_channel.values():
        rows.sort(key=lambda p: (p[0], p[1]))
        previous_stop = None
        for start_dt, stop_dt in rows:
            if previous_stop is not None and start_dt < previous_stop:
                overlaps += 1
            if previous_stop is None or stop_dt > previous_stop:
                previous_stop = stop_dt
    return overlaps

def quality(path):
    channels, programmes = parse(path)
    generic = sum(
        1 for _, _, _, title in programmes
        if title.strip().lower() in GENERIC
    )
    return {
        "channels": len(channels),
        "programmes": len(programmes),
        "overlaps": overlap_count(programmes),
        "generic": generic,
        "generic_ratio": generic / len(programmes) if programmes else 1.0,
    }

new = quality(NEW)
if new["channels"] == 0 or new["programmes"] == 0:
    raise SystemExit("EPG gate BLOCK: generated guide has no usable channels/programmes")

if OLD.exists():
    old = quality(OLD)

    if old["channels"] and new["channels"] < max(1, int(old["channels"] * 0.80)):
        raise SystemExit(
            f"EPG gate BLOCK: channel coverage regressed below the 80% safety floor: "
            f'{old["channels"]} -> {new["channels"]}'
        )

    # Normal path: require the historical 90% programme-volume safeguard.
    if old["programmes"] and new["programmes"] >= int(old["programmes"] * 0.90):
        print(
            f'EPG gate PASS: channels={new["channels"]}, programmes={new["programmes"]} '
            f'(normal volume threshold)'
        )
        sys.exit(0)

    # Quality path: the old guide can itself contain conflicting schedules.
    # Do not let its inflated programme count force publication of known
    # overlapping data. A reduced guide is accepted only when it is materially
    # smaller, clean, and still has strong channel retention (at least 85% of the previous guide).
    quality_override = (
        (not old["programmes"] or new["programmes"] >= int(old["programmes"] * 0.20))
        and new["channels"] >= max(1, int(old["channels"] * 0.85))
        and new["overlaps"] == 0
        and new["generic_ratio"] <= old["generic_ratio"]
    )

    if quality_override:
        print(
            "EPG gate PASS: quality override accepted a smaller clean guide "
            f'(channels {old["channels"]}->{new["channels"]}, '
            f'programmes {old["programmes"]}->{new["programmes"]}, '
            f'overlaps {old["overlaps"]}->{new["overlaps"]}, '
            f'generic ratio {old["generic_ratio"]:.3f}->{new["generic_ratio"]:.3f})'
        )
        sys.exit(0)

    raise SystemExit(
        "EPG gate BLOCK: programme volume fell below 90% and the generated guide "
        "did not meet the clean-guide quality override "
        f'(programmes {old["programmes"]}->{new["programmes"]}, '
        f'overlaps {old["overlaps"]}->{new["overlaps"]}, '
        f'generic ratio {old["generic_ratio"]:.3f}->{new["generic_ratio"]:.3f})'
    )

print(f'EPG gate PASS: channels={new["channels"]}, programmes={new["programmes"]}')
