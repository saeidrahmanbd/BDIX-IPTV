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
            raise RuntimeError("stale state")
        self.state = state
        self.sha = "b" * 40
        return self.sha


class CandidateBundleRunnerTests(unittest.TestCase):
    def make_root(self):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "epg").mkdir()
        (root / "reports").mkdir()
        (root / "IPTV-Playlist.m3u").write_text("#EXTM3U\n", encoding="utf-8")
        (root / "International-Playlist.m3u").write_text("#EXTM3U\n", encoding="utf-8")
        (root / "epg/epg.xml").write_text("<tv/>", encoding="utf-8")
        return temp, root

    def test_combined_runner_stages_all_three_outputs_without_touching_production(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        before = {
            name: (root / name).read_bytes()
            for name in ("IPTV-Playlist.m3u", "International-Playlist.m3u", "epg/epg.xml")
        }
        iptv = SimpleNamespace(candidate=SimpleNamespace(text="#EXTM3U\n", candidate_rows=0), publish=False)
        maintenance = SimpleNamespace(
            candidate=SimpleNamespace(text="#EXTM3U\n", candidate_rows=0),
            ledger_json='{"schema_version":1,"timezone":"Asia/Dhaka","channels":{}}',
            probed_count=0, reused_count=0, publish=False,
        )
        international = SimpleNamespace(maintenance=maintenance, publish=False)
        epg = SimpleNamespace(
            xml_text="<tv/>",
            decision=SimpleNamespace(accepted=True, errors=(), candidate_programmes=0),
            publish=False,
        )
        with patch("automation.core.v2_candidate_runner.run_iptv_discovery", return_value=iptv), \
             patch("automation.core.v2_candidate_runner.derive_primary_stream_targets", return_value=[]), \
             patch("automation.core.v2_candidate_runner.run_international_discovery", return_value=international), \
             patch("automation.core.v2_candidate_runner.assert_international_existing_rows_preserved"), \
             patch("automation.core.v2_candidate_runner.build_epg_source_candidate", return_value="<tv/>"), \
             patch("automation.core.v2_candidate_runner.build_epg_candidate", return_value=epg):
            decision, result = run_candidate_bundle(root, date(2026,11,13), "c"*40, MemoryStore())

        self.assertTrue(decision.allowed)
        self.assertIsNotNone(result)
        self.assertFalse(result.publish)
        self.assertEqual(result.epg_programmes, 0)
        self.assertTrue((Path(result.transaction_path) / "transaction-bundle.json").is_file())
        for name, content in before.items():
            self.assertEqual((root / name).read_bytes(), content)

    def test_missing_production_baseline_fails_before_remote_reservation(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        (root / "epg/epg.xml").unlink()
        store = MemoryStore()
        with self.assertRaisesRegex(FileNotFoundError, "epg.xml"):
            run_candidate_bundle(root, date(2026,11,13), "c"*40, store)
        self.assertEqual(store.state["run_ledger"]["entries"], [])


    def test_live_baseline_change_during_candidate_build_aborts_staging(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        store = MemoryStore()
        iptv = SimpleNamespace(candidate=SimpleNamespace(text="#EXTM3U\\n", candidate_rows=0), publish=False)
        maintenance = SimpleNamespace(
            candidate=SimpleNamespace(text="#EXTM3U\\n", candidate_rows=0),
            ledger_json='{"schema_version":1,"timezone":"Asia/Dhaka","channels":{}}',
            probed_count=0, reused_count=0, publish=False,
        )
        international = SimpleNamespace(maintenance=maintenance, publish=False)
        epg = SimpleNamespace(xml_text="<tv/>", decision=SimpleNamespace(accepted=True, errors=()), publish=False)
        def change_live_baseline(*args, **kwargs):
            (root / "IPTV-Playlist.m3u").write_text("#EXTM3U\\n#concurrent-change\\n", encoding="utf-8")
            return iptv
        with patch("automation.core.v2_candidate_runner.run_iptv_discovery", side_effect=change_live_baseline), \\
             patch("automation.core.v2_candidate_runner.derive_primary_stream_targets", return_value=[]), \\
             patch("automation.core.v2_candidate_runner.run_international_discovery", return_value=international), \\
             patch("automation.core.v2_candidate_runner.assert_international_existing_rows_preserved"), \\
             patch("automation.core.v2_candidate_runner.build_epg_source_candidate", return_value="<tv/>"), \\
             patch("automation.core.v2_candidate_runner.build_epg_candidate", return_value=epg):
            with self.assertRaisesRegex(RuntimeError, "baseline changed during candidate generation"):
                run_candidate_bundle(root, date(2026,11,13), "c"*40, store)
        transactions = root / "reports/automation-v2/candidates/transactions"
        self.assertFalse(transactions.exists())
        self.assertEqual(store.state["run_ledger"]["entries"][0]["status"], "failed")

    def test_iptv_candidate_cannot_silently_drop_existing_rows(self):
        temp, root = self.make_root()
        self.addCleanup(temp.cleanup)
        original = '#EXTM3U\\n#EXTINF:-1 tvg-id="x" group-title="Bangladesh",X\\nhttps://x.example/live\\n'
        (root / "IPTV-Playlist.m3u").write_text(original, encoding="utf-8")
        iptv = SimpleNamespace(candidate=SimpleNamespace(text="#EXTM3U\\n", candidate_rows=0), publish=False)
        with patch("automation.core.v2_candidate_runner.run_iptv_discovery", return_value=iptv):
            with self.assertRaisesRegex(ValueError, "removed"):
                run_candidate_bundle(root, date(2026,11,13), "c"*40, MemoryStore())

if __name__ == "__main__":
    unittest.main()
