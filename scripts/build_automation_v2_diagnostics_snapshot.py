#!/usr/bin/env python3
"""Build a read-only, immutable diagnostics snapshot from V2 candidate reports.

This is deliberately not the production website dashboard generator. It consumes
only reports already produced by the candidate workflow and never reads or writes
playlists, EPG, logos, Git state, or production dashboard files.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def _load(path: Path) -> tuple[dict | None, str | None]:
    if not path.is_file():
        return None, "missing"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return None, f"invalid: {type(exc).__name__}"
    if not isinstance(value, dict):
        return None, "invalid: expected JSON object"
    return value, None


def _sha(path: Path) -> str | None:
    if not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_snapshot(root: Path, generated_at: str | None = None) -> dict:
    reports = root / "reports" / "automation-v2"
    run_path = reports / "candidate-run.json"
    logo_path = reports / "candidate-logo-reference-audit.json"
    run, run_error = _load(run_path)
    logo, logo_error = _load(logo_path)

    transaction_path = None
    transaction = None
    if run and isinstance(run.get("transaction_path"), str):
        raw = Path(run["transaction_path"])
        candidate = raw if raw.is_absolute() else root / raw
        try:
            resolved_root = root.resolve()
            resolved = candidate.resolve()
            if resolved.is_relative_to(resolved_root) and resolved.is_dir():
                transaction_path = resolved
                transaction, _ = _load(resolved / "transaction-bundle.json")
        except OSError:
            transaction_path = None

    run_status = str(run.get("status", "unavailable")) if run else "unavailable"
    snapshot = {
        "schema_version": 1,
        "snapshot_type": "automation-v2-candidate-diagnostics",
        "generated_at": generated_at or datetime.now(timezone.utc).isoformat(),
        "source_files": {
            "candidate_run": {"path": "reports/automation-v2/candidate-run.json",
                              "sha256": _sha(run_path), "error": run_error},
            "logo_reference_audit": {"path": "reports/automation-v2/candidate-logo-reference-audit.json",
                                     "sha256": _sha(logo_path), "error": logo_error},
        },
        "candidate": {
            "status": run_status,
            "allowed": bool(run.get("allowed", False)) if run else False,
            "publish": bool(run.get("publish", False)) if run else False,
            "production_files_modified": bool(run.get("production_files_modified", False)) if run else False,
            "reason": str(run.get("reason", ""))[:2000] if run else "Candidate run report unavailable",
            "business_day": run.get("business_day") if run else None,
            "baseline_commit": run.get("baseline_commit") if run else None,
            "transaction_id": run.get("transaction_id") if run else None,
            "transaction_ready_for_owner_review": bool(transaction.get("ready_for_owner_review", False)) if transaction else False,
        },
        "logo_audit": {
            "available": logo is not None,
            "logo_image_files": logo.get("logo_image_files") if logo else None,
            "playlist_referenced_logo_files": logo.get("playlist_referenced_logo_files") if logo else None,
            "missing_runtime_logo_targets": len(logo.get("missing_runtime_logo_targets", [])) if logo else None,
            "exact_duplicate_groups": logo.get("exact_duplicate_groups") if logo else None,
            "deletion_performed": bool(logo.get("deletion_performed", False)) if logo else False,
            "quarantine_performed": bool(logo.get("quarantine_performed", False)) if logo else False,
        },
        "safety": {
            "production_publish_enabled": False,
            "production_dashboard_written": False,
            "playlist_epg_logo_assets_modified": False,
            "source_reports_modified": False,
        },
    }
    return snapshot


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("reports/automation-v2/candidate-diagnostics-snapshot.json"))
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output if args.output.is_absolute() else root / args.output
    snapshot = build_snapshot(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(snapshot, indent=2, sort_keys=True))
    # Missing reports are represented explicitly so the workflow can still upload
    # a useful failure snapshot after an earlier candidate step fails.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
