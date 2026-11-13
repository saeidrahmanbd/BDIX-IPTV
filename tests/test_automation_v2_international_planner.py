import sys
import unittest
from datetime import date, timedelta
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.international.planner import RowLifecycleInput, plan_lifecycle
from automation.engines.international.stream_failure_policy import Probe

PLAYLIST='#EXTM3U\n#EXTINF:-1 tvg-id="a" tvg-chno="1" group-title="Review",A\nhttps://a.example/a\n#EXTINF:-1 tvg-id="b" tvg-chno="2" group-title="Review",B\nhttps://b.example/b\n'

class InternationalPlannerTests(unittest.TestCase):
    def test_review_channel_returns_to_fixed_india_group_when_verified_primary(self):
        result=plan_lifecycle(PLAYLIST,[RowLifecycleInput(0,"a","India","primary")],date(2026,11,13))
        self.assertEqual(result.changes[0].target_group,"India")
        self.assertFalse(result.publish)

    def test_small_country_group_recovery_goes_to_backup(self):
        result=plan_lifecycle(PLAYLIST,[RowLifecycleInput(0,"a","Nepal","primary")],date(2026,11,13))
        self.assertEqual(result.changes[0].target_group,"Backup")

    def test_five_unique_verified_primary_identities_allow_country_group(self):
        text="#EXTM3U\n"+"".join(f'#EXTINF:-1 tvg-id="n{i}" group-title="Review",N{i}\nhttps://n{i}.example/live\n' for i in range(5))
        inputs=[RowLifecycleInput(i,f"n{i}","Nepal","primary") for i in range(5)]
        result=plan_lifecycle(text,inputs,date(2026,11,13))
        self.assertEqual(len(result.changes),5)
        self.assertTrue(all(change.target_group=="Nepal" for change in result.changes))

    def test_three_failures_authorize_removal_without_review(self):
        today=date(2026,11,13)
        probes=tuple(Probe(today-timedelta(days=i),404) for i in range(3))
        result=plan_lifecycle(PLAYLIST,[RowLifecycleInput(0,"a",probes=probes)],today)
        self.assertEqual(result.remove_identities,("a",))
        self.assertEqual(result.changes,())
        self.assertEqual(result.review_identities,())
        self.assertFalse(result.publish)

    def test_row_identity_must_match_tvg_id(self):
        with self.assertRaisesRegex(ValueError,"does not match"):
            plan_lifecycle(PLAYLIST,[RowLifecycleInput(0,"wrong-id")],date(2026,11,13))

    def test_invalid_duplicate_row_inputs_rejected(self):
        inputs=[RowLifecycleInput(0,"a"),RowLifecycleInput(0,"b")]
        with self.assertRaisesRegex(ValueError,"duplicate"):
            plan_lifecycle(PLAYLIST,inputs,date(2026,11,13))


    def test_verified_indian_movie_group_is_preserved_not_moved_to_backup(self):
        result=plan_lifecycle(PLAYLIST,[RowLifecycleInput(0,"a","Indian Movies","primary")],date(2026,11,13))
        self.assertEqual(result.changes[0].target_group,"Indian Movies")

if __name__=="__main__":
    unittest.main()
