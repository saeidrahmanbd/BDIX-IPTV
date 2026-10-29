"""Regression tests for maintenance order and workflow ownership boundaries."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "iptv-maintenance.yml"
sys.path.insert(0, str(ROOT / "scripts"))
from playlist_order_policy import should_check_alphabetical_order


class MaintenanceReportOrderTests(unittest.TestCase):
    def test_all_main_branch_writers_share_one_concurrency_group(self):
        expected = "iptv-playlist-main-writer-v3"
        writer_workflows = (
            ".github/workflows/iptv-maintenance.yml",
            ".github/workflows/bdix-playlist-update.yml",
            ".github/workflows/new-channel-discovery.yml",
            ".github/workflows/international-channel-discovery.yml",
            ".github/workflows/playlist-logo-localization.yml",
            ".github/workflows/changelog.yml",
        )
        for relative in writer_workflows:
            with self.subTest(workflow=relative):
                source = (ROOT / relative).read_text(encoding="utf-8")
                match = re.search(r"(?m)^  group:\\s*([^\\s#]+)", source)
                self.assertIsNotNone(match, f"{relative}: missing top-level concurrency group")
                self.assertEqual(match.group(1), expected, f"{relative}: writer queue mismatch")

    def test_review_queue_order_is_not_an_automatic_blocker(self):
        self.assertFalse(should_check_alphabetical_order("Backup"))
        self.assertFalse(should_check_alphabetical_order("Not Playing"))
        self.assertFalse(should_check_alphabetical_order(" backup "))
        self.assertTrue(should_check_alphabetical_order("Bangladesh"))
        self.assertTrue(should_check_alphabetical_order("Indian Music"))

    def test_public_epg_generation_is_owned_by_epg_refresh_workflow(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")
        # Playlist maintenance must not own or duplicate EPG generation.
        self.assertNotIn("EPG_ALLOW_UNVERIFIED_SOURCES", workflow)
        self.assertNotIn("M3U4U_XMLTV_URL", workflow)
        self.assertNotIn("python scripts/run_generate_epg.py", workflow)
        self.assertNotIn("python scripts/epg_coverage.py", workflow)
        self.assertNotIn("python scripts/fetch_iptv_org_epg.py", workflow)
        self.assertNotIn("git add -f epg/epg.xml", workflow)

        refresh = (ROOT / ".github" / "workflows" / "epg-refresh.yml").read_text(encoding="utf-8")
        # The dedicated EPG workflow owns the public guide and its source policy.
        self.assertNotIn("vars.EPG_REDISTRIBUTION_APPROVED == 'true'", refresh)
        self.assertNotIn("EPG_ALLOW_UNVERIFIED_SOURCES", refresh)
        self.assertIn("python scripts/validate_report_freshness.py --mode epg", refresh)
        self.assertIn("python scripts/run_generate_epg.py", refresh)
        self.assertIn("python scripts/epg_coverage.py", refresh)
        self.assertIn("python scripts/fetch_iptv_org_epg.py", refresh)
        self.assertIn("git add -f epg/epg.xml", refresh)
        self.assertIn("workflow_dispatch:", refresh)

    def test_final_fingerprinted_reports_follow_all_final_repairs(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertEqual(
            workflow.count("python scripts/validate_report_freshness.py"),
            1,
            "freshness validation should run only after all final reports are regenerated",
        )
        self.assertIn("python scripts/validate_report_freshness.py --mode generated", workflow)

        def last_pos(needle):
            pos = workflow.rfind(needle)
            self.assertGreaterEqual(pos, 0, f"missing workflow step: {needle}")
            return pos

        auxiliary_backfill = last_pos("python scripts/backfill_cross_playlist_metadata.py")
        logo_quality_repair = last_pos("python scripts/repair_logo_asset_technical_quality.py --fix")
        protected_restore = last_pos("python scripts/restore_protected_review.py")
        change_guard = last_pos("python scripts/maintenance_helpers.py verify-no-unauthorized-removals")
        audit_pos = last_pos("python scripts/audit_playlist.py")
        gate_pos = last_pos("python scripts/pre_publish_gate.py")
        manifest_pos = last_pos("python scripts/generate_logo_authenticity_manifest.py")
        provenance_pos = last_pos("python scripts/generate_logo_provenance_review.py")
        metadata_pos = last_pos("python scripts/generate_metadata_normalization_report.py")
        freshness_pos = last_pos("python scripts/validate_report_freshness.py")

        # Final metadata backfill reports must be regenerated after the last
        # playlist/logo repairs and safety guard, then before the final audit/gate.
        self.assertLess(logo_quality_repair, protected_restore)
        self.assertLess(protected_restore, change_guard)
        self.assertLess(change_guard, auxiliary_backfill)
        self.assertLess(auxiliary_backfill, audit_pos)
        self.assertLess(audit_pos, gate_pos)
        self.assertLess(gate_pos, manifest_pos)
        self.assertLess(manifest_pos, provenance_pos)
        self.assertLess(provenance_pos, metadata_pos)
        self.assertLess(metadata_pos, freshness_pos)


if __name__ == "__main__":
    unittest.main()
