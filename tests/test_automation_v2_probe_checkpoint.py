"""Regression tests for durable probe checkpoints preserving active reservations."""
from datetime import date, datetime
from zoneinfo import ZoneInfo
import copy
import unittest

from automation.core.github_state_store import StateSnapshot, checkpoint_remote_probe_ledger, empty_state
from automation.core.run_ledger import LedgerEntry, RunRequest, make_idempotency_key
from automation.core.run_ledger_store import serialize_run_ledger


class FakeStore:
    def __init__(self, state):
        self.state = copy.deepcopy(state)
        self.saves = 0
        self.conflict_once = False

    def load(self):
        return StateSnapshot(copy.deepcopy(self.state), f"blob-{self.saves}")

    def save(self, state, expected_blob_sha):
        if self.conflict_once:
            self.conflict_once = False
            # Simulate an unrelated writer changing the remote object before CAS.
            self.state["unrelated_marker"] = "kept"
            raise RuntimeError("durable state changed concurrently; refusing to overwrite it")
        self.state = copy.deepcopy(state)
        self.saves += 1
        return f"saved-{self.saves}"


class ProbeCheckpointReservationTests(unittest.TestCase):
    def setUp(self):
        self.request = RunRequest(
            "bundle", date(2026, 11, 14), "908982de05bd699b60e6b2b9f26d7da3dd11cae2",
            "a" * 64, datetime(2026, 11, 14, 10, 0, tzinfo=ZoneInfo("Asia/Dhaka")),
        )
        self.key = make_idempotency_key(self.request)
        state = empty_state()
        state["run_ledger"] = __import__("json").loads(serialize_run_ledger([
            LedgerEntry(self.key, "bundle", self.request.business_day,
                        self.request.baseline_commit, "running", 1, self.request.requested_at)
        ]))
        self.state = state
        self.probes = {"schema_version": 1, "timezone": "Asia/Dhaka", "channels": {
            "example": [{"day": "2026-11-14", "status_code": 200, "stream_state": "verified"}]
        }}

    def test_probe_checkpoint_preserves_active_reservation(self):
        store = FakeStore(self.state)
        checkpoint_remote_probe_ledger(store, self.key, self.probes)
        self.assertEqual(len(store.state["run_ledger"]["entries"]), 1)
        entry = store.state["run_ledger"]["entries"][0]
        self.assertEqual(entry["idempotency_key"], self.key)
        self.assertEqual(entry["status"], "running")
        self.assertIn("example", store.state["international_probe_ledger"]["channels"])

    def test_checkpoint_refuses_to_recreate_missing_reservation(self):
        state = copy.deepcopy(self.state)
        state["run_ledger"]["entries"] = []
        store = FakeStore(state)
        with self.assertRaisesRegex(RuntimeError, "active candidate reservation is missing"):
            checkpoint_remote_probe_ledger(store, self.key, self.probes)
        self.assertEqual(store.saves, 0)

    def test_checkpoint_reloads_and_retries_after_compare_and_swap_conflict(self):
        store = FakeStore(self.state)
        store.conflict_once = True
        checkpoint_remote_probe_ledger(store, self.key, self.probes)
        self.assertEqual(store.state["unrelated_marker"], "kept")
        self.assertEqual(store.state["run_ledger"]["entries"][0]["status"], "running")
        self.assertEqual(store.saves, 1)


if __name__ == "__main__":
    unittest.main()
