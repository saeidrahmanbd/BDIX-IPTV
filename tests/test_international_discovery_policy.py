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
    def test_existing_primary_index_counts_review_backup_and_queues_as_represented(self):
        blocks = [
            ['#EXTINF:-1 tvg-name="Star Gold" group-title="Review",Star Gold', "https://example.org/star-gold-review.m3u8"],
            ['#EXTINF:-1 tvg-name="Star Movies Select" group-title="Backup",Star Movies Select', "https://example.org/star-movies-select-backup.m3u8"],
            ['#EXTINF:-1 tvg-name="New Candidate" group-title="New Channels",New Candidate', "https://example.org/new-candidate.m3u8"],
            ['#EXTINF:-1 tvg-name="Queued Alternate" group-title="New Backups",Queued Alternate', "https://example.org/queued-alternate.m3u8"],
            ['#EXTINF:-1 tvg-name="Ignored Test" group-title="Test",Ignored Test', "https://example.org/test.m3u8"],
        ]
        index = discovery.existing_primary_index(blocks)
        self.assertIn(discovery.norm("Star Gold"), index)
        self.assertIn(discovery.norm("Star Movies Select"), index)
        self.assertIn(discovery.norm("New Candidate"), index)
        self.assertIn(discovery.norm("Queued Alternate"), index)
        self.assertNotIn(discovery.norm("Ignored Test"), index)

    def test_queue_candidate_without_local_logo_is_kept_without_external_reference(self):
        name = "Unique Channel Without Local Art 2026"
        url = "https://example.org/unique-channel-without-local-art.m3u8"
        block = [
            f'#EXTINF:-1 tvg-name="{name}" tvg-logo="https://logos.example.test/fake.png" group-title="New Channels",{name}',
            url,
        ]
        kept, repaired, removed = discovery.localize_discovery_queue_logos(
            [block], {url}, []
        )
        self.assertEqual(len(kept), 1)
        self.assertNotIn("tvg-logo=", kept[0][0])
        self.assertEqual(repaired, 0)
        self.assertEqual(removed, 1)


    def classify(self, name, group, country=None, tvg_id=None, language=None):
        attrs = {"group-title": group}
        if country:
            attrs["tvg-country"] = country
        if tvg_id:
            attrs["tvg-id"] = tvg_id
        if language:
            attrs["tvg-language"] = language
        return discovery.policy(attrs, name)

    def test_curated_adult_group_is_preserved_but_backup_alternates_stay_backup(self):
        adult_attrs = {
            "group-title": "Adult",
            "tvg-country": "US",
            "tvg-id": "AdultChannelAlpha.us",
        }
        self.assertEqual(
            reorg.classify(adult_attrs, "Adult Channel Alpha", "Adult", "US"),
            ("Adult", None, None),
        )

        # The correction must not promote an alternate stream out of Backup.
        backup_attrs = dict(adult_attrs, **{"group-title": "Backup"})
        self.assertEqual(
            reorg.classify(backup_attrs, "Adult Channel Alpha", "Backup", "US"),
            ("Backup", None, None),
        )
        self.assertEqual(
            reorg.classify(backup_attrs, "Adult Channel Alpha", "Backup", "US", promote_backup=True),
            ("Adult", None, None),
        )

    def test_explicit_adult_backup_ids_are_restored_to_adult_group(self):
        attrs = {"group-title": "Backup", "tvg-id": "custom.xxx-bang-bus", "tvg-content": ""}
        self.assertEqual(reorg.classify(attrs, "Bang Bus", "Backup", "US"), ("Adult", None, None))

    def test_generic_adult_word_does_not_reclassify_backup(self):
        attrs = {"group-title": "Backup", "tvg-id": "AdultChannelAlpha.us"}
        self.assertEqual(reorg.classify(attrs, "Adult Channel Alpha", "Backup", "US"), ("Backup", None, None))
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

    def test_discovery_workflow_does_not_run_broad_playlist_reorganization(self):
        workflow = Path(".github/workflows/international-channel-discovery.yml").read_text(encoding="utf-8")
        self.assertNotIn("python scripts/reorganize_international_playlist.py", workflow)
        self.assertIn("python scripts/validate_international_playlist.py", workflow)
        lines = workflow.splitlines()
        commit_index = next(i for i, line in enumerate(lines) if line.strip() == "- name: Commit discovery changes")
        self.assertEqual(lines[commit_index + 1].strip(), "if: always() && steps.validate_international_playlist.outcome != 'skipped'")

    def test_international_validator_accepts_repository_relative_local_logo(self):
        import json
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            logos = root / "logos"
            logos.mkdir()
            (logos / "test.svg").write_text("<svg/>", encoding="utf-8")
            playlist = root / "International-Playlist.m3u"
            registry = intl_validator.FIXED + intl_validator.TAIL
            content = (
                "#EXTM3U\n"
                + "\n".join(intl_validator.ATTRIBUTION)
                + "\n#PLAYLIST-STUDIO-CATEGORIES:"
                + json.dumps(registry)
                + '\n#EXTINF:-1 tvg-id="LocalLogo.bd" tvg-name="Local Logo Test" tvg-country="BD" tvg-logo="logos/test.svg" group-title="Bangladesh",Local Logo Test'
                + "\nhttps://example.org/test.m3u8\n"
            )
            playlist.write_text(content, encoding="utf-8")
            with patch.object(intl_validator, "PLAYLIST", playlist), patch.object(intl_validator, "LOGOS", logos):
                intl_validator.main()

    def test_international_validator_rejects_external_logo_url(self):
        import json
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            logos = root / "logos"
            logos.mkdir()
            (logos / "test.svg").write_text("<svg/>", encoding="utf-8")
            playlist = root / "International-Playlist.m3u"
            registry = intl_validator.FIXED + intl_validator.TAIL
            content = (
                "#EXTM3U\n"
                + "\n".join(intl_validator.ATTRIBUTION)
                + "\n#PLAYLIST-STUDIO-CATEGORIES:"
                + json.dumps(registry)
                + '\n#EXTINF:-1 tvg-id="LocalLogo.bd" tvg-name="Local Logo Test" tvg-country="BD" tvg-logo="https://example.org/test.svg" group-title="Bangladesh",Local Logo Test'
                + "\nhttps://example.org/test.m3u8\n"
            )
            playlist.write_text(content, encoding="utf-8")
            with patch.object(intl_validator, "PLAYLIST", playlist), patch.object(intl_validator, "LOGOS", logos):
                with self.assertRaisesRegex(SystemExit, "local /logos asset"):
                    intl_validator.main()

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

    def test_news_channels_are_grouped_by_genre_regardless_of_country(self):
        for country, tvg_id, name in (
            ("BD", "Channel24.bd", "Channel 24"),
            ("BD", "SomoyTV.bd", "Somoy TV"),
            ("PK", "PakistanNews.pk", "Pakistan News"),
            ("IN", "WorldNews.in", "World News"),
            ("US", "WorldNews.us", "World News"),
            ("GB", "BBCNews.uk", "BBC News"),
        ):
            with self.subTest(country=country, name=name):
                self.assertEqual(self.classify(name, "News", country, tvg_id)[0], "News")

    def test_indian_genres_take_precedence_over_country_group(self):
        examples = [
            ("Aaj Tak", "News", "AajTak.in", "News"),
            ("Madani TV", "Religious", "MadaniTV.in", "Religious"),
            ("Peace TV", "Religious", "PeaceTV.in", "Religious"),
            ("Education TV", "Education", "EducationTV.in", "Indian Entertainment"),
            ("DD Gyan Darshan", "General", "GyanDarshan.in", "Religious"),
            ("Cartoon Network", "Kids", "CartoonNetwork.in", "Kids"),
            ("Pogo", "Kids", "Pogo.in", "Kids"),
            ("DD Sports", "Sports", "DDSports.in", "Sports"),
            ("Colors Cineplex", "Entertainment", "ColorsCineplex.in", "Indian Movies"),
        ]
        for name, group, tvg_id, expected in examples:
            with self.subTest(name=name):
                self.assertEqual(self.classify(name, group, "IN", tvg_id)[0], expected)

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

    def test_bangladesh_channels_use_genre_groups_when_identifiable(self):
        examples = [
            ("Madani TV", "Religious", "MadaniTV.bd", "Religious"),
            ("Education TV", "Education", "EducationTV.bd", "Bangladesh"),
            ("Kids Bangla", "Kids", "KidsBangla.bd", "Kids"),
            ("Sports Bangla", "Sports", "SportsBangla.bd", "Sports"),
        ]
        for name, group, tvg_id, expected in examples:
            with self.subTest(name=name):
                self.assertEqual(self.classify(name, group, "BD", tvg_id)[0], expected)

    def test_kids_sports_documentary_and_wildlife_use_genre_groups_for_all_countries(self):
        examples = [
            ("Cartoon World", "Kids", "Kids"),
            ("Disney Junior", "Entertainment", "Kids"),
            ("World Sport", "Sports", "Sports"),
            ("Nature World", "Documentary", "Documentary & Wildlife"),
            ("Discovery Channel", "General", "Documentary & Wildlife"),
            ("National Geographic", "General", "Documentary & Wildlife"),
        ]
        for name, group, expected in examples:
            with self.subTest(name=name):
                self.assertEqual(self.classify(name, group, "US", name.replace(" ", "") + ".us")[0], expected)

    def test_religious_channels_are_grouped_by_genre_in_every_country(self):
        examples = [
            ("Gospel TV", "Religious", "US", "GospelTV.us"),
            ("Sunnah TV", "Religious", "SA", "SunnahTV.sa"),
            ("MTA International", "General", "GB", "MTAInternational.uk"),
            ("Hindu Bhakti Music", "Music", "IN", "BhaktiMusic.in"),
            ("Madani TV", "General", "IN", "MadaniTV.in"),
            ("Madani TV", "Religious", "BD", "MadaniTV.bd"),
        ]
        for name, group, country, tvg_id in examples:
            with self.subTest(name=name, country=country):
                self.assertEqual(self.classify(name, group, country, tvg_id)[0], "Religious")

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

    def test_foreign_religious_channel_is_promoted_to_religious_group(self):
        source = '#EXTINF:-1 tvg-id="custom.hope-channel-proyecto-ja-cr-music" tvg-content="Music" group-title="Costa Rica" tvg-name="Hope Channel PROYECTO JA",Hope Channel PROYECTO JA'
        attrs = reorg.attrs(source)
        self.assertEqual(reorg.classify(attrs, "Hope Channel PROYECTO JA", "Costa Rica", "CR"), ("Review", None, None))

    def test_radio_brands_remain_rejected_and_religious_names_use_religious_group(self):
        for name in ("Hitradio O3", "Bel RTL", "Couleur 3", "Joe FM", "Fame95 FM"):
            with self.subTest(name=name):
                self.assertIsNone(self.classify(name, "Music", "BE", name.replace(" ", "") + ".be")[0])
        for name, code, ident in (("Hope Channel PROYECTO JA", "US", "HopeChannel.us"), ("Canal Cine Dios", "CO", "CanalCineDios.co")):
            attrs = {"group-title": "International", "tvg-country": code, "tvg-id": ident}
            self.assertIsNone(discovery.discovery_eligibility(attrs, name, allow_legacy_group=True)[0])

    def test_country_groups_are_used_for_non_genre_channels_only(self):
        self.assertEqual(self.classify("Entertainment World", "General", "BD", "EntertainmentWorld.bd")[0], "Bangladesh")
        self.assertEqual(self.classify("Entertainment World", "General", "IN", "EntertainmentWorld.in")[0], "Indian Entertainment")
        self.assertEqual(self.classify("Entertainment World", "General", "PK", "EntertainmentWorld.pk")[0], "Pakistani")
        for country, name, group, tvg_id, expected in (
            ("BD", "World News", "News", "WorldNews.bd", "News"),
            ("IN", "Aaj Tak", "News", "AajTak.in", "News"),
            ("PK", "ARY QTV", "Religious", "ARYQTV.pk", "Religious"),
            ("PK", "Pakistan Sports", "Sports", "PakistanSports.pk", "Sports"),
        ):
            with self.subTest(country=country, name=name):
                self.assertEqual(self.classify(name, group, country, tvg_id)[0], expected)

    def test_backup_queue_policy_rejects_non_movie_music_genres_worldwide(self):
        cases = [
            ("Colors Rishtey", "General", "IN", "ColorsRishtey.in"),
            ("DD Sports", "Sports", "IN", "DDSports.in"),
            ("Madani TV", "Religious", "BD", "MadaniTV.bd"),
            ("Hum TV", "General", "PK", "HumTV.pk"),
            ("ARY News", "News", "PK", "ARYNews.pk"),
        ]
        for name, group, country, tvg_id in cases:
            attrs = {"group-title": "New Backups", "tvg-country": country, "tvg-id": tvg_id}
            target, reason, verified, genre = discovery.queue_policy(attrs, name)
            with self.subTest(name=name, country=country):
                self.assertIsNone(target)
                self.assertTrue(reason)
                self.assertEqual(verified, country)

    def test_five_channel_country_threshold_is_retained(self):
        self.assertEqual(discovery.COUNTRY_THRESHOLD, 5)
        self.assertNotIn("AT", discovery.qualified_country_groups({"AT": {"a", "b", "c", "d"}}))
        self.assertIn("AT", discovery.qualified_country_groups({"AT": {"a", "b", "c", "d", "e"}}))
        # Every country except Bangladesh and India, including Pakistan, needs
        # five unique primary identities before its dedicated group is used.
        self.assertEqual(discovery.primary_target("International Movies", "AT", {"AT"}), "Austria")
        self.assertEqual(discovery.primary_target("International Music", "AT", {"AT"}), "Austria")
        self.assertEqual(discovery.primary_target("International Movies", "AT", set()), "International")
        self.assertEqual(discovery.primary_target("International Music", "DE", set()), "International")
        self.assertEqual(discovery.primary_target("International Movies", "BD", set()), "Bangladesh")
        self.assertNotIn("PK", discovery.qualified_country_groups({"PK": {"a", "b", "c", "d"}}))
        self.assertIn("PK", discovery.qualified_country_groups({"PK": {"a", "b", "c", "d", "e"}}))
        self.assertEqual(discovery.primary_target("Pakistani", "PK", set()), "International")
        self.assertEqual(discovery.primary_target("Pakistani", "PK", {"PK"}), "Pakistani")
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

        pakistan = {
            "group-title": "International",
            "tvg-country": "PK",
            "tvg-id": "HumTV.pk",
        }
        target, reason, genre = discovery.existing_international_target(
            pakistan, "Hum TV", set()
        )
        self.assertEqual((target, reason, genre), ("International", None, ""))

        target, reason, genre = discovery.existing_international_target(
            pakistan, "Hum TV", {"PK"}
        )
        self.assertEqual((target, reason, genre), ("Pakistani", None, ""))

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

    def test_review_candidate_without_authentic_logo_remains_in_queue(self):
        block = [
            '#EXTINF:-1 tvg-id="Colors.us" tvg-country="US" group-title="New Backups" tvg-content="Movies",Colors',
            "https://example.org/colors.m3u8",
        ]
        rejected = []
        with tempfile.TemporaryDirectory() as tmp, patch.object(discovery, "LOGOS", Path(tmp) / "logos"):
            kept, repaired, removed = discovery.localize_discovery_queue_logos(
                [block], {block[1]}, rejected
            )
        self.assertEqual(kept, [block])
        self.assertEqual(repaired, 0)
        self.assertEqual(removed, 0)
        self.assertEqual(rejected, [])

    def test_tokenized_urls_are_rejected_without_playback_testing(self):
        self.assertFalse(discovery.safe_url("https://example.org/live.m3u8?token=abc"))
        self.assertFalse(discovery.safe_url("https://example.org/live.m3u8?play_token=abc"))
        self.assertFalse(discovery.safe_url("https://example.org/live.m3u8?access_token=abc"))
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
        registry = discovery.category_registry(["Belarus", "International", "Albania", "Sports", "News"])
        self.assertLess(registry.index("Albania"), registry.index("Belarus"))
        self.assertLess(registry.index("Belarus"), registry.index("International"))
        self.assertLess(registry.index("International"), registry.index("News"))
        self.assertLess(registry.index("News"), registry.index("Fashion TV"))
        self.assertLess(registry.index("Fashion TV"), registry.index("Sports"))


    def test_foreign_primary_country_groups_require_explicit_movie_music_content(self):
        valid_movie = {
            "group-title": "United States", "tvg-country": "US",
            "tvg-id": "CinemaWorld.us", "tvg-content": "Movies",
        }
        valid_music = {
            "group-title": "United Kingdom", "tvg-country": "GB",
            "tvg-id": "WorldMusic.uk", "tvg-content": "Music",
        }
        self.assertEqual(
            intl_validator.foreign_movie_music_error(valid_movie, "Cinema World", "US"), ""
        )
        self.assertEqual(
            intl_validator.foreign_movie_music_error(valid_music, "World Music", "GB"), ""
        )

    def test_foreign_channels_are_allowed_in_their_genre_groups(self):
        examples = [
            ("Documentary & Wildlife", "US", "4K Travel", "custom.4k.travel"),
            ("Kids", "PL", "4 Fun Kids", "4FunKids.pl"),
            ("Sports", "TR", "A Spor", "ASpor.tr"),
            ("Religious", "SA", "Sunnah TV", "SunnahTV.sa"),
            ("News", "GB", "BBC News", "BBCNews.uk"),
        ]
        for group, country, name, tvg_id in examples:
            with self.subTest(group=group, country=country, name=name):
                attrs = {"group-title": group, "tvg-country": country, "tvg-id": tvg_id}
                self.assertEqual(intl_validator.genre_group_policy_error(attrs, name, group), "")

    def test_bangladesh_indian_and_pakistani_genre_exceptions_are_preserved(self):
        examples = [
            ("Religious", "BD", "Madani TV", "MadaniTV.bd"),
            ("Documentary & Wildlife", "BD", "Discovery Bangla", "DiscoveryBangla.bd"),
            ("Kids", "IN", "Pogo", "Pogo.in"),
            ("Sports", "IN", "DD Sports", "DDSports.in"),
            ("Religious", "PK", "ARY Qtv", "ARYQTV.pk"),
            ("Kids", "PK", "Cartoon Pakistan", "CartoonPakistan.pk"),
            ("Sports", "PK", "Pakistan Sports", "PakistanSports.pk"),
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

    def test_indian_religious_genre_group_is_allowed(self):
        attrs = {"group-title": "Religious", "tvg-country": "IN", "tvg-id": "PeaceTV.in"}
        self.assertEqual(intl_validator.genre_group_policy_error(attrs, "Peace TV", "Religious"), "")

    def test_country_group_policy_still_requires_movie_music_but_genres_are_independent(self):
        missing = {"group-title": "Pakistani", "tvg-country": "PK", "tvg-id": "HumTV.pk"}
        conflicting = {"group-title": "United States", "tvg-country": "US", "tvg-id": "CinemaWorld.us", "tvg-content": "Music"}
        non_movie_music = {"group-title": "United Kingdom", "tvg-country": "GB", "tvg-id": "WorldNews.uk", "tvg-content": "Movies"}
        self.assertEqual(intl_validator.foreign_movie_music_error(missing, "Hum TV", "PK"), "")
        self.assertNotEqual(intl_validator.foreign_movie_music_error(conflicting, "Cinema World", "US"), "")
        self.assertNotEqual(intl_validator.foreign_movie_music_error(non_movie_music, "World News", "GB"), "")
        self.assertEqual(reorg.classify({"tvg-country": "PK"}, "Pakistan News", "International", "PK"), ("News", None, None))


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
        self.assertEqual(
            legacy_repair.classify_primary_group(info("Hum TV", "PK"), "International"),
            "Pakistani",
        )
        self.assertEqual(
            legacy_repair.classify_primary_group(info("Adult Channel Alpha", "US", "Adult"), "Adult"),
            "Adult",
        )



class StrictWorldwideDiscoveryTests(unittest.TestCase):
    def eligible(self, name, genre, country, tvg_id):
        attrs = {"group-title": genre, "tvg-country": country, "tvg-id": tvg_id}
        return discovery.discovery_eligibility(attrs, name)

    def test_movie_and_music_discovery_is_allowed_for_all_countries(self):
        for country, tvg_id in (("BD", "Cinema.bd"), ("IN", "Cinema.in"), ("PK", "Cinema.pk"), ("US", "Cinema.us")):
            with self.subTest(country=country):
                target, reason, verified = self.eligible("Cinema World", "Movies", country, tvg_id)
                self.assertIsNone(reason)
                self.assertEqual(verified, country)
                self.assertIsNotNone(target)
        for country, tvg_id in (("BD", "Music.bd"), ("IN", "Music.in"), ("PK", "Music.pk"), ("GB", "Music.uk")):
            with self.subTest(country=country):
                target, reason, verified = self.eligible("World Music", "Music", country, tvg_id)
                self.assertIsNone(reason)
                self.assertEqual(verified, country)
                self.assertIsNotNone(target)

    def test_missing_country_metadata_does_not_reject_clear_movie_music_candidate(self):
        attrs = {"group-title": "Movies", "tvg-id": "CinemaChannel"}
        target, reason, code = discovery.discovery_eligibility(attrs, "Cinema Channel")
        self.assertIsNone(reason)
        self.assertEqual(code, "ZZ")
        self.assertEqual(target, "International Movies")

    def test_general_source_category_is_rejected_even_if_name_suggests_movies(self):
        for country, ident in (("BD", "Cinema.bd"), ("IN", "Cinema.in"), ("PK", "Cinema.pk")):
            attrs = {"group-title": "Entertainment", "tvg-country": country, "tvg-id": ident}
            target, reason, _ = discovery.discovery_eligibility(attrs, "Cinema World")
            with self.subTest(country=country):
                self.assertIsNone(target)
                self.assertEqual(reason, "source category is not Movies or Music")

    def test_non_movie_music_genres_are_rejected_worldwide(self):
        cases = [
            ("World News", "News", "BD", "WorldNews.bd"),
            ("Madani TV", "Religious", "PK", "MadaniTV.pk"),
            ("Pogo", "Kids", "IN", "Pogo.in"),
            ("DD Sports", "Sports", "IN", "DDSports.in"),
            ("Discovery Channel", "Documentary", "US", "Discovery.us"),
            ("General Entertainment", "Entertainment", "BD", "General.bd"),
        ]
        for name, genre, country, tvg_id in cases:
            with self.subTest(name=name, country=country):
                target, reason, _ = self.eligible(name, genre, country, tvg_id)
                self.assertIsNone(target)
                self.assertTrue(reason)

    def test_fashion_tv_is_allowed_as_an_explicit_global_exception(self):
        attrs = {"group-title": "Fashion", "tvg-country": "FR", "tvg-id": "FashionTV.fr"}
        target, reason, code = discovery.discovery_eligibility(attrs, "Fashion TV")
        self.assertEqual((target, reason, code), ("Fashion TV", None, "FR"))
        queued_target, queued_reason, queued_code, _ = discovery.queue_policy(attrs, "Fashion TV")
        self.assertEqual((queued_target, queued_reason, queued_code), ("Fashion TV", None, "FR"))

    def test_adult_channels_are_allowed_directly_in_adult_group_worldwide(self):
        examples = [
            ("Adult Channel", "Adult", "US", "AdultChannel.us"),
            ("Playboy TV", "Movies", "GB", "PlayboyTV.uk"),
            ("Penthouse", "Adult", "FR", "Penthouse.fr"),
            ("XXX Network", "XXX", "IN", "XXXNetwork.in"),
            ("Erotic TV", "Entertainment", "BD", "EroticTV.bd"),
        ]
        for name, genre, country, tvg_id in examples:
            with self.subTest(name=name, country=country):
                attrs = {"group-title": genre, "tvg-country": country, "tvg-id": tvg_id}
                target, reason, verified = discovery.discovery_eligibility(attrs, name)
                self.assertIsNone(reason)
                self.assertEqual(target, "Adult")
                self.assertEqual(verified, country)

    def test_adult_swim_is_not_misclassified_as_adult_content(self):
        attrs = {"group-title": "Entertainment", "tvg-country": "US", "tvg-id": "AdultSwim.us"}
        target, reason, _ = discovery.discovery_eligibility(attrs, "Adult Swim")
        self.assertIsNone(target)
        self.assertTrue(reason)

    def test_missing_local_logo_does_not_remove_review_candidate(self):
        block = ['#EXTINF:-1 tvg-name="Cinema World" group-title="New Channels",Cinema World', "https://example.org/cinema.m3u8"]
        with tempfile.TemporaryDirectory() as tmp, patch.object(discovery, "LOGOS", Path(tmp) / "logos"):
            kept, repaired, removed = discovery.localize_discovery_queue_logos([block], {block[1]}, [])
        self.assertEqual(len(kept), 1)
        self.assertEqual((repaired, removed), (0, 0))

if __name__ == "__main__":
    unittest.main()
