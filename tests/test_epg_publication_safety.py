from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EPGPublicationSafetyTests(unittest.TestCase):
    def test_public_xmltv_payload_and_old_mapping_are_removed(self):
        self.assertFalse((ROOT / "epg/epg.xml").exists())
        self.assertFalse((ROOT / "reports/epg-india-channel-mapping.csv").exists())
        mapping = ROOT / "reports/epg-channel-mapping.csv"
        self.assertTrue(mapping.is_file())
        self.assertNotIn("\nAdult,", mapping.read_text(encoding="utf-8"))

    def test_unapproved_sundirect_source_is_not_configured(self):
        for relative in ("scripts/epg_coverage.py", "scripts/generate_epg.py"):
            with self.subTest(script=relative):
                text = (ROOT / relative).read_text(encoding="utf-8")
                self.assertNotIn("sundirectgo.xml", text)

    def test_both_automated_publication_paths_fail_closed(self):
        refresh = (ROOT / ".github/workflows/epg-refresh.yml").read_text(encoding="utf-8")
        maintenance = (ROOT / ".github/workflows/iptv-maintenance.yml").read_text(encoding="utf-8")
        self.assertIn("vars.EPG_REDISTRIBUTION_APPROVED == 'true'", refresh)
        self.assertNotIn("python scripts/epg_coverage.py", maintenance)
        self.assertNotIn("python scripts/fetch_iptv_org_epg.py", maintenance)
        self.assertNotIn("python scripts/run_generate_epg.py", maintenance)
        self.assertNotIn("git add -f epg/epg.xml", maintenance)

    def test_epg_reports_do_not_publish_old_coverage_percentages(self):
        for relative in (
            "reports/epg-coverage.md",
            "reports/epg-three-playlist-audit.md",
            "reports/epg-unmapped-audit.md",
            "reports/epg-publish-freshness.md",
            "reports/epg-timing-audit.md",
        ):
            with self.subTest(report=relative):
                text = (ROOT / relative).read_text(encoding="utf-8")
                self.assertIn("disabled", text.casefold())
                self.assertNotIn("34.8%", text)
                self.assertNotIn("978/2658", text)


if __name__ == "__main__":
    unittest.main()
