import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from automation.core.github_state_store import StateSnapshot, empty_state
from automation.core.v2_candidate_runner import run_candidate_bundle


class MemoryStore:
    def __init__(self):
        self.state = empty_state()
        self.sha = "a" * 40
    def load(self):
        return StateSnapshot(self.state, self.sha)
    def save(self, state, expected_sha):
        if expected_sha != self.sha:
            raise RuntimeError("state compare-and-swap failed")
        self.state = state
        self.sha = chr(ord(self.sha[0]) + 1) * 40
        return self.sha


def fixture_runs(iptv_text, intl_text, ledger):
    iptv = SimpleNamespace(
        candidate=SimpleNamespace(text=iptv_text, candidate_rows=1),
        source_warnings=(),
        publish=False,
    )
    maintenance = SimpleNamespace(
        candidate=SimpleNamespace(text=intl_text, candidate_rows=1),
        ledger_json=ledger,
        probed_count=2,
        reused_count=3,
        publish=False,
    )
    international = SimpleNamespace(maintenance=maintenance, publish=False)
    epg = SimpleNamespace(
        xml_text='<tv><programme channel="a" start="20261113090000 +0600" stop="20261113100000 +0600"><title>News</title></programme></tv>',
        decision=SimpleNamespace(accepted=True, errors=()),
        publish=False,
    )
    return iptv, international, epg


class CandidateBundleRunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "epg").mkdir()
        self.iptv = '#EXTM3U\n#EXTINF:-1 tvg-id="bd" group-title="Bangladesh",BD\nhttps://bd.example/live\n'
        self.international = '#EXTM3U\n#EXTINF:-1 tvg-id="np" group-title="Nepal",NP\nhttps://np.example/live\n'
        self.epg = '<tv><channel id="bd"><display-name>BD</display-name></channel></tv>'
        (self.root / "IPTV-Playlist.m3u").write_text(self.iptv)
        (self.root / "International-Playlist.m3u").write_text(self.international)
        (self.root / "epg/epg.xml").write_text(self.epg)
        self.store = MemoryStore()

    def tearDown(self):
        self.temp.cleanup()

    def test_all_three_candidates_stage_as_one_non_publishing_bundle(self):
        ledger = '{"schema_version":1,"timezone":"Asia/Dhaka","channels":{}}'
        iptv, intl, epg = fixture_runs(self.iptv, self.international, ledger)
        with patch("automation.core.v2_candidate_runner.run_iptv_discovery", return_value=iptv), \
             patch("automation.core.v2_candidate_runner.run_international_discovery", return_value=intl), \
             patch("automation.core.v2_candidate_runner.build_epg_source_candidate", return_value="<tv/>"), \
             patch("automation.core.v2_candidate_runner.build_epg_candidate", return_value=epg):
            decision, result = run_candidate_bundle(self.root, date(2026,11,13), "b"*40, self.store)
        self.assertTrue(decision.allowed)
        self.assertFalse(result.publish)
        self.assertEqual(result.epg_programmes, 1)
        self.assertTrue(Path(result.transaction_path).is_dir())
        self.assertEqual(self.store.state["run_ledger"]["entries"][0]["status"], "succeeded")
        self.assertEqual((self.root / "IPTV-Playlist.m3u").read_text(), self.iptv)
        self.assertEqual((self.root / "International-Playlist.m3u").read_text(), self.international)
        self.assertEqual((self.root / "epg/epg.xml").read_text(), self.epg)

    def test_rejected_epg_candidate_fails_bundle_without_staging(self):
        ledger = '{"schema_version":1,"timezone":"Asia/Dhaka","channels":{}}'
        iptv, intl, epg = fixture_runs(self.iptv, self.international, ledger)
        epg.decision = SimpleNamespace(accepted=False, reason="coverage regression")
        with patch("automation.core.v2_candidate_runner.run_iptv_discovery", return_value=iptv), \
             patch("automation.core.v2_candidate_runner.run_international_discovery", return_value=intl), \
             patch("automation.core.v2_candidate_runner.build_epg_source_candidate", return_value="<tv/>"), \
             patch("automation.core.v2_candidate_runner.build_epg_candidate", return_value=epg):
            with self.assertRaisesRegex(ValueError, "coverage regression"):
                run_candidate_bundle(self.root, date(2026,11,13), "b"*40, self.store)
        self.assertEqual(self.store.state["run_ledger"]["entries"][0]["status"], "failed")
        transactions = self.root / "reports/automation-v2/candidates/transactions"
        self.assertFalse(transactions.exists())

    def test_successful_identical_bundle_is_not_reexecuted(self):
        ledger = '{"schema_version":1,"timezone":"Asia/Dhaka","channels":{}}'
        iptv, intl, epg = fixture_runs(self.iptv, self.international, ledger)
        with patch("automation.core.v2_candidate_runner.run_iptv_discovery", return_value=iptv) as run_iptv, \
             patch("automation.core.v2_candidate_runner.run_international_discovery", return_value=intl), \
             patch("automation.core.v2_candidate_runner.build_epg_source_candidate", return_value="<tv/>"), \
             patch("automation.core.v2_candidate_runner.build_epg_candidate", return_value=epg):
            first, result = run_candidate_bundle(self.root, date(2026,11,13), "b"*40, self.store)
            second, skipped = run_candidate_bundle(self.root, date(2026,11,13), "b"*40, self.store)
        self.assertTrue(first.allowed)
        self.assertFalse(second.allowed)
        self.assertIsNone(skipped)
        run_iptv.assert_called_once()



    def test_epg_source_failure_preserves_completed_probe_checkpoint_and_marks_run_failed(self):
        from automation.engines.international.probe_ledger import record_probe
        from automation.engines.international.stream_failure_policy import Probe

        observation = Probe(
            date(2026, 11, 14), 404, stream_state="dead",
            reason="HTTP 404", url_fingerprint="d" * 64,
        )
        ledger = record_probe(
            '{"schema_version":1,"timezone":"Asia/Dhaka","channels":{}}',
            "probe-me", observation,
        )
        iptv, intl, epg = fixture_runs(self.iptv, self.international, ledger)

        with patch("automation.core.v2_candidate_runner.run_iptv_discovery", return_value=iptv), \\
             patch("automation.core.v2_candidate_runner.run_international_discovery", return_value=intl), \\
             patch("automation.core.v2_candidate_runner.build_epg_source_candidate", side_effect=RuntimeError("EPG source timeout")):
            with self.assertRaisesRegex(RuntimeError, "EPG source timeout"):
                run_candidate_bundle(self.root, date(2026, 11, 14), "b" * 40, self.store)

        saved = self.store.state["international_probe_ledger"]["channels"]["probe-me"]
        self.assertEqual(len(saved), 1)
        self.assertEqual(saved[0]["day"], "2026-11-14")
        self.assertEqual(saved[0]["url_fingerprint"], "d" * 64)
        self.assertEqual(self.store.state["run_ledger"]["entries"][0]["status"], "failed")
        self.assertFalse((self.root / "reports/automation-v2/candidates/transactions").exists())
        self.assertEqual((self.root / "IPTV-Playlist.m3u").read_text(), self.iptv)
        self.assertEqual((self.root / "International-Playlist.m3u").read_text(), self.international)
        self.assertEqual((self.root / "epg/epg.xml").read_text(), self.epg)

if __name__ == "__main__":
    unittest.main()
