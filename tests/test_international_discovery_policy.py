#!/usr/bin/env python3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import discover_international_channels as discovery
import reorganize_international_playlist as reorg
import validate_international_playlist as intl_validator
import repair_international_playlist as legacy_repair


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

    def test_known_channel_aliases_share_one_identity_key(self):
        pairs = [
            ("Rupasi Bangla", "Ruposhi Bangla"),
            ("Mastiii", "Music Mastii"),
            ("Discovery Channel", "Discovery Channel East"),
            ("Disney Channel India", "DISNEY CHANNEL [IN]"),
            ("Animal Planet", "Animal Planet (India)"),
            ("TLC", "TLC (India) (720p)"),
            ("Zee Anmol TV", "Anmol TV (720p)"),
        ]
        for left, right in pairs:
            with self.subTest(left=left, right=right):
                self.assertEqual(reorg.channel_key(left), reorg.channel_key(right))

    def test_primary_id_reuse_for_different_channels_is_rejected(self):
        seen = {}
        reorg.register_primary_id(seen, {
            "a": {"tvg-id": "travel.us"}, "key": "travelchanneleast", "name": "Travel Channel East"
        })
        with self.assertRaisesRegex(SystemExit, "Assign distinct exact IDs"):
            reorg.register_primary_id(seen, {
                "a": {"tvg-id": "travel.us"}, "key": "4ktravel", "name": "4K Travel"
            })

    def test_same_primary_id_for_same_channel_is_not_a_conflicting_identity(self):
        seen = {}
        first = {"a": {"tvg-id": "gazitv.bd"}, "key": "gtv", "name": "G TV"}
        second = {"a": {"tvg-id": "gazitv.bd"}, "key": "gtv", "name": "G TV"}
        reorg.register_primary_id(seen, first)
        reorg.register_primary_id(seen, second)
        self.assertIs(seen["gazitv.bd"], first)

    def test_discovery_workflow_reorganizes_before_final_validation(self):
        workflow = Path(".github/workflows/international-channel-discovery.yml").read_text(encoding="utf-8")
        reorganize = workflow.index("python scripts/reorganize_international_playlist.py")
        validate = workflow.index("python scripts/validate_international_playlist.py")
        self.assertLess(reorganize, validate)

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
        ]
        for name, group, tvg_id in excluded:
            with self.subTest(name=name):
                self.assertIsNone(self.classify(name, group, "IN", tvg_id)[0])
        for name, group, tvg_id in [
            ("Cartoon Network", "Kids", "CartoonNetwork.in"),
            ("Pogo", "Kids", "Pogo.in"),
        ]:
            self.assertEqual(self.classify(name, group, "IN", tvg_id)[0], "Kids")
        self.assertEqual(self.classify("DD Sports", "Sports", "IN", "DDSports.in")[0], "Sports")
        self.assertEqual(self.classify("Colors Cineplex", "Entertainment", "IN", "ColorsCineplex.in")[0], "Indian Movies")

    def test_aruba_vip_tv_music_exception_is_limited_to_verified_identity(self):
        attrs = {
            "group-title": "Aruba",
            "tvg-country": "AW",
            "tvg-id": "custom.vip-tv-aw-music",
            "channel-id": "custom.vip-tv-aw-music",
            "tvg-content": "Music",
        }
        policy_attrs = dict(attrs, **{"group-title": "International"})
        self.assertEqual(discovery.policy(policy_attrs, "VIP TV", allow_legacy_group=True), ("International Music", None, "AW"))
        self.assertEqual(intl_validator.foreign_movie_music_error(attrs, "VIP TV", "AW"), "")
        wrong_identity = dict(policy_attrs, **{"tvg-id": "VIPTV.aw"})
        self.assertIsNone(discovery.policy(wrong_identity, "VIP TV", allow_legacy_group=True)[0])

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

    def test_non_movie_music_foreign_religious_channel_is_demoted_from_primary_group(self):
        source = '#EXTINF:-1 tvg-id="custom.hope-channel-proyecto-ja-cr-music" tvg-content="Music" group-title="Costa Rica" tvg-name="Hope Channel PROYECTO JA",Hope Channel PROYECTO JA'
        attrs = reorg.attrs(source)
        self.assertEqual(
            reorg.classify(attrs, "Hope Channel PROYECTO JA", "Costa Rica", "CR"),
            ("Backup", None, None),
        )
    def test_radio_brands_and_religious_movie_music_false_positives_are_rejected(self):
        for name in ("Hitradio O3", "Bel RTL", "Couleur 3", "Joe FM", "Fame95 FM"):
            with self.subTest(name=name):
                self.assertIsNone(self.classify(name, "Music", "BE", name.replace(" ", "") + ".be")[0])
        self.assertIsNone(self.classify("Hope Channel PROYECTO JA", "Music", "US", "HopeChannel.us")[0])
        self.assertIsNone(self.classify("Canal Cine Dios", "Movies", "CO", "CanalCineDios.co")[0])

    def test_generic_genre_policy_has_bangladesh_and_india_exceptions(self):
        for name, group, tvg_id in (
            ("Entertainment World", "General", "EntertainmentWorld.bd"),
            ("World Channel", "", "WorldChannel.bd"),
        ):
            with self.subTest(country="BD", name=name):
                self.assertEqual(self.classify(name, group, "BD", tvg_id)[0], "Bangladesh")
        for name, group, tvg_id in (
            ("Entertainment World", "General", "EntertainmentWorld.in"),
            ("World Channel", "", "WorldChannel.in"),
        ):
            with self.subTest(country="IN", name=name):
                self.assertEqual(self.classify(name, group, "IN", tvg_id)[0], "Indian Entertainment")
        for country, tvg_id in (("PK", "EntertainmentWorld.pk"), ("US", "EntertainmentWorld.us"), (None, "EntertainmentWorld.us")):
            with self.subTest(country=country):
                self.assertIsNone(self.classify("Entertainment World", "General", country, tvg_id)[0])
                self.assertIsNone(self.classify("World Channel", "", country, tvg_id)[0])

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

    def test_qualified_country_never_promotes_manual_review_candidates(self):
        blocks = [
            [
                f'#EXTINF:-1 tvg-id="Channel{i}.mk" tvg-country="MK" group-title="New Channels",Channel {i}',
                f"https://example.org/channel{i}.m3u8",
            ]
            for i in range(5)
        ]
        before = [block[0] for block in blocks]
        migrations = discovery.promote_qualified_country_candidates(blocks, {"MK"})
        self.assertEqual(migrations, [])
        self.assertEqual([block[0] for block in blocks], before)
        self.assertTrue(all('group-title="New Channels"' in block[0] for block in blocks))

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

    def test_review_candidate_without_authentic_logo_is_rejected_from_queue(self):
        block = [
            '#EXTINF:-1 tvg-id="Colors.us" tvg-country="US" group-title="New Backups" tvg-content="Movies",Colors',
            "https://example.org/colors.m3u8",
        ]
        rejected = []
        with tempfile.TemporaryDirectory() as tmp, patch.object(discovery, "LOGOS", Path(tmp) / "logos"):
            kept, repaired, removed = discovery.localize_discovery_queue_logos(
                [block], {block[1]}, rejected
            )
        self.assertEqual(kept, [])
        self.assertEqual(repaired, 0)
        self.assertEqual(removed, 1)
        self.assertEqual(
            rejected,
            [("Colors", "New Backups", "no authentic local repository logo after localization")],
        )

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


    def test_foreign_primary_country_groups_require_explicit_movie_music_content(self):
        valid_movie = {
            "group-title": "United States", "tvg-country": "US",
            "tvg-id": "CinemaWorld.us", "tvg-content": "Movies",
        }
        valid_music = {
            "group-title": "Pakistani", "tvg-country": "PK",
            "tvg-id": "8XM.pk", "tvg-content": "Music",
        }
        self.assertEqual(
            intl_validator.foreign_movie_music_error(valid_movie, "Cinema World", "US"), ""
        )
        self.assertEqual(
            intl_validator.foreign_movie_music_error(valid_music, "8XM", "PK"), ""
        )

    def test_foreign_channels_in_generic_genre_groups_are_rejected(self):
        examples = [
            ("Documentary & Wildlife", "US", "4K Travel", "custom.4k.travel"),
            ("Kids", "PL", "4 Fun Kids", "4FunKids.pl"),
            ("Religious", "PK", "ARY Qtv", "ARYQTV.pk"),
            ("Sports", "TR", "A Spor", "ASpor.tr"),
        ]
        for group, country, name, tvg_id in examples:
            with self.subTest(group=group, country=country, name=name):
                attrs = {
                    "group-title": group,
                    "tvg-country": country,
                    "tvg-id": tvg_id,
                    "tvg-content": "Movies",
                }
                self.assertNotEqual(
                    intl_validator.genre_group_policy_error(attrs, name, group), ""
                )

    def test_bangladesh_and_allowed_indian_genre_groups_are_preserved(self):
        examples = [
            ("Religious", "BD", "Madani TV", "MadaniTV.bd"),
            ("Documentary & Wildlife", "BD", "Discovery Bangla", "DiscoveryBangla.bd"),
            ("Kids", "IN", "Pogo", "Pogo.in"),
            ("Sports", "IN", "DD Sports", "DDSports.in"),
        ]
        for group, country, name, tvg_id in examples:
            with self.subTest(group=group, country=country, name=name):
                attrs = {
                    "group-title": group,
                    "tvg-country": country,
                    "tvg-id": tvg_id,
                }
                self.assertEqual(
                    intl_validator.genre_group_policy_error(attrs, name, group), ""
                )

    def test_indian_religious_genre_group_is_rejected(self):
        attrs = {
            "group-title": "Religious",
            "tvg-country": "IN",
            "tvg-id": "PeaceTV.in",
        }
        self.assertNotEqual(
            intl_validator.genre_group_policy_error(attrs, "Peace TV", "Religious"), ""
        )

    def test_foreign_primary_country_groups_reject_missing_or_conflicting_movie_music_tags(self):
        missing = {
            "group-title": "Pakistani", "tvg-country": "PK", "tvg-id": "HumTV.pk",
        }
        conflicting = {
            "group-title": "United States", "tvg-country": "US",
            "tvg-id": "CinemaWorld.us", "tvg-content": "Music",
        }
        non_movie_music = {
            "group-title": "United Kingdom", "tvg-country": "GB",
            "tvg-id": "WorldNews.uk", "tvg-content": "Movies",
        }
        self.assertNotEqual(
            intl_validator.foreign_movie_music_error(missing, "Hum TV", "PK"), ""
        )
        self.assertNotEqual(
            intl_validator.foreign_movie_music_error(conflicting, "Cinema World", "US"), ""
        )
        self.assertNotEqual(
            intl_validator.foreign_movie_music_error(non_movie_music, "World News", "GB"), ""
        )


class LegacyInternationalRepairPolicyTests(unittest.TestCase):
    def test_legacy_repair_keeps_indian_kids_and_sports_but_not_foreign_genres(self):
        def info(name, country, group="International"):
            return (
                f'#EXTINF:-1 tvg-name="{name}" tvg-country="{country}" '
                f'group-title="{group}",{name}'
            )

        self.assertEqual(
            legacy_repair.classify_primary_group(info("Cartoon Network", "IN"), "International"),
            "Kids",
        )
        self.assertEqual(
            legacy_repair.classify_primary_group(info("DD Sports", "IN"), "International"),
            "Sports",
        )
        self.assertEqual(
            legacy_repair.classify_primary_group(info("Cartoon Network", "US"), "International"),
            "",
        )
        self.assertEqual(
            legacy_repair.classify_primary_group(info("World Sport", "US"), "International"),
            "",
        )
        self.assertEqual(
            legacy_repair.classify_primary_group(info("Cinema World", "US"), "International"),
            "International Movies",
        )
        self.assertEqual(
            legacy_repair.classify_primary_group(info("World Music", "US"), "International"),
            "International Music",
        )
        self.assertEqual(
            legacy_repair.classify_primary_group(info("Channel 24", "BD"), "International"),
            "Bangladesh",
        )


if __name__ == "__main__":
    unittest.main()
