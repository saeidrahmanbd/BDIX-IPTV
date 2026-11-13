import sys
import unittest
import json
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.international.probe_ledger import empty_ledger, parse_ledger, probes_for, record_probe
from automation.engines.international.stream_failure_policy import Probe, consecutive_definitive_failure_days

class ProbeLedgerTests(unittest.TestCase):
    def test_record_and_reload_probe(self):
        text=record_probe(None,"channel-a",Probe(date(2026,11,13),404))
        ledger=parse_ledger(text)
        self.assertEqual(len(probes_for(ledger,"channel-a")),1)
        self.assertEqual(probes_for(ledger,"channel-a")[0].stream_state,"unknown")

    def test_duplicate_same_day_probes_fail_closed(self):
        text=record_probe(None,"channel-a",Probe(date(2026,11,13),404))
        text=record_probe(text,"channel-a",Probe(date(2026,11,13),410))
        probes=probes_for(parse_ledger(text),"channel-a")
        self.assertEqual(consecutive_definitive_failure_days(list(probes),date(2026,11,13)),0)

    def test_observations_are_sorted_by_calendar_day(self):
        text=record_probe(None,"channel-a",Probe(date(2026,11,12),404))
        text=record_probe(text,"channel-a",Probe(date(2026,11,10),404))
        dates=[item["day"] for item in json.loads(text)["channels"]["channel-a"]]
        self.assertEqual(dates,["2026-11-10","2026-11-12"])

    def test_invalid_timezone_rejected(self):
        bad=json.dumps({"schema_version":1,"timezone":"UTC","channels":{}})
        with self.assertRaisesRegex(ValueError,"timezone"):
            parse_ledger(bad)

    def test_malformed_date_rejected(self):
        bad=json.dumps({"schema_version":1,"timezone":"Asia/Dhaka","channels":{"a":[{"day":"13-11-2026"}]}})
        with self.assertRaisesRegex(ValueError,"calendar date"):
            parse_ledger(bad)

    def test_empty_identity_rejected(self):
        with self.assertRaisesRegex(ValueError,"identity"):
            record_probe(None," ",Probe(date(2026,11,13),404))

if __name__=="__main__":
    unittest.main()
