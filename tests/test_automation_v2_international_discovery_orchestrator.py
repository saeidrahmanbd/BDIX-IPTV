import sys
import tempfile
import unittest
from datetime import date
from unittest.mock import patch
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.international.discovery_orchestrator import run_international_discovery
from automation.engines.international.orchestrator import StreamTarget
from automation.engines.international.stream_failure_policy import Probe

DAY=date(2026,11,13)
PLAYLIST='#EXTM3U\n#EXTINF:-1 tvg-id="a.bd" group-title="Bangladesh",A\nhttps://a.example/live.m3u8\n'
FEED='#EXTM3U\n#EXTINF:-1 tvg-id="new.in" tvg-name="India Cinema" tvg-country="IN" group-title="Movies",India Cinema\nhttps://new.example/live.m3u8\n'

class InternationalDiscoveryOrchestratorTests(unittest.TestCase):
    @patch("automation.engines.international.discovery_orchestrator.fetch_international_source")
    @patch("automation.engines.iptv.probe_candidates.probe_stream")
    def test_source_discovery_and_probe_feed_manual_review_queue(self,probe,fetch):
        fetch.return_value=FEED
        probe.return_value=Probe(DAY,200,stream_state="verified")
        with tempfile.TemporaryDirectory() as temp:
            result=run_international_discovery(PLAYLIST,None,[],DAY,temp)
        self.assertIn('group-title="New Channels"',result.maintenance.candidate.text)
        self.assertIn("India Cinema",result.maintenance.candidate.text)
        self.assertFalse(result.publish)

    @patch("automation.engines.international.discovery_orchestrator.fetch_international_source")
    @patch("automation.engines.iptv.probe_candidates.probe_stream")
    def test_definitively_dead_discovery_not_added(self,probe,fetch):
        fetch.return_value=FEED
        probe.return_value=Probe(DAY,404,stream_state="dead",reason="HTTP 404")
        with tempfile.TemporaryDirectory() as temp:
            result=run_international_discovery(PLAYLIST,None,[],DAY,temp)
        self.assertNotIn("India Cinema",result.maintenance.candidate.text)
        self.assertEqual(result.probes.removed_dead,("India Cinema",))

    @patch("automation.engines.international.discovery_orchestrator.fetch_international_source")
    def test_source_failure_does_not_abort_existing_maintenance(self,fetch):
        fetch.side_effect=TimeoutError()
        with tempfile.TemporaryDirectory() as temp:
            result=run_international_discovery(PLAYLIST,None,[],DAY,temp)
        self.assertEqual(result.maintenance.candidate.text,PLAYLIST)
        self.assertTrue(result.source_warnings)

    @patch("automation.engines.international.discovery_orchestrator.fetch_international_source")
    @patch("automation.engines.iptv.probe_candidates.probe_stream")
    def test_non_movie_indian_channel_is_rejected(self,probe,fetch):
        fetch.return_value='#EXTM3U\n#EXTINF:-1 tvg-id="sports.in" tvg-name="India Sports" tvg-country="IN" group-title="Sports",India Sports\nhttps://sports.example/live.m3u8\n'
        probe.return_value=Probe(DAY,200,stream_state="verified")
        with tempfile.TemporaryDirectory() as temp:
            result=run_international_discovery(PLAYLIST,None,[],DAY,temp)
        self.assertNotIn("India Sports",result.maintenance.candidate.text)

    def test_movie_candidate_without_country_metadata_is_retained(self):
        from automation.engines.international.discovery import build_international_discovery_batch
        source='#EXTM3U\n#EXTINF:-1 tvg-id="MysteryCinema" tvg-name="Mystery Cinema" group-title="Movies",Mystery Cinema\nhttps://unknown.example/live.m3u8\n'
        with tempfile.TemporaryDirectory() as temp:
            batch=build_international_discovery_batch(PLAYLIST,source,temp)
        self.assertEqual(len(batch.candidates),1)
        self.assertIn('group-title="New Channels"',batch.candidates[0].extinf)
        self.assertNotIn('tvg-country=',batch.candidates[0].extinf)
        self.assertIn('tvg-content="Movies"',batch.candidates[0].extinf)

if __name__=="__main__":
    unittest.main()
