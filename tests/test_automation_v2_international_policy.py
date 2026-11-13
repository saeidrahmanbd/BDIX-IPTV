import sys
import unittest
from datetime import date, timedelta
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "automation/engines/international"))
from stream_failure_policy import Probe, is_definitive_failure, consecutive_definitive_failure_days, action_for_failure_streak

class InternationalFailurePolicyTests(unittest.TestCase):
    def test_only_404_and_410_are_definitive(self):
        self.assertTrue(is_definitive_failure(Probe(date(2026,11,13),404)))
        self.assertTrue(is_definitive_failure(Probe(date(2026,11,13),410)))
        for code in (401,403,429,500,502,503,None):
            self.assertFalse(is_definitive_failure(Probe(date(2026,11,13),code)))

    def test_network_auth_rate_limit_and_geo_block_never_definitive(self):
        d=date(2026,11,13)
        self.assertFalse(is_definitive_failure(Probe(d,404,network_error=True)))
        self.assertFalse(is_definitive_failure(Probe(d,404,auth_error=True)))
        self.assertFalse(is_definitive_failure(Probe(d,404,rate_limited=True)))
        self.assertFalse(is_definitive_failure(Probe(d,404,geo_blocked=True)))

    def test_two_days_move_to_review_not_remove(self):
        today=date(2026,11,13)
        probes=[Probe(today-timedelta(days=i),404) for i in range(2)]
        self.assertEqual(consecutive_definitive_failure_days(probes,today),2)
        self.assertEqual(action_for_failure_streak(2),"MOVE_TO_REVIEW")

    def test_three_consecutive_days_are_only_eligible_for_removal_review(self):
        today=date(2026,11,13)
        probes=[Probe(today-timedelta(days=i),410) for i in range(3)]
        self.assertEqual(consecutive_definitive_failure_days(probes,today),3)
        self.assertEqual(action_for_failure_streak(3),"ELIGIBLE_FOR_REMOVAL_REVIEW")

    def test_missing_day_resets_streak(self):
        today=date(2026,11,13)
        probes=[Probe(today,404),Probe(today-timedelta(days=2),404)]
        self.assertEqual(consecutive_definitive_failure_days(probes,today),1)

    def test_ambiguous_duplicate_day_resets_streak(self):
        today=date(2026,11,13)
        probes=[Probe(today,404),Probe(today,410),Probe(today-timedelta(days=1),404)]
        self.assertEqual(consecutive_definitive_failure_days(probes,today),0)

    def test_inconclusive_day_resets_streak(self):
        today=date(2026,11,13)
        probes=[Probe(today,404),Probe(today-timedelta(days=1),403),Probe(today-timedelta(days=2),404)]
        self.assertEqual(consecutive_definitive_failure_days(probes,today),1)

if __name__=="__main__":
    unittest.main()
