import sys
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from automation.core.github_state_store import StateSnapshot, empty_state
from automation.engines.iptv.orchestrator import run_iptv_discovery_persisted, IptvDiscoveryRun
from automation.engines.international.orchestrator import (
    run_international_candidate_persisted, InternationalMaintenanceResult,
)
from automation.engines.epg.candidate_engine import build_epg_candidate_persisted, EpgCandidate


class MemoryStateStore:
    def __init__(self):
        self.state = empty_state()
        self.sha = "a" * 40
        self.saves = 0
    def load(self):
        return StateSnapshot(self.state, self.sha)
    def save(self, state, expected_sha):
        if expected_sha != self.sha:
            raise RuntimeError("stale state")
        self.state = state
        self.saves += 1
        self.sha = chr(ord("a") + self.saves) * 40
        return self.sha


class PersistedOrchestratorTests(unittest.TestCase):
    def test_iptv_orchestrator_uses_durable_reservation_and_never_publishes(self):
        store = MemoryStateStore()
        result = IptvDiscoveryRun(candidate=None, discovery=None, probes=None, source_warnings=())
        with patch("automation.engines.iptv.orchestrator.run_iptv_discovery", return_value=result) as run:
            decision, value = run_iptv_discovery_persisted(
                "#EXTM3U\n", ".", date(2026, 11, 13), "b" * 40, store, source_feeds={}
            )
            self.assertTrue(decision.allowed)
            self.assertIs(value, result)
            self.assertFalse(value.publish)
            run.assert_called_once()
            second, skipped = run_iptv_discovery_persisted(
                "#EXTM3U\n", ".", date(2026, 11, 13), "b" * 40, store, source_feeds={}
            )
            self.assertFalse(second.allowed)
            self.assertIsNone(skipped)
            run.assert_called_once()

    def test_international_orchestrator_persists_probe_ledger_and_run_status(self):
        store = MemoryStateStore()
        fake = InternationalMaintenanceResult(
            candidate=None, ledger_json='{"schema_version":1,"timezone":"Asia/Dhaka","channels":{}}',
            probed_count=0, reused_count=0,
        )
        with patch("automation.engines.international.orchestrator.run_international_candidate", return_value=fake) as run:
            decision, value = run_international_candidate_persisted(
                "#EXTM3U\n", [], date(2026, 11, 13), "b" * 40, store
            )
        self.assertTrue(decision.allowed)
        self.assertIs(value, fake)
        self.assertFalse(value.publish)
        self.assertEqual(store.state["international_probe_ledger"]["channels"], {})
        self.assertEqual(store.state["run_ledger"]["entries"][0]["status"], "succeeded")
        run.assert_called_once()

    def test_epg_orchestrator_uses_durable_reservation(self):
        store = MemoryStateStore()
        fake = EpgCandidate(xml_text="<tv/>", decision=None)
        with patch("automation.engines.epg.candidate_engine.build_epg_candidate", return_value=fake) as build:
            decision, value = build_epg_candidate_persisted(
                "#EXTM3U\n", "<tv/>", "b" * 40, store,
                source_candidate_xml="<tv/>",
                as_of=__import__("datetime").datetime(2026, 11, 13, 9, 0),
            )
        self.assertTrue(decision.allowed)
        self.assertIs(value, fake)
        self.assertFalse(value.publish)
        self.assertEqual(store.state["run_ledger"]["entries"][0]["engine"], "epg")
        build.assert_called_once()

    def test_failed_engine_operation_is_marked_failed_and_can_retry(self):
        store = MemoryStateStore()
        fake = EpgCandidate(xml_text="<tv/>", decision=None)
        with patch("automation.engines.epg.candidate_engine.build_epg_candidate", side_effect=RuntimeError("candidate failure")):
            with self.assertRaisesRegex(RuntimeError, "candidate failure"):
                build_epg_candidate_persisted(
                    "#EXTM3U\n", "<tv/>", "b" * 40, store,
                    source_candidate_xml="<tv/>",
                    as_of=__import__("datetime").datetime(2026, 11, 13, 9, 0),
                )
        self.assertEqual(store.state["run_ledger"]["entries"][0]["status"], "failed")
        with patch("automation.engines.epg.candidate_engine.build_epg_candidate", return_value=fake):
            retry, _ = build_epg_candidate_persisted(
                "#EXTM3U\n", "<tv/>", "b" * 40, store,
                source_candidate_xml="<tv/>",
                as_of=__import__("datetime").datetime(2026, 11, 13, 9, 0),
            )
        self.assertTrue(retry.allowed)
        self.assertEqual(retry.attempt, 2)


    def test_epg_persisted_runner_fetches_source_in_isolated_workspace_when_requested(self):
        store = MemoryStateStore()
        fake = EpgCandidate(xml_text="<tv/>", decision=None)
        as_of = __import__("datetime").datetime(2026, 11, 13, 9, 0)
        with patch("automation.engines.epg.source_provider.build_epg_source_candidate", return_value="<tv/>") as source:
            with patch("automation.engines.epg.candidate_engine.build_epg_candidate", return_value=fake) as build:
                decision, value = build_epg_candidate_persisted(
                    "#EXTM3U\n", "<tv/>", "b" * 40, store,
                    as_of=as_of, repository_root=".",
                )
        self.assertTrue(decision.allowed)
        self.assertIs(value, fake)
        source.assert_called_once_with(".", iptv_playlist_text=None, international_playlist_text=None)
        build.assert_called_once()

if __name__ == "__main__":
    unittest.main()
