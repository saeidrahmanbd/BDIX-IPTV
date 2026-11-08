#!/usr/bin/env python3
"""Validate report timestamps and source fingerprints for IPTV publication."""
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

PLAYLIST_NAMES = ("IPTV-Playlist.m3u", "International-Playlist.m3u")
MAX_REPORT_AGE = timedelta(hours=48)
SINGLE_PLAYLIST_REPORTS = {
    "reports/iptv-playlist-audit.md": ("IPTV-Playlist.m3u", ("Source playlist SHA-256", "Playlist SHA-256")),
    "reports/pre-publish-gate.md": ("IPTV-Playlist.m3u", ("Source playlist SHA-256",)),
    "reports/iptv-metadata-backfill.md": ("IPTV-Playlist.m3u", ("After playlist SHA-256", "Playlist SHA-256", "Source playlist SHA-256")),
    "reports/iptv-fragile-streams.md": ("IPTV-Playlist.m3u", ("IPTV-Playlist.m3u SHA-256",)),
    "reports/stream-risk-review.md": ("IPTV-Playlist.m3u", ("IPTV-Playlist.m3u SHA-256",)),
    "reports/metadata-normalization.md": ("IPTV-Playlist.m3u", ("Source playlist SHA-256",)),
    "reports/Update Report.md": ("IPTV-Playlist.m3u", ("Source playlist SHA-256",)),
    "reports/maintenance-report.md": ("IPTV-Playlist.m3u", ("Source playlist SHA-256",)),
    "reports/playlist-logo-repair-results.md": ("IPTV-Playlist.m3u", ("Source playlist SHA-256",)),
}
SHARED_EPG_REPORTS = ("reports/epg-coverage.md", "reports/epg-playlist-audit.md", "reports/epg-unmapped-audit.md")
SHARED_PLAYLIST_REPORTS = ("reports/logo-asset-quality-audit.md",)
TIMESTAMP_ONLY_REPORTS = ("reports/epg-publish-freshness.md",)
PROVENANCE_REPORT = "reports/logo-provenance-review.md"
CROSS_PLAYLIST_METADATA_REPORT = "reports/playlist-metadata-backfill.md"
STREAM_HEALTH_REPORT = "reports/stream-health.md"
# Reports owned by IPTV New Channel Discovery; other maintenance reports have separate owners.
DISCOVERY_REPORTS = (
    "reports/iptv-channel-discovery.md",
    "reports/metadata-normalization.md",
    "reports/logo-asset-quality-audit.md",
    "reports/playlist-logo-repair-results.md",
)


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
    match = re.search(r"(?im)^_?(?:Generated|Last generated|Checked):\s*\*\*([^*]+)\*\*", text)
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


IPTV_EPG_JSON = "reports/epg-iptv-coverage.json"
IPTV_EPG_INVENTORY_CSV = "reports/epg-research-inventory.csv"
IPTV_EPG_INVENTORY_MD = "reports/epg-research-inventory.md"


def check_iptv_epg_research(root: Path, now, max_age, hashes, errors):
    """IPTV-only EPG coverage JSON and research inventory must be fresh and mutually consistent.

    Depends only on IPTV-Playlist.m3u, epg/epg.xml and the generated reports. It never reads
    International-Playlist.m3u.
    """
    import csv
    import json
    import re

    json_path, csv_path, md_path = root / IPTV_EPG_JSON, root / IPTV_EPG_INVENTORY_CSV, root / IPTV_EPG_INVENTORY_MD
    for path in (json_path, csv_path, md_path):
        if not path.is_file():
            errors.append(f"{path.relative_to(root).as_posix()}: missing IPTV-only EPG research output")
    if not all(p.is_file() for p in (json_path, csv_path, md_path)):
        return
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        errors.append(f"{IPTV_EPG_JSON}: invalid JSON")
        return
    try:
        generated = datetime.fromisoformat(str(data.get("generated_at", "")))
        if generated.tzinfo is None:
            generated = generated.replace(tzinfo=timezone.utc)
    except ValueError:
        errors.append(f"{IPTV_EPG_JSON}: missing or invalid generated_at")
    else:
        if now - generated > max_age:
            errors.append(f"{IPTV_EPG_JSON}: stale (older than {max_age.total_seconds() / 3600:g} hours)")
    if data.get("inventory_sha256") != hashes["IPTV-Playlist.m3u"]:
        errors.append(f"{IPTV_EPG_JSON}: inventory_sha256 does not match current IPTV-Playlist.m3u")
    guide = root / "epg" / "epg.xml"
    if not guide.is_file() or data.get("guide_sha256") != sha256(guide):
        errors.append(f"{IPTV_EPG_JSON}: guide_sha256 does not match current epg/epg.xml")
    csv_sha = hashlib.sha256(csv_path.read_bytes()).hexdigest()
    if data.get("research_inventory_csv_sha256") != csv_sha:
        errors.append(f"{IPTV_EPG_JSON}: research_inventory_csv_sha256 does not match {IPTV_EPG_INVENTORY_CSV}")
    with csv_path.open(encoding="utf-8", newline="") as handle:
        csv_rows = list(csv.DictReader(handle))
    if data.get("research_inventory_records") != len(csv_rows):
        errors.append(f"{IPTV_EPG_JSON}: research_inventory_records does not match CSV row count")
    md_text = md_path.read_text(encoding="utf-8", errors="replace")
    md_fp = re.search(r"IPTV-Playlist\.m3u SHA-256:\s*\*\*([0-9a-f]{64})\*\*", md_text)
    if not md_fp or md_fp.group(1) != hashes["IPTV-Playlist.m3u"]:
        errors.append(f"{IPTV_EPG_INVENTORY_MD}: IPTV-Playlist.m3u fingerprint does not match current playlist")
    md_count = re.search(r"Channels needing research:\s*\*\*(\d+)\*\*", md_text)
    if not md_count or int(md_count.group(1)) != len(csv_rows):
        errors.append(f"{IPTV_EPG_INVENTORY_MD}: channel count does not match CSV row count")
    md_usable = re.search(r"Usable now:\s*\*\*(\d+)\*\*", md_text)
    if not md_usable or md_usable.group(1) != str(data.get("research_inventory_usable_now")):
        errors.append(f"{IPTV_EPG_INVENTORY_MD}: usable count does not match {IPTV_EPG_JSON}")


def check_reports(root: Path = Path("."), now=None, max_age=MAX_REPORT_AGE, mode="all", epg_publication_approved=None):
    """Return freshness errors for all, maintenance, EPG-only, or discovery-owned reports.

    The legacy epg_publication_approved argument is accepted for compatibility
    but ignored; it must never hide EPG freshness or fingerprint failures.
    """
    root = Path(root)
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    if mode not in {"all", "generated", "epg", "discovery"}:
        return [f"Unknown freshness validation mode: {mode}"]
    hashes = {}
    for name in PLAYLIST_NAMES:
        path = root / name
        if not path.is_file():
            # EPG-only validation depends on IPTV-Playlist.m3u alone; a missing
            # International playlist must not break it.
            if mode == "epg" and name != "IPTV-Playlist.m3u":
                continue
            return [f"{name}: missing"]
        hashes[name] = sha256(path)

    errors = []
    generated_paths = (
        list(SINGLE_PLAYLIST_REPORTS)
        + list(SHARED_PLAYLIST_REPORTS)
        + [PROVENANCE_REPORT, CROSS_PLAYLIST_METADATA_REPORT, STREAM_HEALTH_REPORT]
    )
    epg_paths = list(SHARED_EPG_REPORTS) + list(TIMESTAMP_ONLY_REPORTS)
    # The playlist workflow checks only reports it owns; the EPG workflow
    # explicitly validates the shared EPG reports after it regenerates them.
    # "all" always includes EPG reports, independent of any legacy approval flag.
    report_paths = (
        generated_paths + epg_paths if mode == "all"
        else epg_paths if mode == "epg"
        else list(DISCOVERY_REPORTS) if mode == "discovery"
        else generated_paths
    )

    for relative in report_paths:
        path = root / relative
        if not path.is_file():
            errors.append(f"{relative}: missing")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        check_timestamp(relative, text, now, max_age, errors)
        if mode == "discovery" and relative == "reports/iptv-channel-discovery.md":
            generated = report_timestamp(text)
            if generated is not None:
                bd_tz = ZoneInfo("Asia/Dhaka")
                if generated.astimezone(bd_tz).date() != now.astimezone(bd_tz).date():
                    errors.append(
                        f"{relative}: discovery report was not regenerated for the current Bangladesh date"
                    )
        if relative in SINGLE_PLAYLIST_REPORTS:
            playlist_name, labels = SINGLE_PLAYLIST_REPORTS[relative]
            actual = read_fingerprint(text, labels)
            if actual is None:
                errors.append(f"{relative}: missing {playlist_name} SHA-256 fingerprint")
            elif actual != hashes[playlist_name]:
                errors.append(f"{relative}: fingerprint does not match current {playlist_name}")
        elif relative in SHARED_EPG_REPORTS:
            # EPG headline reports are measured on IPTV-Playlist.m3u only; International is out of EPG scope.
            actual = read_fingerprint(text, ("IPTV-Playlist.m3u SHA-256",))
            if actual is None:
                errors.append(f"{relative}: missing IPTV-Playlist.m3u SHA-256 fingerprint")
            elif actual != hashes["IPTV-Playlist.m3u"]:
                errors.append(f"{relative}: fingerprint does not match current IPTV-Playlist.m3u")
        elif relative in SHARED_PLAYLIST_REPORTS or relative in {PROVENANCE_REPORT, CROSS_PLAYLIST_METADATA_REPORT}:
            for playlist_name in PLAYLIST_NAMES:
                actual = read_fingerprint(text, (f"{playlist_name} SHA-256",))
                if actual is None:
                    errors.append(f"{relative}: missing {playlist_name} SHA-256 fingerprint")
                elif actual != hashes[playlist_name]:
                    errors.append(f"{relative}: fingerprint does not match current {playlist_name}")

    if mode in {"all", "generated", "discovery"}:
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

    if mode in {"all", "generated"}:
        health_path = root / STREAM_HEALTH_REPORT
        if health_path.is_file():
            health_text = health_path.read_text(encoding="utf-8", errors="replace")
            expected = stream_url_inventory_sha256(root / PLAYLIST_NAMES[0])
            actual = read_fingerprint(health_text, ("Stream URL inventory SHA-256",))
            if actual is None:
                errors.append(f"{STREAM_HEALTH_REPORT}: missing stream URL inventory SHA-256")
            elif actual != expected:
                errors.append(f"{STREAM_HEALTH_REPORT}: stream URL inventory fingerprint does not match current playlist")
    if mode in {"all", "epg"}:
        check_iptv_epg_research(root, now, max_age, hashes, errors)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("all", "generated", "epg", "discovery"), default="all")
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
