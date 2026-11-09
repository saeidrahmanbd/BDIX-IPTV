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
        registry_line = next(
            line for line in normalizer.splitlines()
            if line.startswith("CATEGORY_REGISTRY=")
        )
        import json
        registry = json.loads(registry_line.split("=", 1)[1])
        self.assertEqual(
            registry,
            [
                "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
                "Indian Entertainment", "Pakistani", "International",
                "Documentary & Wildlife", "Kids", "Religious", "Sports",
                "Review", "New Channels", "New Backups", "Backup",
            ],
        )
        self.assertIn(
            "REGISTRY_ORDER = CATEGORY_ORDER",
            audit,
        )

    def test_review_queue_order_is_not_an_automatic_blocker(self):
        self.assertFalse(should_check_alphabetical_order("Backup"))
        self.assertFalse(should_check_alphabetical_order("Review"))
        self.assertFalse(should_check_alphabetical_order("New Channels"))
        self.assertFalse(should_check_alphabetical_order("New Backups"))
        self.assertFalse(should_check_alphabetical_order("Not Playing"))
        self.assertFalse(should_check_alphabetical_order(" backup "))
        self.assertTrue(should_check_alphabetical_order("Bangladesh"))
        self.assertTrue(should_check_alphabetical_order("Indian Music"))

    def test_missing_logos_in_review_are_nonblocking_quarantine_items(self):
        audit = (ROOT / "scripts" / "audit_playlist.py").read_text(encoding="utf-8")
        self.assertIn('group in {"Review", "Not Playing", "New Channels", "New Backups"}', audit)
        self.assertIn("review_logo_exceptions.append(item)", audit)

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
        run = workflow[workflow.index("run_mutations() {"):]
        mutations = run[:run.index("\n          }\n")]
        after = run[run.index("\n          }\n"):]

        # Freshness validation exactly once, after every fingerprinted report.
        self.assertEqual(workflow.count("python scripts/validate_report_freshness.py"), 1)
        self.assertIn("python scripts/validate_report_freshness.py --mode generated", workflow)

        # Single-writer reports: each generator appears once after the mutation block.
        for script in (
            "stream_health", "report_iptv_fragile_streams", "stream_risk_review",
            "generate_logo_authenticity_manifest", "generate_logo_repair_summary",
            "generate_logo_provenance_review", "generate_metadata_normalization_report",
            "generate_dashboard", "record_maintenance_history", "build_identity_index",
        ):
            call = f"python scripts/{script}.py"
            self.assertEqual(workflow.count(call), 1, f"{script} must run exactly once")
            self.assertIn(call, after, f"{script} must run after all playlist mutations")
            self.assertNotIn(call, mutations)

        # Audit and gate run after the mutation block, in the correction path they rerun
        # the full mutation function; their exit status is never discarded.
        self.assertIn("python scripts/audit_playlist.py", after)
        self.assertIn("python scripts/pre_publish_gate.py", after)
        self.assertNotIn("|| true", workflow)

        def pos(block, needle):
            index = block.rfind(needle)
            self.assertGreaterEqual(index, 0, f"missing workflow step: {needle}")
            return index

        # Inside the mutation block. normalize/sort/hardening run first and migrate_external_logos
        # runs after them: the two scripts rewrite logo references differently, so the migrator
        # must be the last logo-reference writer. The migrator no longer emits tvg-logo="".
        first = lambda needle: (mutations.find(needle), self.assertGreaterEqual(mutations.find(needle), 0, needle))[0]
        normalize = first("python scripts/normalize_metadata.py")
        sort = first("python scripts/sort_playlists.py")
        hardening = first("python scripts/final_playlist_hardening.py")
        migrate = pos(mutations, "python scripts/migrate_external_logos_fixed.py")
        self.assertEqual(mutations.count("python scripts/restore_protected_review.py"), 2)
        restore_early = first("python scripts/restore_protected_review.py")
        # backfill_cross is called twice on purpose: early, because reorganize_international_playlist
        # reads the country/language it fills in; last, so its fingerprinted report matches final bytes.
        self.assertEqual(mutations.count("python scripts/backfill_cross_playlist_metadata.py"), 2)
        cross_early = first("python scripts/backfill_cross_playlist_metadata.py")
        cross_final = pos(mutations, "python scripts/backfill_cross_playlist_metadata.py")
        reconcile = pos(mutations, "python scripts/reconcile_playlist_consistency.py")
        reorganize = pos(mutations, "python scripts/reorganize_international_playlist.py")
        attribution = pos(mutations, "python scripts/enforce_playlist_attribution.py IPTV-Playlist.m3u")
        restore = pos(mutations, "python scripts/restore_protected_review.py")
        metadata = pos(mutations, "python scripts/iptv_metadata_backfill.py")
        logo_fix = pos(mutations, "python scripts/repair_logo_asset_technical_quality.py --fix")
        backup_languages = pos(mutations, "python scripts/reconcile_backup_metadata_exact_id.py")
        integrity = pos(mutations, "python scripts/enforce_primary_backup_integrity.py")
        renumber = pos(mutations, "python scripts/renumber_active_channels.py IPTV-Playlist.m3u")
        guard = pos(mutations, "python scripts/maintenance_helpers.py verify-no-unauthorized-removals")
        self.assertLess(normalize, sort)
        self.assertLess(sort, hardening)
        self.assertLess(hardening, migrate)
        self.assertLess(migrate, restore_early)
        self.assertLess(restore_early, cross_early)
        self.assertLess(cross_early, reconcile)
        self.assertLess(reconcile, reorganize)
        self.assertLess(reorganize, attribution)
        self.assertLess(attribution, restore)
        final_sort = pos(mutations, "python scripts/sort_playlists.py IPTV-Playlist.m3u")
        self.assertLess(restore, backup_languages)
        self.assertLess(backup_languages, integrity)
        self.assertLess(integrity, final_sort)
        self.assertLess(final_sort, renumber)
        self.assertLess(renumber, metadata)
        self.assertLess(metadata, cross_final)
        self.assertLess(cross_final, logo_fix)
        self.assertLess(logo_fix, guard)
        intl_guard = pos(mutations, "python scripts/verify_international_protected.py verify")
        self.assertLess(guard, intl_guard)
        self.assertLess(reorganize, intl_guard)
        # the baseline must be recorded before the mutation block runs
        self.assertIn("python scripts/verify_international_protected.py snapshot", workflow)

        # After the mutation block: audit -> gate -> reports -> freshness.
        audit = pos(after, "python scripts/audit_playlist.py")
        gate = pos(after, "python scripts/pre_publish_gate.py")
        health = pos(after, "python scripts/stream_health.py")
        manifest = pos(after, "python scripts/generate_logo_authenticity_manifest.py")
        provenance = pos(after, "python scripts/generate_logo_provenance_review.py")
        metadata_report = pos(after, "python scripts/generate_metadata_normalization_report.py")
        dashboard = pos(after, "python scripts/generate_dashboard.py")
        freshness = pos(after, "python scripts/validate_report_freshness.py")
        self.assertLess(audit, gate)
        self.assertLess(gate, health)
        self.assertLess(health, manifest)
        self.assertLess(manifest, provenance)
        self.assertLess(provenance, metadata_report)
        self.assertLess(metadata_report, dashboard)
        self.assertLess(dashboard, freshness)

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
