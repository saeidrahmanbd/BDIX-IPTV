from __future__ import annotations

import unittest

from scripts.render_automation_v2_candidate_dashboard import render


class CandidateDashboardRendererTests(unittest.TestCase):
    def test_dashboard_reports_status_and_safety_without_claiming_publication(self):
        value = {
            "snapshot_type": "automation-v2-candidate-diagnostics",
            "generated_at": "2026-11-14T00:00:00+00:00",
            "candidate": {"status": "failed", "allowed": False, "business_day": "2026-11-14",
                          "reason": "EPG source timed out", "transaction_ready_for_owner_review": False},
            "logo_audit": {"available": True, "missing_runtime_logo_targets": 4,
                           "exact_duplicate_groups": 2},
            "logo_repair_candidates": {"proposal_count": 3, "unique_exact_match": 2,
                                       "ambiguous_exact_match": 1},
            "safety": {"production_publish_enabled": False, "production_dashboard_written": False,
                       "playlist_epg_logo_assets_modified": False},
        }
        report = render(value)
        self.assertIn("Candidate status: **failed**", report)
        self.assertIn("EPG source timed out", report)
        self.assertIn("Ambiguous matches (not assigned): 1", report)
        self.assertIn("Production publish enabled: False", report)
        self.assertIn("not the production website dashboard", report)


if __name__ == "__main__":
    unittest.main()
