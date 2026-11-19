import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from discover_bd_in_new_queues import (
    PERMANENTLY_BANNED_CHANNEL_NAMES, PERMANENTLY_BANNED_CHANNEL_IDS, canonical_channel_name,
    evaluate, prohibited_channel, purge_forbidden_existing_queue_rows,
    is_indian_discovery_candidate, known_indian_forbidden_category,
)


class ChannelDiscoveryPolicyTests(unittest.TestCase):
    def test_indian_farming_and_agriculture_channels_are_allowed_when_live(self):
        for name in ("Indian Farming TV", "Krishi Darshan", "Agri World", "Agriculture Today", "Horticulture Channel"):
            with self.subTest(name=name):
                self.assertIsNone(prohibited_channel({"tvg-country": "IN", "group-title": "Entertainment"}, name, discovery=True))
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

    def test_indian_news_and_non_islamic_religious_channels_are_rejected(self):
        examples = [
            ("Sample News Channel", "News"),
            ("Sample Religious Channel", "Religious"),
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

    def test_darshana_tv_is_classified_as_indian_religious(self):
        attrs = {"tvg-country": "IN", "tvg-id": "DarshanaTV.in@SD", "group-title": "Indian Entertainment"}
        reason = prohibited_channel(attrs, "Darshana TV", iptv_discovery=True)
        self.assertIsNotNone(reason)
        self.assertIn("religious", reason)

    def test_mh_one_music_is_allowed_but_mh_one_prime_remains_blocked(self):
        music = {"tvg-country": "IN", "tvg-id": "Mh1Music.in@SD", "group-title": "Indian Music"}
        prime = {"tvg-country": "IN", "tvg-id": "MH1Prime.in@SD", "group-title": "Indian Entertainment"}
        self.assertIsNone(prohibited_channel(music, "MH One Music", iptv_discovery=True))
        self.assertIn("MH One Prime", prohibited_channel(prime, "MH One Prime", iptv_discovery=True))

    def test_explicit_non_indian_country_is_not_overridden_by_indian_alias(self):
        attrs = {"tvg-country": "US", "tvg-id": "Doraemon.us@SD", "group-title": "Review"}
        self.assertIsNone(prohibited_channel(attrs, "Doraemon", iptv_discovery=True))

    def test_indian_id_suffix_catches_conflict_with_stale_foreign_country(self):
        attrs = {"tvg-country": "US", "tvg-id": "DisneyChannel.in@HD", "group-title": "Backup"}
        self.assertIsNotNone(prohibited_channel(attrs, "Disney Channel", iptv_discovery=True))

    def test_indian_islamic_religious_channels_are_rejected_for_iptv_policy(self):
        attrs = {"group-title": "Religious", "tvg-country": "IN", "tvg-id": "SampleChannel.in"}
        self.assertIsNotNone(prohibited_channel(attrs, "Islamic TV", iptv_discovery=True))

    def test_indian_kids_are_rejected_for_active_and_discovery_policy(self):
        for name, group in [
            ("Kids TV", "Kids"), ("Cartoon Network", "Entertainment"),
            ("Green Gold TV", "Entertainment"), ("Pogo", "Entertainment"),
            ("Disney Channel", "Kids"),
        ]:
            with self.subTest(name=name, group=group):
                attrs = {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"}
                self.assertIsNotNone(prohibited_channel(attrs, name, iptv_discovery=True))

    def test_indian_sports_remain_allowed_but_knowledge_business_and_education_are_rejected(self):
        for name, group in [("Star Sports", "Sports"), ("DD Sports", "Sports")]:
            attrs = {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"}
            self.assertIsNone(prohibited_channel(attrs, name, iptv_discovery=True))
        for name, group in [
            ("Discovery Channel", "Knowledge"), ("National Geographic", "Documentary"),
            ("Animal Planet", "Entertainment"), ("Corporate Channel", "Business"),
            ("Money TV", "Finance"), ("Education TV", "Education"),
            ("Krishi Darshan", "Agriculture"),
        ]:
            attrs = {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"}
            with self.subTest(name=name, group=group):
                self.assertIsNotNone(prohibited_channel(attrs, name, iptv_discovery=True))

    def test_bangladesh_channels_of_all_six_prohibited_indian_genres_remain_eligible(self):
        for name, group in [
            ("Bangla News", "News"), ("Kids Bangla", "Kids"),
            ("Education Bangladesh", "Education"), ("Knowledge Bangla", "Knowledge"),
            ("Business Bangladesh", "Business"), ("Islamic Bangla", "Religious"),
        ]:
            attrs = {"group-title": group, "tvg-country": "BD", "tvg-id": "SampleChannel.bd"}
            with self.subTest(name=name):
                self.assertIsNone(prohibited_channel(attrs, name, iptv_discovery=True))

    def test_existing_prohibited_indian_education_queue_rows_are_purged(self):
        text = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-name="Vyas Channel" tvg-country="IN" group-title="New Channels",Vyas Channel\n'
            "https://example.invalid/vyas.m3u8\n"
            '#EXTINF:-1 tvg-name="Shiksha TV" tvg-id="ShikshaTV.in" group-title="New Backups",Shiksha TV\n'
            "https://example.invalid/shiksha.m3u8\n"
            '#EXTINF:-1 tvg-name="Gyandarshan HD" tvg-country="IN" group-title="New Backups",Gyandarshan HD\n'
            "https://example.invalid/gyandarshan.m3u8\n"
            '#EXTINF:-1 tvg-name="Channel 24" tvg-country="BD" group-title="New Channels",Channel 24\n'
            "https://example.invalid/channel24.m3u8\n"
        )
        filtered, removed = purge_forbidden_existing_queue_rows(text)
        self.assertEqual(set(removed), {"Vyas Channel", "Shiksha TV", "Gyandarshan HD"})
        self.assertIn("Channel 24", filtered)

    def test_bangladesh_discovery_channels_remain_unrestricted_by_genre(self):
        examples = [
            ("T Sports", "Sports"),
            ("Discovery Bangladesh", "Knowledge"),
            ("Business Bangladesh", "Business"),
            ("News Bangladesh", "News"),
            ("Kids Bangladesh", "Kids"),
            ("Religious Bangladesh", "Religious"),
        ]
        for name, group in examples:
            with self.subTest(name=name, group=group):
                self.assertIsNone(prohibited_channel(
                    {"group-title": group, "tvg-country": "BD", "tvg-id": "SampleChannel.bd"},
                    name,
                    discovery=True,
                    iptv_discovery=True,
                ))

    def test_indian_education_aliases_are_rejected_even_with_misleading_genre_metadata(self):
        examples = [
            ("Vyas Channel", "General", {}),
            ("Shiksha TV", "Entertainment", {}),
            ("Gyandarshan", "General", {}),
            ("DD Gyan Darshan", "Entertainment", {}),
            ("Kite Victers", "General", {}),
            ("Generic TV", "Entertainment", {"tvg-description": "24x7 higher education television channel"}),
            ("Generic TV", "Entertainment", {"tvg-genre": "Education"}),
            ("Generic TV", "Entertainment", {"tvg-id": "UniversityEducation.in"}),
        ]
        for name, group, extra in examples:
            attrs = {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in", **extra}
            with self.subTest(name=name, extra=extra):
                self.assertIsNotNone(prohibited_channel(attrs, name, iptv_discovery=True))

    def test_compact_indian_news_brands_are_rejected(self):
        for name in ("News18 Bangla", "TV9 Bangla", "Aaj Tak", "India Today", "Times Now", "Republic Bangla", "ABP Ananda", "Zee News", "WION"):
            attrs = {"group-title": "General", "tvg-country": "IN", "tvg-id": "GenericChannel.in"}
            with self.subTest(name=name):
                reason = prohibited_channel(attrs, name, iptv_discovery=True)
                self.assertIsNotNone(reason)
                self.assertIn("news", reason)

    def test_known_indian_news_kids_religious_and_vtu_aliases_are_rejected(self):
        examples = [
            ("TV 100", {"tvg-id": "TV100.in@SD"}, "news"),
            ("R Plus", {"tvg-id": "RPlus.in@SD"}, "news"),
            ("Sony Yay!", {"tvg-id": "SonyYay.in@SD"}, "kids"),
            ("Disha TV", {"tvg-id": "DishaTV.in@SD"}, "religious"),
            ("VTU", {"tvg-id": "VTU.in@SD"}, "education"),
            ("Disha TV", {}, "religious"),
            ("R Plus Gold", {"tvg-id": "RPlusGold.in@SD"}, "news"),
            ("BHI Channel", {"tvg-id": "BHI.Channel.in"}, "news"),
            ("Q TV", {"tvg-id": "QTV.in"}, "religious"),
            ("Shekinah TV", {"tvg-id": "ShekinahTV.in@SD"}, "religious"),
            ("Disney Channel", {"tvg-id": "DisneyChannel.in@HD"}, "kids"),
        ]
        for name, extra, category in examples:
            attrs = {"group-title": "General", **extra}
            with self.subTest(name=name, extra=extra):
                reason = prohibited_channel(attrs, name, iptv_discovery=True)
                self.assertIsNotNone(reason)
                self.assertIn(category, reason)
                self.assertEqual(known_indian_forbidden_category(attrs, name), category)

    def test_indian_identity_uses_source_then_country_then_known_alias(self):
        self.assertTrue(is_indian_discovery_candidate({"tvg-id": "DishaTV.in@SD"}, "Disha TV"))
        self.assertFalse(is_indian_discovery_candidate(
            {"tvg-country": "BD", "tvg-id": "DishaTV.in@SD"}, "Disha TV"
        ))
        self.assertFalse(is_indian_discovery_candidate(
            {"x-discovery-source-country": "BD", "tvg-id": "SonyYay.in@SD"}, "Sony Yay!"
        ))
        self.assertIsNone(prohibited_channel(
            {"x-discovery-source-country": "BD", "tvg-id": "SonyYay.in@SD", "group-title": "Kids"},
            "Sony Yay!",
            iptv_discovery=True,
        ))
        self.assertTrue(is_indian_discovery_candidate(
            {"x-discovery-source-country": "IN", "tvg-country": "BD"}, "Sony Yay!"
        ))

    def test_legacy_queue_purge_removes_known_indian_categories_without_country_metadata(self):
        text = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-id="TV100.in@SD" group-title="New Channels",TV 100\n'
            "https://example.invalid/tv100.m3u8\n"
            '#EXTINF:-1 tvg-id="RPlus.in@SD" group-title="New Channels",R Plus\n'
            "https://example.invalid/rplus.m3u8\n"
            '#EXTINF:-1 tvg-id="SonyYay.in@SD" group-title="New Backups",Sony Yay!\n'
            "https://example.invalid/sonyyay.m3u8\n"
            '#EXTINF:-1 tvg-id="DishaTV.in@SD" group-title="New Backups",Disha TV\n'
            "https://example.invalid/disha.m3u8\n"
            '#EXTINF:-1 tvg-id="VTU.in@SD" group-title="New Backups",VTU\n'
            "https://example.invalid/vtu.m3u8\n"
            '#EXTINF:-1 tvg-id="DDKisan.in@SD" group-title="New Channels",DD Kisan (1080p)\n'
            "https://example.invalid/dd-kisan.m3u8\n"
            '#EXTINF:-1 tvg-id="Gyandarshan.in@SD" group-title="New Channels",Gyandarshan (720p)\n'
            "https://example.invalid/gyandarshan.m3u8\n"
            '#EXTINF:-1 tvg-id="KiteVicters.in@SD" group-title="New Channels",Kite Victers (720p)\n'
            "https://example.invalid/kite-victers.m3u8\n"
            '#EXTINF:-1 tvg-id="ShikshaTV.in@SD" group-title="New Channels",Shiksha TV (720p)\n'
            "https://example.invalid/shiksha.m3u8\n"
            '#EXTINF:-1 tvg-id="VyasChannel.in@SD" group-title="New Channels",Vyas Channel (576p)\n'
            "https://example.invalid/vyas.m3u8\n"
            '#EXTINF:-1 tvg-id="NickJr.in@SD" group-title="New Backups",Nick Jr. (India) (576p)\n'
            "https://example.invalid/nick-jr.m3u8\n"
            '#EXTINF:-1 tvg-id="DiscoveryChannel.in@HD" group-title="New Backups",Discovery Channel (India) HD (1080p)\n'
            "https://example.invalid/discovery.m3u8\n"
            '#EXTINF:-1 tvg-id="HistoryTV18.in@HD" group-title="New Backups",History TV18 HD (1080p)\n'
            "https://example.invalid/history.m3u8\n"
            '#EXTINF:-1 tvg-id="SafariTV.in@SD" group-title="New Backups",Safari TV (576p)\n'
            "https://example.invalid/safari.m3u8\n"
            '#EXTINF:-1 tvg-country="BD" tvg-id="Channel24.bd" group-title="New Channels",Channel 24\n'
            "https://example.invalid/channel24.m3u8\n"
        )
        filtered, removed = purge_forbidden_existing_queue_rows(text)
        self.assertEqual(set(removed), {
            "TV 100", "R Plus", "Sony Yay!", "Disha TV", "VTU",
            "DD Kisan (1080p)", "Gyandarshan (720p)", "Kite Victers (720p)",
            "Shiksha TV (720p)", "Vyas Channel (576p)", "Nick Jr. (India) (576p)",
            "Discovery Channel (India) HD (1080p)", "History TV18 HD (1080p)", "Safari TV (576p)",
        })
        self.assertIn("Channel 24", filtered)

    def test_iptv_evaluate_uses_india_source_country_despite_misleading_metadata(self):
        attrs = {"tvg-country": "US", "tvg-id": "VyasChannel.us", "group-title": "General"}
        candidate, reason = evaluate(
            "India", attrs, "Vyas Channel", "https://example.org/vyas.m3u8"
        )
        self.assertIsNone(candidate)
        self.assertIn("education", reason)


    def test_all_indian_religious_channels_are_rejected(self):
        for name in ("Madani TV", "Peace TV", "Quran TV", "Islam Channel", "Al Huda", "Aastha"):
            attrs = {"group-title": "Religious", "tvg-country": "IN", "tvg-id": "SampleChannel.in"}
            with self.subTest(name=name):
                self.assertIsNotNone(prohibited_channel(attrs, name, iptv_discovery=True))


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
