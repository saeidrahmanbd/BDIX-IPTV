"""Tests for conservative duplicate-logo cleanup planning."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from plan_duplicate_logo_cleanup import build_plan


class DuplicateLogoCleanupPlanTests(unittest.TestCase):
    def make_repo(self, runtime_mention=""):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "logos" / "unused").mkdir(parents=True)
        (root / "scripts").mkdir()
        (root / "logos" / "channel.png").write_bytes(b"identical-png-bytes")
        (root / "logos" / "unused" / "channel.png").write_bytes(b"identical-png-bytes")
        if runtime_mention:
            (root / "scripts" / "consumer.py").write_text(runtime_mention, encoding="utf-8")
        return temp, root

    def test_same_named_unused_copy_is_only_a_review_candidate(self):
        temp, root = self.make_repo()
        with temp:
            plan = build_plan(root)
            self.assertEqual(len(plan["low_risk_review_candidates"]), 1)
            candidate = plan["low_risk_review_candidates"][0]
            self.assertEqual(candidate["candidate"], "logos/unused/channel.png")
            self.assertEqual(candidate["retain"], "logos/channel.png")
            self.assertTrue(candidate["requires_review"])
            self.assertFalse(plan["deletion_performed"])
            self.assertTrue((root / "logos" / "unused" / "channel.png").is_file())

    def test_runtime_basename_mention_blocks_candidate(self):
        temp, root = self.make_repo('LOGO_NAME = "channel.png"')
        with temp:
            plan = build_plan(root)
            self.assertEqual(plan["low_risk_review_candidates"], [])
            self.assertEqual(len(plan["held_for_review"]), 1)
            self.assertIn("runtime basename/path mention", " ".join(plan["held_for_review"][0]["reasons"]))

    def test_different_filename_duplicate_is_held(self):
        temp, root = self.make_repo()
        with temp:
            (root / "logos" / "unused" / "channel-alt.png").write_bytes(b"identical-png-bytes")
            plan = build_plan(root)
            held_paths = {item["candidate"] for item in plan["held_for_review"]}
            self.assertIn("logos/unused/channel-alt.png", held_paths)

    def test_nonidentical_files_are_not_candidates(self):
        temp, root = self.make_repo()
        with temp:
            (root / "logos" / "unused" / "channel.png").write_bytes(b"different")
            plan = build_plan(root)
            self.assertEqual(plan["low_risk_review_candidates"], [])
            self.assertEqual(plan["exact_duplicate_groups"], 0)


if __name__ == "__main__":
    unittest.main()
