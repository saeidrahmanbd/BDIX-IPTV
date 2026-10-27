import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import check_epg_source_rights as rights


class EPGSourceRightsTests(unittest.TestCase):
    def test_register_covers_active_feeds_and_scraped_sites(self):
        register = rights.read_register()
        required = rights.required_source_keys({})
        self.assertTrue(required.issubset(set(register)))
        self.assertIn(rights.REPOSITORY_KEY, required)

    def test_runtime_supplemental_sources_are_in_rights_register(self):
        required = rights.required_source_keys({})
        register = rights.read_register()
        for url in (
            "https://epg.lat/files/in.xml.gz",
            "https://epg.lat/files/us.xml.gz",
            "https://www.free-epg.de/api/epg/in.xml.gz",
            "https://www.free-epg.de/api/epg/us.xml.gz",
            "https://www.open-epg.com/files/india.xml.gz",
        ):
            self.assertIn(url, required)
            self.assertIn(url, register)

    def test_restricted_epg_pw_feeds_are_not_active(self):
        required = rights.required_source_keys({})
        self.assertFalse(any("epg.pw/" in key for key in required))
        register = rights.read_register()
        for key in (
            "https://epg.pw/xmltv/epg_IN.xml",
            "https://epg.pw/api/epg.xml?channel_id=9374",
            "https://epg.pw/api/epg.xml?channel_id=12504",
        ):
            self.assertEqual(register[key]["status"], "PROHIBITED")

    def test_unapproved_current_sources_fail_closed(self):
        errors = rights.policy_errors(env={})
        self.assertTrue(errors)
        self.assertTrue(any("Not approved for public redistribution" in e for e in errors))

    def test_private_feed_requires_a_rights_entry_when_configured(self):
        required = rights.required_source_keys({"M3U4U_XMLTV_URL": "https://m3u4u.com/epg/PRIVATE"})
        self.assertIn(rights.PRIVATE_KEY, required)

    def test_approved_record_requires_positive_documented_scope(self):
        row = {
            "status": "APPROVED",
            "evidence_url": "https://example.com/terms",
            "reviewed_on": "2026-10-27",
            "rights_scope": "Public redistribution expressly permitted",
        }
        self.assertEqual(rights.approved_row_errors("example", row), [])
        row["rights_scope"] = "Rights not confirmed"
        self.assertTrue(rights.approved_row_errors("example", row))
        row["rights_scope"] = "Personal use only; no public redistribution allowed"
        self.assertTrue(rights.approved_row_errors("example", row))


if __name__ == "__main__":
    unittest.main()
