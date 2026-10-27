import os
import sys
import unittest
from unittest.mock import patch
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

    def test_epg_source_pool_has_no_provider_specific_exclusion(self):
        required = rights.required_source_keys({})
        self.assertTrue(required)
        register = rights.read_register()
        self.assertTrue(required.issubset(set(register)))

    def test_unapproved_sources_need_explicit_owner_override(self):
        errors = rights.policy_errors(env={})
        self.assertTrue(errors)
        self.assertTrue(any("Not approved for public redistribution" in e for e in errors))
        with patch.dict(os.environ, {"EPG_ALLOW_UNVERIFIED_SOURCES": ""}):
            with self.assertRaises(SystemExit):
                rights.require_approved_sources("test default")
        with patch.dict(os.environ, {"EPG_ALLOW_UNVERIFIED_SOURCES": "true"}):
            self.assertTrue(rights.require_approved_sources("test override"))

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
