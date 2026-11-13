import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.epg.candidate_gate import evaluate_candidate

BASE='<tv><channel id="a"/><programme channel="a" start="20261113090000" stop="20261113100000"/></tv>'
BETTER='<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261113090000" stop="20261113100000"/><programme channel="b" start="20261113090000" stop="20261113100000"/></tv>'

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
        baseline='<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261113090000" stop="20261113100000"/><programme channel="b" start="20261113090000" stop="20261113100000"/></tv>'
        candidate='<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261113090000" stop="20261113100000"/></tv>'
        result=evaluate_candidate(baseline,candidate,playlist)
        self.assertFalse(result.accepted)
        self.assertIn("coverage regressed",result.reason)

    def test_channel_count_regression_rejected(self):
        result=evaluate_candidate(BETTER,BASE)
        self.assertFalse(result.accepted)
        self.assertIn("regressed",result.reason)

if __name__=="__main__":
    unittest.main()
