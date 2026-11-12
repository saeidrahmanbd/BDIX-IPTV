"""Regression tests for isolated IPTV discovery and report ordering."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "new-channel-discovery.yml"


class DiscoveryReportOrderTests(unittest.TestCase):
    def test_discovery_does_not_run_playlist_maintenance_or_rewrite_existing_rows(self):
        source = WORKFLOW.read_text(encoding="utf-8")

        def position(fragment):
            index = source.find(fragment)
            self.assertGreaterEqual(index, 0, f"missing workflow command: {fragment}")
            return index

        snapshot = position("cp IPTV-Playlist.m3u /tmp/IPTV-Playlist.before.m3u")
        policy_tests = position("python -m unittest discover -s tests -p 'test_channel_discovery_policy.py'")
        discovery = position("python scripts/run_bd_discovery_with_policy.py")
        probe = position("python scripts/validate_discovery_run.py probe ")
        country_warnings = position("python scripts/country_verification.py validate ")
        final_validation = position("python scripts/validate_discovery_run.py finalize ")
        commit = position("- name: Commit discovery queue additions only")

        self.assertLess(snapshot, policy_tests)
        self.assertLess(policy_tests, discovery)
        self.assertLess(discovery, probe)
        self.assertLess(probe, country_warnings)
        self.assertLess(country_warnings, final_validation)
        self.assertLess(final_validation, commit)

        # Discovery must never call whole-playlist repair/sort steps.
        for forbidden in (
            "python scripts/normalize_metadata.py",
            "python scripts/migrate_external_logos_fixed.py",
            "python scripts/final_playlist_hardening.py IPTV-Playlist.m3u",
            "python scripts/enforce_primary_backup_integrity.py",
            "python scripts/sort_playlists.py IPTV-Playlist.m3u",
            "python scripts/repair_logo_asset_technical_quality.py --fix",
        ):
            self.assertNotIn(forbidden, source)

        self.assertIn("New Channels/New Backups", source)
        self.assertIn("Commit discovery queue additions only", source)
        self.assertIn("git add IPTV-Playlist.m3u reports/iptv-channel-discovery.md", source)

    def test_workflow_triggers_and_runs_the_relevant_discovery_regressions(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        for path in (
            "tests/test_channel_discovery_policy.py",
            "tests/test_country_verification.py",
            "tests/test_discovery_run_validation.py",
            "tests/test_discovery_schedule_guard.py",
            "tests/test_discovery_report_order.py",
            "tests/test_report_freshness.py",
            "tests/test_stream_url_identity.py",
        ):
            self.assertIn(path, source)

        self.assertIn("python -m unittest discover -s tests -p 'test_discovery_report_order.py'", source)
        self.assertIn("python -m unittest discover -s tests -p 'test_report_freshness.py'", source)
        self.assertIn("path: reports/iptv-channel-discovery.md", source)


if __name__ == "__main__":
    unittest.main()
