import sys
import unittest
from datetime import date, timedelta
from unittest.mock import patch
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.international.orchestrator import StreamTarget, run_international_candidate, derive_primary_stream_targets
from automation.engines.international.stream_failure_policy import Probe
from automation.engines.international.probe_ledger import parse_ledger, record_probes, url_fingerprint

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
        mock.return_value=Probe(DAY,200,stream_state="verified")
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


    @patch("automation.engines.international.monitor.probe_stream")
    def test_unverified_http_success_does_not_restore_review_channel(self,mock):
        review=PLAYLIST.replace('group-title="Nepal"','group-title="Review"')
        mock.return_value=Probe(DAY,200,stream_state="unknown")
        result=run_international_candidate(review,None,[StreamTarget(0,"a","https://a.example/live","India","primary")],DAY)
        self.assertIn('group-title="Review"',result.candidate.text)

    def test_target_derivation_excludes_queues_and_ambiguous_duplicate_ids(self):
        text = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="primary" group-title="Nepal",Primary\nhttps://one.example/live\n'
            '#EXTINF:-1 tvg-id="duplicate" group-title="Nepal",Duplicate A\nhttps://two.example/live\n'
            '#EXTINF:-1 tvg-id="duplicate" group-title="Nepal",Duplicate B\nhttps://three.example/live\n'
            '#EXTINF:-1 tvg-id="backup" group-title="Backup",Backup\nhttps://four.example/live\n'
            '#EXTINF:-1 tvg-id="review" group-title="Review",Review\nhttps://five.example/live\n'
            '#EXTINF:-1 group-title="Nepal",Missing ID\nhttps://six.example/live\n'
        )
        targets = derive_primary_stream_targets(text)
        self.assertEqual(
            [(item.identity,item.row_index,item.primary_group,item.verified_stream_role) for item in targets],
            [("primary",0,"Nepal","primary"),("review",4,None,None)],
        )


    def test_review_destination_uses_only_explicit_country_and_language_metadata(self):
        text = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="bd-review" tvg-country="BD" group-title="Review",BD Review\nhttps://bd.example/live\n'
            '#EXTINF:-1 tvg-id="in-bn-review" tvg-country="IN" tvg-language="Bengali" group-title="Review",Bangla Review\nhttps://in.example/live\n'
            '#EXTINF:-1 tvg-id="unknown-review" tvg-country="ZZ" group-title="Review",Unknown Review\nhttps://unknown.example/live\n'
        )
        targets = derive_primary_stream_targets(text)
        self.assertEqual(
            [(item.primary_group,item.verified_stream_role) for item in targets],
            [("Bangladesh","primary"),("Indian Bangla","primary"),(None,None)],
        )


    @patch("automation.engines.international.monitor.probe_stream")
    def test_verified_review_channel_returns_to_metadata_supported_primary_group(self,mock):
        review=PLAYLIST.replace('group-title="Nepal"','group-title="Review"')
        mock.return_value=Probe(DAY,200,stream_state="verified")
        result=run_international_candidate(
            review,None,[StreamTarget(0,"a","https://a.example/live","Bangladesh","primary")],DAY
        )
        self.assertIn('group-title="Bangladesh"',result.candidate.text)
        self.assertNotIn('group-title="Review"',result.candidate.text)


    @patch("automation.engines.international.monitor.probe_stream")
    def test_independent_targets_are_probed_and_ledgered_as_one_batch(self,mock):
        playlist = PLAYLIST + (
            '#EXTINF:-1 tvg-id="b" group-title="Nepal",B\n'
            'https://b.example/live\n'
        )
        mock.side_effect = [
            Probe(DAY,200,stream_state="verified"),
            Probe(DAY,200,stream_state="verified"),
        ]
        result = run_international_candidate(
            playlist,None,
            [
                StreamTarget(0,"a","https://a.example/live","Nepal","primary"),
                StreamTarget(1,"b","https://b.example/live","Nepal","primary"),
            ],
            DAY,
        )
        self.assertEqual(result.probed_count,2)
        self.assertEqual(set(parse_ledger(result.ledger_json)["channels"]),{"a","b"})
        self.assertEqual(mock.call_count,2)


    @patch("automation.engines.international.monitor.probe_stream")
    def test_changed_stream_url_is_not_reused_from_prior_probe(self,mock):
        mock.return_value=Probe(DAY,404)
        old=run_international_candidate(
            PLAYLIST,None,[StreamTarget(0,"a","https://a.example/old.m3u8","Nepal","primary")],DAY
        )
        mock.reset_mock()
        mock.return_value=Probe(DAY,200,stream_state="verified")
        new=run_international_candidate(
            PLAYLIST,old.ledger_json,
            [StreamTarget(0,"a","https://a.example/new.m3u8","Nepal","primary")],DAY
        )
        self.assertEqual(new.probed_count,1)
        self.assertEqual(new.reused_count,0)
        self.assertEqual(mock.call_count,1)


    @patch("automation.engines.international.monitor.probe_stream")
    def test_three_consecutive_url_bound_404_days_remove_primary_candidate(self,mock):
        fingerprint=url_fingerprint("https://a.example/live")
        ledger=record_probes(None,[
            ("a",Probe(DAY-timedelta(days=offset),404,url_fingerprint=fingerprint))
            for offset in (2,1,0)
        ])
        result=run_international_candidate(
            PLAYLIST,ledger,
            [StreamTarget(0,"a","https://a.example/live","Nepal","primary")],
            DAY,
        )
        self.assertNotIn('tvg-id="a"',result.candidate.text)
        self.assertEqual(result.candidate.plan.remove_identities,("a",))
        self.assertEqual(result.probed_count,0)
        self.assertEqual(result.reused_count,1)
        mock.assert_not_called()

if __name__=="__main__":
    unittest.main()
