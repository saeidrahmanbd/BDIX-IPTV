import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.core.run_ledger import LedgerEntry
from automation.core.run_ledger_store import LEDGER_PATH, finish_persisted_run, load_run_ledger, parse_run_ledger_json, reserve_persisted_run, save_run_ledger, serialize_run_ledger

class RunLedgerStoreTests(unittest.TestCase):
    def setUp(self):
        self.entries=[LedgerEntry("a"*64,"iptv",date(2026,11,13),"b"*40,"running",1),
                      LedgerEntry("c"*64,"epg",date(2026,11,13),"b"*40,"failed",2)]

    def test_round_trip_serialization(self):
        actual=parse_run_ledger_json(serialize_run_ledger(self.entries))
        self.assertEqual({(e.engine,e.attempt,e.status) for e in actual},{(e.engine,e.attempt,e.status) for e in self.entries})

    def test_local_save_load_uses_atomic_state_path(self):
        with tempfile.TemporaryDirectory() as temp:
            path=save_run_ledger(temp,self.entries)
            self.assertEqual(path,Path(temp)/LEDGER_PATH)
            actual=load_run_ledger(temp)
            self.assertEqual({(e.engine,e.attempt,e.status) for e in actual},{(e.engine,e.attempt,e.status) for e in self.entries})

    def test_missing_ledger_loads_empty(self):
        with tempfile.TemporaryDirectory() as temp:
            self.assertEqual(load_run_ledger(temp),[])

    def test_duplicate_attempt_rejected(self):
        with self.assertRaisesRegex(ValueError,"duplicate"):
            serialize_run_ledger([self.entries[0],self.entries[0]])

    def test_persisted_reservation_blocks_duplicate_same_engine(self):
        from automation.core.run_ledger import RunRequest
        with tempfile.TemporaryDirectory() as temp:
            request=RunRequest("iptv",date(2026,11,13),"b"*40,"d"*64)
            first=reserve_persisted_run(temp,request)
            second=reserve_persisted_run(temp,request)
            self.assertTrue(first.allowed)
            self.assertFalse(second.allowed)
            self.assertEqual(len(load_run_ledger(temp)),1)

    def test_engine_case_does_not_bypass_persisted_lock(self):
        from automation.core.run_ledger import RunRequest
        with tempfile.TemporaryDirectory() as temp:
            reserve_persisted_run(temp,RunRequest("iptv",date(2026,11,13),"b"*40,"d"*64))
            blocked=reserve_persisted_run(temp,RunRequest("IPTV",date(2026,11,13),"b"*40,"e"*64))
            self.assertFalse(blocked.allowed)

    def test_finalize_run_and_allow_retry_after_failure(self):
        from automation.core.run_ledger import RunRequest
        with tempfile.TemporaryDirectory() as temp:
            request=RunRequest("epg",date(2026,11,13),"b"*40,"d"*64)
            first=reserve_persisted_run(temp,request)
            failed=finish_persisted_run(temp,first.idempotency_key,first.attempt,"failed")
            self.assertEqual(failed.status,"failed")
            retry=reserve_persisted_run(temp,request)
            self.assertTrue(retry.allowed)
            self.assertEqual(retry.attempt,2)

    def test_successful_run_cannot_be_reserved_twice(self):
        from automation.core.run_ledger import RunRequest
        with tempfile.TemporaryDirectory() as temp:
            request=RunRequest("epg",date(2026,11,13),"b"*40,"d"*64)
            first=reserve_persisted_run(temp,request)
            finish_persisted_run(temp,first.idempotency_key,first.attempt,"succeeded")
            second=reserve_persisted_run(temp,request)
            self.assertFalse(second.allowed)

    def test_running_attempt_cannot_be_finalized_twice(self):
        from automation.core.run_ledger import RunRequest
        with tempfile.TemporaryDirectory() as temp:
            first=reserve_persisted_run(temp,RunRequest("iptv",date(2026,11,13),"b"*40,"d"*64))
            finish_persisted_run(temp,first.idempotency_key,first.attempt,"cancelled")
            with self.assertRaisesRegex(ValueError,"running"):
                finish_persisted_run(temp,first.idempotency_key,first.attempt,"failed")

    def test_unknown_status_rejected(self):
        bad='{"schema_version":1,"timezone":"Asia/Dhaka","entries":[{"idempotency_key":"'+("a"*64)+'","engine":"iptv","business_day":"2026-11-13","baseline_commit":"'+("b"*40)+'","status":"unknown","attempt":1}]}'
        with self.assertRaisesRegex(ValueError,"status"):
            parse_run_ledger_json(bad)

    def test_invalid_attempt_rejected(self):
        bad='{"schema_version":1,"timezone":"Asia/Dhaka","entries":[{"idempotency_key":"'+("a"*64)+'","engine":"iptv","business_day":"2026-11-13","baseline_commit":"'+("b"*40)+'","status":"running","attempt":0}]}'
        with self.assertRaisesRegex(ValueError,"attempt"):
            parse_run_ledger_json(bad)

    def test_recent_running_lease_blocks_but_expired_lease_allows_retry(self):
        from datetime import datetime, timedelta
        from automation.core.run_ledger import RunRequest, reserve_run, make_idempotency_key
        started = datetime.fromisoformat("2026-11-13T09:00:00+06:00")
        request = RunRequest("iptv", date(2026,11,13), "b"*40, "d"*64,
                             requested_at=started + timedelta(minutes=30))
        running_request = RunRequest("iptv", date(2026,11,13), "b"*40, "d"*64, requested_at=started)
        running = LedgerEntry(make_idempotency_key(running_request),"iptv",date(2026,11,13),"b"*40,"running",1,started)
        blocked = reserve_run(request,[running])
        self.assertFalse(blocked.allowed)
        expired_request = RunRequest("iptv", date(2026,11,13), "b"*40, "d"*64,
                                     requested_at=started + timedelta(hours=4))
        retried = reserve_run(expired_request,[running])
        self.assertTrue(retried.allowed)
        self.assertEqual(retried.attempt,2)

    def test_running_entry_without_timestamp_fails_closed(self):
        from datetime import datetime
        from automation.core.run_ledger import RunRequest, reserve_run
        request = RunRequest("iptv",date(2026,11,13),"b"*40,"d"*64,
                             requested_at=datetime.fromisoformat("2026-11-13T10:00:00+06:00"))
        unknown_age = LedgerEntry(make_idempotency_key(request),"iptv",date(2026,11,13),"b"*40,"running",1)
        self.assertFalse(reserve_run(request,[unknown_age]).allowed)

if __name__=="__main__":
    unittest.main()
