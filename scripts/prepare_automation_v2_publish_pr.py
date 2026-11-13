#!/usr/bin/env python3
"""Validate a successful V2 shadow artifact and prepare a production-change PR branch.

This script never pushes to main. It only writes the three allowlisted files into a
clean worktree after verifying the artifact, baseline, preservation contracts and EPG.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

from automation.core.playlist_contract import (
    parse_rows,
    assert_iptv_existing_rows_preserved,
)
from automation.engines.international.candidate_engine import (
    assert_international_existing_rows_preserved,
)
from automation.engines.epg.validator import validate_xmltv

PRODUCTION_PATHS = (
    "IPTV-Playlist.m3u",
    "International-Playlist.m3u",
    "epg/epg.xml",
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def git_bytes(root: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", *args], cwd=root, check=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout


def _safe_artifact_file(root: Path, path: Path, label: str) -> Path:
    root_resolved = root.resolve()
    try:
        relative = path.relative_to(root_resolved)
    except ValueError as exc:
        raise ValueError(f"{label} escapes the candidate artifact") from exc
    current = root_resolved
    for part in relative.parts:
        current = current / part
        if current.is_symlink() or not current.resolve().is_relative_to(root_resolved):
            raise ValueError(f"{label} traverses a symlink or escapes the candidate artifact")
    if not current.is_file():
        raise ValueError(f"{label} is missing from the candidate artifact")
    return current


def load_artifact(candidate_root: Path, transaction_id: str, baseline_commit: str):
    candidate_root = candidate_root.resolve()
    report_path = _safe_artifact_file(candidate_root, candidate_root / "candidate-run.json", "candidate run report")
    transaction_root = candidate_root / "candidates" / "transactions" / transaction_id
    if transaction_root.is_symlink() or not transaction_root.resolve().is_relative_to(candidate_root):
        raise ValueError("candidate transaction directory is a symlink or escapes the artifact")
    manifest_path = _safe_artifact_file(candidate_root, transaction_root / "transaction-bundle.json", "transaction manifest")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if report.get("status") != "staged_for_owner_review" or report.get("allowed") is not True:
        raise ValueError("candidate run is not marked staged_for_owner_review and allowed")
    if report.get("publish") is not False or report.get("production_files_modified") is not False:
        raise ValueError("candidate run report does not prove shadow-only execution")
    if report.get("transaction_id") != transaction_id:
        raise ValueError("candidate run transaction ID does not match the requested transaction")
    if report.get("baseline_commit") != baseline_commit:
        raise ValueError("candidate run baseline does not match the requested baseline")
    if manifest.get("schema_version") != 1:
        raise ValueError("transaction manifest schema version is unsupported")
    if manifest.get("transaction_id") != transaction_id:
        raise ValueError("transaction manifest ID mismatch")
    if manifest.get("engines") != ["epg", "international", "iptv"]:
        raise ValueError("transaction manifest does not contain exactly the three expected engines")
    if manifest.get("baseline_commit") != baseline_commit:
        raise ValueError("transaction manifest baseline mismatch")
    if manifest.get("ready_for_owner_review") is not True or manifest.get("publish") is not False:
        raise ValueError("transaction manifest is not an owner-review-only candidate")
    if manifest.get("errors") != []:
        raise ValueError("transaction manifest contains errors")
    if set(manifest.get("candidate_fingerprints", {})) != set(PRODUCTION_PATHS):
        raise ValueError("transaction manifest does not contain exactly the three production outputs")
    contents = {}
    for relative in PRODUCTION_PATHS:
        path = _safe_artifact_file(candidate_root, transaction_root / relative, f"candidate output {relative}")
        raw = path.read_bytes()
        if sha256_bytes(raw) != manifest["candidate_fingerprints"][relative]:
            raise ValueError(f"candidate fingerprint mismatch: {relative}")
        contents[relative] = raw
    return report, manifest, contents


def validate_against_baseline(root: Path, baseline_commit: str, report: dict, contents: dict[str, bytes]):
    head = git_bytes(root, "rev-parse", "HEAD").decode().strip()
    if head != baseline_commit:
        raise ValueError(f"worktree HEAD {head} is not the requested baseline {baseline_commit}")
    if git_bytes(root, "status", "--porcelain"):
        raise ValueError("publisher worktree must be clean before candidate preparation")

    baseline = {}
    for relative in PRODUCTION_PATHS:
        original = git_bytes(root, "show", f"{baseline_commit}:{relative}")
        baseline[relative] = original
        working = (root / relative).read_bytes()
        if working != original:
            raise ValueError(f"production worktree differs from approved baseline: {relative}")

    iptv_before = baseline["IPTV-Playlist.m3u"].decode("utf-8-sig")
    iptv_after = contents["IPTV-Playlist.m3u"].decode("utf-8-sig")
    intl_before = baseline["International-Playlist.m3u"].decode("utf-8-sig")
    intl_after = contents["International-Playlist.m3u"].decode("utf-8-sig")
    assert_iptv_existing_rows_preserved(iptv_before, iptv_after)
    # The publication PR builder deliberately refuses all removals. Any stream
    # deletion must first pass its separate three-day authorization workflow.
    assert_international_existing_rows_preserved(intl_before, intl_after)

    iptv_rows = parse_rows(iptv_after)
    intl_rows = parse_rows(intl_after)
    if len(iptv_rows) != report.get("iptv_candidate_rows"):
        raise ValueError("IPTV row count does not match the candidate run report")
    if len(intl_rows) != report.get("international_candidate_rows"):
        raise ValueError("International row count does not match the candidate run report")

    epg_text = contents["epg/epg.xml"].decode("utf-8")
    epg = validate_xmltv(epg_text)
    if not epg.valid:
        raise ValueError("candidate EPG failed XMLTV validation: " + "; ".join(epg.errors[:10]))
    if epg.programme_count != report.get("epg_programmes"):
        raise ValueError("EPG programme count does not match the candidate run report")
    old_root = ET.fromstring(baseline["epg/epg.xml"])
    new_root = ET.fromstring(contents["epg/epg.xml"])
    old_ids = {item.get("id") for item in old_root.findall("channel")}
    new_ids = {item.get("id") for item in new_root.findall("channel")}
    missing_ids = sorted(old_ids - new_ids)
    if missing_ids:
        raise ValueError(f"candidate EPG removed baseline channel definitions: {', '.join(missing_ids[:10])}")

    return {
        "baseline_commit": baseline_commit,
        "transaction_id": report["transaction_id"],
        "iptv_rows": len(iptv_rows),
        "international_rows": len(intl_rows),
        "epg_channels": epg.channel_count,
        "epg_programmes": epg.programme_count,
        "removed_international_rows": 0,
        "production_main_modified": False,
        "publication": "pull_request_only",
    }


def prepare_worktree(root: Path, contents: dict[str, bytes]) -> None:
    for relative, raw in contents.items():
        target = root / relative
        if target.is_symlink() or not target.resolve().is_relative_to(root.resolve()):
            raise ValueError(f"refusing unsafe production target: {relative}")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate-root", required=True, type=Path)
    parser.add_argument("--transaction-id", required=True)
    parser.add_argument("--baseline-commit", required=True)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    root = args.repo_root.resolve()
    try:
        report, manifest, contents = load_artifact(
            args.candidate_root.resolve(), args.transaction_id, args.baseline_commit
        )
        evidence = validate_against_baseline(root, args.baseline_commit, report, contents)
        prepare_worktree(root, contents)
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps(evidence, indent=2, sort_keys=True))
        return 0
    except Exception as exc:
        print(f"V2 publication PR preparation refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
