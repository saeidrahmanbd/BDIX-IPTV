import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from automation.core.rollback_policy import validate_publication_pr


class RollbackPolicyTests(unittest.TestCase):
    def valid_pr(self):
        return {
            "state": "CLOSED",
            "mergedAt": "2026-11-14T04:00:00Z",
            "baseRefName": "main",
            "headRefName": "automation-v2/publish-tx-123-456",
            "title": "Review Automation V2 production candidates: tx-123",
            "mergeCommit": {"oid": "a" * 40},
            "files": [
                {"path": "IPTV-Playlist.m3u"},
                {"path": "International-Playlist.m3u"},
                {"path": "epg/epg.xml"},
            ],
        }

    def test_accepts_merged_candidate_pr_with_only_allowlisted_outputs(self):
        target = validate_publication_pr(self.valid_pr(), 154)
        self.assertEqual(target.pull_request_number, 154)
        self.assertEqual(target.merge_commit_sha, "a" * 40)
        self.assertEqual(
            target.changed_paths,
            ("IPTV-Playlist.m3u", "International-Playlist.m3u", "epg/epg.xml"),
        )

    def test_unmerged_pr_is_rejected(self):
        pr = self.valid_pr()
        pr["mergedAt"] = None
        with self.assertRaisesRegex(ValueError, "must be merged"):
            validate_publication_pr(pr, 154)

    def test_non_main_base_is_rejected(self):
        pr = self.valid_pr()
        pr["baseRefName"] = "develop"
        with self.assertRaisesRegex(ValueError, "target main"):
            validate_publication_pr(pr, 154)

    def test_non_v2_publication_pr_is_rejected(self):
        pr = self.valid_pr()
        pr["headRefName"] = "feature/playlist"
        with self.assertRaisesRegex(ValueError, "publication branch"):
            validate_publication_pr(pr, 154)

    def test_unapproved_path_is_rejected(self):
        pr = self.valid_pr()
        pr["files"].append({"path": "logos/unrelated.png"})
        with self.assertRaisesRegex(ValueError, "unapproved paths"):
            validate_publication_pr(pr, 154)

    def test_duplicate_paths_are_rejected(self):
        pr = self.valid_pr()
        pr["files"].append({"path": "IPTV-Playlist.m3u"})
        with self.assertRaisesRegex(ValueError, "duplicate changed paths"):
            validate_publication_pr(pr, 154)

    def test_invalid_merge_commit_is_rejected(self):
        pr = self.valid_pr()
        pr["mergeCommit"] = {"oid": "not-a-sha"}
        with self.assertRaisesRegex(ValueError, "valid merge commit"):
            validate_publication_pr(pr, 154)


if __name__ == "__main__":
    unittest.main()
