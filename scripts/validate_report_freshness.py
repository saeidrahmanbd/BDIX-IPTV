#!/usr/bin/env python3
"""Validate report timestamps and source fingerprints for IPTV publication."""
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

PLAYLIST_NAMES = ("IPTV-Playlist.m3u", "BDIX-Playlist.m3u", "International-Playlist.m3u")
MAX_REPORT_AGE = timedelta(hours=48)
SINGLE_PLAYLIST_REPORTS = {
    "reports/playlist-audit.md": ("IPTV-Playlist.m3u", ("Source playlist SHA-256", "Playlist SHA-256")),
    "reports/pre-publish-gate.md": ("IPTV-Playlist.m3u", ("Source playlist SHA-256",)),
    "reports/iptv-metadata-backfill.md": ("IPTV-Playlist.m3u", ("After playlist SHA-256", "Playlist SHA-256", "Source playlist SHA-256")),
    "reports/iptv-fragile-streams.md": ("IPTV-Playlist.m3u", ("IPTV-Playlist.m3u SHA-256",)),
    "reports/stream-risk-review.md": ("IPTV-Playlist.m3u", ("IPTV-Playlist.m3u SHA-256",)),
    "reports/metadata-normalization.md": ("IPTV-Playlist.m3u", ("Source playlist SHA-256",)),
    "reports/Update Report.md": ("IPTV-Playlist.m3u", ("Source playlist SHA-256",)),
    "reports/maintenance-report.md": ("IPTV-Playlist.m3u", ("Source playlist SHA-256",)),
    "reports/playlist-logo-repair-results.md": ("IPTV-Playlist.m3u", ("Source playlist SHA-256",)),
}
SHARED_EPG_REPORTS = ("reports/epg-coverage.md", "reports/epg-three-playlist-audit.md", "reports/epg-unmapped-audit.md")
PROVENANCE_REPORT = "reports/logo-provenance-review.md"
CROSS_PLAYLIST_METADATA_REPORT = "reports/cross-playlist-metadata-backfill.md"
STREAM_HEALTH_REPORT = "reports/stream-health.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stream_url_inventory_sha256(path: Path) -> str:
    """Hash sorted exact stream URLs; unlike a playlist hash this ignores metadata edits."""
    urls = sorted(
        line.strip()
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip().startswith(("http://", "https://"))
    )
    return hashlib.sha256("\n".join(urls).encode("utf-8")).hexdigest()


def parse_timestamp(value: str):
    value = (value or "").strip()
    if value.endswith(" UTC"):
        value = value[:-4] + "+00:00"
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
    match = re.search(r"(?im)^_?(?:Generated|Last generated):\s*\*\*([^*]+)\*\*", text)
    return parse_timestamp(match.group(1)) if match else None


def read_fingerprint(text: str, labels):
    """Read a 64-character SHA-256 in the standard Markdown report format."""
    for label in labels:
        match = re.search(rf"(?im)^\s*(?:-\s*)?{re.escape(label)}:\s*\*\*([0-9a-f]{{64}})\*\*\s*$", text)
        if match:
            return match.group(1).lower()
    return None


def check_timestamp(relative: str, text: str, now, max_age, errors):
    generated = report_timestamp(text)
    if generated is None:
        errors.append(f"{relative}: missing or invalid generated timestamp")
    elif generated > now + timedelta(minutes=5):
        errors.append(f"{relative}: generated timestamp is in the future")
    elif now - generated > max_age:
        errors.append(f"{relative}: stale report (older than {max_age.total_seconds() / 3600:g} hours)")


def check_reports(root: Path = Path("."), now=None, max_age=MAX_REPORT_AGE, mode="all"):
    """Return errors. all checks active outputs and health; generated checks report-sync outputs."""
    root = Path(root)
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    if mode not in {"all", "generated"}:
        return [f"Unknown freshness validation mode: {mode}"]
    hashes = {}
    for name in PLAYLIST_NAMES:
        path = root / name
        if not path.is_file():
            return [f"{name}: missing"]
        hashes[name] = sha256(path)

    errors = []
    report_paths = list(SINGLE_PLAYLIST_REPORTS) + list(SHARED_EPG_REPORTS) + [PROVENANCE_REPORT, CROSS_PLAYLIST_METADATA_REPORT]
    report_paths.append(STREAM_HEALTH_REPORT)

    for relative in report_paths:
        path = root / relative
        if not path.is_file():
            errors.append(f"{relative}: missing")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        check_timestamp(relative, text, now, max_age, errors)
        if relative in SINGLE_PLAYLIST_REPORTS:
            playlist_name, labels = SINGLE_PLAYLIST_REPORTS[relative]
            actual = read_fingerprint(text, labels)
            if actual is None:
                errors.append(f"{relative}: missing {playlist_name} SHA-256 fingerprint")
            elif actual != hashes[playlist_name]:
                errors.append(f"{relative}: fingerprint does not match current {playlist_name}")
        elif relative in SHARED_EPG_REPORTS or relative in {PROVENANCE_REPORT, CROSS_PLAYLIST_METADATA_REPORT}:
            for playlist_name in PLAYLIST_NAMES:
                actual = read_fingerprint(text, (f"{playlist_name} SHA-256",))
                if actual is None:
                    errors.append(f"{relative}: missing {playlist_name} SHA-256 fingerprint")
                elif actual != hashes[playlist_name]:
                    errors.append(f"{relative}: fingerprint does not match current {playlist_name}")

    manifest_path = root / "reports/logo-authenticity-manifest.json"
    if not manifest_path.is_file():
        errors.append("reports/logo-authenticity-manifest.json: missing")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"reports/logo-authenticity-manifest.json: invalid JSON ({exc})")
        else:
            source_hashes = manifest.get("source_sha256_by_playlist", {})
            for playlist_name in PLAYLIST_NAMES:
                recorded = source_hashes.get(playlist_name)
                if not isinstance(recorded, str):
                    errors.append(f"reports/logo-authenticity-manifest.json: missing {playlist_name} fingerprint")
                elif recorded.lower() != hashes[playlist_name]:
                    errors.append(f"reports/logo-authenticity-manifest.json: fingerprint does not match current {playlist_name}")
            generated = parse_timestamp(manifest.get("generated_at_utc", ""))
            if generated is None:
                errors.append("reports/logo-authenticity-manifest.json: missing or invalid generated_at_utc")
            elif generated > now + timedelta(minutes=5):
                errors.append("reports/logo-authenticity-manifest.json: generated timestamp is in the future")
            elif now - generated > max_age:
                errors.append("reports/logo-authenticity-manifest.json: stale manifest (older than 48 hours)")

    health_path = root / STREAM_HEALTH_REPORT
    if health_path.is_file():
        health_text = health_path.read_text(encoding="utf-8", errors="replace")
        expected = stream_url_inventory_sha256(root / PLAYLIST_NAMES[0])
        actual = read_fingerprint(health_text, ("Stream URL inventory SHA-256",))
        if actual is None:
            errors.append(f"{STREAM_HEALTH_REPORT}: missing stream URL inventory SHA-256")
        elif actual != expected:
            errors.append(f"{STREAM_HEALTH_REPORT}: stream URL inventory fingerprint does not match current playlist")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("all", "generated"), default="all")
    args = parser.parse_args()
    errors = check_reports(mode=args.mode)
    for error in errors:
        print("REPORT_STALE:", error)
    if errors:
        return 1
    print(f"Report freshness check passed ({args.mode}): timestamps and source fingerprints match current playlist inputs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
