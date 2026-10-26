#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import discover_international_channels as discovery


class InternationalDiscoveryPolicyTests(unittest.TestCase):
    def classify(self, name, group, country=None, tvg_id=None, language=None):
        attrs = {"group-title": group}
        if country:
            attrs["tvg-country"] = country
        if tvg_id:
            attrs["tvg-id"] = tvg_id
        if language:
            attrs["tvg-language"] = language
        return discovery.policy(attrs, name)

    def test_movies_and_music_are_allowed_for_international_countries(self):
        self.assertEqual(self.classify("Cinema World", "Movies", "NP", "CinemaWorld.np"),
                         ("International Movies", None, "NP"))
        self.assertEqual(self.classify("World Music", "Music", "TH", "WorldMusic.th"),
                         ("International Music", None, "TH"))

    def test_movie_music_content_keeps_existing_region_grouping(self):
        self.assertEqual(self.classify("Star Movies", "Movies", "IN", "StarMovies.in")[0], "Indian Movies")
        self.assertEqual(self.classify("V2BEAT", "Music", "IN", "V2BEAT.in")[0], "Indian Music")
        self.assertEqual(self.classify("Cinema Bangla", "Movies", "BD", "CinemaBangla.bd")[0], "Bangladesh")
        self.assertEqual(self.classify("World Music", "Music", "PK", "WorldMusic.pk")[0], "Pakistani")

    def test_general_entertainment_or_other_source_categories_are_rejected_even_with_movie_music_names(self):
        for group in ("General", "Entertainment", "Variety", "Series", "Lifestyle", "Education", "International"):
            with self.subTest(group=group):
                self.assertIsNone(self.classify("Cinema World", group, "US", "CinemaWorld.us")[0])
                self.assertIsNone(self.classify("World Music", group, "US", "WorldMusic.us")[0])

    def test_news_is_rejected_for_every_country(self):
        for country in ("BD", "IN", "PK", "US", None):
            with self.subTest(country=country):
                self.assertIsNone(self.classify("World News", "News", country, "WorldNews.us")[0])
        self.assertIsNone(self.classify("Channel 24", "General", "BD", "Channel24.bd")[0])
        self.assertIsNone(self.classify("Somoy TV", "Entertainment", "BD", "SomoyTV.bd")[0])
        self.assertIsNone(self.classify("CNBC World", "Business", "SG", "CNBCWorld.sg")[0])

    def test_kids_sports_documentary_and_wildlife_channels_are_rejected(self):
        examples = [
            ("Cartoon World", "Kids"),
            ("Disney Junior", "Entertainment"),
            ("World Sport", "Sports"),
            ("Nature World", "Documentary"),
            ("Discovery Channel", "General"),
            ("National Geographic", "General"),
        ]
        for name, group in examples:
            with self.subTest(name=name):
                self.assertIsNone(self.classify(name, group, "US", name.replace(" ", "") + ".us")[0])

    def test_all_religious_channels_including_islamic_are_rejected(self):
        examples = [
            ("Gospel TV", "Religious", "US", "GospelTV.us"),
            ("Sunnah TV", "Religious", "SA", "SunnahTV.sa"),
            ("MTA International", "General", "GB", "MTAInternational.uk"),
            ("3ABN Kids", "Kids", "US", "3ABNKids.us@SD"),
            ("Hindu Bhakti Music", "Music", "IN", "BhaktiMusic.in"),
            ("Madani TV", "General", "BD", "MadaniTV.bd"),
        ]
        for name, group, country, tvg_id in examples:
            with self.subTest(name=name):
                self.assertIsNone(self.classify(name, group, country, tvg_id)[0])

    def test_unknown_and_generic_channels_are_rejected(self):
        for country in ("BD", "IN", "PK", "US", None):
            with self.subTest(country=country):
                self.assertIsNone(self.classify("Entertainment World", "General", country, "EntertainmentWorld")[0])
                self.assertIsNone(self.classify("World Channel", "", country, "WorldChannel")[0])

    def test_five_channel_country_threshold_is_retained(self):
        self.assertEqual(discovery.COUNTRY_THRESHOLD, 5)
        self.assertNotIn("AT", discovery.qualified_country_groups({"AT": {"a", "b", "c", "d"}}))
        self.assertIn("AT", discovery.qualified_country_groups({"AT": {"a", "b", "c", "d", "e"}}))
        # Routing changed in 2f5ee4f: a country that has reached the threshold
        # gets its dedicated group; below it, channels wait in New Channels.
        # BD, IN and PK always keep their established regional groups.
        self.assertEqual(discovery.primary_target("International Movies", "AT", {"AT"}), "Austria")
        self.assertEqual(discovery.primary_target("International Music", "AT", {"AT"}), "Austria")
        self.assertEqual(discovery.primary_target("International Movies", "AT", set()), "New Channels")
        self.assertEqual(discovery.primary_target("International Music", "DE", set()), "New Channels")
        self.assertEqual(discovery.primary_target("International Movies", "BD", set()), "Bangladesh")
        self.assertEqual(discovery.primary_target("International Music", "PK", set()), "Pakistani")
        self.assertEqual(discovery.primary_target("International Movies", "IN", set()), "Indian Movies")
        self.assertEqual(discovery.primary_target("International Music", "IN", set()), "Indian Music")

    def test_tokenized_urls_are_rejected_without_playback_testing(self):
        self.assertFalse(discovery.safe_url("https://example.org/live.m3u8?token=abc"))
        self.assertTrue(discovery.safe_url("https://example.org/channel/index.m3u8"))


if __name__ == "__main__":
    unittest.main()
