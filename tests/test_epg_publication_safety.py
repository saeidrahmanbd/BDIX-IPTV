from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class EPGPublicationSafetyTests(unittest.TestCase):
    def test_public_xmltv_payload_is_well_formed_when_published_and_old_mapping_is_removed(self):
        guide = ROOT / "epg/epg.xml"
        if guide.exists():
            root = ET.parse(guide).getroot()
            self.assertEqual(root.tag, "tv")
            self.assertTrue(root.findall("channel"))
            self.assertTrue(root.findall("programme"))
        self.assertFalse((ROOT / "reports/epg-india-channel-mapping.csv").exists())
        mapping = ROOT / "reports/epg-channel-mapping.csv"
        self.assertTrue(mapping.is_file())
        self.assertNotIn("\nAdult,", mapping.read_text(encoding="utf-8"))

    def test_unapproved_sundirect_source_is_not_configured(self):
        for relative in ("scripts/epg_coverage.py", "scripts/generate_epg.py"):
            with self.subTest(script=relative):
                text = (ROOT / relative).read_text(encoding="utf-8")
                self.assertNotIn("sundirectgo.xml", text)

    def test_automated_publication_is_enabled_with_owner_override(self):
        refresh = (ROOT / ".github/workflows/epg-refresh.yml").read_text(encoding="utf-8")
        maintenance = (ROOT / ".github/workflows/iptv-maintenance.yml").read_text(encoding="utf-8")
        self.assertNotIn("vars.EPG_REDISTRIBUTION_APPROVED == 'true'", refresh)
        self.assertIn("EPG_ALLOW_UNVERIFIED_SOURCES: 'true'", refresh)
        self.assertIn("python scripts/epg_coverage.py", refresh)
        self.assertIn("python scripts/fetch_iptv_org_epg.py", refresh)
        self.assertIn("python scripts/run_generate_epg.py", refresh)
        self.assertIn("git add -f epg/epg.xml", refresh)
        self.assertIn("EPG_ALLOW_UNVERIFIED_SOURCES: 'true'", maintenance)
        self.assertNotIn("M3U4U_XMLTV_URL", refresh)
        self.assertNotIn("M3U4U_XMLTV_URL", maintenance)
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
