import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from discover_bd_in_new_queues import (
    PERMANENTLY_BANNED_CHANNEL_NAMES, canonical_channel_name,
    prohibited_channel, purge_forbidden_existing_queue_rows,
)


class ChannelDiscoveryPolicyTests(unittest.TestCase):
    def test_permanently_banned_names_are_blocked_with_quality_and_country_suffixes(self):
        names = [
            "E-Vidya 10 (576p) (India)", "E-Vidya 11 (576p) (India)",
            "E-Vidya 12 (576p) (India)", "E-Vidya 4 (576p) (India)",
            "E-Vidya 5 (576p) (India)", "E-Vidya 6 (576p) (India)",
            "E-Vidya 7 (576p) (India)", "E-Vidya 8 (576p) (India)",
            "E-Vidya 9 (576p) (India)", "Friends TV (1080p) (India)",
        ]
        self.assertEqual(len(PERMANENTLY_BANNED_CHANNEL_NAMES), 10)
        for name in names:
            with self.subTest(name=name):
                self.assertIn(canonical_channel_name(name), PERMANENTLY_BANNED_CHANNEL_NAMES)
                self.assertEqual(prohibited_channel({"tvg-name": name}, name), "permanently banned channel")

    def test_disallowed_categories_and_known_brands_are_rejected(self):
        examples = [
            ("Sample News Channel", "News"), ("Sample Sports Channel", "Sports"),
            ("Sample Kids Channel", "Kids"), ("Sample Religious Channel", "Religious"),
            ("Kids TV", "Entertainment"), ("Sansad TV 2", "New Channels"),
            ("Green Gold TV", "New Channels"), ("Sai TV", "New Channels"),
            ("Zee Business", "New Channels"),
        ]
        for name, group in examples:
            with self.subTest(name=name, group=group):
                self.assertIsNotNone(prohibited_channel({"group-title": group}, name))

    def test_ordinary_general_entertainment_is_not_blocked(self):
        self.assertIsNone(prohibited_channel({"group-title": "Entertainment"}, "Mahua Play"))

    def test_existing_prohibited_queue_rows_are_purged_but_other_rows_are_preserved(self):
        text = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-name="E-Vidya 4 (576p) (India)" tvg-country="IN" group-title="New Channels",E-Vidya 4 (576p) (India)\n'
            "https://example.invalid/evidya.m3u8\n"
            '#EXTINF:-1 tvg-name="Sansad TV 2" tvg-country="IN" group-title="New Backup",Sansad TV 2\n'
            "https://example.invalid/sansad.m3u8\n"
            '#EXTINF:-1 tvg-name="Mahua Play" tvg-country="IN" group-title="New Channels",Mahua Play\n'
            "https://example.invalid/mahua.m3u8\n"
            '#EXTINF:-1 tvg-name="E-Vidya 4" tvg-country="IN" group-title="Indian Entertainment",E-Vidya 4\n'
            "https://example.invalid/active-evidya.m3u8\n"
        )
        filtered, removed = purge_forbidden_existing_queue_rows(text)
        self.assertEqual(len(removed), 2)
        self.assertNotIn('group-title="New Channels",E-Vidya 4', filtered)
        self.assertNotIn('group-title="New Backup",Sansad TV 2', filtered)
        self.assertIn('group-title="New Channels",Mahua Play', filtered)
        self.assertIn('group-title="Indian Entertainment",E-Vidya 4', filtered)


if __name__ == "__main__":
    unittest.main()
