import sys
import unittest
from datetime import date
from unittest.mock import patch
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.iptv.probe_candidates import probe_discovery_candidates
from automation.engines.iptv.candidate_engine import DiscoveryCandidate
from automation.engines.international.stream_failure_policy import Probe

DAY=date(2026,11,13)
CANDIDATES=[
    DiscoveryCandidate('#EXTINF:-1 group-title="New Channels",Working','https://working.example/live'),
    DiscoveryCandidate('#EXTINF:-1 group-title="New Channels",Dead','https://dead.example/live'),
    DiscoveryCandidate('#EXTINF:-1 group-title="New Backups",Unknown','https://unknown.example/live',True),
]

class IptvDiscoveryProbeTests(unittest.TestCase):
    @patch("automation.engines.iptv.probe_candidates.probe_stream")
    def test_verified_retained_dead_removed_unknown_retained(self,mock):
        mock.side_effect=[
            Probe(DAY,200,stream_state="verified",reason="HLS playlist"),
            Probe(DAY,404,stream_state="dead",reason="HTTP 404"),
            Probe(DAY,403,auth_error=True,reason="access inconclusive"),
        ]
        result=probe_discovery_candidates(CANDIDATES,DAY)
        self.assertEqual([x.extinf for x in result.retained],[CANDIDATES[0].extinf,CANDIDATES[2].extinf])
        self.assertEqual(result.verified_count,1)
        self.assertEqual(result.inconclusive_count,1)
        self.assertEqual(result.removed_dead,("Dead",))

    @patch("automation.engines.iptv.probe_candidates.probe_stream")
    def test_html_success_marked_dead_is_removed(self,mock):
        mock.return_value=Probe(DAY,200,stream_state="dead",reason="HTML page")
        result=probe_discovery_candidates([CANDIDATES[0]],DAY)
        self.assertEqual(result.retained,())
        self.assertEqual(result.removed_dead,("Working",))

    @patch("automation.engines.iptv.probe_candidates.probe_stream")
    def test_network_failure_retained_for_manual_review(self,mock):
        mock.return_value=Probe(DAY,None,network_error=True)
        result=probe_discovery_candidates([CANDIDATES[0]],DAY)
        self.assertEqual(len(result.retained),1)
        self.assertEqual(result.inconclusive_count,1)

    def test_invalid_worker_count_rejected(self):
        with self.assertRaisesRegex(ValueError,"max_workers"):
            probe_discovery_candidates(CANDIDATES,DAY,max_workers=0)

if __name__=="__main__":
    unittest.main()
