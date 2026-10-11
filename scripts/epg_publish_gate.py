#!/usr/bin/env python3
"""Prevent publication of a materially degraded EPG while allowing a clean guide
to replace a larger but internally conflicting legacy guide."""
import sys
import unicodedata
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
TEXT_FIELDS = {"title", "sub-title", "desc"}
XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"


def is_english_text_element(elem):
    """Require English language tags and Latin-script text for visible guide fields."""
    text = (elem.text or "").strip()
    if not text:
        return True
    lang = (elem.attrib.get(XML_LANG) or elem.attrib.get("lang") or "").strip().lower()
    if lang and not (
        lang == "en" or lang == "eng" or lang.startswith("en-") or lang.startswith("en_")
    ):
        return False
    for char in text:
        if unicodedata.category(char).startswith("L"):
            if "LATIN" not in unicodedata.name(char, ""):
                return False
    return True

def parse(path):
    if not path.exists() or path.stat().st_size == 0:
        return set(), [], 0, 0
    root = ET.parse(path).getroot()
    channels = {x.get("id") for x in root.findall("channel") if x.get("id")}
    programmes = []
    language_violations = 0
    title_violations = 0
    for x in root.findall("programme"):
        channel = x.get("channel")
        start = x.get("start")
        stop = x.get("stop")
        title_elements = x.findall("title")
        title = (title_elements[0].text or "").strip() if title_elements else ""
        if not title_elements or not title:
            title_violations += 1
        for field in x.iter():
            if field.tag in TEXT_FIELDS and not is_english_text_element(field):
                language_violations += 1
        if channel and start and stop and title:
            programmes.append((channel, start, stop, title))
    return channels, programmes, language_violations, title_violations

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
    channels, programmes, language_violations, title_violations = parse(path)
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
        "language_violations": language_violations,
        "title_violations": title_violations,
    }


new = quality(NEW)
if new["channels"] == 0 or new["programmes"] == 0:
    raise SystemExit("EPG gate BLOCK: generated guide has no usable channels/programmes")

# Never publish the previous wrong-language behaviour again. English-only means
# English language metadata (when specified) and Latin-script visible text in
# programme titles, subtitles, and descriptions.
if new["language_violations"] or new["title_violations"]:
    raise SystemExit(
        "EPG gate BLOCK: English-only validation failed: "
        f'{new["language_violations"]} non-English text fields, '
        f'{new["title_violations"]} missing/blank programme titles'
    )

if OLD.exists():
    old = quality(OLD)

    if old["channels"] and new["channels"] < max(1, int(old["channels"] * 0.80)):
        raise SystemExit(
            f"EPG gate BLOCK: channel coverage regressed below the 80% safety floor: "
            f'{old["channels"]} -> {new["channels"]}'
        )

    # Schedule volume is secondary to the English-only and conflict-free rules.
    # A guide retaining at least 85% of programme volume passes when it has no
    # overlaps and placeholder titles remain a small fraction of the result.
    clean_volume_pass = (
        (not old["programmes"] or new["programmes"] >= int(old["programmes"] * 0.85))
        and new["overlaps"] == 0
        and new["generic_ratio"] <= 0.01
    )
    if clean_volume_pass:
        print(
            "EPG gate PASS: English-only clean guide accepted "
            f'(channels={new["channels"]}, programmes={new["programmes"]}, '
            f'previous programmes={old["programmes"]}, '
            f'language violations={new["language_violations"]}, '
            f'overlaps={new["overlaps"]}, generic ratio={new["generic_ratio"]:.3f})'
        )
        sys.exit(0)

    # Allow a substantial but still useful clean guide when it materially
    # improves quality or corrects old conflicts. Keep a conservative channel
    # retention floor and reject overlap-heavy or placeholder-heavy outputs.
    quality_override = (
        (not old["programmes"] or new["programmes"] >= int(old["programmes"] * 0.20))
        and new["channels"] >= max(1, int(old["channels"] * 0.85))
        and new["overlaps"] == 0
        and new["generic_ratio"] <= 0.01
    )

    if quality_override:
        print(
            "EPG gate PASS: English-only quality override accepted a smaller clean guide "
            f'(channels {old["channels"]}->{new["channels"]}, '
            f'programmes {old["programmes"]}->{new["programmes"]}, '
            f'overlaps {old["overlaps"]}->{new["overlaps"]}, '
            f'generic ratio {old["generic_ratio"]:.3f}->{new["generic_ratio"]:.3f})'
        )
        sys.exit(0)

    raise SystemExit(
        "EPG gate BLOCK: new English-only guide failed retention/quality checks "
        f'(channels {old["channels"]}->{new["channels"]}, '
        f'programmes {old["programmes"]}->{new["programmes"]}, '
        f'overlaps {old["overlaps"]}->{new["overlaps"]}, '
        f'generic ratio {old["generic_ratio"]:.3f}->{new["generic_ratio"]:.3f})'
    )

print(
    "EPG gate PASS: English-only guide accepted "
    f'(channels={new["channels"]}, programmes={new["programmes"]})'
)
