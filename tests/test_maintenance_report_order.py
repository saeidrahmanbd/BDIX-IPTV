"""Regression tests for maintenance order and workflow ownership boundaries."""
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "iptv-maintenance.yml"
sys.path.insert(0, str(ROOT / "scripts"))
from playlist_order_policy import should_check_alphabetical_order


class MaintenanceReportOrderTests(unittest.TestCase):
    def test_iptv_maintenance_ignores_test_only_and_unrelated_workflow_edits(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("- .github/workflows/iptv-maintenance.yml", workflow)
        self.assertNotIn("      - tests/", workflow)
        self.assertNotIn("- .github/workflows/**", workflow)

    def test_all_main_branch_writers_share_one_concurrency_group(self):
        expected = "iptv-playlist-main-writer-v5"
        writer_workflows = (
            ".github/workflows/iptv-maintenance.yml",
            ".github/workflows/new-channel-discovery.yml",
            ".github/workflows/international-channel-discovery.yml",
            ".github/workflows/playlist-logo-localization.yml",
            ".github/workflows/changelog.yml",
            ".github/workflows/epg-refresh.yml",
        )
        for relative in writer_workflows:
            with self.subTest(workflow=relative):
                source = (ROOT / relative).read_text(encoding="utf-8")
                # The queue must live on the writing job (6-space indent), not the
                # workflow, so runs whose jobs are skipped do not hold the queue.
                self.assertIsNone(
                    re.search(r"(?m)^  concurrency:", source),
                    f"{relative}: writer queue must be job-level, not workflow-level",
                )
                match = re.search(r"(?m)^ {4}concurrency:\n {6}group:\s*([^\s#]+)", source)
                self.assertIsNotNone(match, f"{relative}: missing job-level concurrency group")
                self.assertEqual(match.group(1), expected, f"{relative}: writer queue mismatch")

    def test_iptv_playlist_registry_includes_review_queues(self):
        normalizer = (ROOT / "scripts" / "normalize_metadata.py").read_text(encoding="utf-8")
        audit = (ROOT / "scripts" / "audit_playlist.py").read_text(encoding="utf-8")
        self.assertIn('l.startswith("#PLAYLIST-STUDIO-CATEGORIES:")', normalizer)
        self.assertIn("Preserve its exact", normalizer)
        self.assertNotIn("CATEGORY_REGISTRY=", normalizer)
        self.assertIn(
            "REGISTRY_ORDER = CATEGORY_ORDER",
            audit,
        )
        renumber = (ROOT / "scripts" / "renumber_active_channels.py").read_text(encoding="utf-8")
        self.assertIn("ordered = records", renumber)
        self.assertNotIn("primary.sort(", renumber)
        sorter = (ROOT / "scripts" / "sort_playlists.py").read_text(encoding="utf-8")
        self.assertIn('if path.name == "IPTV-Playlist.m3u":', sorter)
        self.assertIn("records.sort(key=category_key)", sorter)
        self.assertIn("Do not rewrite channel numbers or group metadata.", sorter)

    def test_review_queue_order_is_not_an_automatic_blocker(self):
        self.assertFalse(should_check_alphabetical_order("Backup"))
        self.assertFalse(should_check_alphabetical_order("Review"))
        self.assertFalse(should_check_alphabetical_order("New Channels"))
        self.assertFalse(should_check_alphabetical_order("New Backups"))
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

    def test_main_playlist_owner_migration_is_explicitly_authorized_and_protected(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")
        mutations = workflow[workflow.index("run_mutations() {"):workflow.index("\n          }", workflow.index("run_mutations() {"))]
        self.assertIn('d.get("status") == "authorized"', workflow)
        self.assertIn("OWNER_MIGRATION_REQUESTED=true", workflow)
        self.assertIn("touch /tmp/iptv-owner-migration-authorized", workflow)
        self.assertNotIn("sort_playlists.py IPTV-Playlist.m3u", mutations)
        # Number normalization is authorized only for this one-time owner
        # migration, never for routine maintenance.
        self.assertIn('if [[ "$OWNER_MIGRATION_REQUESTED" == "true" ]]; then', mutations)
        self.assertIn("python scripts/renumber_active_channels.py IPTV-Playlist.m3u", mutations)
        marker = json.loads((ROOT / "maintenance" / "owner-requested-iptv-migration.json").read_text(encoding="utf-8"))
        self.assertEqual(marker["status"], "authorized")
        guard = (ROOT / "scripts" / "protect_main_playlist.py").read_text(encoding="utf-8")
        self.assertIn("new_order != old_order", guard)
        self.assertIn("Unapproved existing group change", guard)
        self.assertIn("Existing channel number changed", guard)
        self.assertNotIn("migration_mode", guard)
        self.assertIn("python scripts/protect_main_playlist.py snapshot IPTV-Playlist.m3u", workflow)
        self.assertGreaterEqual(workflow.count("python scripts/protect_main_playlist.py verify IPTV-Playlist.m3u"), 2)
        self.assertIn("python -m unittest discover -s tests -p 'test_main_playlist_protection.py'", workflow)


    def test_international_health_reconciles_country_threshold_after_stream_actions(self):
        workflow = (ROOT / ".github" / "workflows" / "international-stream-health.yml").read_text(encoding="utf-8")
        health = workflow.index("python scripts/international_stream_health.py")
        reorganize = workflow.index("python scripts/reorganize_international_playlist.py")
        validate = workflow.index("python scripts/validate_international_playlist.py")
        self.assertLess(health, reorganize)
        self.assertLess(reorganize, validate)
        self.assertIn("reports/international-playlist-audit.md", workflow)

    def test_main_playlist_review_metadata_and_discovery_issues_are_warnings(self):
        gate = (ROOT / "scripts" / "pre_publish_gate.py").read_text(encoding="utf-8")
        self.assertIn("warnings=[]", gate)
        self.assertIn("if queue_errors: warnings.append", gate)
        self.assertNotIn("if queue_errors: issues.append", gate)
        for finding in (
            "orphan Backup entries awaiting owner review",
            "entries missing tvg-chno",
            "Backup/Review/discovery entries still numbered",
            "raw resolution/geoblock tags in channel names",
            "missing logos",
        ):
            self.assertIn(finding, gate)

        audit = (ROOT / "scripts" / "audit_playlist.py").read_text(encoding="utf-8")
        for legacy_blocker in (
            'if category_order_issues or alphabetical_order_issues: raise',
            'if backup_channel_numbers: raise',
            'if missing_primary_chno: raise',
            'if review_queue_country_issues: raise',
            'if logo_exceptions: raise',
        ):
            self.assertNotIn(legacy_blocker, audit)
        self.assertIn("preserving owner order", audit)
        self.assertIn("manual review", audit)

    def test_blocked_maintenance_dashboard_recovery_never_writes_playlist_bytes(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")
        recovery = workflow[workflow.index("Publish fresh dashboard diagnostics after blocked maintenance"):]
        self.assertNotIn("git add IPTV-Playlist.m3u International-Playlist.m3u", recovery)
        self.assertIn("git diff --exit-code -- IPTV-Playlist.m3u International-Playlist.m3u", recovery)
        recovery_script = (ROOT / "scripts" / "refresh_dashboard_diagnostics.py").read_text(encoding="utf-8")
        self.assertNotIn('run_script("scripts/iptv_metadata_backfill.py")', recovery_script)
        self.assertNotIn('run_script("scripts/backfill_cross_playlist_metadata.py")', recovery_script)

    def test_xtream_health_check_uses_commit_pinned_playlist_snapshot(self):
        source = (ROOT / ".github" / "workflows" / "check-xtream.yml").read_text(encoding="utf-8")
        self.assertIn("SOURCE_COMMIT: ${{ github.sha }}", source)
        self.assertIn(
            'url = f"https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/{SOURCE_COMMIT}/IPTV-Playlist.m3u"',
            source,
        )
        self.assertIn('"Cache-Control": "no-cache, no-store"', source)
        self.assertIn('if not re.fullmatch(r"[0-9a-fA-F]{40}", SOURCE_COMMIT):', source)
        self.assertNotIn(
            "raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/IPTV-Playlist.m3u",
            source,
        )


if __name__ == "__main__":
    unittest.main()
