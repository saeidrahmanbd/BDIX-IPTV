import json
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from stream_health import canonical_url, load_history, migrate_history_keys, update_failure_history, url_fingerprint


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
        self.assertEqual(migrated[url_fingerprint(url)]["legacy_run_failure_count"], 2)
        self.assertEqual(migrated[url_fingerprint(url)]["consecutive_failure_days"], 0)
        self.assertNotIn(url, str(migrated))
        self.assertEqual(migrate_history_keys(migrated), migrated)

    def test_committed_history_contains_only_fingerprints(self):
        history_path = Path(__file__).resolve().parents[1] / "reports" / "stream-health-history.json"
        history = json.loads(history_path.read_text(encoding="utf-8"))
        self.assertGreater(len(history), 0, "stream-health history must never be silently purged")
        self.assertTrue(all(re.fullmatch(r"[0-9a-f]{64}", key) for key in history))

    def test_near_duplicate_family_key_omits_userinfo_and_query(self):
        first = canonical_url("https://alice:secret@provider.example/live/u/p/ch.m3u8?token=one")
        second = canonical_url("https://bob:other@provider.example/live/x/y/ch.m3u8?token=two")
        self.assertEqual(first, second)
        self.assertNotIn("alice", first)
        self.assertNotIn("secret", first)
        self.assertNotIn("token", first)

    def test_legacy_run_history_is_normalized_without_inventing_daily_streaks(self):
        legacy = {
            "a" * 64: {
                "checks": 20, "successes": 12, "failures": 8,
                "consecutive_failures": 7, "last_status": 500,
                "last_ok": "2026-11-14T15:00:00+00:00",
                "last_failure": "2026-11-15T02:25:32+00:00",
            },
            "b" * 64: {
                "checks": 5, "successes": 2, "failures": 3,
                "consecutive_failures": 3, "last_status": 404,
                "last_ok": "2026-11-12T10:00:00+00:00",
                "last_failure": "2026-11-15T02:25:32+00:00",
            },
        }
        migrated = migrate_history_keys(legacy)
        transient = migrated["a" * 64]
        definitive = migrated["b" * 64]
        self.assertEqual(transient["checks"], 20)
        self.assertEqual(transient["successes"], 12)
        self.assertEqual(transient["failures"], 8)
        self.assertEqual(transient["last_status"], "inconclusive")
        self.assertEqual(transient["consecutive_failure_days"], 0)
        self.assertEqual(transient["last_checked_date"], "2026-11-15")
        self.assertEqual(definitive["last_status"], "definitive_failure")
        self.assertEqual(definitive["consecutive_failure_days"], 1)
        self.assertEqual(definitive["consecutive_failures"], 1)

    def test_load_history_fails_loudly_for_missing_corrupt_or_empty_history(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "history.json"
            with self.assertRaises(RuntimeError):
                load_history(path)
            path.write_text("{broken", encoding="utf-8")
            with self.assertRaises(RuntimeError):
                load_history(path)
            path.write_text("{}", encoding="utf-8")
            with self.assertRaises(RuntimeError):
                load_history(path)


    def test_only_404_and_410_advance_one_failure_per_bangladesh_day(self):
        history = {}
        history, streak, state = update_failure_history(history, {"ok": False, "status": 404}, "2026-11-15")
        self.assertEqual((streak, state), (1, "definitive_failure"))
        history, streak, state = update_failure_history(history, {"ok": False, "status": 404}, "2026-11-15")
        self.assertEqual((streak, state), (1, "already-checked-today"))
        history, streak, state = update_failure_history(history, {"ok": False, "status": 410}, "2026-11-16")
        self.assertEqual((streak, state), (2, "definitive_failure"))
        history, streak, state = update_failure_history(history, {"ok": False, "status": 503}, "2026-11-17")
        self.assertEqual((streak, state), (0, "inconclusive"))
        history, streak, state = update_failure_history(history, {"ok": False, "status": 404}, "2026-11-18")
        self.assertEqual((streak, state), (1, "definitive_failure"))

    def test_success_or_missed_day_resets_definitive_failure_streak(self):
        history = {}
        history, _, _ = update_failure_history(history, {"ok": False, "status": 404}, "2026-11-15")
        history, streak, _ = update_failure_history(history, {"ok": False, "status": 404}, "2026-11-17")
        self.assertEqual(streak, 1)
        history, streak, _ = update_failure_history(history, {"ok": True, "status": 206}, "2026-11-18")
        self.assertEqual(streak, 0)

if __name__ == "__main__":
    unittest.main()
