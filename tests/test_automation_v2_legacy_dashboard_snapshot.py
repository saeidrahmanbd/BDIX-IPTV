from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.build_automation_v2_legacy_dashboard_snapshot import build_snapshot


class LegacyDashboardSnapshotTests(unittest.TestCase):
    def test_captures_reports_with_hashes_without_mutating_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            reports = root / "reports"
            reports.mkdir()
            source = reports / "Update Report.md"
            source.write_text("# dashboard\nStreams: 10\n", encoding="utf-8")
            before = source.read_bytes()
            result = build_snapshot(root, generated_at="2026-11-14T00:00:00+00:00")
            item = result["sources"]["dashboard_markdown"]
            self.assertEqual(item["status"], "available")
            self.assertEqual(item["content"], before.decode())
            self.assertEqual(len(item["sha256"]), 64)
            self.assertEqual(source.read_bytes(), before)
            self.assertFalse(result["safety"]["production_reports_modified"])

    def test_missing_and_symlink_sources_are_explicit(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            root = Path(tmp)
            reports = root / "reports"
            reports.mkdir()
            target = Path(outside) / "report.md"
            target.write_text("external", encoding="utf-8")
            (reports / "iptv-playlist-audit.md").symlink_to(target)
            result = build_snapshot(root)
            self.assertEqual(result["sources"]["playlist_audit"]["status"], "rejected_symlink")
            self.assertEqual(result["sources"]["epg_coverage"]["status"], "missing")

    def test_invalid_json_report_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "reports").mkdir()
            (root / "reports" / "maintenance-history.json").write_text("{bad", encoding="utf-8")
            result = build_snapshot(root)
            self.assertEqual(result["sources"]["maintenance_history"]["status"], "invalid")


if __name__ == "__main__":
    unittest.main()
