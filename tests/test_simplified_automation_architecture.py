import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SimplifiedAutomationArchitectureTests(unittest.TestCase):
    def test_v2_candidate_bundle_has_no_automatic_trigger(self):
        workflow = (ROOT / ".github" / "workflows" / "automation-v2-candidate-bundle.yml").read_text(encoding="utf-8")
        trigger_block = workflow.split("permissions:", 1)[0]
        self.assertNotIn("\n  push:", trigger_block)
        self.assertNotIn("\n  schedule:", trigger_block)
        self.assertNotIn("\n  workflow_run:", trigger_block)
        self.assertIn("workflow_dispatch:", trigger_block)

    def test_isolated_logo_fallback_is_manual_only(self):
        workflow = (ROOT / ".github" / "workflows" / "logo-localization.yml").read_text(encoding="utf-8")
        trigger_block = workflow.split("permissions:", 1)[0]
        self.assertNotIn("\n  push:", trigger_block)
        self.assertNotIn("\n  schedule:", trigger_block)
        self.assertIn("workflow_dispatch:", trigger_block)

    def test_owner_curated_playlist_contract_is_documented(self):
        workflow = (ROOT / ".github" / "workflows" / "iptv-maintenance.yml").read_text(encoding="utf-8")
        self.assertIn("IPTV-Playlist.m3u is owner-curated", workflow)
        self.assertIn("Existing IPTV rows are never structurally migrated, sorted or renumbered.", workflow)


if __name__ == "__main__":
    unittest.main()
