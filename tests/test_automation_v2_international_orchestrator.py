import sys
import unittest
from datetime import date
from unittest.mock import patch
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.international.orchestrator import StreamTarget, run_international_candidate
from automation.engines.international.stream_failure_policy import Probe

DAY=date(2026,11,13)
PLAYLIST='#EXTM3U\n#EXTINF:-1 tvg-id="a" group-title="Nepal",A\nhttps://a.example/live\n'

class InternationalOrchestratorTests(unittest.TestCase):
    @patch("automation.engines.international.monitor.probe_stream")
    def test_first_failure_moves_to_review_and_records_ledger(self,mock):
        mock.return_value=Probe(DAY,404)
        result=run_international_candidate(PLAYLIST,None,[StreamTarget(0,"a","https://a.example/live")],DAY)
        self.assertEqual(result.probed_count,1)
        self.assertEqual(result.reused_count,0)
        self.assertIn('group-title="Review"',result.candidate.text)
        self.assertIn('"status_code": 404',result.ledger_json)
        self.assertFalse(result.publish)

    @patch("automation.engines.international.monitor.probe_stream")
    def test_same_day_rerun_reuses_probe_without_network_call(self,mock):
        mock.return_value=Probe(DAY,404)
        first=run_international_candidate(PLAYLIST,None,[StreamTarget(0,"a","https://a.example/live")],DAY)
        mock.reset_mock()
        second=run_international_candidate(PLAYLIST,first.ledger_json,[StreamTarget(0,"a","https://a.example/live")],DAY)
        mock.assert_not_called()
        self.assertEqual(second.probed_count,0)
        self.assertEqual(second.reused_count,1)
        self.assertEqual(second.ledger_json,first.ledger_json)

    @patch("automation.engines.international.monitor.probe_stream")
    def test_verified_working_review_stream_restores_primary(self,mock):
        review=PLAYLIST.replace('group-title="Nepal"','group-title="Review"')
        mock.return_value=Probe(DAY,200)
        result=run_international_candidate(review,None,[StreamTarget(0,"a","https://a.example/live","India","primary")],DAY)
        self.assertIn('group-title="India"',result.candidate.text)

    @patch("automation.engines.international.monitor.probe_stream")
    def test_discovery_candidates_are_combined_with_existing_maintenance(self,mock):
        from automation.engines.iptv.candidate_engine import DiscoveryCandidate
        mock.return_value=Probe(DAY,200,stream_state="verified")
        discovery=DiscoveryCandidate('#EXTINF:-1 group-title="New Channels",New','https://new.example/live.m3u8')
        result=run_international_candidate(PLAYLIST,None,[],DAY,discoveries=[discovery])
        self.assertIn('group-title="New Channels"',result.candidate.text)
        self.assertIn('https://new.example/live.m3u8',result.candidate.text)
        self.assertEqual(result.candidate.candidate_rows,2)

    def test_duplicate_targets_rejected(self):
        targets=[StreamTarget(0,"a","https://a.example/live"),StreamTarget(0,"b","https://b.example/live")]
        with self.assertRaisesRegex(ValueError,"row index"):
            run_international_candidate(PLAYLIST,None,targets,DAY)

if __name__=="__main__":
    unittest.main()
