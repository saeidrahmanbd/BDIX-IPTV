import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.epg.candidate_gate import evaluate_candidate

BASE='<tv><channel id="a"/><programme channel="a" start="20261113090000" stop="20261113100000"/></tv>'
BETTER='<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261114090000" stop="20261114100000"/><programme channel="b" start="20261114090000" stop="20261114100000"/></tv>'

class EpgCandidateGateTests(unittest.TestCase):
    def test_valid_nonregressing_candidate_accepted_but_not_published(self):
        result=evaluate_candidate(BASE,BETTER)
        self.assertTrue(result.accepted)
        self.assertIn("publication remains disabled",result.reason)

    def test_invalid_candidate_rejected(self):
        result=evaluate_candidate(BASE,"<tv>")
        self.assertFalse(result.accepted)
        self.assertIn("candidate failed validation",result.reason)

    def test_invalid_baseline_fails_closed(self):
        result=evaluate_candidate("<tv/>",BETTER)
        self.assertFalse(result.accepted)
        self.assertIn("baseline",result.reason)

    def test_active_playlist_coverage_regression_rejected(self):
        playlist='#EXTM3U\n#EXTINF:-1 tvg-id="a" group-title="Bangladesh",A\nhttps://a.example/a\n#EXTINF:-1 tvg-id="b" group-title="Bangladesh",B\nhttps://b.example/b\n'
        baseline='<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261114090000" stop="20261114100000"/><programme channel="b" start="20261114090000" stop="20261114100000"/></tv>'
        candidate='<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261114090000" stop="20261114100000"/></tv>'
        # Pin the clock before the programme start; relying on wall-clock time
        # made this regression test pass or fail depending on when CI ran.
        from datetime import datetime, timezone
        as_of = datetime(2026, 11, 13, 23, 0, tzinfo=timezone.utc)
        result=evaluate_candidate(baseline,candidate,playlist,as_of)
        self.assertFalse(result.accepted)
        self.assertIn("schedule freshness regressed",result.reason)

    def test_future_schedule_regression_rejected(self):
        from datetime import datetime, timezone
        playlist='#EXTM3U\n#EXTINF:-1 tvg-id="a" group-title="Bangladesh",A\nhttps://a.example/a\n#EXTINF:-1 tvg-id="b" group-title="Bangladesh",B\nhttps://b.example/b\n'
        baseline='<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261113090000 +0600" stop="20261113100000 +0600"/><programme channel="b" start="20261113110000 +0600" stop="20261113120000 +0600"/></tv>'
        candidate='<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261112090000 +0600" stop="20261112100000 +0600"/><programme channel="b" start="20261112090000 +0600" stop="20261112100000 +0600"/></tv>'
        as_of=datetime(2026,11,13,3,0,tzinfo=timezone.utc)
        result=evaluate_candidate(baseline,candidate,playlist,as_of)
        self.assertFalse(result.accepted)
        self.assertIn("schedule freshness regressed",result.reason)

    def test_channel_count_regression_rejected_without_playlist_context(self):
        result=evaluate_candidate(BETTER,BASE)
        self.assertFalse(result.accepted)
        self.assertIn("channel count regressed",result.reason)

    def test_orphan_xmltv_channels_may_be_removed_when_active_playlist_coverage_is_preserved(self):
        playlist='#EXTM3U\n#EXTINF:-1 tvg-id="a" group-title="Bangladesh",A\nhttps://a.example/a\n'
        baseline='<tv><channel id="a"/><channel id="orphan"/><programme channel="a" start="20261113090000" stop="20261113100000"/></tv>'
        candidate='<tv><channel id="a"/><programme channel="a" start="20261113090000" stop="20261113100000"/></tv>'
        result=evaluate_candidate(baseline,candidate,playlist)
        self.assertTrue(result.accepted, result.reason)

if __name__=="__main__":
    unittest.main()
