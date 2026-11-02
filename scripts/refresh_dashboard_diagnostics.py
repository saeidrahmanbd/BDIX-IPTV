#!/usr/bin/env python3
"""Rebuild dashboard inputs from the committed two-playlist state after a blocked maintenance run.

This is a diagnostics-only recovery path: it never weakens the audit or pre-publish gate,
never deletes streams, and never manufactures missing logos or EPG schedules.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAYLISTS = ("IPTV-Playlist.m3u", "International-Playlist.m3u")


def run_script(relative: str, accepted: tuple[int, ...] = (0,)) -> int:
    command = [sys.executable, str(ROOT / relative)]
    print(f"\n[dashboard-recovery] $ {' '.join(command)}", flush=True)
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode not in accepted:
        raise SystemExit(f"{relative} failed with exit code {result.returncode}")
    if result.returncode:
        print(
            f"[dashboard-recovery] {relative} reported blocking findings "
            f"(exit {result.returncode}); its report is retained for the dashboard.",
            flush=True,
        )
    return result.returncode


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def url_inventory_sha256(path: Path) -> str:
    urls = sorted(
        line.strip()
        for line in path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip().startswith(("http://", "https://"))
    )
    return hashlib.sha256("\n".join(urls).encode("utf-8")).hexdigest()


def report_fingerprint(path: Path, label: str) -> str:
    if not path.is_file():
        raise SystemExit(f"Required dashboard input is missing: {path.relative_to(ROOT)}")
    match = re.search(
        rf"(?im)^\s*(?:-\s*)?{re.escape(label)}:\s*\*\*([0-9a-f]{{64}})\*\*\s*$",
        path.read_text(encoding="utf-8", errors="replace"),
    )
    return match.group(1).lower() if match else ""


def verify_dashboard_inputs() -> None:
    main_path = ROOT / "IPTV-Playlist.m3u"
    international_path = ROOT / "International-Playlist.m3u"
    hashes = {
        "IPTV-Playlist.m3u": sha256(main_path),
        "International-Playlist.m3u": sha256(international_path),
    }

    for relative in ("reports/iptv-playlist-audit.md", "reports/pre-publish-gate.md"):
        path = ROOT / relative
        actual = report_fingerprint(path, "Source playlist SHA-256")
        if actual != hashes["IPTV-Playlist.m3u"]:
            raise SystemExit(f"{relative} does not match the committed IPTV playlist.")

    health_path = ROOT / "reports/stream-health.md"
    actual_health = report_fingerprint(health_path, "Stream URL inventory SHA-256")
    if actual_health != url_inventory_sha256(main_path):
        raise SystemExit("Stream-health report does not match the committed IPTV stream URLs.")

    manifest_path = ROOT / "reports/logo-authenticity-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest_hashes = manifest.get("source_sha256_by_playlist", {})
    for playlist, digest in hashes.items():
        if str(manifest_hashes.get(playlist, "")).lower() != digest:
            raise SystemExit(f"Logo authenticity manifest does not match {playlist}.")

    for relative in (
        "reports/logo-asset-quality-audit.md",
        "reports/logo-provenance-review.md",
    ):
        path = ROOT / relative
        for playlist, digest in hashes.items():
            actual = report_fingerprint(path, f"{playlist} SHA-256")
            if actual != digest:
                raise SystemExit(f"{relative} does not match {playlist}.")

    dashboard_svg = ROOT / "assets/dashboard.svg"
    dashboard_md = ROOT / "reports/Update Report.md"
    maintenance_md = ROOT / "reports/maintenance-report.md"
    for path in (dashboard_svg, dashboard_md, maintenance_md):
        if not path.is_file() or path.stat().st_size == 0:
            raise SystemExit(f"Dashboard output is missing or empty: {path.relative_to(ROOT)}")

    # The dashboard must reflect the current gate result, including BLOCK.
    gate_text = (ROOT / "reports/pre-publish-gate.md").read_text(encoding="utf-8")
    gate = re.search(r"(?im)^Status:\s*\*\*(PASS|BLOCK)\*\*\s*$", gate_text)
    if not gate:
        raise SystemExit("Pre-publish gate report has no valid PASS/BLOCK status.")
    dashboard_text = dashboard_md.read_text(encoding="utf-8", errors="replace")
    if f"Pre-publish gate status: **{gate.group(1)}**" not in dashboard_text:
        raise SystemExit("Dashboard summary does not show the current pre-publish gate status.")

    print(
        "[dashboard-recovery] Verified current playlist fingerprints, audit, gate, "
        "stream health, logo reports and dashboard outputs.",
        flush=True,
    )
    print(f"[dashboard-recovery] Pre-publish gate: {gate.group(1)}", flush=True)


def main() -> None:
    for playlist in PLAYLISTS:
        if not (ROOT / playlist).is_file():
            raise SystemExit(f"Required maintained playlist is missing: {playlist}")

    # These metadata-only backfills are part of normal maintenance and regenerate
    # their fingerprinted reports before the final audit is created.
    run_script("scripts/iptv_metadata_backfill.py")
    run_script("scripts/backfill_cross_playlist_metadata.py")

    # Read-only technical logo audit; do not fabricate or assign missing logos.
    run_script("scripts/repair_logo_asset_technical_quality.py")

    # The report-generating audit and gate may return 1 when real blockers exist.
    audit_status = run_script("scripts/audit_playlist.py", accepted=(0, 1))
    gate_status = run_script("scripts/pre_publish_gate.py", accepted=(0, 1))

    run_script("scripts/stream_health.py")
    run_script("scripts/report_iptv_fragile_streams.py")
    run_script("scripts/stream_risk_review.py")
    run_script("scripts/build_identity_index.py")
    run_script("scripts/generate_logo_authenticity_manifest.py")
    run_script("scripts/generate_logo_repair_summary.py")
    run_script("scripts/generate_logo_provenance_review.py")
    run_script("scripts/generate_metadata_normalization_report.py")
    run_script("scripts/record_maintenance_history.py")
    run_script("scripts/generate_dashboard.py")

    # Check the broader report set. Auxiliary findings are logged; the dashboard
    # is still publishable only after its own inputs pass verify_dashboard_inputs().
    freshness_status = run_script("scripts/validate_report_freshness.py", accepted=(0, 1))
    verify_dashboard_inputs()

    if audit_status or gate_status:
        print(
            "[dashboard-recovery] Dashboard is fresh and accurately reports blocking "
            "playlist/logo findings. No safety gate was bypassed.",
            flush=True,
        )
    else:
        print("[dashboard-recovery] Dashboard is fresh; audit and gate both pass.", flush=True)
    if freshness_status:
        print(
            "[dashboard-recovery] One or more auxiliary generated reports still need "
            "separate freshness attention; critical dashboard inputs have been verified.",
            flush=True,
        )

    # The manifest tool stages logos/ itself. Leave logo binaries unstaged; the
    # workflow explicitly stages report artifacts, playlist metadata and dashboard.
    subprocess.run(["git", "reset", "--", "logos/"], cwd=ROOT, check=False)


if __name__ == "__main__":
    main()
