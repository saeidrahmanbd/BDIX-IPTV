#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import discover_international_channels as discovery


class InternationalDiscoveryPolicyTests(unittest.TestCase):
    def classify(self, name, group, country=None, tvg_id=None, language=None):
        a = {"group-title": group}
        if country:
            a["tvg-country"] = country
        if tvg_id:
            a["tvg-id"] = tvg_id
        if language:
            a["tvg-language"] = language
        return discovery.policy_group(a, name)

    def test_movies_are_allowed_for_any_country(self):
        group, reason, country = self.classify("Cinema World", "Movies", "US", "CinemaWorld.us")
        self.assertEqual((group, reason, country), ("International Movies", None, "US"))

    def test_music_is_allowed_for_any_country(self):
        group, reason, country = self.classify("World Music", "Music", "BR", "WorldMusic.br")
        self.assertEqual((group, reason, country), ("International Music", None, "BR"))

    def test_bangladesh_news_is_allowed(self):
        group, reason, country = self.classify("Channel 24", "News", "BD", "Channel24.bd")
        self.assertEqual((group, reason, country), ("Bangladesh", None, "BD"))

    def test_foreign_news_is_rejected(self):
        group, reason, country = self.classify("World News", "News", "US", "WorldNews.us")
        self.assertIsNone(group)
        self.assertEqual(reason, "non-Bangladeshi or unverified-country news channel")

    def test_news_with_unknown_country_is_rejected(self):
        group, reason, country = self.classify("Global News", "General", None, "GlobalNews.custom")
        self.assertIsNone(group)
        self.assertEqual(reason, "non-Bangladeshi or unverified-country news channel")

    def test_foreign_news_brands_are_rejected_even_if_mislabelled(self):
        group, reason, country = self.classify("CNBC World", "Business", "SG", "CNBCWorld.sg")
        self.assertIsNone(group)
        self.assertEqual(reason, "non-Bangladeshi or unverified-country news channel")

    def test_islamic_religious_channel_is_allowed(self):
        group, reason, country = self.classify("Sunnah TV", "Religious", "SA", "SunnahTV.sa")
        self.assertEqual((group, reason, country), ("Religious", None, "SA"))

    def test_non_islamic_religious_channel_is_rejected(self):
        group, reason, country = self.classify("Gospel TV", "Religious", "US", "GospelTV.us")
        self.assertIsNone(group)
        self.assertEqual(reason, "non-Islamic religious channel")

    def test_religious_content_is_rejected_even_if_tagged_music(self):
        group, reason, country = self.classify("Hindu Bhakti Music", "Music", "IN", "BhaktiMusic.in")
        self.assertIsNone(group)
        self.assertEqual(reason, "non-Islamic religious channel")

    def test_country_is_inferred_from_id_suffix(self):
        group, reason, country = self.classify("World News", "News", None, "WorldNews.uk@HD")
        self.assertIsNone(group)
        self.assertEqual(country, "GB")

    def test_sports_and_documentaries_are_allowed(self):
        sports, sports_reason, _ = self.classify("World Sport", "Sports", "US", "WorldSport.us")
        doc, doc_reason, _ = self.classify("Nature World", "Documentary", "ZA", "NatureWorld.za")
        self.assertEqual((sports, sports_reason), ("Sports", None))
        self.assertEqual((doc, doc_reason), ("Documentary & Wildlife", None))

    def test_tokenized_urls_are_held_without_playback_checks(self):
        okay, reason = discovery.safe_stream_url("https://example.org/live.m3u8?token=abc")
        self.assertFalse(okay)
        self.assertEqual(reason, "tokenized or credentialed URL")

    def test_plain_stream_urls_are_accepted_by_syntax_only(self):
        okay, reason = discovery.safe_stream_url("https://example.org/channel/index.m3u8")
        self.assertTrue(okay)
        self.assertIsNone(reason)


if __name__ == "__main__":
    unittest.main()
