#!/usr/bin/env python3
"""Run the full Automation V2 candidate-only bundle; production files remain read-only."""
from __future__ import annotations

import argparse
from datetime import datetime
import json
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from automation.core.github_state_store import store_from_environment
from automation.core.v2_candidate_runner import run_candidate_bundle


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--baseline-commit", required=True)
    parser.add_argument("--epg-timeout-seconds", type=int, default=1200)
    parser.add_argument("--probe-timeout-seconds", type=int, default=8)
    args = parser.parse_args()

    today = datetime.now(ZoneInfo("Asia/Dhaka")).date()
    store = store_from_environment()
    decision, result = run_candidate_bundle(
        args.root,
        today,
        args.baseline_commit,
        store,
        epg_timeout_seconds=args.epg_timeout_seconds,
        probe_timeout_seconds=args.probe_timeout_seconds,
    )
    report = {
        "schema_version": 1,
        "timezone": "Asia/Dhaka",
        "business_day": today.isoformat(),
        "baseline_commit": args.baseline_commit,
        "allowed": decision.allowed,
        "reason": decision.reason,
        "publish": False,
        "production_files_modified": False,
    }
    if result is None:
        report["status"] = "skipped"
    else:
        report.update({
            "status": "staged_for_owner_review",
            "transaction_id": result.transaction_id,
            "transaction_path": result.transaction_path,
            "iptv_candidate_rows": result.iptv_candidate_rows,
            "international_candidate_rows": result.international_candidate_rows,
            "international_probed": result.international_probed,
            "international_reused": result.international_reused,
            "epg_programmes": result.epg_programmes,
        })
    output = ROOT / "reports" / "automation-v2" / "candidate-run.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    if not decision.allowed and "already completed successfully" not in decision.reason:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
