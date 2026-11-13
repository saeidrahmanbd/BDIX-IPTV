import sys
import tempfile
import unittest
from datetime import date
from unittest.mock import patch
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.iptv.orchestrator import run_iptv_discovery
from automation.engines.international.stream_failure_policy import Probe

DAY=date(2026,11,13)
BASE='#EXTM3U\n#EXTINF:-1 tvg-id="existing.in" tvg-name="Existing",Existing\nhttps://existing.example/live.m3u8\n'
FEED='#EXTM3U\n#EXTINF:-1 tvg-id="new.bd" tvg-name="New Channel",New Channel\nhttps://new.example/live.m3u8\n'

class IptvDiscoveryOrchestratorTests(unittest.TestCase):
    @patch("automation.engines.iptv.orchestrator.fetch_all_source_feeds")
    @patch("automation.engines.iptv.probe_candidates.probe_stream")
    def test_candidate_discovery_and_stream_probe_are_integrated(self,probe,fetch):
        fetch.return_value=({"Bangladesh":FEED},())
        probe.return_value=Probe(DAY,200,stream_state="verified")
        with tempfile.TemporaryDirectory() as temp:
            result=run_iptv_discovery(BASE,temp,DAY)
        self.assertIn('group-title="New Channels"',result.candidate.text)
        self.assertEqual(result.candidate.candidate_rows,2)
        self.assertEqual(result.probes.verified_count,1)
        self.assertFalse(result.publish)

    @patch("automation.engines.iptv.orchestrator.fetch_all_source_feeds")
    def test_source_unavailable_returns_unchanged_candidate(self,fetch):
        fetch.return_value=({},("Bangladesh source unavailable: URLError",))
        with tempfile.TemporaryDirectory() as temp:
            result=run_iptv_discovery(BASE,temp,DAY)
        self.assertEqual(result.candidate.text,BASE)
        self.assertEqual(result.source_warnings,("Bangladesh source unavailable: URLError",))

if __name__=="__main__":
    unittest.main()
