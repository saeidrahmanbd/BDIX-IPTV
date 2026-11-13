import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.core.run_ledger import LedgerEntry
from automation.core.run_ledger_store import LEDGER_PATH, load_run_ledger, parse_run_ledger_json, save_run_ledger, serialize_run_ledger

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
            self.assertEqual(load_run_ledger(temp),self.entries)

    def test_missing_ledger_loads_empty(self):
        with tempfile.TemporaryDirectory() as temp:
            self.assertEqual(load_run_ledger(temp),[])

    def test_duplicate_attempt_rejected(self):
        with self.assertRaisesRegex(ValueError,"duplicate"):
            serialize_run_ledger([self.entries[0],self.entries[0]])

    def test_unknown_status_rejected(self):
        bad='{"schema_version":1,"timezone":"Asia/Dhaka","entries":[{"idempotency_key":"'+("a"*64)+'","engine":"iptv","business_day":"2026-11-13","baseline_commit":"'+("b"*40)+'","status":"unknown","attempt":1}]}'
        with self.assertRaisesRegex(ValueError,"status"):
            parse_run_ledger_json(bad)

    def test_invalid_attempt_rejected(self):
        bad='{"schema_version":1,"timezone":"Asia/Dhaka","entries":[{"idempotency_key":"'+("a"*64)+'","engine":"iptv","business_day":"2026-11-13","baseline_commit":"'+("b"*40)+'","status":"running","attempt":0}]}'
        with self.assertRaisesRegex(ValueError,"attempt"):
            parse_run_ledger_json(bad)

if __name__=="__main__":
    unittest.main()
