#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import discover_international_channels as discovery
import reorganize_international_playlist as reorg


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

    def test_pakistani_movie_music_entries_keep_content_tag_for_validator(self):
        source = (
            '#EXTINF:-1 tvg-id="8xm.pk@sd" tvg-name="8XM" '
            'group-title="Pakistani",8XM'
        )
        attrs = reorg.attrs(source)
        group, kind, reason = reorg.classify(attrs, "8XM", "Pakistani", "PK")
        self.assertEqual((group, kind, reason), ("Pakistani", "music", None))

        rendered = reorg.set_extinf(
            [source, "https://example.invalid/8xm.m3u8"],
            "8XM",
            group,
            "PK",
            kind,
            keep_logo=True,
        )
        self.assertIn('tvg-content="Music"', rendered)
        self.assertIn('group-title="Pakistani"', rendered)

    def test_axn_movies_is_allowed_but_general_axn_channels_remain_rejected(self):
        self.assertEqual(
            self.classify("AXN Movies (Portugal)", "Movies", "PT", "AXNMovies.pt")[0],
            "International Movies",
        )
        self.assertIsNone(
            self.classify("AXN Latin America South", "Movies", "US", "AXNLatinAmerica.us")[0]
        )

    def test_general_entertainment_or_other_source_categories_are_rejected_even_with_movie_music_names(self):
        for group in ("General", "Entertainment", "Variety", "Series", "Lifestyle", "Education", "International"):
            with self.subTest(group=group):
                self.assertIsNone(self.classify("Cinema World", group, "US", "CinemaWorld.us")[0])
                self.assertIsNone(self.classify("World Music", group, "US", "WorldMusic.us")[0])

    def test_bangladesh_news_is_allowed_but_indian_and_foreign_news_are_rejected(self):
        self.assertEqual(self.classify("Channel 24", "News", "BD", "Channel24.bd")[0], "Bangladesh")
        self.assertEqual(self.classify("Somoy TV", "Entertainment", "BD", "SomoyTV.bd")[0], "Bangladesh")
        for country, tvg_id in (("IN", "WorldNews.in"), ("PK", "WorldNews.pk"), ("US", "WorldNews.us"), (None, "WorldNews.us")):
            with self.subTest(country=country):
                self.assertIsNone(self.classify("World News", "News", country, tvg_id)[0])
        self.assertIsNone(self.classify("CNBC World", "Business", "SG", "CNBCWorld.sg")[0])

    def test_indian_policy_matches_iptv_playlist_exclusions_and_keeps_sports(self):
        excluded = [
            ("Aaj Tak", "News", "AajTak.in"),
            ("Madani TV", "Religious", "MadaniTV.in"),
            ("Peace TV", "Religious", "PeaceTV.in"),
            ("Education TV", "Education", "EducationTV.in"),
            ("DD Gyan Darshan", "General", "GyanDarshan.in"),
            ("Cartoon Network", "Kids", "CartoonNetwork.in"),
            ("Pogo", "Kids", "Pogo.in"),
        ]
        for name, group, tvg_id in excluded:
            with self.subTest(name=name):
                self.assertIsNone(self.classify(name, group, "IN", tvg_id)[0])
        self.assertEqual(self.classify("DD Sports", "Sports", "IN", "DDSports.in")[0], "Indian Entertainment")

    def test_bangladesh_religious_educational_kids_and_sports_are_not_genre_filtered(self):
        examples = [
            ("Madani TV", "Religious", "MadaniTV.bd"),
            ("Education TV", "Education", "EducationTV.bd"),
            ("Kids Bangla", "Kids", "KidsBangla.bd"),
            ("Sports Bangla", "Sports", "SportsBangla.bd"),
        ]
        for name, group, tvg_id in examples:
            with self.subTest(name=name):
                self.assertEqual(self.classify(name, group, "BD", tvg_id)[0], "Bangladesh")

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

    def test_all_religious_channels_are_rejected_in_india_and_other_countries(self):
        examples = [
            ("Gospel TV", "Religious", "US", "GospelTV.us"),
            ("Sunnah TV", "Religious", "SA", "SunnahTV.sa"),
            ("MTA International", "General", "GB", "MTAInternational.uk"),
            ("Hindu Bhakti Music", "Music", "IN", "BhaktiMusic.in"),
            ("Madani TV", "General", "IN", "MadaniTV.in"),
        ]
        for name, group, country, tvg_id in examples:
            with self.subTest(name=name):
                self.assertIsNone(self.classify(name, group, country, tvg_id)[0])
        self.assertEqual(self.classify("Madani TV", "Religious", "BD", "MadaniTV.bd")[0], "Bangladesh")

    def test_radio_and_series_or_general_entertainment_channels_are_rejected(self):
        examples = [
            ("Radio Bonita 106.7", "Music", "US", "RadioBonita.us"),
            ("Radio Chisinau", "Music", "MD", "RadioChisinau.md"),
            ("Wavez FM", "Music", "US", "WavezFM.us"),
            ("X 102.7 FM", "Music", "US", "X1027FM.us"),
            ("Melody FM", "Music", "JO", "MelodyFM.jo"),
            ("Tropicalia 93.9 FM", "Music", "ZZ", "Tropicalia939FM.zz"),
            ("La Que Buena Atlanta", "Music", "US", "LaQueBuenaAtlanta.us"),
            ("Pequeradio", "Music", "ES", "Pequeradio.es"),
            ("Dega TV", "Music", "US", "DegaTV.us"),
            ("AXN Latin America South", "Movies", "US", "AXNLatinAmerica.us"),
            ("VIP TV (720p)", "Music", "ZZ", "VIPTV.zz"),
            ("Video Tour Channel", "Music", "ZZ", "VideoTourChannel.zz"),
            ("Vos y TV", "Music", "NI", "VosYTV.ni"),
            ("New Channel (480p)", "Music", "CA", "NewChannel.ca"),
            ("YleX", "Music", "FI", "YleX.fi"),
            ("MNM", "Music", "BE", "MNM.be"),
            ("Kronehit", "Music", "AT", "Kronehit.at"),
            ("Zo'r TV", "Music", "UZ", "ZorTV.uz"),
            ("Star Trek: Deep Space Nine", "Movies", "US", "StarTrekDeepSpaceNine.us"),
            ("The Twilight Zone", "Movies", "US", "TheTwilightZone.us"),
            ("USA Network", "Movies", "US", "USANetwork.us"),
            ("RTSH Shqip", "Movies", "AL", "RTSHShqip.al"),
            ("Paramount Network", "Movies", "US", "ParamountNetwork.us"),
        ]
        for name, group, country, tvg_id in examples:
            with self.subTest(name=name):
                self.assertIsNone(self.classify(name, group, country, tvg_id)[0])

    def test_hope_channel_is_rejected_by_playlist_reorganizer(self):
        source = '#EXTINF:-1 tvg-id="custom.hope-channel-proyecto-ja-cr-music" tvg-content="Music" group-title="Costa Rica" tvg-name="Hope Channel PROYECTO JA",Hope Channel PROYECTO JA'
        attrs = reorg.attrs(source)
        self.assertEqual(
            reorg.classify(attrs, "Hope Channel PROYECTO JA", "Costa Rica", "CR"),
            (None, None, "non-Islamic religious"),
        )
    def test_radio_brands_and_religious_movie_music_false_positives_are_rejected(self):
        for name in ("Hitradio O3", "Bel RTL", "Couleur 3", "Joe FM", "Fame95 FM"):
            with self.subTest(name=name):
                self.assertIsNone(self.classify(name, "Music", "BE", name.replace(" ", "") + ".be")[0])
        self.assertIsNone(self.classify("Hope Channel PROYECTO JA", "Music", "US", "HopeChannel.us")[0])
        self.assertIsNone(self.classify("Canal Cine Dios", "Movies", "CO", "CanalCineDios.co")[0])

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
        # gets its dedicated group; below it, channels remain in International.
        # BD, IN and PK always keep their established regional groups.
        self.assertEqual(discovery.primary_target("International Movies", "AT", {"AT"}), "Austria")
        self.assertEqual(discovery.primary_target("International Music", "AT", {"AT"}), "Austria")
        self.assertEqual(discovery.primary_target("International Movies", "AT", set()), "International")
        self.assertEqual(discovery.primary_target("International Music", "DE", set()), "International")
        self.assertEqual(discovery.primary_target("International Movies", "BD", set()), "Bangladesh")
        self.assertEqual(discovery.primary_target("International Music", "PK", set()), "Pakistani")
        self.assertEqual(discovery.primary_target("International Movies", "IN", set()), "Indian Movies")
        self.assertEqual(discovery.primary_target("International Music", "IN", set()), "Indian Music")

    def test_existing_international_rows_are_revalidated_and_promoted_at_five(self):
        music = {
            "group-title": "International",
            "tvg-content": "Music",
            "tvg-country": "MK",
            "tvg-id": "MacedonianMusic.mk",
        }
        target, reason, genre = discovery.existing_international_target(
            music, "Macedonian Music TV", set()
        )
        self.assertEqual((target, reason, genre), ("International", None, "Music"))

        target, reason, genre = discovery.existing_international_target(
            music, "Macedonian Music TV", {"MK"}
        )
        self.assertEqual((target, reason, genre), ("North Macedonia", None, "Music"))

        radio = dict(music, **{"tvg-country": "AT", "tvg-id": "Kronehit.at"})
        target, reason, _ = discovery.existing_international_target(
            radio, "Kronehit", set()
        )
        self.assertIsNone(target)
        self.assertIn("test/VOD/non-TV name", reason)

    def test_qualified_country_promotes_queued_candidates_at_five_identity_threshold(self):
        blocks = [
            [
                f'#EXTINF:-1 tvg-id="Channel{i}.mk" tvg-country="MK" group-title="International",Channel {i}',
                f"https://example.org/channel{i}.m3u8",
            ]
            for i in range(5)
        ]
        migrations = discovery.promote_qualified_country_candidates(blocks, {"MK"})
        self.assertEqual(len(migrations), 5)
        self.assertTrue(all('group-title="North Macedonia"' in block[0] for block in blocks))

        below_threshold = [
            [
                f'#EXTINF:-1 tvg-id="Channel{i}.mk" tvg-country="MK" group-title="International",Channel {i}',
                f"https://example.org/below{i}.m3u8",
            ]
            for i in range(4)
        ]
        self.assertEqual(discovery.promote_qualified_country_candidates(below_threshold, set()), [])
        self.assertTrue(all('group-title="International"' in block[0] for block in below_threshold))

    def test_duplicate_queue_urls_are_removed_but_primary_entries_are_preserved(self):
        url_a = "https://example.org/epic-music.m3u8"
        url_b = "https://example.org/oli-tv.m3u8"
        url_c = "https://example.org/new-music.m3u8"
        blocks = [
            ['#EXTINF:-1 tvg-name="Epic Music Digital" group-title="Indian Music",Epic Music Digital', url_a],
            ['#EXTINF:-1 tvg-name="Epic Music" group-title="New Backups",Epic Music', url_a],
            ['#EXTINF:-1 tvg-name="Oli TV" group-title="Indian Entertainment",Oli TV', url_b],
            ['#EXTINF:-1 tvg-name="Oli TV" group-title="New Channels",Oli TV', url_b],
            ['#EXTINF:-1 tvg-name="New Music" group-title="New Channels",New Music', url_c],
            ['#EXTINF:-1 tvg-name="Duplicate New Music" group-title="New Backups",Duplicate New Music', url_c],
        ]
        kept, removed = discovery.remove_duplicate_queue_urls(blocks)
        self.assertEqual(len(removed), 3)
        self.assertEqual(len(kept), 3)
        self.assertEqual(kept[0][0], blocks[0][0])
        self.assertEqual(kept[1][0], blocks[2][0])
        self.assertEqual(kept[2][0], blocks[4][0])
        self.assertEqual({name for name, _, _ in removed},
                         {"Epic Music", "Oli TV", "Duplicate New Music"})

    def test_known_non_tv_discovery_rows_are_removed_only_from_country_groups(self):
        self.assertEqual(
            discovery.known_non_tv_discovery_reason("YleX (720p)", "Finland"),
            "known radio station; not a linear TV channel",
        )
        self.assertEqual(
            discovery.known_non_tv_discovery_reason("Zo'r TV (576p)", "Uzbekistan"),
            "general entertainment channel; not a dedicated Movies/Music channel",
        )
        self.assertIsNone(discovery.known_non_tv_discovery_reason("YleX (720p)", "New Channels"))
        self.assertIsNone(discovery.known_non_tv_discovery_reason("YleX (720p)", "Backup"))

    def test_tokenized_urls_are_rejected_without_playback_testing(self):
        self.assertFalse(discovery.safe_url("https://example.org/live.m3u8?token=abc"))
        self.assertTrue(discovery.safe_url("https://example.org/channel/index.m3u8"))

    def test_country_threshold_counts_unique_normalized_channel_names_not_stream_ids(self):
        names = [
            discovery.primary_identity({"tvg-id": "A-HD.mk"}, "A Movie HD"),
            discovery.primary_identity({"tvg-id": "A-SD.mk"}, "A Movie SD"),
            discovery.primary_identity({"tvg-id": "B.mk"}, "B Movie"),
            discovery.primary_identity({"tvg-id": "C.mk"}, "C Movie"),
            discovery.primary_identity({"tvg-id": "D.mk"}, "D Movie"),
        ]
        self.assertEqual(len(set(names)), 4)
        self.assertNotIn("MK", discovery.qualified_country_groups({"MK": set(names)}))
        names.append(discovery.primary_identity({"tvg-id": "E.mk"}, "E Movie"))
        self.assertIn("MK", discovery.qualified_country_groups({"MK": set(names)}))

    def test_category_registry_places_international_after_country_groups(self):
        registry = discovery.category_registry(["Belarus", "International", "Albania", "Sports"])
        self.assertLess(registry.index("Albania"), registry.index("Belarus"))
        self.assertLess(registry.index("Belarus"), registry.index("International"))
        self.assertLess(registry.index("International"), registry.index("Sports"))


if __name__ == "__main__":
    unittest.main()
