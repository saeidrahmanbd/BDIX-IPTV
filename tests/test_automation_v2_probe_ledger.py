import sys
import unittest
import json
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.international.probe_ledger import empty_ledger, parse_ledger, probes_for, record_probe, record_probes
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


    def test_url_fingerprint_round_trips_with_observation(self):
        fingerprint="a"*64
        text=record_probe(None,"channel-a",Probe(date(2026,11,13),404,url_fingerprint=fingerprint))
        self.assertEqual(probes_for(parse_ledger(text),"channel-a")[0].url_fingerprint,fingerprint)

    def test_invalid_url_fingerprint_is_rejected(self):
        bad=json.dumps({
            "schema_version":1,"timezone":"Asia/Dhaka",
            "channels":{"channel-a":[{"day":"2026-11-13","url_fingerprint":"not-a-digest"}]},
        })
        with self.assertRaisesRegex(ValueError,"URL fingerprint"):
            parse_ledger(bad)


    def test_batch_recording_persists_multiple_url_bound_observations(self):
        from automation.engines.international.probe_ledger import record_probes
        observations=[
            ("channel-a",Probe(date(2026,11,13),404,url_fingerprint="a"*64)),
            ("channel-b",Probe(date(2026,11,13),200,stream_state="verified",url_fingerprint="b"*64)),
        ]
        ledger=parse_ledger(record_probes(None,observations))
        self.assertEqual(probes_for(ledger,"channel-a")[0].url_fingerprint,"a"*64)
        self.assertEqual(probes_for(ledger,"channel-b")[0].stream_state,"verified")

if __name__=="__main__":
    unittest.main()
