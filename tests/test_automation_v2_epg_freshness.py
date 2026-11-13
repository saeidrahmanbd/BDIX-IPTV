import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.epg.freshness import calculate_freshness, compare_freshness

PLAYLIST='#EXTM3U\n#EXTINF:-1 tvg-id="a" group-title="Bangladesh",A\nhttps://a.example/a\n#EXTINF:-1 tvg-id="b" group-title="Bangladesh",B\nhttps://b.example/b\n'
BASE='<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261113090000 +0600" stop="20261113100000 +0600"/><programme channel="b" start="20261112090000 +0600" stop="20261112100000 +0600"/></tv>'
BETTER='<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261113090000 +0600" stop="20261113100000 +0600"/><programme channel="b" start="20261113110000 +0600" stop="20261113120000 +0600"/></tv>'
WORSE='<tv><channel id="a"/><channel id="b"/><programme channel="a" start="20261112090000 +0600" stop="20261112100000 +0600"/><programme channel="b" start="20261112090000 +0600" stop="20261112100000 +0600"/></tv>'
AS_OF=datetime(2026,11,13,3,0,tzinfo=timezone.utc)

class EpgFreshnessTests(unittest.TestCase):
    def test_counts_future_scheduled_and_stale_only_channels(self):
        result=calculate_freshness(PLAYLIST,BASE,AS_OF)
        self.assertEqual(result.fresh_scheduled_channel_ids,("a",))
        self.assertEqual(result.stale_only_channel_ids,("b",))
        self.assertEqual(result.no_schedule_channel_ids,())

    def test_candidate_with_improved_freshness_accepted(self):
        result=compare_freshness(PLAYLIST,BASE,BETTER,AS_OF)
        self.assertTrue(result.accepted)
        self.assertEqual(result.candidate.fresh_scheduled_channel_ids,("a","b"))

    def test_candidate_losing_future_schedule_rejected(self):
        result=compare_freshness(PLAYLIST,BASE,WORSE,AS_OF)
        self.assertFalse(result.accepted)
        self.assertIn("b",result.reasons[0])

    def test_naive_as_of_rejected(self):
        with self.assertRaisesRegex(ValueError,"timezone-aware"):
            calculate_freshness(PLAYLIST,BASE,datetime(2026,11,13,3,0))

    def test_invalid_timezone_offset_rejected(self):
        bad='<tv><channel id="a"/><programme channel="a" start="20261113090000 +9999" stop="20261113100000 +9999"/></tv>'
        with self.assertRaisesRegex(ValueError,"failed validation|timezone offset"):
            calculate_freshness(PLAYLIST,bad,AS_OF)

if __name__=="__main__":
    unittest.main()
