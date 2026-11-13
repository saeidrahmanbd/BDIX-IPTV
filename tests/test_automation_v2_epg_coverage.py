import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.epg.coverage import calculate_coverage, compare_coverage

PLAYLIST = '#EXTM3U\n#EXTINF:-1 tvg-id="a" group-title="Bangladesh",A\nhttps://a.example/a\n#EXTINF:-1 tvg-id="b" group-title="Bangladesh",B\nhttps://b.example/b\n'
BASE = '<tv><channel id="a"/><programme channel="a" start="20261113090000" stop="20261113100000"/></tv>'
BETTER = '<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261113090000" stop="20261113100000"/><programme channel="b" start="20261113090000" stop="20261113100000"/></tv>'
WORSE = '<tv><channel id="a"/><programme channel="a" start="20261113090000" stop="20261113100000"/></tv>'

class EpgCoverageTests(unittest.TestCase):
    def test_calculate_mapping_and_schedule_coverage(self):
        result=calculate_coverage(PLAYLIST,BASE)
        self.assertEqual((result.active_channel_ids,result.mapped_channel_ids,result.scheduled_channel_ids),(2,1,1))
        self.assertEqual(result.unmapped_ids,("b",))

    def test_coverage_improvement_accepted(self):
        result=compare_coverage(PLAYLIST,BASE,BETTER)
        self.assertTrue(result.accepted)
        self.assertEqual(result.candidate.mapped_channel_ids,2)

    def test_coverage_regression_rejected(self):
        result=compare_coverage(PLAYLIST,BETTER,WORSE)
        self.assertFalse(result.accepted)
        self.assertIn("mapped channel coverage regressed",result.reasons)
        self.assertIn("programme schedule coverage regressed",result.reasons)

    def test_equal_counts_cannot_hide_lost_channel_mappings(self):
        playlist=PLAYLIST + '#EXTINF:-1 tvg-id="c" group-title="Bangladesh",C\nhttps://c.example/c\n'
        baseline='<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261113090000" stop="20261113100000"/><programme channel="b" start="20261113090000" stop="20261113100000"/></tv>'
        candidate='<tv><channel id="a"/><channel id="c"/><programme channel="a" start="20261113090000" stop="20261113100000"/><programme channel="c" start="20261113090000" stop="20261113100000"/></tv>'
        result=compare_coverage(playlist,baseline,candidate)
        self.assertFalse(result.accepted)
        self.assertIn("mapped channel IDs lost: b",result.reasons)

    def test_inactive_queue_groups_are_not_counted_as_active_epg_channels(self):
        playlist=PLAYLIST + '#EXTINF:-1 tvg-id="backup-id" group-title="Backup",Backup\nhttps://backup.example/live\n' + '#EXTINF:-1 tvg-id="review-id" group-title="Review",Review\nhttps://review.example/live\n'
        result=calculate_coverage(playlist,BASE)
        self.assertEqual(result.active_channel_ids,2)
        self.assertEqual(result.unmapped_ids,("b",))

    def test_invalid_xmltv_rejected(self):
        with self.assertRaisesRegex(ValueError,"failed validation"):
            calculate_coverage(PLAYLIST,"<tv>")

    def test_playlist_without_tvg_ids_rejected(self):
        with self.assertRaisesRegex(ValueError,"no active tvg-id"):
            calculate_coverage('#EXTM3U\n#EXTINF:-1 group-title="Bangladesh",A\nhttps://a.example/a\n',BASE)

if __name__=="__main__":
    unittest.main()
