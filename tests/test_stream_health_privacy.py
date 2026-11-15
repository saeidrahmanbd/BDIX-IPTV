import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from stream_health import canonical_url, migrate_history_keys, url_fingerprint


class StreamHealthPrivacyTests(unittest.TestCase):
    def test_history_key_is_one_way_and_does_not_embed_stream_credentials(self):
        url = "https://provider.example/live/private-user/private-password/channel.m3u8?token=secret"
        key = url_fingerprint(url)
        self.assertEqual(len(key), 64)
        self.assertNotIn("private-user", key)
        self.assertNotIn("private-password", key)
        self.assertNotIn("secret", key)

    def test_legacy_raw_url_history_is_migrated_without_losing_failure_streak(self):
        url = "https://provider.example/live/user/pass/channel.m3u8?token=secret"
        history = {url: {"checks": 4, "successes": 1, "failures": 3, "consecutive_failures": 2}}
        migrated = migrate_history_keys(history)
        self.assertEqual(list(migrated), [url_fingerprint(url)])
        self.assertEqual(migrated[url_fingerprint(url)]["consecutive_failures"], 2)
        self.assertNotIn(url, str(migrated))

    def test_near_duplicate_family_key_omits_userinfo_and_query(self):
        first = canonical_url("https://alice:secret@provider.example/live/u/p/ch.m3u8?token=one")
        second = canonical_url("https://bob:other@provider.example/live/x/y/ch.m3u8?token=two")
        self.assertEqual(first, second)
        self.assertNotIn("alice", first)
        self.assertNotIn("secret", first)
        self.assertNotIn("token", first)


if __name__ == "__main__":
    unittest.main()
