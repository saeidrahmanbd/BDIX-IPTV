import sys
import unittest
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.core.run_ledger import RunRequest, LedgerEntry, make_idempotency_key, reserve_run

class RunLedgerTests(unittest.TestCase):
    def setUp(self):
        self.request=RunRequest("iptv",date(2026,11,13),"a"*40,"b"*64)

    def test_idempotency_key_is_deterministic(self):
        self.assertEqual(make_idempotency_key(self.request),make_idempotency_key(self.request))

    def test_hex_case_does_not_change_idempotency_key(self):
        upper=RunRequest("IPTV",date(2026,11,13),"A"*40,"B"*64)
        self.assertEqual(make_idempotency_key(self.request),make_idempotency_key(upper))

    def test_exact_successful_input_is_not_run_twice(self):
        key=make_idempotency_key(self.request)
        entry=LedgerEntry(key,"iptv",date(2026,11,13),"a"*40,"succeeded",1)
        result=reserve_run(self.request,[entry])
        self.assertFalse(result.allowed)
        self.assertIn("already completed",result.reason)

    def test_same_engine_running_is_blocked(self):
        entry=LedgerEntry("other","iptv",date(2026,11,12),"a"*40,"running",1)
        result=reserve_run(self.request,[entry])
        self.assertFalse(result.allowed)
        self.assertIn("already running",result.reason)

    def test_global_transaction_lock_blocks_all_engines(self):
        result=reserve_run(self.request,[],active_transaction_id="tx-1")
        self.assertFalse(result.allowed)
        self.assertIn("global lock",result.reason)

    def test_failed_run_can_retry_with_incremented_attempt(self):
        key=make_idempotency_key(self.request)
        entry=LedgerEntry(key,"iptv",date(2026,11,13),"a"*40,"failed",2)
        result=reserve_run(self.request,[entry])
        self.assertTrue(result.allowed)
        self.assertEqual(result.attempt,3)

    def test_different_engine_has_independent_running_lock(self):
        entry=LedgerEntry("other","international",date(2026,11,13),"a"*40,"running",1)
        self.assertTrue(reserve_run(self.request,[entry]).allowed)

    def test_invalid_fingerprint_rejected(self):
        request=RunRequest("iptv",date(2026,11,13),"a"*40,"bad")
        with self.assertRaisesRegex(ValueError,"SHA-256"):
            reserve_run(request,[])

if __name__=="__main__":
    unittest.main()
