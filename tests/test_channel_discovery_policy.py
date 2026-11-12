import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from discover_bd_in_new_queues import (
    PERMANENTLY_BANNED_CHANNEL_NAMES, PERMANENTLY_BANNED_CHANNEL_IDS, canonical_channel_name,
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
            "Bangla Jago TV", "DD Bharati", "Food Food",
            "Discovery Turbo India", "XXTreme Jobs Hindi", "Power Turk",
            "Safari TV Tamil (Not 24/7)",
        ]
        self.assertEqual(len(PERMANENTLY_BANNED_CHANNEL_NAMES), 43)
        self.assertEqual(len(PERMANENTLY_BANNED_CHANNEL_IDS), 31)
        for name in names:
            with self.subTest(name=name):
                self.assertIn(canonical_channel_name(name), PERMANENTLY_BANNED_CHANNEL_NAMES)
                self.assertEqual(prohibited_channel({"tvg-name": name}, name), "permanently banned channel")

    def test_permanently_banned_ids_block_renamed_aliases_and_quality_suffixes(self):
        examples = [
            ("4SiDESTV.in@HD", "Renamed regional feed"),
            ("DDIndia.in@SD", "Renamed news feed"),
            ("GlobalPunjab.in", "Punjabi alternative stream"),
            ("JanTV.in@SD", "Education HD"),
            ("KaumudyTV.in@HD", "Alternate Kaumudy"),
            ("JeevanTV.in@SD", "Generic Malayalam TV"),
            ("MeiAlaiTV.in", "Tamil entertainment"),
            ("MadhimugamTV.in", "Regional feed"),
            ("BanglaJagoTV.in@HD", "Bangla Jago alternate"),
            ("DDBharati.in@HD", "DD Bharati alternate"),
            ("FoodFood.in@HD", "Food Food alternate"),
            ("DiscoveryTurbo.in@HD", "Discovery Turbo alternate"),
            ("XXTremeJobsHindi.in@SD", "XXTreme Jobs alternate"),
            ("PowerTurkTV.tr@HD", "Power Turk alternate"),
        ]
        for channel_id, alias in examples:
            with self.subTest(channel_id=channel_id):
                self.assertEqual(
                    prohibited_channel(
                        {"tvg-id": channel_id, "channel-id": channel_id,
                         "tvg-country": "IN", "group-title": "New Channels"},
                        alias,
                    ),
                    "permanently banned channel",
                )

    def test_safari_tv_tamil_is_blocked_without_blocking_main_safari_tv(self):
        attrs = {"tvg-id": "SafariTV.in@SD", "tvg-name": "Safari TV Tamil (Not 24/7)"}
        self.assertEqual(
            prohibited_channel(attrs, "Safari TV Tamil (Not 24/7)"),
            "permanently banned channel",
        )
        self.assertIsNone(
            prohibited_channel({"tvg-id": "SafariTV.in@SD", "tvg-name": "Safari TV"}, "Safari TV")
        )

    def test_permanently_banned_channels_are_purged_from_existing_review_queues(self):
        text = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-id="TaazaTV.in@SD" tvg-name="Taaza TV" tvg-country="IN" group-title="New Channels",Taaza TV\n'
            "https://example.invalid/taaza.m3u8\n"
            '#EXTINF:-1 tvg-id="PulariTV.in@SD" tvg-name="Pulari TV" tvg-country="IN" group-title="New Channels",Pulari TV\n'
            "https://example.invalid/pulari.m3u8\n"
        )
        filtered, removed = purge_forbidden_existing_queue_rows(text)
        self.assertEqual(removed, ["Taaza TV"])
        self.assertNotIn("Taaza TV", filtered)
        self.assertIn("Pulari TV", filtered)

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

    def test_indian_kids_are_allowed_for_active_and_discovery_policy(self):
        for name, group in [
            ("Kids TV", "Kids"),
            ("Cartoon Network", "Entertainment"),
            ("Green Gold TV", "Entertainment"),
            ("Pogo", "Entertainment"),
            ("Disney Channel", "Kids"),
        ]:
            with self.subTest(name=name, group=group):
                attrs = {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"}
                self.assertIsNone(prohibited_channel(attrs, name))
                self.assertIsNone(prohibited_channel(attrs, name, discovery=True))

    def test_indian_sports_are_allowed_but_knowledge_and_business_remain_discovery_only_exclusions(self):
        for name, group in [("Star Sports", "Sports"), ("DD Sports", "Entertainment")]:
            with self.subTest(name=name, group=group):
                attrs = {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"}
                self.assertIsNone(prohibited_channel(attrs, name))
                self.assertIsNone(prohibited_channel(attrs, name, discovery=True))

        examples = [
            ("Discovery Channel", "Knowledge"),
            ("National Geographic", "Documentary"),
            ("Animal Planet", "Entertainment"),
            ("Corporate Channel", "Business"),
            ("Money TV", "Finance"),
        ]
        for name, group in examples:
            attrs = {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"}
            with self.subTest(name=name, group=group):
                self.assertIsNone(prohibited_channel(attrs, name))
                self.assertIsNotNone(prohibited_channel(attrs, name, discovery=True))

    def test_bangladesh_discovery_channels_remain_unrestricted_by_genre(self):
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
                    discovery=True,
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

    def test_cricket_and_football_are_eligible_from_india_feed_even_with_country_metadata_mismatch(self):
        for name, genre in [
            ("Cricket 24", "Cricket"),
            ("Test Cricket HD", "Cricket"),
            ("Football Live", "Football"),
        ]:
            with self.subTest(name=name):
                source_metadata = {
                    "tvg-id": "Candidate.us",
                    "channel-id": "Candidate.us",
                    "tvg-country": "US",
                    "group-title": genre,
                }
                candidate, reason = evaluate(
                    "India", source_metadata, name, "https://example.org/live/index.m3u8"
                )
                self.assertEqual(reason, "")
                self.assertEqual(candidate, source_metadata)

    def test_indian_cricket_and_football_sports_channels_are_discovery_eligible(self):
        for name in ("Cricket 24", "Test Cricket HD", "Football Live", "Football Sports"):
            with self.subTest(name=name):
                attrs = {
                    "tvg-id": "ExampleChannel.in",
                    "channel-id": "ExampleChannel.in",
                    "tvg-country": "IN",
                    "group-title": "Sports",
                }
                candidate, reason = evaluate(
                    "India", attrs, name, "https://example.org/sports/live/index.m3u8"
                )
                self.assertEqual(reason, "")
                self.assertEqual(candidate, attrs)

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

    def test_foreign_country_metadata_does_not_purge_manual_review_candidates(self):
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
        self.assertEqual(removed, ["Gopal Bhar"])
        self.assertIn('group-title="New Channels",ARY Music', filtered)
        self.assertIn('group-title="New Channels",Madani Channel', filtered)
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



    def test_expiry_timestamps_are_not_mistaken_for_auth_tokens(self):
        attrs = {"tvg-id": "SampleChannel.in", "group-title": "Indian Entertainment"}
        for parameter in ("expires=1790000000", "e=1790000000"):
            with self.subTest(parameter=parameter):
                entry, reason = evaluate(
                    "India", attrs, "Sample Channel",
                    f"https://example.org/channel.m3u8?{parameter}",
                )
                self.assertIsNotNone(entry, reason)

        # Expiry metadata is safe to preserve; credential-bearing URLs still
        # require a separate owner-approved/manual path.
        entry, reason = evaluate(
            "India", attrs, "Sample Channel",
            "https://example.org/channel.m3u8?token=secret",
        )
        self.assertIsNone(entry)
        self.assertEqual(reason, "tokenized URL")


if __name__ == "__main__":
    unittest.main()
