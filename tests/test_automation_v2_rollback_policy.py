import json
import subprocess
import sys
import tempfile
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
            "headRepository": {"nameWithOwner": "saeidrahmanbd/BDIX-IPTV"},
            "title": "Review Automation V2 production candidates: tx-123",
            "mergeCommit": {"oid": "a" * 40},
            "files": [
                {"path": "IPTV-Playlist.m3u"},
                {"path": "International-Playlist.m3u"},
                {"path": "epg/epg.xml"},
            ],
        }

    def test_accepts_merged_candidate_pr_with_only_allowlisted_outputs(self):
        target = validate_publication_pr(self.valid_pr(), 154, "saeidrahmanbd/BDIX-IPTV")
        self.assertEqual(target.pull_request_number, 154)
        self.assertEqual(target.merge_commit_sha, "a" * 40)
        self.assertEqual(
            target.changed_paths,
            ("IPTV-Playlist.m3u", "International-Playlist.m3u", "epg/epg.xml"),
        )

    def test_accepts_merged_state_enum_from_github_cli(self):
        pr = self.valid_pr()
        pr["state"] = "MERGED"
        target = validate_publication_pr(pr, 154, "saeidrahmanbd/BDIX-IPTV")
        self.assertEqual(target.pull_request_number, 154)

    def test_unmerged_pr_is_rejected(self):
        pr = self.valid_pr()
        pr["mergedAt"] = None
        with self.assertRaisesRegex(ValueError, "must be merged"):
            validate_publication_pr(pr, 154, "saeidrahmanbd/BDIX-IPTV")

    def test_forked_publication_pr_is_rejected(self):
        pr = self.valid_pr()
        pr["headRepository"] = {"nameWithOwner": "someone/BDIX-IPTV"}
        with self.assertRaisesRegex(ValueError, "same repository"):
            validate_publication_pr(pr, 154, "saeidrahmanbd/BDIX-IPTV")

    def test_non_main_base_is_rejected(self):
        pr = self.valid_pr()
        pr["baseRefName"] = "develop"
        with self.assertRaisesRegex(ValueError, "target main"):
            validate_publication_pr(pr, 154, "saeidrahmanbd/BDIX-IPTV")

    def test_non_v2_publication_pr_is_rejected(self):
        pr = self.valid_pr()
        pr["headRefName"] = "feature/playlist"
        with self.assertRaisesRegex(ValueError, "publication branch"):
            validate_publication_pr(pr, 154, "saeidrahmanbd/BDIX-IPTV")

    def test_unapproved_path_is_rejected(self):
        pr = self.valid_pr()
        pr["files"].append({"path": "logos/unrelated.png"})
        with self.assertRaisesRegex(ValueError, "unapproved paths"):
            validate_publication_pr(pr, 154, "saeidrahmanbd/BDIX-IPTV")

    def test_duplicate_paths_are_rejected(self):
        pr = self.valid_pr()
        pr["files"].append({"path": "IPTV-Playlist.m3u"})
        with self.assertRaisesRegex(ValueError, "duplicate changed paths"):
            validate_publication_pr(pr, 154, "saeidrahmanbd/BDIX-IPTV")

    def test_merge_commit_rollback_creates_only_a_local_revert_commit(self):
        with tempfile.TemporaryDirectory() as temp:
            scratch = Path(temp)
            root = scratch / "repo"
            root.mkdir()
            def git(*args):
                return subprocess.run(
                    ["git", *args], cwd=root, check=True, text=True,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                ).stdout.strip()

            git("init", "-b", "main")
            git("config", "user.name", "Automation V2 Test")
            git("config", "user.email", "automation-v2-test@example.invalid")
            original = {
                "IPTV-Playlist.m3u": "#EXTM3U\n",
                "International-Playlist.m3u": "#EXTM3U\n",
                "epg/epg.xml": "<tv/>\n",
            }
            for path, content in original.items():
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")
            git("add", ".")
            git("commit", "-m", "baseline")
            git("switch", "-c", "automation-v2/publish-tx-1-123")
            for path in original:
                (root / path).write_text(original[path] + "<candidate/>\n", encoding="utf-8")
            git("add", ".")
            git("commit", "-m", "candidate publication")
            git("switch", "main")
            git("merge", "--no-ff", "automation-v2/publish-tx-1-123", "-m", "merge publication")
            merge_sha = git("rev-parse", "HEAD")

            pr = self.valid_pr()
            pr["mergeCommit"] = {"oid": merge_sha}
            pr["number"] = 154
            pr_json = scratch / "publication-pr.json"
            pr_json.write_text(json.dumps(pr), encoding="utf-8")
            report_path = scratch / "rollback-report.json"
            script = ROOT / "scripts" / "prepare_automation_v2_rollback_pr.py"
            result = subprocess.run(
                [sys.executable, str(script), "--pr-json", str(pr_json),
                 "--repo-root", str(root), "--report", str(report_path)],
                cwd=ROOT, check=False, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

            for path, content in original.items():
                self.assertEqual((root / path).read_text(encoding="utf-8"), content)
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["source_merge_commit"], merge_sha)
            self.assertEqual(report["revert_mode"], "merge-mainline-parent-1")
            self.assertFalse(report["main_modified"])
            self.assertFalse(report["force_push"])
            self.assertTrue(report["owner_review_required"])
            self.assertEqual(git("branch", "--show-current"), "main")
            self.assertEqual(git("status", "--porcelain"), "")

    def test_invalid_merge_commit_is_rejected(self):
        pr = self.valid_pr()
        pr["mergeCommit"] = {"oid": "not-a-sha"}
        with self.assertRaisesRegex(ValueError, "valid merge commit"):
            validate_publication_pr(pr, 154, "saeidrahmanbd/BDIX-IPTV")


if __name__ == "__main__":
    unittest.main()
