import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.international.candidate_engine import GroupChange, build_candidate

BASE = '#EXTM3U\n#EXTINF:-1 tvg-id="x" tvg-chno="1" group-title="Nepal",A\nhttps://a.example/a.m3u8\n#EXTINF:-1 tvg-id="y" tvg-chno="2" group-title="Nepal",B\nhttps://b.example/b.m3u8\n'

class InternationalCandidateEngineTests(unittest.TestCase):
    def test_group_change_preserves_stream_and_metadata(self):
        result=build_candidate(BASE,[GroupChange(0,"Review","first failed probe")])
        self.assertIn('group-title="Review"',result)
        self.assertIn('https://a.example/a.m3u8',result)
        self.assertIn('tvg-id="x"',result)

    def test_three_day_review_decision_does_not_delete(self):
        result=build_candidate(BASE,[GroupChange(1,"Review","removal review only")])
        self.assertEqual(result.count("#EXTINF:"),2)
        self.assertEqual(result.count("https://"),2)

    def test_duplicate_row_change_rejected(self):
        with self.assertRaisesRegex(ValueError,"duplicate group change"):
            build_candidate(BASE,[GroupChange(0,"Review","x"),GroupChange(0,"Backup","y")])

    def test_out_of_range_row_rejected(self):
        with self.assertRaisesRegex(ValueError,"out of range"):
            build_candidate(BASE,[GroupChange(5,"Review","x")])

    def test_missing_header_rejected(self):
        with self.assertRaisesRegex(ValueError,"#EXTM3U"):
            build_candidate("not a playlist",[GroupChange(0,"Review","x")])

    def test_unchanged_input_returns_identical_text(self):
        self.assertEqual(build_candidate(BASE,[]),BASE)

if __name__=="__main__":
    unittest.main()
