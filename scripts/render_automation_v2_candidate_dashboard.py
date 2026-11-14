#!/usr/bin/env python3
"""Render a human-readable V2 diagnostics dashboard from a JSON snapshot only."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def render(snapshot: dict) -> str:
    candidate = snapshot.get("candidate", {})
    logo = snapshot.get("logo_audit", {})
    proposals = snapshot.get("logo_repair_candidates", {})
    safety = snapshot.get("safety", {})
    status = str(candidate.get("status", "unavailable"))
    reason = str(candidate.get("reason", "")).replace("\n", " ").strip()
    lines = [
        "# Automation V2 — Candidate Diagnostics",
        "",
        f"- Generated: {snapshot.get('generated_at', 'unknown')}",
        f"- Business date: {candidate.get('business_day') or 'unavailable'}",
        f"- Baseline: {candidate.get('baseline_commit') or 'unavailable'}",
        f"- Candidate status: **{status}**",
        f"- Candidate allowed: **{'yes' if candidate.get('allowed') else 'no'}**",
        f"- Owner-review transaction: **{'ready' if candidate.get('transaction_ready_for_owner_review') else 'not ready / unavailable'}**",
        f"- Transaction ID: {candidate.get('transaction_id') or 'unavailable'}",
        "",
        "## Candidate outcome",
        "",
        reason or "No candidate-run reason was recorded.",
        "",
        "## Logo diagnostics",
        "",
        f"- Reference audit available: {'yes' if logo.get('available') else 'no'}",
        f"- Missing runtime logo targets: {logo.get('missing_runtime_logo_targets') if logo.get('missing_runtime_logo_targets') is not None else 'unavailable'}",
        f"- Exact duplicate groups: {logo.get('exact_duplicate_groups') if logo.get('exact_duplicate_groups') is not None else 'unavailable'}",
        f"- Repair proposals: {proposals.get('proposal_count', 'unavailable')}",
        f"- Unique exact-match proposals: {proposals.get('unique_exact_match', 'unavailable')}",
        f"- Ambiguous matches (not assigned): {proposals.get('ambiguous_exact_match', 'unavailable')}",
        "",
        "## Safety",
        "",
        f"- Production publish enabled: {bool(safety.get('production_publish_enabled', False))}",
        f"- Production dashboard written: {bool(safety.get('production_dashboard_written', False))}",
        f"- Playlist / EPG / logo assets modified: {bool(safety.get('playlist_epg_logo_assets_modified', False))}",
        "",
        "> This report is a read-only artifact generated from candidate diagnostics. It is not the production website dashboard and does not authorize publication.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", type=Path, default=Path("reports/automation-v2/candidate-diagnostics-snapshot.json"))
    parser.add_argument("--output", type=Path, default=Path("reports/automation-v2/candidate-dashboard.md"))
    args = parser.parse_args()
    snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
    if not isinstance(snapshot, dict) or snapshot.get("snapshot_type") != "automation-v2-candidate-diagnostics":
        raise ValueError("input is not an Automation V2 candidate diagnostics snapshot")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(snapshot), encoding="utf-8")
    print(f"Wrote read-only candidate dashboard: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
