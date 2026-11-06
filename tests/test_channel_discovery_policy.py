import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from discover_bd_in_new_queues import (
    PERMANENTLY_BANNED_CHANNEL_NAMES, canonical_channel_name,
    evaluate, prohibited_channel, purge_forbidden_existing_queue_rows,
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

    def test_indian_news_and_all_religious_channels_are_rejected(self):
        examples = [
            ("Sample News Channel", "News"),
            ("Sample Religious Channel", "Religious"),
            ("Madani TV", "Religious"),
            ("Madani TV", "General"),
            ("Iqra TV", "General"),
            ("MTA International", "General"),
            ("Madani TV", "General"),
            ("Iqra TV", "General"),
            ("MTA International", "General"),
            ("Peace TV", "Religious"),
            ("Quran TV", "Religious"),
            ("Network 10", "New Channels"),
            ("Saam TV", "New Backups"),
            ("Total TV Haryana", "New Backups"),
            ("Calvary TV", "New Channels"),
            ("Santvani Channel", "New Channels"),
            ("Sharnam TV", "New Channels"),
            ("Sai TV", "New Channels"),
            ("Zee Business", "New Channels"),
        ]
        for name, group in examples:
            with self.subTest(name=name, group=group):
                attrs = {"group-title": group, "tvg-country": "IN"}
                self.assertIsNotNone(prohibited_channel(attrs, name))

    def test_indian_kids_and_sports_channels_are_rejected(self):
        for name, group in [
            ("Kids TV", "Kids"),
            ("Cartoon Network", "Entertainment"),
            ("Green Gold TV", "Entertainment"),
            ("Pogo", "Entertainment"),
            ("Disney Channel", "Kids"),
            ("Star Sports", "Sports"),
            ("DD Sports", "Entertainment"),
        ]:
            with self.subTest(name=name, group=group):
                self.assertIsNotNone(prohibited_channel(
                    {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"}, name
                ))

    def test_indian_knowledge_and_business_channels_are_rejected(self):
        examples = [
            ("Discovery Channel", "Knowledge"),
            ("National Geographic", "Documentary"),
            ("Animal Planet", "Entertainment"),
            ("CNBC TV18", "Business"),
            ("Bloomberg", "Finance"),
            ("Zee Business", "Entertainment"),
        ]
        for name, group in examples:
            with self.subTest(name=name, group=group):
                self.assertIsNotNone(prohibited_channel(
                    {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"},
                    name,
                ))

    def test_bangladesh_sports_knowledge_and_business_channels_remain_allowed(self):
        examples = [
            ("T Sports", "Sports"),
            ("Discovery Bangladesh", "Knowledge"),
            ("Business Bangladesh", "Business"),
        ]
        for name, group in examples:
            with self.subTest(name=name, group=group):
                self.assertIsNone(prohibited_channel(
                    {"group-title": group, "tvg-country": "BD", "tvg-id": "SampleChannel.bd"},
                    name,
                ))

    def test_indian_educational_channels_are_rejected(self):
        for name, group in [("Education TV", "Education"), ("DD Gyan Darshan", "General")]:
            with self.subTest(name=name, group=group):
                self.assertIsNotNone(prohibited_channel(
                    {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"}, name
                ))


    def test_indian_islamic_religious_channels_are_rejected(self):
        examples = [
            ("Madani TV", "Religious"),
            ("Peace TV", "Religious"),
            ("Quran TV", "Religious"),
            ("Islam Channel", "Religious"),
            ("Al Huda", "Religious"),
        ]
        for name, group in examples:
            with self.subTest(name=name, group=group):
                self.assertIsNotNone(prohibited_channel(
                    {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"},
                    name,
                ))

    def test_bangladeshi_news_is_allowed(self):
        attrs = {"group-title": "News", "tvg-country": "BD", "tvg-id": "Channel24.bd"}
        self.assertIsNone(prohibited_channel(attrs, "Channel 24"))
        self.assertIsNone(prohibited_channel(
            {"group-title": "New Channels", "tvg-country": "BD", "tvg-id": "SomoyTV.bd"},
            "Somoy TV"
        ))

    def test_bangladeshi_sports_kids_and_religious_channels_are_not_blocked_by_india_only_rule(self):
        examples = [
            ("Sports Bangla", "Sports"),
            ("Kids Bangla", "Kids"),
            ("Religious Bangla", "Religious"),
        ]
        for name, group in examples:
            with self.subTest(name=name, group=group):
                self.assertIsNone(prohibited_channel(
                    {"group-title": group, "tvg-country": "BD"}, name
                ))

    def test_indian_category_is_inferred_from_id_when_country_attribute_is_missing(self):
        self.assertIsNotNone(prohibited_channel(
            {"group-title": "News", "tvg-id": "SampleNews.in"},
            "Sample News"
        ))
        self.assertIsNone(prohibited_channel(
            {"group-title": "News", "tvg-id": "Channel24.bd"},
            "Channel 24"
        ))

    def test_ordinary_general_entertainment_is_not_blocked(self):
        self.assertIsNone(prohibited_channel(
            {"group-title": "Entertainment", "tvg-country": "IN"}, "Mahua Play"
        ))

    def test_existing_prohibited_indian_queue_rows_are_purged_but_bd_news_and_canonical_rows_are_preserved(self):
        text = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-name="E-Vidya 4 (576p) (India)" tvg-country="IN" group-title="New Channels",E-Vidya 4 (576p) (India)\n'
            "https://example.invalid/evidya.m3u8\n"
            '#EXTINF:-1 tvg-name="Sansad TV 2" tvg-id="SansadTV2.in" tvg-country="IN" group-title="New Backups",Sansad TV 2\n'
            "https://example.invalid/sansad.m3u8\n"
            '#EXTINF:-1 tvg-name="Channel 24" tvg-id="Channel24.bd" tvg-country="BD" group-title="New Channels",Channel 24\n'
            "https://example.invalid/channel24.m3u8\n"
            '#EXTINF:-1 tvg-name="Mahua Play" tvg-country="IN" group-title="New Channels",Mahua Play\n'
            "https://example.invalid/mahua.m3u8\n"
            '#EXTINF:-1 tvg-name="E-Vidya 4" tvg-country="IN" group-title="Indian Entertainment",E-Vidya 4\n'
            "https://example.invalid/active-evidya.m3u8\n"
        )
        filtered, removed = purge_forbidden_existing_queue_rows(text)
        self.assertEqual(len(removed), 2)
        self.assertNotIn('group-title="New Channels",E-Vidya 4', filtered)
        self.assertNotIn('group-title="New Backups",Sansad TV 2', filtered)
        self.assertIn('group-title="New Channels",Channel 24', filtered)
        self.assertIn('group-title="New Channels",Mahua Play', filtered)
        self.assertIn('group-title="Indian Entertainment",E-Vidya 4', filtered)

    def test_foreign_country_and_program_title_rows_are_purged_from_discovery_queues(self):
        text = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-name="ARY Music" tvg-country="PK" tvg-id="ARYMusic.pk" group-title="New Channels",ARY Music\n'
            "https://example.invalid/ary-music.m3u8\n"
            '#EXTINF:-1 tvg-name="Madani Channel" tvg-country="PK" tvg-id="MadaniChannel.pk" group-title="New Channels",Madani Channel\n'
            "https://example.invalid/madani.m3u8\n"
            '#EXTINF:-1 tvg-name="Gopal Bhar" tvg-country="IN" group-title="New Channels",Gopal Bhar\n'
            "https://example.invalid/gopal-bhar.m3u8\n"
            '#EXTINF:-1 tvg-name="Channel 24" tvg-id="Channel24.bd" tvg-country="BD" group-title="New Channels",Channel 24\n'
            "https://example.invalid/channel24.m3u8\n"
        )
        filtered, removed = purge_forbidden_existing_queue_rows(text)
        self.assertEqual(set(removed), {"ARY Music", "Madani Channel", "Gopal Bhar"})
        self.assertNotIn('group-title="New Channels",ARY Music', filtered)
        self.assertNotIn('group-title="New Channels",Madani Channel', filtered)
        self.assertNotIn('group-title="New Channels",Gopal Bhar', filtered)
        self.assertIn('group-title="New Channels",Channel 24', filtered)

    def test_only_bd_in_source_feeds_are_allowed_and_bangladesh_news_passes(self):
        bd, bd_reason = evaluate(
            "Bangladesh",
            {"tvg-id": "Channel24.bd", "group-title": "News"},
            "Channel 24",
            "https://example.org/channel24.m3u8",
        )
        self.assertIsNotNone(bd, bd_reason)

        india, india_reason = evaluate(
            "India",
            {"tvg-id": "AajTak.in", "group-title": "News"},
            "Aaj Tak",
            "https://example.org/aajtak.m3u8",
        )
        self.assertIsNone(india)
        self.assertIn("Indian news", india_reason)

        foreign, foreign_reason = evaluate(
            "Nepal",
            {"tvg-id": "ExampleNews.np", "group-title": "News"},
            "Example News",
            "https://example.org/news.m3u8",
        )
        self.assertIsNone(foreign)
        self.assertEqual(foreign_reason, "unknown source feed")


if __name__ == "__main__":
    unittest.main()
