#!/usr/bin/env python3
"""Render a V2 dashboard parity mirror from an immutable legacy report snapshot.

The legacy dashboard is the source of truth during shadow migration. This
renderer preserves its metrics verbatim, verifies the source hash, and appends
V2 candidate diagnostics without recalculating or publishing production data.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def render(snapshot: dict, candidate_snapshot: dict | None = None) -> str:
    if snapshot.get("snapshot_type") != "automation-v2-legacy-dashboard-inputs":
        raise ValueError("input is not a legacy dashboard input snapshot")
    source = snapshot.get("sources", {}).get("dashboard_markdown", {})
    if source.get("status") != "available":
        raise ValueError("legacy dashboard markdown is unavailable in the snapshot")
    content = source.get("content")
    if not isinstance(content, str) or not content.strip():
        raise ValueError("legacy dashboard markdown content is empty")
    actual_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
    if actual_hash != source.get("sha256"):
        raise ValueError("legacy dashboard markdown SHA-256 mismatch")
    sources = snapshot.get("sources", {})
    if not isinstance(sources, dict):
        raise ValueError("legacy snapshot sources must be an object")
    source_rows = []
    for key in sorted(sources):
        item = sources[key]
        if not isinstance(item, dict):
            raise ValueError(f"invalid legacy source record: {key}")
        status = item.get("status", "unavailable")
        digest = item.get("sha256", "—") if status == "available" else "—"
        source_rows.append(f"| {key} | {status} | {digest} |")
    available_count = sum(1 for item in sources.values()
                          if isinstance(item, dict) and item.get("status") == "available")
    lines = [
        "# Automation V2 — Dashboard Parity Mirror", "",
        f"- Snapshot generated: {snapshot.get('generated_at', 'unknown')}",
        f"- Legacy dashboard source SHA-256: {actual_hash}",
        "- Metric authority: **legacy dashboard snapshot (verbatim)**",
        "- This shadow artifact does not replace or write the production dashboard.",
        f"- Captured legacy report inputs: **{available_count}/{len(sources)} available**", "",
        "## Legacy report input provenance", "",
        "| Input | Snapshot status | SHA-256 |",
        "|---|---|---|",
        *source_rows, "",
        "---", "", content.rstrip(), "", "---", "", "## Automation V2 shadow diagnostics", "",
    ]
    if candidate_snapshot is None:
        lines.extend(["- Candidate diagnostics: unavailable",
                      "- Production publishing: disabled",
                      "- Production dashboard modified: no", ""])
    else:
        if candidate_snapshot.get("snapshot_type") != "automation-v2-candidate-diagnostics":
            raise ValueError("candidate input is not a V2 diagnostics snapshot")
        candidate = candidate_snapshot.get("candidate", {})
        logo = candidate_snapshot.get("logo_audit", {})
        proposals = candidate_snapshot.get("logo_repair_candidates", {})
        lines.extend([
            f"- Candidate status: **{candidate.get('status', 'unavailable')}**",
            f"- Candidate allowed: **{bool(candidate.get('allowed', False))}**",
            f"- Candidate business date: {candidate.get('business_day') or 'unavailable'}",
            f"- Candidate baseline: {candidate.get('baseline_commit') or 'unavailable'}",
            f"- Logo audit available: **{bool(logo.get('available', False))}**",
            f"- Missing runtime logo targets: {logo.get('missing_runtime_logo_targets', 'unavailable')}",
            f"- Approved-logo proposals: {proposals.get('proposal_count', 'unavailable')}", "",
        ])
    lines.extend([
        "## Shadow safety", "",
        "- Production playlist, EPG and logo assets modified: **no**",
        "- Production dashboard/report files modified: **no**",
        "- Legacy dashboard generators executed by this renderer: **no**",
        "- Production publication authorized: **no**", "",
    ])
    return "\n".join(lines)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--legacy-snapshot", type=Path,
        default=Path("reports/automation-v2/legacy-dashboard-input-snapshot.json"))
    parser.add_argument("--candidate-snapshot", type=Path,
        default=Path("reports/automation-v2/candidate-diagnostics-snapshot.json"))
    parser.add_argument("--output", type=Path,
        default=Path("reports/automation-v2/dashboard-parity-mirror.md"))
    args = parser.parse_args()
    legacy = json.loads(args.legacy_snapshot.read_text(encoding="utf-8"))
    candidate = json.loads(args.candidate_snapshot.read_text(encoding="utf-8")) if args.candidate_snapshot.is_file() else None
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(legacy, candidate), encoding="utf-8")
    print(f"Wrote shadow dashboard parity mirror: {args.output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
