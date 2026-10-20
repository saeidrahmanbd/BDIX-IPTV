import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from report_iptv_fragile_streams import redact_url


class RedactUrlTests(unittest.TestCase):
    def test_sensitive_query_values_are_redacted_but_parameter_names_remain(self):
        safe = redact_url("https://media.example/live.m3u8?hdnts=secret-signature&token=secret-token&quality=hd")
        self.assertNotIn("secret-signature", safe)
        self.assertNotIn("secret-token", safe)
        self.assertIn("hdnts=REDACTED", safe)
        self.assertIn("quality=hd", safe)

    def test_userinfo_and_xtream_path_credentials_are_redacted(self):
        safe = redact_url("https://alice:password123@provider.example/live/myuser/mypass/12345.ts?token=private")
        for secret in ("alice", "password123", "myuser", "mypass", "private"):
            self.assertNotIn(secret, safe)
        self.assertIn("REDACTED", safe)
        self.assertIn("12345.ts", safe)

    def test_url_fragment_is_not_preserved(self):
        self.assertNotIn("fragment-secret", redact_url("https://example.invalid/a.m3u8#fragment-secret"))


if __name__ == "__main__":
    unittest.main()
