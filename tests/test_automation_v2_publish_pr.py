from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from scripts.prepare_automation_v2_publish_pr import load_artifact, validate_against_baseline

BASELINE_FILES = {
    "IPTV-Playlist.m3u": """#EXTM3U
#EXTINF:-1 tvg-id="one" tvg-chno="1" group-title="Bangladesh",One
https://example.test/one.m3u8
""",
    "International-Playlist.m3u": """#EXTM3U
#EXTINF:-1 tvg-id="movie.one" tvg-chno="1" group-title="Movies",Movie One
https://example.test/movie-one.m3u8
""",
    "epg/epg.xml": """<?xml version="1.0" encoding="UTF-8"?>
<tv><channel id="one"><display-name>One</display-name></channel>
<programme start="20261113000000 +0600" stop="20261113010000 +0600" channel="one"><title>Show</title></programme></tv>
""",
}
CANDIDATE_FILES = {
    "IPTV-Playlist.m3u": BASELINE_FILES["IPTV-Playlist.m3u"] + """#EXTINF:-1 tvg-id="two" tvg-chno="2" group-title="New Channels",Two
https://example.test/two.m3u8
""",
    "International-Playlist.m3u": BASELINE_FILES["International-Playlist.m3u"] + """#EXTINF:-1 tvg-id="movie.two" tvg-chno="2" group-title="New Channels",Movie Two
https://example.test/movie-two.m3u8
""",
    "epg/epg.xml": BASELINE_FILES["epg/epg.xml"].replace("</tv>", """<channel id="two"><display-name>Two</display-name></channel>
<programme start="20261113000000 +0600" stop="20261113010000 +0600" channel="two"><title>Show Two</title></programme></tv>"""),
}


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


class AutomationV2PublishPRTests(unittest.TestCase):
    def make_artifact(self, root: Path, *, publish: bool = False, baseline_commit: str = "a" * 40):
        transaction_id = "v2-test-transaction"
        transaction = root / "candidates" / "transactions" / transaction_id
        transaction.mkdir(parents=True)
        raw = {path: value.encode("utf-8") for path, value in CANDIDATE_FILES.items()}
        manifest = {
            "schema_version": 1,
            "transaction_id": transaction_id,
            "baseline_commit": baseline_commit,
            "engines": ["epg", "international", "iptv"],
            "candidate_fingerprints": {path: digest(data) for path, data in raw.items()},
            "ready_for_owner_review": True,
            "publish": publish,
            "errors": [],
        }
        (transaction / "transaction-bundle.json").write_text(json.dumps(manifest), encoding="utf-8")
        for path, data in raw.items():
            target = transaction / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        report = {
            "status": "staged_for_owner_review",
            "allowed": True,
            "publish": False,
            "production_files_modified": False,
            "transaction_id": transaction_id,
            "baseline_commit": baseline_commit,
            "iptv_candidate_rows": 2,
            "international_candidate_rows": 2,
            "epg_programmes": 2,
        }
        (root / "candidate-run.json").write_text(json.dumps(report), encoding="utf-8")
        return transaction_id, manifest

    def make_git_repo(self, root: Path):
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.test"], cwd=root, check=True)
        for path, value in BASELINE_FILES.items():
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(value, encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "baseline"], cwd=root, check=True)
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()

    def test_valid_artifact_is_loaded_and_verified(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            transaction_id, _ = self.make_artifact(root)
            _, _, contents = load_artifact(root, transaction_id, "a" * 40)
            self.assertEqual(set(contents), set(CANDIDATE_FILES))

    def test_publishable_manifest_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            transaction_id, _ = self.make_artifact(root, publish=True)
            with self.assertRaisesRegex(ValueError, "owner-review-only"):
                load_artifact(root, transaction_id, "a" * 40)

    def test_wrong_candidate_fingerprint_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            transaction_id, _ = self.make_artifact(root)
            candidate = root / "candidates" / "transactions" / transaction_id / "IPTV-Playlist.m3u"
            candidate.write_text(candidate.read_text(encoding="utf-8") + "# tampered\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "fingerprint mismatch"):
                load_artifact(root, transaction_id, "a" * 40)

    def test_valid_candidates_pass_preservation_and_epg_checks(self):
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            repo = temp_root / "repo"
            repo.mkdir()
            baseline = self.make_git_repo(repo)
            artifact = temp_root / "artifact"
            artifact.mkdir()
            transaction_id, _ = self.make_artifact(artifact, baseline_commit=baseline)
            report, _, contents = load_artifact(artifact, transaction_id, baseline)
            evidence = validate_against_baseline(repo, baseline, report, contents)
            self.assertEqual(evidence["publication"], "pull_request_only")
            self.assertEqual(evidence["removed_international_rows"], 0)
            self.assertFalse(evidence["production_main_modified"])

    def test_missing_baseline_epg_channel_definitions_are_restored_without_programmes(self):
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            repo = temp_root / "repo"
            repo.mkdir()
            baseline = self.make_git_repo(repo)
            artifact = temp_root / "artifact"
            artifact.mkdir()
            transaction_id, _ = self.make_artifact(artifact, baseline_commit=baseline)
            report, _, contents = load_artifact(artifact, transaction_id, baseline)
            # Remove the baseline channel definition from the candidate, while
            # retaining its programme to prove only definitions are restored.
            contents["epg/epg.xml"] = contents["epg/epg.xml"].replace(
                b'<channel id="one"><display-name>One</display-name></channel>', b""
            )
            evidence = validate_against_baseline(repo, baseline, report, contents)
            self.assertEqual(evidence["restored_baseline_epg_channel_definitions"], 1)
            self.assertIn(b'<channel id="one">', contents["epg/epg.xml"])
            self.assertEqual(evidence["epg_programmes"], 2)

    def test_manifest_with_missing_engine_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            transaction_id, manifest = self.make_artifact(root)
            manifest["engines"] = ["epg", "iptv"]
            path = root / "candidates" / "transactions" / transaction_id / "transaction-bundle.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "exactly the three expected engines"):
                load_artifact(root, transaction_id, "a" * 40)

    def test_symlinked_candidate_parent_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            transaction_id, _ = self.make_artifact(root)
            transaction = root / "candidates" / "transactions" / transaction_id
            epg_dir = transaction / "epg"
            epg_dir.rename(transaction / "epg-original")
            epg_dir.symlink_to(transaction / "epg-original", target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "symlink or escapes"):
                load_artifact(root, transaction_id, "a" * 40)

    def test_symlinked_candidate_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            transaction_id, _ = self.make_artifact(root)
            transaction = root / "candidates" / "transactions" / transaction_id
            outside = root.parent / (root.name + "-outside")
            outside.mkdir()
            (outside / "epg.xml").write_text(CANDIDATE_FILES["epg/epg.xml"], encoding="utf-8")
            import shutil
            shutil.rmtree(transaction / "epg")
            (transaction / "epg").symlink_to(outside, target_is_directory=True)
            try:
                with self.assertRaisesRegex(ValueError, "symlink or escapes"):
                    load_artifact(root, transaction_id, "a" * 40)
            finally:
                import shutil
                shutil.rmtree(outside, ignore_errors=True)

    def test_baseline_mismatch_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            repo = temp_root / "repo"
            repo.mkdir()
            baseline = self.make_git_repo(repo)
            artifact = temp_root / "artifact"
            artifact.mkdir()
            transaction_id, _ = self.make_artifact(artifact)
            report, _, contents = load_artifact(artifact, transaction_id, "a" * 40)
            with self.assertRaisesRegex(ValueError, "not the requested baseline"):
                validate_against_baseline(repo, "a" * 40, report, contents)


if __name__ == "__main__":
    unittest.main()
