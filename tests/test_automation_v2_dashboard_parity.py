from __future__ import annotations
import hashlib, unittest
from scripts.render_automation_v2_dashboard_parity import render

class DashboardParityMirrorTests(unittest.TestCase):
    def snapshot(self, content):
        return {"snapshot_type":"automation-v2-legacy-dashboard-inputs",
                "generated_at":"2026-11-14T00:00:00+00:00",
                "sources":{"dashboard_markdown":{"status":"available","content":content,
                    "sha256":hashlib.sha256(content.encode()).hexdigest()}}}
    def test_preserves_legacy_dashboard_metrics_verbatim(self):
        legacy="# Update Report\n\n| Metric | Current |\n|---|---:|\n| Streams | **1284** |\n| EPG | **51%** |\n"
        result=render(self.snapshot(legacy))
        self.assertIn("| Streams | **1284** |",result)
        self.assertIn("| EPG | **51%** |",result)
        self.assertIn("Metric authority: **legacy dashboard snapshot (verbatim)**",result)
        self.assertIn("Production publishing: disabled",result)
    def test_appends_candidate_diagnostics(self):
        legacy="# Update Report\n\n| Streams | **1284** |\n"
        candidate={"snapshot_type":"automation-v2-candidate-diagnostics",
          "candidate":{"status":"staged_for_owner_review","allowed":True,"business_day":"2026-11-14","baseline_commit":"a"*40},
          "logo_audit":{"available":True,"missing_runtime_logo_targets":3},
          "logo_repair_candidates":{"proposal_count":2}}
        result=render(self.snapshot(legacy),candidate)
        self.assertIn("| Streams | **1284** |",result)
        self.assertIn("Candidate status: **staged_for_owner_review**",result)
        self.assertIn("Missing runtime logo targets: 3",result)
    def test_rejects_tampered_snapshot_content(self):
        snap=self.snapshot("# Update Report\n")
        snap["sources"]["dashboard_markdown"]["content"] += "tampered"
        with self.assertRaisesRegex(ValueError,"SHA-256 mismatch"): render(snap)
    def test_rejects_missing_legacy_dashboard(self):
        snap=self.snapshot("# Update Report\n")
        snap["sources"]["dashboard_markdown"]["status"]="missing"
        with self.assertRaisesRegex(ValueError,"unavailable"): render(snap)

if __name__ == "__main__": unittest.main()
