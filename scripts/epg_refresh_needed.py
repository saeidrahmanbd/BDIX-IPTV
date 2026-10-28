#!/usr/bin/env python3
"""Skip a scheduled EPG rebuild only when the published guide is fresh and matches current playlists."""
from __future__ import annotations

import argparse
import hashlib
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

PLAYLIST_NAMES = ("IPTV-Playlist.m3u", "BDIX-Playlist.m3u", "International-Playlist.m3u")
COVERAGE_REPORTS = ("reports/epg-coverage.md", "reports/epg-three-playlist-audit.md", "reports/epg-unmapped-audit.md")
FRESHNESS_REPORT = "reports/epg-publish-freshness.md"
GUIDE = "epg/epg.xml"
TIMESTAMP_RE = re.compile(r"(?im)^_?(?:Generated|Last generated|Checked):\s*\*\*([^*]+)\*\*")


def parse_timestamp(value: str):
    value = (value or "").strip()
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(value)
    except (TypeError, ValueError):
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def report_timestamp(text: str):
    match = TIMESTAMP_RE.search(text)
    return parse_timestamp(match.group(1)) if match else None


def read_fingerprint(text: str, playlist_name: str):
    match = re.search(
        rf"(?im)^\s*(?:-\s*)?{re.escape(playlist_name)} SHA-256:\s*\*\*([0-9a-f]{{64}})\*\*\s*$",
        text,
    )
    return match.group(1).lower() if match else None


def guide_has_programmes(path: Path) -> bool:
    """Parse the full XMLTV file and return whether it contains programme entries."""
    found = False
    for _, element in ET.iterparse(path, events=("end",)):
        if element.tag == "programme":
            found = True
        element.clear()
    return found


def assess_freshness(root: Path = Path("."), now=None, max_age_hours: float = 8):
    """Return (safe_to_skip_refresh, reasons). Missing/invalid/stale inputs require a refresh."""
    root = Path(root)
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    now = now.astimezone(timezone.utc)
    max_age = timedelta(hours=max_age_hours)
    errors = []
    playlist_hashes = {}

    for name in PLAYLIST_NAMES:
        path = root / name
        if not path.is_file():
            return False, [f"{name}: missing"]
        playlist_hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()

    for relative in COVERAGE_REPORTS:
        path = root / relative
        if not path.is_file():
            errors.append(f"{relative}: missing")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        timestamp = report_timestamp(text)
        if timestamp is None:
            errors.append(f"{relative}: missing or invalid generation timestamp")
        elif timestamp > now + timedelta(minutes=5):
            errors.append(f"{relative}: timestamp is in the future")
        elif now - timestamp > max_age:
            errors.append(f"{relative}: stale report")
        for playlist_name, expected_hash in playlist_hashes.items():
            actual_hash = read_fingerprint(text, playlist_name)
            if actual_hash is None:
                errors.append(f"{relative}: missing {playlist_name} fingerprint")
            elif actual_hash != expected_hash:
                errors.append(f"{relative}: fingerprint does not match current {playlist_name}")

    freshness_path = root / FRESHNESS_REPORT
    if not freshness_path.is_file():
        errors.append(f"{FRESHNESS_REPORT}: missing")
    else:
        freshness_text = freshness_path.read_text(encoding="utf-8", errors="replace")
        checked_at = report_timestamp(freshness_text)
        if checked_at is None:
            errors.append(f"{FRESHNESS_REPORT}: missing or invalid check timestamp")
        elif checked_at > now + timedelta(minutes=5):
            errors.append(f"{FRESHNESS_REPORT}: check timestamp is in the future")
        elif now - checked_at > max_age:
            errors.append(f"{FRESHNESS_REPORT}: stale report")
        if not re.search(r"(?im)^Status:\s*\*\*PASS\*\*\s*$", freshness_text):
            errors.append(f"{FRESHNESS_REPORT}: status is not PASS")

    guide = root / GUIDE
    if not guide.is_file() or guide.stat().st_size == 0:
        errors.append(f"{GUIDE}: missing or empty")
    else:
        try:
            if not guide_has_programmes(guide):
                errors.append(f"{GUIDE}: contains no programme entries")
        except (OSError, ET.ParseError) as exc:
            errors.append(f"{GUIDE}: invalid XMLTV ({exc})")

    return not errors, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-age-hours", type=float, default=8)
    args = parser.parse_args()
    fresh, reasons = assess_freshness(max_age_hours=args.max_age_hours)
    if fresh:
        print("EPG is fresh: guide, coverage reports, timestamps and all three playlist fingerprints match.")
        return 0
    print("EPG refresh required:")
    for reason in reasons:
        print(f"- {reason}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
