import base64
import json
import sys
import unittest
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from automation.core.github_state_store import (
    GitHubStateStore, empty_state, validate_state,
)


class FakeResponse:
    status = 200
    def __init__(self, payload):
        self.payload = json.dumps(payload).encode()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return False
    def read(self):
        return self.payload


class GitHubStateStoreTests(unittest.TestCase):
    def setUp(self):
        self.calls = []
        def opener(request, timeout=20):
            self.calls.append(request)
            if request.method == "GET":
                return FakeResponse({
                    "sha": "f" * 40,
                    "content": base64.b64encode(
                        (json.dumps(empty_state()) + "\n").encode()
                    ).decode(),
                })
            return FakeResponse({"content": {"sha": "e" * 40}})
        self.opener = opener

    def test_empty_state_contains_both_persistent_ledgers(self):
        state = empty_state()
        self.assertEqual(state["timezone"], "Asia/Dhaka")
        self.assertEqual(state["run_ledger"]["entries"], [])
        self.assertEqual(state["international_probe_ledger"]["channels"], {})

    def test_load_state_reads_from_dedicated_branch(self):
        store = GitHubStateStore("owner/repo", "automation-v2-state", "token", self.opener)
        snapshot = store.load()
        self.assertEqual(snapshot.blob_sha, "f" * 40)
        self.assertEqual(snapshot.state, empty_state())
        self.assertIn("ref=automation-v2-state", self.calls[0].full_url)

    def test_save_uses_compare_and_swap_blob_sha(self):
        store = GitHubStateStore("owner/repo", "automation-v2-state", "token", self.opener)
        sha = store.save(empty_state(), "f" * 40)
        self.assertEqual(sha, "e" * 40)
        payload = json.loads(self.calls[-1].data)
        self.assertEqual(payload["sha"], "f" * 40)
        self.assertEqual(payload["branch"], "automation-v2-state")

    def test_save_initializes_state_file_without_fabricated_sha(self):
        store = GitHubStateStore("owner/repo", "automation-v2-state", "token", self.opener)
        store.save(empty_state(), None)
        payload = json.loads(self.calls[-1].data)
        self.assertNotIn("sha", payload)

    def test_invalid_state_is_rejected(self):
        bad = empty_state()
        bad["timezone"] = "UTC"
        with self.assertRaisesRegex(ValueError, "timezone"):
            validate_state(bad)

    def test_missing_credentials_rejected(self):
        with self.assertRaisesRegex(ValueError, "required"):
            GitHubStateStore("owner/repo", "automation-v2-state", "")

    def test_concurrent_update_fails_closed(self):
        def conflict(request, timeout=20):
            raise urllib.error.HTTPError(request.full_url, 409, "conflict", {}, None)
        store = GitHubStateStore("owner/repo", "automation-v2-state", "token", conflict)
        with self.assertRaisesRegex(RuntimeError, "concurrently"):
            store.save(empty_state(), "f" * 40)

    def test_network_failure_fails_closed(self):
        def offline(request, timeout=20):
            raise urllib.error.URLError("offline")
        store = GitHubStateStore("owner/repo", "automation-v2-state", "token", offline)
        with self.assertRaisesRegex(RuntimeError, "refusing to continue"):
            store.load()

    def test_corrupt_remote_state_is_not_reset(self):
        def corrupt(request, timeout=20):
            return FakeResponse({"sha": "f" * 40, "content": base64.b64encode(b'{"broken":').decode()})
        store = GitHubStateStore("owner/repo", "automation-v2-state", "token", corrupt)
        with self.assertRaisesRegex(RuntimeError, "corrupt"):
            store.load()


if __name__ == "__main__":
    unittest.main()
