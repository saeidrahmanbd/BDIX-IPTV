import sys
import unittest
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from stream_risk_review import expiry_status, token_expiry


class SignedUrlExpiryTests(unittest.TestCase):
    def test_extracts_expiry_from_hdnts_signature(self):
        url = "https://cdn.example/live.m3u8?hdnts=st=1735898689~exp=1835898688~acl=*~hmac=secret"
        self.assertEqual(token_expiry(url), 1835898688)

    def test_extracts_ayna_expiry_parameter(self):
        self.assertEqual(token_expiry("https://tv.example/live.m3u8?e=1784102598&u=opaque&token=secret"), 1784102598)

    def test_ignores_opaque_tokens_without_expiry(self):
        self.assertIsNone(token_expiry("https://tv.example/live.m3u8?token=opaque&auth=private"))

    def test_classifies_expired_and_future_tokens(self):
        now = datetime(2026, 11, 11, tzinfo=timezone.utc)
        expired, expired_at = expiry_status(1784102598, now)
        future, future_at = expiry_status(1835898688, now)
        self.assertEqual(expired, "EXPIRED")
        self.assertTrue(expired_at.startswith("2026-"))
        self.assertEqual(future, "FUTURE")
        self.assertTrue(future_at.startswith("2028-"))


if __name__ == "__main__":
    unittest.main()
