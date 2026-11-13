import sys
import unittest
from datetime import date, timedelta
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"automation/engines/international"))
from stream_failure_policy import Probe
from lifecycle import ChannelState, decide_channel

class InternationalLifecycleTests(unittest.TestCase):
    def test_first_definitive_failure_moves_to_review(self):
        today=date(2026,11,13)
        state=ChannelState("id-1","Nepal",probes=(Probe(today,404),))
        result=decide_channel(state,today)
        self.assertEqual((result.target_group,result.action),("Review","MOVE_TO_REVIEW"))

    def test_three_days_require_review_not_automatic_deletion(self):
        today=date(2026,11,13)
        probes=tuple(Probe(today-timedelta(days=i),404) for i in range(3))
        result=decide_channel(ChannelState("id-1","Nepal",probes=probes),today)
        self.assertEqual(result.target_group,"Review")
        self.assertEqual(result.action,"REQUIRES_OWNER_REMOVAL_REVIEW")

    def test_recovered_verified_primary_returns_to_primary(self):
        state=ChannelState("id-1","Review","Nepal","primary",())
        result=decide_channel(state,date(2026,11,13))
        self.assertEqual((result.target_group,result.action),("Nepal","RESTORE_TO_PRIMARY"))

    def test_recovered_verified_alternate_goes_to_backup(self):
        state=ChannelState("id-1","Review","Nepal","alternate",())
        result=decide_channel(state,date(2026,11,13))
        self.assertEqual((result.target_group,result.action),("Backup","RESTORE_TO_BACKUP"))

    def test_unverified_review_channel_stays_in_review(self):
        state=ChannelState("id-1","Review","Nepal",None,())
        result=decide_channel(state,date(2026,11,13))
        self.assertEqual(result.action,"KEEP_REVIEW_UNVERIFIED_OR_UNCLASSIFIED")

    def test_invalid_identity_rejected(self):
        with self.assertRaises(ValueError):
            decide_channel(ChannelState(" ","Review"),date(2026,11,13))

if __name__=="__main__":
    unittest.main()
