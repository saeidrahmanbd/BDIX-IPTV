"""Regression tests for playlist discovery report ordering."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "new-channel-discovery.yml"


class DiscoveryReportOrderTests(unittest.TestCase):
    def test_fingerprinted_reports_are_generated_after_final_playlist_mutation(self):
        source = WORKFLOW.read_text(encoding="utf-8")

        def position(fragment):
            index = source.find(fragment)
            self.assertGreaterEqual(index, 0, f"missing workflow command: {fragment}")
            return index

        normalize = position("python scripts/normalize_metadata.py")
        migrate = position("python scripts/migrate_external_logos_fixed.py")
        hardening = position("python scripts/final_playlist_hardening.py IPTV-Playlist.m3u")
        probe = position("python scripts/validate_discovery_run.py probe ")
        finalize = position("python scripts/validate_discovery_run.py finalize ")
        quality = position("python scripts/repair_logo_asset_technical_quality.py --fix")
        manifest = position("python scripts/generate_logo_authenticity_manifest.py")
        metadata_report = position("python scripts/generate_metadata_normalization_report.py")
        logo_summary = position("python scripts/generate_logo_repair_summary.py")
        freshness = position("python scripts/validate_report_freshness.py --mode discovery")
        commit = position("- name: Commit discovered candidates")

        self.assertLess(normalize, migrate)
        self.assertLess(migrate, hardening)
        self.assertLess(hardening, probe)
        self.assertLess(probe, finalize)
        self.assertLess(finalize, quality)
        self.assertLess(quality, manifest)
        self.assertLess(manifest, metadata_report)
        self.assertLess(metadata_report, logo_summary)
        self.assertLess(logo_summary, freshness)
        self.assertLess(freshness, commit)

        for command in (
            "python scripts/repair_logo_asset_technical_quality.py --fix",
            "python scripts/generate_logo_authenticity_manifest.py",
            "python scripts/generate_metadata_normalization_report.py",
            "python scripts/generate_logo_repair_summary.py",
            "python scripts/validate_report_freshness.py --mode discovery",
        ):
            self.assertEqual(source.count(command), 1, f"expected one final report pass: {command}")

    def test_workflow_runs_freshness_and_order_regressions(self):
        source = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("tests/test_report_freshness.py", source)
        self.assertIn("tests/test_discovery_report_order.py", source)
        self.assertIn("reports/logo-asset-quality-audit.md", source)


if __name__ == "__main__":
    unittest.main()
