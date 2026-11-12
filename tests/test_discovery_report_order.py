"""Regression tests for the owner-controlled discovery queue workflow."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "new-channel-discovery.yml"


class DiscoveryReportOrderTests(unittest.TestCase):
    def test_discovery_validates_candidates_before_committing_only_queue_additions(self):
        source = WORKFLOW.read_text(encoding="utf-8")

        def position(fragment):
            index = source.find(fragment)
            self.assertGreaterEqual(index, 0, f"missing workflow command: {fragment}")
            return index

        policy = position("python -m unittest discover -s tests -p 'test_channel_discovery_policy.py'")
        country = position("python -m unittest discover -s tests -p 'test_country_verification.py'")
        discover = position("python scripts/run_bd_discovery_with_policy.py")
        probe = position("python scripts/validate_discovery_run.py probe ")
        advisory = position("python scripts/country_verification.py validate IPTV-Playlist.m3u")
        finalize = position("python scripts/validate_discovery_run.py finalize ")
        commit = position("- name: Commit discovery queue additions only")

        self.assertLess(policy, discover)
        self.assertLess(country, discover)
        self.assertLess(discover, probe)
        self.assertLess(probe, advisory)
        self.assertLess(advisory, finalize)
        self.assertLess(finalize, commit)

        # Metadata/logo fixes belong to the separate daily maintenance jobs.
        # Their absence here ensures an incomplete logo or metadata record does
        # not suppress a newly discovered candidate from the manual queues.
        for command in (
            "python scripts/normalize_metadata.py",
            "python scripts/migrate_external_logos_fixed.py",
            "python scripts/final_playlist_hardening.py IPTV-Playlist.m3u",
            "python scripts/renumber_active_channels.py IPTV-Playlist.m3u",
            "python scripts/sort_playlists.py IPTV-Playlist.m3u",
        ):
            self.assertNotIn(command, source)

        self.assertIn("git add IPTV-Playlist.m3u reports/iptv-channel-discovery.md", source)
        self.assertIn("New discovery candidate validation failed; existing playlist rows were not rewritten.", source)

    def test_workflow_runs_freshness_and_order_regressions(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("tests/test_report_freshness.py", source)
        self.assertIn("tests/test_discovery_report_order.py", source)
        self.assertIn("reports/iptv-channel-discovery.md", source)


if __name__ == "__main__":
    unittest.main()
