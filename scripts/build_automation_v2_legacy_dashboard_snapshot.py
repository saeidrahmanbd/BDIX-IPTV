#!/usr/bin/env python3
"""Capture legacy dashboard/report outputs as a hash-pinned, read-only V2 input.

The snapshot deliberately consumes generated reports only. It does not execute
legacy generators, inspect or modify playlists, EPG, logos, or production output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

REPORTS = {
    "playlist_audit": "reports/iptv-playlist-audit.md",
    "epg_coverage": "reports/epg-coverage.md",
    "epg_playlist_audit": "reports/epg-playlist-audit.md",
    "stream_health": "reports/stream-health.md",
    "pre_publish_gate": "reports/pre-publish-gate.md",
    "dashboard_markdown": "reports/Update Report.md",
    "maintenance_report": "reports/maintenance-report.md",
    "maintenance_history": "reports/maintenance-history.json",
    "epg_freshness": "reports/epg-publish-freshness.md",
    "logo_authenticity_manifest": "reports/logo-authenticity-manifest.json",
}
PROTECTED_OUTPUTS = {
    "reports/Update Report.md",
    "reports/maintenance-report.md",
    "assets/dashboard.svg",
    "reports/maintenance-history.json",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_snapshot(root: Path, generated_at: str | None = None) -> dict:
    root = root.resolve(strict=True)
    sources = {}
    for key, relative in REPORTS.items():
        path = root / relative
        if path.is_symlink():
            sources[key] = {"path": relative, "status": "rejected_symlink"}
            continue
        if not path.is_file():
            sources[key] = {"path": relative, "status": "missing"}
            continue
        try:
            raw = path.read_bytes()
            content = raw.decode("utf-8")
            if key.endswith("_json") or key == "maintenance_history":
                json.loads(content)
            sources[key] = {
                "path": relative,
                "status": "available",
                "sha256": sha256(raw),
                "bytes": len(raw),
                "content": content,
            }
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            sources[key] = {
                "path": relative,
                "status": "invalid",
                "error": type(exc).__name__,
            }
    return {
        "schema_version": 1,
        "snapshot_type": "automation-v2-legacy-dashboard-inputs",
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "sources": sources,
        "safety": {
            "production_reports_modified": False,
            "playlists_epg_logos_modified": False,
            "legacy_generators_executed": False,
            "publication_performed": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path,
                        default=Path("reports/automation-v2/legacy-dashboard-input-snapshot.json"))
    args = parser.parse_args()
    root = args.root.resolve(strict=True)
    output = args.output if args.output.is_absolute() else root / args.output
    output = output.absolute()
    if not output.is_relative_to(root):
        parser.error("snapshot output must remain inside repository root")
    relative = output.relative_to(root).as_posix()
    if relative in PROTECTED_OUTPUTS:
        parser.error("snapshot output cannot overwrite a production dashboard/report")
    current = root
    for part in Path(relative).parts:
        current = current / part
        if current.is_symlink():
            parser.error("snapshot output path cannot contain symlinks")
    snapshot = build_snapshot(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "snapshot_type": snapshot["snapshot_type"],
        "output": relative,
        "sources": {k: v["status"] for k, v in snapshot["sources"].items()},
        "safety": snapshot["safety"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
