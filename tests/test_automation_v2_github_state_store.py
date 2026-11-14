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

    def test_large_state_reads_exact_immutable_blob_when_contents_api_omits_content(self):
        state = empty_state()
        state["international_probe_ledger"]["channels"] = {"large-channel": []}
        raw = (json.dumps(state) + "\n").encode()
        encoded = base64.b64encode(raw).decode()
        calls = []
        def large_opener(request, timeout=20):
            calls.append(request)
            if request.method == "GET" and request.full_url.endswith("/contents/automation-v2-state.json?ref=automation-v2-state"):
                return FakeResponse({
                    "sha": "a" * 40,
                    "content": "",
                    "download_url": "https://raw.githubusercontent.com/owner/repo/automation-v2-state/automation-v2-state.json",
                })
            if request.method == "GET" and request.full_url.endswith("/git/blobs/" + "a" * 40):
                return FakeResponse({
                    "sha": "a" * 40,
                    "encoding": "base64",
                    "content": encoded,
                })
            raise AssertionError("unexpected request: " + request.full_url)
        store = GitHubStateStore("owner/repo", "automation-v2-state", "token", large_opener)
        snapshot = store.load()
        self.assertEqual(snapshot.blob_sha, "a" * 40)
        self.assertEqual(snapshot.state, state)
        self.assertEqual(len(calls), 2)
        self.assertIn("git/blobs/" + "a" * 40, calls[1].full_url)
        self.assertNotIn("raw.githubusercontent.com", calls[1].full_url)

    def test_large_state_rejects_mismatched_blob_sha(self):
        def mismatch(request, timeout=20):
            if request.full_url.endswith("/contents/automation-v2-state.json?ref=automation-v2-state"):
                return FakeResponse({"sha": "a" * 40, "content": ""})
            return FakeResponse({"sha": "b" * 40, "encoding": "base64",
                                 "content": base64.b64encode(json.dumps(empty_state()).encode()).decode()})
        store = GitHubStateStore("owner/repo", "automation-v2-state", "token", mismatch)
        with self.assertRaisesRegex(RuntimeError, "mismatched"):
            store.load()

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


    def test_remote_run_reservation_and_terminal_status_survive_reload(self):
        from datetime import date
        from automation.core.github_state_store import reserve_remote_run, finish_remote_run
        from automation.core.run_ledger import RunRequest
        state = empty_state()
        current = {"sha": "a" * 40, "state": state}
        def memory_opener(request, timeout=20):
            if request.method == "GET":
                return FakeResponse({
                    "sha": current["sha"],
                    "content": base64.b64encode(json.dumps(current["state"]).encode()).decode(),
                })
            payload = json.loads(request.data)
            self.assertEqual(payload.get("sha"), current["sha"])
            current["state"] = json.loads(base64.b64decode(payload["content"]).decode())
            current["sha"] = "b" * 40
            return FakeResponse({"content": {"sha": current["sha"]}})
        store = GitHubStateStore("owner/repo", "automation-v2-state", "token", memory_opener)
        request = RunRequest("iptv", date(2026, 11, 13), "c" * 40, "d" * 64)
        first = reserve_remote_run(store, request)
        self.assertTrue(first.allowed)
        blocked = reserve_remote_run(store, request)
        self.assertFalse(blocked.allowed)
        terminal = finish_remote_run(store, first.idempotency_key, first.attempt, "succeeded")
        self.assertEqual(terminal.status, "succeeded")
        self.assertEqual(current["state"]["run_ledger"]["entries"][0]["status"], "succeeded")

    def test_remote_probe_history_survives_reload(self):
        from datetime import date
        from automation.core.github_state_store import record_remote_probe
        from automation.engines.international.probe_ledger import probes_for
        from automation.engines.international.stream_failure_policy import Probe
        current = {"sha": "a" * 40, "state": empty_state()}
        def memory_opener(request, timeout=20):
            if request.method == "GET":
                return FakeResponse({
                    "sha": current["sha"],
                    "content": base64.b64encode(json.dumps(current["state"]).encode()).decode(),
                })
            payload = json.loads(request.data)
            self.assertEqual(payload.get("sha"), current["sha"])
            current["state"] = json.loads(base64.b64decode(payload["content"]).decode())
            current["sha"] = "b" * 40
            return FakeResponse({"content": {"sha": current["sha"]}})
        store = GitHubStateStore("owner/repo", "automation-v2-state", "token", memory_opener)
        record_remote_probe(store, "channel-1", Probe(date(2026, 11, 11), 404))
        record_remote_probe(store, "channel-1", Probe(date(2026, 11, 12), 404))
        probes = probes_for(current["state"]["international_probe_ledger"], "channel-1")
        self.assertEqual([item.day.isoformat() for item in probes], ["2026-11-11", "2026-11-12"])


if __name__ == "__main__":
    unittest.main()
