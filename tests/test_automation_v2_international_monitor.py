import sys
import unittest
from datetime import date
from unittest.mock import patch
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.international.monitor import probe_and_record
from automation.engines.international.probe_ledger import record_probe
from automation.engines.international.stream_failure_policy import Probe

DAY=date(2026,11,13)

class InternationalMonitorTests(unittest.TestCase):
    @patch("automation.engines.international.monitor.probe_stream")
    def test_probe_is_recorded_and_streak_returned(self,mock):
        mock.return_value=Probe(DAY,404)
        result=probe_and_record(None,"channel-a","https://example.com/live",DAY)
        self.assertEqual(result.probe_status,404)
        self.assertEqual(result.failure_streak,1)
        self.assertFalse(result.already_probed_today)

    @patch("automation.engines.international.monitor.probe_stream")
    def test_second_daily_run_reuses_existing_probe_idempotently(self,mock):
        ledger=record_probe(None,"channel-a",Probe(DAY,404))
        result=probe_and_record(ledger,"channel-a","https://example.com/live",DAY)
        mock.assert_not_called()
        self.assertTrue(result.already_probed_today)
        self.assertEqual(result.probe_status,404)
        self.assertEqual(result.ledger_json,ledger)

    @patch("automation.engines.international.monitor.probe_stream")
    def test_network_failure_is_recorded_but_does_not_count(self,mock):
        mock.return_value=Probe(DAY,None,network_error=True)
        result=probe_and_record(None,"channel-a","https://example.com/live",DAY)
        self.assertEqual(result.failure_streak,0)

    def test_malformed_or_unsafe_url_is_recorded_as_inconclusive(self):
        result=probe_and_record(None,"channel-a","file:///tmp/live",DAY)
        self.assertEqual(result.probe_status,None)
        self.assertEqual(result.failure_streak,0)

    def test_identity_required(self):
        with self.assertRaisesRegex(ValueError,"identity"):
            probe_and_record(None," ","https://example.com/live",DAY)

if __name__=="__main__":
    unittest.main()
