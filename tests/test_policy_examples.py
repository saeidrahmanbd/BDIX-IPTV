"""Owner-approved channel policy examples, asserted against the shared discovery policy.

Bangladesh is unrestricted by genre. India allows Kids, Sports, Movies, Music,
Entertainment and Indian Bangla, and prohibits News, Religious (including Islamic),
Educational/knowledge, Business/Finance and Farming. Every other foreign country is
Movies/Music only, and Pakistan does not inherit the Indian Kids/Sports exception.
"""
import unittest
from pathlib import Path
import sys

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import discover_bd_in_new_queues as bd  # noqa: E402
import discover_international_channels as intl  # noqa: E402


def attrs(country, group="", language="eng"):
    return {"tvg-country": country, "group-title": group, "tvg-language": language}


class IndianAllowedExamples(unittest.TestCase):
    def test_kids_and_sports_are_allowed_in_main_pipeline(self):
        self.assertIsNone(bd.prohibited_channel(attrs("IN"), "Cartoon Network", "IN"))
        self.assertIsNone(bd.prohibited_channel(attrs("IN"), "Sony Sports", "IN"))

    def test_entertainment_and_movie_channels_are_allowed(self):
        self.assertIsNone(bd.prohibited_channel(attrs("IN"), "Colors Cineplex", "IN"))
        self.assertIsNone(bd.prohibited_channel(attrs("IN"), "Star Bharat", "IN"))

    def test_indian_bangla_is_allowed(self):
        self.assertIsNone(bd.prohibited_channel(attrs("IN", language="ben"), "Jalsha Movies", "IN"))

    def test_cartoon_network_and_colors_cineplex_resolve_to_permitted_targets(self):
        self.assertEqual(intl.policy(attrs("IN"), "Cartoon Network")[0], "Kids")
        self.assertEqual(intl.policy(attrs("IN"), "Colors Cineplex")[0], "Indian Movies")


class IndianProhibitedExamples(unittest.TestCase):
    def assertProhibited(self, name, country="IN"):
        reason = bd.prohibited_channel(attrs(country), name, country)
        self.assertIsNotNone(reason, name)

    def test_news_is_prohibited(self):
        self.assertProhibited("Kolkata News")
        self.assertProhibited("Aaj Tak")

    def test_religious_including_islamic_is_prohibited(self):
        self.assertProhibited("PTC Punjabi Gospel")
        self.assertProhibited("Madani TV")
        self.assertProhibited("Peace TV")

    def test_business_finance_is_prohibited(self):
        self.assertProhibited("Zee Business")

    def test_farming_is_prohibited(self):
        self.assertProhibited("Krishi Darshan")
        self.assertProhibited("Kisan Channel")

    def test_educational_is_prohibited(self):
        self.assertProhibited("Gyan Darshan")


class BangladeshAndForeignExamples(unittest.TestCase):
    def test_bangladesh_is_unrestricted_by_genre(self):
        self.assertIsNone(bd.prohibited_channel(attrs("BD", language="ben"), "Bangla News 24", "BD"))
        self.assertEqual(intl.policy(attrs("BD", language="ben"), "Bangla News 24")[0], "Bangladesh")

    def test_pakistan_does_not_inherit_indian_kids_sports_exception(self):
        target, reason, _ = intl.policy(attrs("PK", language="urd"), "PTV Sports")
        self.assertIsNone(target)
        self.assertIn("sports", reason)

    def test_foreign_kids_channels_remain_prohibited(self):
        target, reason, _ = intl.policy(attrs("US", language="eng"), "Cartoon Network")
        self.assertIsNone(target)
        self.assertIn("kids", reason)

    def test_bangladesh_and_india_are_not_blanket_excluded_from_international_discovery(self):
        self.assertEqual(intl.policy(attrs("BD", language="ben"), "NTV Europe")[0], "Bangladesh")
        self.assertIsNotNone(intl.policy(attrs("IN"), "Aaj Tak")[1])
        self.assertIn(intl.policy(attrs("IN"), "Sony Sports")[0], {"Sports", "Indian Entertainment"})


class VipTvIdentityException(unittest.TestCase):
    def test_vip_tv_aruba_music_is_exempt_only_by_exact_identity(self):
        exact = {"tvg-id": "custom.vip-tv-aw-music", "tvg-country": "AW", "tvg-content": "Music", "group-title": "Aruba"}
        self.assertTrue(intl.identity_music_exception(exact, "AW"))
        other = dict(exact, **{"tvg-id": "custom.vip-tv-other"})
        self.assertFalse(intl.identity_music_exception(other, "AW"))
        wrong_country = dict(exact)
        self.assertFalse(intl.identity_music_exception(wrong_country, "CW"))
        not_music = dict(exact, **{"tvg-content": "Movies"})
        self.assertFalse(intl.identity_music_exception(not_music, "AW"))


if __name__ == "__main__":
    unittest.main()
