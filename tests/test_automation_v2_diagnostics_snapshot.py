from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.build_automation_v2_diagnostics_snapshot import build_snapshot


class CandidateDiagnosticsSnapshotTests(unittest.TestCase):
    def test_missing_reports_are_explicit_and_safe(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            result = build_snapshot(root, generated_at="2026-11-14T00:00:00+00:00")
            self.assertEqual(result["candidate"]["status"], "unavailable")
            self.assertEqual(result["source_files"]["candidate_run"]["error"], "missing")
            self.assertFalse(result["safety"]["production_publish_enabled"])
            self.assertFalse(result["safety"]["production_dashboard_written"])

    def test_reads_candidate_and_logo_reports_without_changing_them(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            reports = root / "reports" / "automation-v2"
            reports.mkdir(parents=True)
            run = {"status": "staged_for_owner_review", "allowed": True, "publish": False,
                   "production_files_modified": False, "business_day": "2026-11-14",
                   "baseline_commit": "a" * 40, "transaction_id": "v2-test"}
            logo = {"logo_image_files": 10, "playlist_referenced_logo_files": 8,
                    "missing_runtime_logo_targets": ["logos/missing.png"],
                    "exact_duplicate_groups": 1, "deletion_performed": False,
                    "quarantine_performed": False}
            run_path = reports / "candidate-run.json"
            logo_path = reports / "candidate-logo-reference-audit.json"
            run_path.write_text(json.dumps(run), encoding="utf-8")
            logo_path.write_text(json.dumps(logo), encoding="utf-8")
            before = (run_path.read_bytes(), logo_path.read_bytes())
            result = build_snapshot(root, generated_at="2026-11-14T00:00:00+00:00")
            self.assertEqual(result["candidate"]["status"], "staged_for_owner_review")
            self.assertEqual(result["logo_audit"]["missing_runtime_logo_targets"], 1)
            self.assertEqual((run_path.read_bytes(), logo_path.read_bytes()), before)
            self.assertFalse(result["safety"]["playlist_epg_logo_assets_modified"])


    def test_symlinked_source_report_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            root = Path(tmp)
            reports = root / "reports" / "automation-v2"
            reports.mkdir(parents=True)
            external = Path(outside) / "run.json"
            external.write_text(json.dumps({"status": "forged"}), encoding="utf-8")
            (reports / "candidate-run.json").symlink_to(external)
            result = build_snapshot(root)
            self.assertEqual(result["source_files"]["candidate_run"]["error"], "unsafe: symlinked report")
            self.assertEqual(result["candidate"]["status"], "unavailable")

    def test_symlinked_transaction_directory_is_not_followed(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            root = Path(tmp)
            reports = root / "reports" / "automation-v2"
            reports.mkdir(parents=True)
            target = Path(outside)
            (target / "transaction-bundle.json").write_text(
                json.dumps({"ready_for_owner_review": True}), encoding="utf-8")
            (reports / "candidate-run.json").write_text(
                json.dumps({"status": "staged_for_owner_review",
                            "transaction_path": str(root / "linked-transaction")}),
                encoding="utf-8")
            (root / "linked-transaction").symlink_to(target, target_is_directory=True)
            result = build_snapshot(root)
            self.assertFalse(result["candidate"]["transaction_ready_for_owner_review"])

    def test_rejects_transaction_path_outside_repository(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            root = Path(tmp)
            reports = root / "reports" / "automation-v2"
            reports.mkdir(parents=True)
            (reports / "candidate-run.json").write_text(
                json.dumps({"status": "staged_for_owner_review", "transaction_path": outside}),
                encoding="utf-8")
            result = build_snapshot(root)
            self.assertFalse(result["candidate"]["transaction_ready_for_owner_review"])


if __name__ == "__main__":
    unittest.main()
