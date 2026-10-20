#!/usr/bin/env python3
"""Validate freshness and playlist fingerprints for generated IPTV reports.

This gate deliberately checks only reports about IPTV-Playlist.m3u and shared EPG
reports that carry a per-playlist fingerprint. It never edits the playlist.
"""
import hashlib
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

PLAYLIST_REL = Path("IPTV-Playlist.m3u")
MAX_REPORT_AGE = timedelta(hours=48)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_timestamp(value: str):
    value = (value or "").strip()
    if value.endswith(" UTC"):
        value = value[:-4] + "+00:00"
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(value)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def report_timestamp(text: str):
    match = re.search(r"(?:Generated|Last generated):\s*\*\*([^*]+)\*\*", text, re.I)
    return parse_timestamp(match.group(1)) if match else None


def check_reports(root: Path = Path("."), now=None, max_age=MAX_REPORT_AGE):
    """Return a list of actionable errors for the current checkout."""
    root = Path(root)
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    playlist = root / PLAYLIST_REL
    errors = []
    if not playlist.is_file():
        return ["IPTV-Playlist.m3u: missing"]
    current_hash = sha256(playlist)

    # Markdown reports identify exactly which IPTV playlist bytes they audited.
    markdown_reports = {
        "reports/playlist-audit.md": "Source playlist SHA-256",
        "reports/pre-publish-gate.md": "Source playlist SHA-256",
        "reports/epg-coverage.md": "IPTV-Playlist.m3u SHA-256",
        "reports/epg-three-playlist-audit.md": "IPTV-Playlist.m3u SHA-256",
    }
    for relative, marker in markdown_reports.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"{relative}: missing")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        match = re.search(
            rf"{re.escape(marker)}:\s*\*\*([0-9a-f]{{64}})\*\*",
            text,
            re.I,
        )
        if not match:
            errors.append(f"{relative}: missing playlist SHA-256 fingerprint")
        elif match.group(1).lower() != current_hash:
            errors.append(f"{relative}: fingerprint does not match current IPTV-Playlist.m3u")
        generated = report_timestamp(text)
        if generated is None:
            errors.append(f"{relative}: missing or invalid generated timestamp")
        elif generated > now + timedelta(minutes=5):
            errors.append(f"{relative}: generated timestamp is in the future")
        elif now - generated > max_age:
            errors.append(f"{relative}: stale report (older than {max_age.total_seconds() / 3600:g} hours)")

    manifest_path = root / "reports/logo-authenticity-manifest.json"
    if not manifest_path.is_file():
        errors.append("reports/logo-authenticity-manifest.json: missing")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"reports/logo-authenticity-manifest.json: invalid JSON ({exc})")
        else:
            manifest_hash = manifest.get("source_sha256_by_playlist", {}).get("IPTV-Playlist.m3u")
            if not isinstance(manifest_hash, str):
                errors.append("reports/logo-authenticity-manifest.json: missing IPTV playlist fingerprint")
            elif manifest_hash.lower() != current_hash:
                errors.append("reports/logo-authenticity-manifest.json: fingerprint does not match current IPTV-Playlist.m3u")
            generated = parse_timestamp(manifest.get("generated_at_utc", ""))
            if generated is None:
                errors.append("reports/logo-authenticity-manifest.json: missing or invalid generated_at_utc")
            elif generated > now + timedelta(minutes=5):
                errors.append("reports/logo-authenticity-manifest.json: generated timestamp is in the future")
            elif now - generated > max_age:
                errors.append("reports/logo-authenticity-manifest.json: stale manifest (older than 48 hours)")

    return errors


def main():
    errors = check_reports()
    for error in errors:
        print("REPORT_STALE:", error)
    if errors:
        return 1
    print("Report freshness check passed: audit, EPG coverage, pre-publish gate, and logo manifest match the current IPTV-Playlist.m3u.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
