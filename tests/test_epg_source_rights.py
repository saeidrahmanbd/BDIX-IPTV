import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import check_epg_source_rights as rights


class EPGSourceRightsTests(unittest.TestCase):
    def test_metadata_gaps_are_advisory_and_do_not_block(self):
        with patch.object(rights, "policy_errors", return_value=["review-required source"]):
            self.assertTrue(rights.require_approved_sources("test advisory audit"))

    def test_missing_register_is_advisory_and_does_not_block(self):
        with patch.object(rights, "policy_errors", return_value=["Configuration error: register missing"]):
            self.assertTrue(rights.require_approved_sources("test missing register"))

    def test_legacy_override_values_do_not_change_build_permission(self):
        with patch.object(rights, "policy_errors", return_value=["review-required source"]):
            for value in ("", "true", "false"):
                with self.subTest(value=value), patch.dict(os.environ, {"EPG_ALLOW_UNVERIFIED_SOURCES": value}):
                    self.assertTrue(rights.require_approved_sources("test legacy environment"))

    def test_epg_pipeline_and_reports_have_no_register_dependency(self):
        for relative in (
            "scripts/epg_coverage.py",
            "scripts/generate_epg.py",
            "scripts/run_generate_epg.py",
            "scripts/fetch_iptv_org_epg.py",
            "scripts/augment_epg_mapping_from_additional_sources.py",
        ):
            with self.subTest(script=relative):
                content = (ROOT / relative).read_text(encoding="utf-8")
                self.assertNotIn("check_epg_source_rights", content)
        for relative in ("scripts/generate_dashboard.py", "scripts/update_epg_published_coverage.py"):
            with self.subTest(report_script=relative):
                content = (ROOT / relative).read_text(encoding="utf-8")
                self.assertNotIn("source-rights-register.csv", content)

    def test_scope_classifier_remains_audit_only(self):
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
