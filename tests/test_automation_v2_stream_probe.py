import sys
import unittest
from datetime import date
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError, URLError
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.international.stream_probe import probe_stream
from automation.engines.international.stream_failure_policy import is_definitive_failure

DAY=date(2026,11,13)

class StreamProbeTests(unittest.TestCase):
    @patch("automation.engines.international.stream_probe.urlopen")
    def test_200_is_working(self,mock):
        response=MagicMock()
        response.__enter__.return_value.getcode.return_value=200
        mock.return_value=response
        result=probe_stream("https://example.com/live.m3u8",DAY)
        self.assertEqual(result.status_code,200)
        self.assertFalse(is_definitive_failure(result))

    @patch("automation.engines.international.stream_probe.urlopen")
    def test_404_is_definitive(self,mock):
        mock.side_effect=HTTPError("https://example.com/live",404,"Not Found",{},None)
        result=probe_stream("https://example.com/live",DAY)
        self.assertTrue(is_definitive_failure(result))

    @patch("automation.engines.international.stream_probe.urlopen")
    def test_410_is_definitive(self,mock):
        mock.side_effect=HTTPError("https://example.com/live",410,"Gone",{},None)
        result=probe_stream("https://example.com/live",DAY)
        self.assertTrue(is_definitive_failure(result))

    @patch("automation.engines.international.stream_probe.urlopen")
    def test_auth_rate_limit_and_geo_block_are_inconclusive(self,mock):
        for status,flag in ((401,"auth_error"),(403,"auth_error"),(429,"rate_limited"),(451,"geo_blocked")):
            mock.side_effect=HTTPError("https://example.com/live",status,"Error",{},None)
            result=probe_stream("https://example.com/live",DAY)
            self.assertTrue(getattr(result,flag))
            self.assertFalse(is_definitive_failure(result))

    @patch("automation.engines.international.stream_probe.urlopen")
    def test_network_failure_is_inconclusive(self,mock):
        mock.side_effect=URLError("connection failed")
        result=probe_stream("https://example.com/live",DAY)
        self.assertTrue(result.network_error)
        self.assertFalse(is_definitive_failure(result))

    def test_private_and_credential_urls_rejected(self):
        for url in ("http://127.0.0.1/live","http://192.168.1.2/live","https://user:pass@example.com/live","http://localhost/live"):
            with self.assertRaises(ValueError):
                probe_stream(url,DAY)

    def test_invalid_timeout_rejected(self):
        with self.assertRaisesRegex(ValueError,"timeout"):
            probe_stream("https://example.com/live",DAY,0)

if __name__=="__main__":
    unittest.main()
