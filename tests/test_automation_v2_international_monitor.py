import sys
import unittest
from datetime import date, timedelta
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
        mock.return_value=Probe(DAY,404)
        ledger=probe_and_record(None,"channel-a","https://example.com/live",DAY).ledger_json
        mock.reset_mock()
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


    @patch("automation.engines.international.monitor.probe_stream")
    def test_changed_stream_url_is_reprobed_on_the_same_day(self,mock):
        mock.side_effect=[Probe(DAY,404),Probe(DAY,200,stream_state="verified")]
        first=probe_and_record(None,"channel-a","https://example.com/old.m3u8",DAY)
        second=probe_and_record(first.ledger_json,"channel-a","https://example.com/new.m3u8",DAY)
        self.assertFalse(second.already_probed_today)
        self.assertEqual(second.probe_status,200)
        self.assertEqual(second.failure_streak,0)
        self.assertEqual(mock.call_count,2)


    @patch("automation.engines.international.monitor.probe_stream")
    def test_failure_streak_does_not_transfer_to_replacement_url(self,mock):
        from automation.engines.international.probe_ledger import record_probe, url_fingerprint
        old_fingerprint=url_fingerprint("https://example.com/old.m3u8")
        ledger=None
        for offset in (2,1,0):
            day=DAY-timedelta(days=offset)
            ledger=record_probe(
                ledger,"channel-a",
                Probe(day,404,url_fingerprint=old_fingerprint),
            )
        mock.return_value=Probe(DAY,404)
        result=probe_and_record(ledger,"channel-a","https://example.com/new.m3u8",DAY)
        self.assertEqual(result.failure_streak,1)
        self.assertFalse(result.already_probed_today)
        mock.assert_called_once()

if __name__=="__main__":
    unittest.main()
