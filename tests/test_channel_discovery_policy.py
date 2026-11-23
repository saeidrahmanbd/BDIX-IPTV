import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from discover_bd_in_new_queues import (
    PERMANENTLY_BANNED_CHANNEL_NAMES, PERMANENTLY_BANNED_CHANNEL_IDS, canonical_channel_name,
    evaluate, extinf, explicit_foreign_country, prohibited_channel, purge_forbidden_existing_queue_rows,
    is_indian_discovery_candidate, known_indian_forbidden_category,
    normalize_queue_logo, normalize_existing_queue_roles, channel_identity_keys,
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
            "XXTreme Jobs Hindi", "Power Turk",
            "Safari TV Tamil (Not 24/7)", "CVR Health", "Vokta TV (720p)",
        ]
        self.assertEqual(len(PERMANENTLY_BANNED_CHANNEL_NAMES), 44)
        self.assertEqual(len(PERMANENTLY_BANNED_CHANNEL_IDS), 32)
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
            ("XXTremeJobsHindi.in@SD", "XXTreme Jobs alternate"),
            ("PowerTurkTV.tr@HD", "Power Turk alternate"),
            ("CVRHealth.in@SD", "Renamed CVR Health feed"),
            ("VoktaTV.bd@SD", "Renamed Vokta TV feed"),
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

    def test_explicit_foreign_country_is_rejected_even_when_name_matches_indian_alias(self):
        attrs = {"tvg-country": "US", "tvg-id": "Doraemon.us@SD", "group-title": "New Channels"}
        self.assertEqual(
            prohibited_channel(attrs, "Doraemon", iptv_discovery=True),
            "channel country US is outside Bangladesh/India",
        )

    def test_explicit_foreign_ids_are_rejected_even_when_listed_in_bd_feed(self):
        examples = [
            ("BTLTV.nl@SD", "BTL TV", "NL", "BD"),
            ("CartoonNetwork.pk@SD", "Cartoon Network", "PK", "BD"),
            ("QelloConcertsbyStingray.ca@SD", "Qello Concerts by Stingray", "CA", "IN"),
        ]
        for channel_id, name, country, source in examples:
            with self.subTest(channel_id=channel_id):
                attrs = {"tvg-id": channel_id, "x-discovery-source-country": source}
                self.assertEqual(explicit_foreign_country(attrs, name), country)
                self.assertIn("outside Bangladesh/India", prohibited_channel(
                    attrs, name, source, discovery=True, iptv_discovery=True
                ))

    def test_regional_diaspora_channel_with_ca_id_is_not_rejected_from_india_feed(self):
        attrs = {"tvg-id": "GaundaPunjabTV.ca@SD", "x-discovery-source-country": "IN"}
        self.assertIsNone(explicit_foreign_country(attrs, "Gaunda Punjab TV"))
        self.assertTrue(is_indian_discovery_candidate(attrs, "Gaunda Punjab TV"))
        self.assertIsNone(prohibited_channel(
            attrs, "Gaunda Punjab TV", "IN", discovery=True, iptv_discovery=True
        ))

    def test_indian_id_suffix_applies_indian_discovery_rules_even_in_bd_source_feed(self):
        for channel_id, name in [
            ("NationalGeographic.in@HD", "National Geographic"),
            ("NationalGeographicWild.in@HD", "National Geographic Wild"),
            ("AnimalPlanet.in@SD", "Animal Planet"),
            ("DiscoveryChannel.in@HD", "Discovery Channel"),
            ("HistoryTV18.in@HD", "History TV18"),
            ("DiscoveryTurbo.in@HD", "Discovery Turbo India"),
        ]:
            with self.subTest(channel_id=channel_id):
                attrs = {"tvg-id": channel_id, "x-discovery-source-country": "BD"}
                self.assertTrue(is_indian_discovery_candidate(attrs, name))
                self.assertIsNone(prohibited_channel(attrs, name, "BD", discovery=True, iptv_discovery=True))
        attrs = {"tvg-id": "NickJr.in@SD", "x-discovery-source-country": "BD"}
        self.assertTrue(is_indian_discovery_candidate(attrs, "Nick Jr."))
        self.assertIn("kids", prohibited_channel(
            attrs, "Nick Jr.", "BD", discovery=True, iptv_discovery=True
        ))

    def test_queue_country_metadata_uses_explicit_id_before_source_feed(self):
        line = extinf(
            {"tvg-id": "NationalGeographic.in@HD", "tvg-name": "National Geographic"},
            "National Geographic", "New Channels", "BD",
        )
        self.assertIn('tvg-country="IN"', line)

    def test_foreign_country_queue_rows_are_purged(self):
        text = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-id="BTLTV.nl@SD" x-discovery-source-country="BD" group-title="New Channels",BTL TV\n'
            "https://example.org/btl.m3u8\n"
            '#EXTINF:-1 tvg-id="ValidBD.bd@SD" x-discovery-source-country="BD" group-title="New Channels",Valid BD\n'
            "https://example.org/valid-bd.m3u8\n"
        )
        filtered, removed = purge_forbidden_existing_queue_rows(text)
        self.assertEqual(removed, ["BTL TV"])
        self.assertNotIn("BTL TV", filtered)
        self.assertIn("Valid BD", filtered)

    def test_indian_id_suffix_catches_conflict_with_stale_foreign_country(self):
        attrs = {"tvg-country": "US", "tvg-id": "DisneyChannel.in@HD", "group-title": "Backup"}
        self.assertIsNotNone(prohibited_channel(attrs, "Disney Channel", iptv_discovery=True))

    def test_indian_channel_id_overrides_source_feed_for_indian_exclusion_policy(self):
        attrs = {"x-discovery-source-country": "BD", "tvg-country": "IN", "tvg-id": "DisneyChannel.in@HD"}
        reason = prohibited_channel(attrs, "Disney Channel", "BD", iptv_discovery=True)
        self.assertIn("kids", reason)

    def test_indian_islamic_religious_channels_are_allowed_for_iptv_policy(self):
        examples = [
            ("Islamic TV", "SampleChannel.in"),
            ("Q TV", "QTV.in"),
            ("Madani TV", "MadaniTV.in"),
            ("Peace TV", "PeaceTV.in"),
            ("Quran TV", "QuranTV.in"),
            ("Al Huda", "AlHuda.in"),
        ]
        for name, channel_id in examples:
            attrs = {"group-title": "Religious", "tvg-country": "IN", "tvg-id": channel_id}
            with self.subTest(name=name):
                self.assertIsNone(prohibited_channel(attrs, name, iptv_discovery=True))

    def test_indian_kids_are_rejected_for_new_discovery(self):
        for name, group in [
            ("Kids TV", "Kids"), ("Cartoon Network", "Entertainment"),
            ("Green Gold TV", "Entertainment"), ("Pogo", "Entertainment"),
            ("Disney Channel", "Kids"),
        ]:
            with self.subTest(name=name, group=group):
                attrs = {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"}
                self.assertIsNotNone(prohibited_channel(attrs, name, iptv_discovery=True))

    def test_indian_sports_and_documentary_knowledge_are_allowed_but_business_education_remain_rejected(self):
        for name, group in [
            ("Star Sports", "Sports"), ("Sony Sports Ten 1 HD", "Entertainment"),
            ("Unite8 Sports 1", "Entertainment"), ("Kabaddi 24x7", "Entertainment"),
            ("Pickleball Now", "Entertainment"), ("Eurosport India", "Entertainment"),
            ("Cricket 24", "Cricket"), ("Football Live", "Football"),
            ("Discovery Channel", "Knowledge"), ("National Geographic", "Documentary"),
            ("National Geographic Wild", "Documentary"), ("Animal Planet", "Entertainment"),
            ("History TV18", "Documentary"), ("Discovery Turbo India", "Documentary"),
        ]:
            attrs = {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"}
            with self.subTest(name=name, group=group):
                self.assertIsNone(prohibited_channel(attrs, name, iptv_discovery=True))
        for name, group in [
            ("Corporate Channel", "Business"), ("Money TV", "Finance"),
            ("Education TV", "Education"), ("Krishi Darshan", "Agriculture"),
        ]:
            attrs = {"group-title": group, "tvg-country": "IN", "tvg-id": "SampleChannel.in"}
            with self.subTest(name=name, group=group):
                self.assertIsNotNone(prohibited_channel(attrs, name, iptv_discovery=True))

    def test_bangladesh_channels_of_prohibited_indian_genres_remain_eligible(self):
        for name, group in [
            ("Bangla News", "News"), ("Bangla Sports", "Sports"), ("Kids Bangla", "Kids"),
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

    def test_existing_indian_sports_queue_rows_are_preserved(self):
        text = (
            "#EXTM3U\\n"
            '#EXTINF:-1 tvg-name="Sony Sports Ten 1" tvg-country="IN" group-title="New Channels",Sony Sports Ten 1\\n'
            "https://example.org/sony-sports.m3u8\\n"
            '#EXTINF:-1 tvg-name="Kabaddi 24x7" tvg-country="IN" group-title="New Backups",Kabaddi 24x7\\n'
            "https://example.org/kabaddi.m3u8\\n"
            '#EXTINF:-1 tvg-name="T Sports" tvg-country="BD" group-title="New Backups",T Sports\\n'
            "https://example.org/t-sports.m3u8\\n"
        )
        filtered, removed = purge_forbidden_existing_queue_rows(text)
        self.assertEqual(removed, [])
        self.assertIn("Sony Sports Ten 1", filtered)
        self.assertIn("Kabaddi 24x7", filtered)
        self.assertIn("T Sports", filtered)

    def test_existing_queue_roles_are_normalized_by_channel_identity(self):
        text = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-id="ApnaPunjabTV.ca@SD" tvg-name="Apna Punjab TV" group-title="Indian Entertainment",Apna Punjab TV\n'
            "https://example.org/apna-primary.m3u8\n"
            '#EXTINF:-1 tvg-id="ApnaPunjabTV.in@HD" tvg-name="Apna Punjab TV (India) HD" group-title="New Backups",Apna Punjab TV (India) HD\n'
            "https://example.org/apna-alt.m3u8\n"
            '#EXTINF:-1 tvg-id="Existing.in" tvg-name="Existing Channel" group-title="Indian Entertainment",Existing Channel\n'
            "https://example.org/existing-primary.m3u8\n"
            '#EXTINF:-1 tvg-id="Existing.in@HD" tvg-name="Existing Channel HD" group-title="New Channels",Existing Channel HD\n'
            "https://example.org/existing-alt.m3u8\n"
            '#EXTINF:-1 tvg-id="SonyMax.in@HD" tvg-name="Sony Max HD" group-title="New Backups",Sony Max HD\n'
            "https://example.org/sony-max.m3u8\n"
            '#EXTINF:-1 tvg-id="SonyMax.in@SD" tvg-name="Sony Max (720p)" group-title="New Backups",Sony Max (720p)\n'
            "https://example.org/sony-max-alt.m3u8\n"
        )
        normalized, moved_to_channels, moved_to_backups, removed = normalize_existing_queue_roles(text)
        self.assertEqual(moved_to_channels, ["Sony Max HD"])
        self.assertEqual(moved_to_backups, ["Existing Channel HD"])
        self.assertEqual(removed, ["Sony Max (720p)"])
        self.assertIn('group-title="New Backups",Apna Punjab TV (India) HD', normalized)
        self.assertIn('group-title="New Backups",Existing Channel HD', normalized)
        self.assertIn('group-title="New Channels",Sony Max HD', normalized)
        self.assertNotIn("Sony Max (720p)", normalized)
        self.assertIn("name:apnapunjabtv", channel_identity_keys({"tvg-id":"ApnaPunjabTV.in@HD"}, "Apna Punjab TV (India) HD"))

    def test_queue_logo_normalizer_keeps_only_existing_local_repository_assets(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "logos"
            root.mkdir()
            (root / "broadcaster.png").write_bytes(b"authentic-local-logo")
            raw = (
                '#EXTINF:-1 tvg-name="Broadcaster" '
                'tvg-logo="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/broadcaster.png" '
                'group-title="New Channels",Broadcaster'
            )
            normalized = normalize_queue_logo(raw, root)
            self.assertIn('tvg-logo="logos/broadcaster.png"', normalized)
            missing = raw.replace("broadcaster.png", "missing.png")
            self.assertNotIn("tvg-logo=", normalize_queue_logo(missing, root))
            external = raw.replace(
                "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/broadcaster.png",
                "https://example.net/placeholder.png",
            )
            self.assertNotIn("tvg-logo=", normalize_queue_logo(external, root))

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

    def test_known_indian_news_kids_non_islamic_religious_and_vtu_aliases_are_rejected(self):
        examples = [
            ("TV 100", {"tvg-id": "TV100.in@SD"}, "news"),
            ("R Plus", {"tvg-id": "RPlus.in@SD"}, "news"),
            ("Sony Yay!", {"tvg-id": "SonyYay.in@SD"}, "kids"),
            ("Disha TV", {"tvg-id": "DishaTV.in@SD"}, "religious"),
            ("VTU", {"tvg-id": "VTU.in@SD"}, "education"),
            ("Disha TV", {}, "religious"),
            ("BHI Channel", {"tvg-id": "BHI.Channel.in"}, "news"),
            ("Shekinah TV", {"tvg-id": "ShekinahTV.in@SD"}, "religious"),
            ("Disney Channel", {"tvg-id": "DisneyChannel.in@HD"}, "kids"),
            ("CVR Health", {"tvg-id": "CVRHealth.in@SD"}, "knowledge"),
        ]
        self.assertIsNone(known_indian_forbidden_category(
            {"tvg-id": "RPlusGold.in@SD", "tvg-country": "IN"}, "R Plus Gold"
        ))
        self.assertIsNone(prohibited_channel(
            {"tvg-id": "RPlusGold.in@SD", "tvg-country": "IN", "group-title": "Indian Bangla"},
            "R Plus Gold", iptv_discovery=True
        ))
        for name, extra, category in examples:
            attrs = {"group-title": "General", **extra}
            with self.subTest(name=name, extra=extra):
                reason = prohibited_channel(attrs, name, iptv_discovery=True)
                self.assertIsNotNone(reason)
                if name == "CVR Health":
                    self.assertEqual(reason, "permanently banned channel")
                else:
                    self.assertIn(category, reason)
                self.assertEqual(known_indian_forbidden_category(attrs, name), category)

    def test_cvr_health_and_vokta_tv_are_permanently_rejected_and_purged(self):
        examples = [("CVR Health (576p)", "CVRHealth.in@SD"), ("Vokta TV (720p)", "voktatv.bd@SD")]
        for name, channel_id in examples:
            with self.subTest(name=name):
                attrs = {"tvg-id": channel_id, "group-title": "New Channels"}
                self.assertEqual(prohibited_channel(attrs, name), "permanently banned channel")
        queue = "#EXTM3U\n"
        for name, channel_id in examples:
            queue += '#EXTINF:-1 tvg-id="' + channel_id + '" group-title="New Channels",' + name + '\n'
            queue += 'https://example.org/' + channel_id + '.m3u8\n'
        filtered, removed = purge_forbidden_existing_queue_rows(queue)
        self.assertEqual(removed, [name for name, _ in examples])
        self.assertNotIn("CVR Health", filtered)
        self.assertNotIn("Vokta TV", filtered)
    def test_cvr_health_is_rejected_as_indian_knowledge_and_purged_from_queue(self):
        attrs = {"tvg-id": "CVRHealth.in@SD", "group-title": "New Channels"}
        candidate, reason = evaluate(
            "India", attrs, "CVR Health (576p)", "https://example.org/cvrhealth.m3u8"
        )
        self.assertIsNone(candidate)
        self.assertEqual(reason, "permanently banned channel")

        queue = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-id="CVRHealth.in@SD" group-title="New Channels",CVR Health (576p)\n'
            "https://example.org/cvrhealth.m3u8\n"
        )
        filtered, removed = purge_forbidden_existing_queue_rows(queue)
        self.assertEqual(removed, ["CVR Health (576p)"])
        self.assertNotIn("CVR Health", filtered)
    def test_indian_identity_uses_source_then_country_then_known_alias(self):
        self.assertTrue(is_indian_discovery_candidate({"tvg-id": "DishaTV.in@SD"}, "Disha TV"))
        self.assertTrue(is_indian_discovery_candidate(
            {"tvg-country": "BD", "tvg-id": "DishaTV.in@SD"}, "Disha TV"
        ))
        self.assertTrue(is_indian_discovery_candidate(
            {"x-discovery-source-country": "BD", "tvg-id": "SonyYay.in@SD"}, "Sony Yay!"
        ))
        self.assertIn("kids", prohibited_channel(
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
        })
        self.assertIn("Discovery Channel (India) HD (1080p)", filtered)
        self.assertIn("History TV18 HD (1080p)", filtered)
        self.assertIn("Safari TV (576p)", filtered)
        self.assertIn("Channel 24", filtered)

    def test_iptv_evaluate_uses_india_source_country_despite_misleading_metadata(self):
        attrs = {"tvg-country": "US", "tvg-id": "VyasChannel.us", "group-title": "General"}
        candidate, reason = evaluate(
            "India", attrs, "Vyas Channel", "https://example.org/vyas.m3u8"
        )
        self.assertIsNone(candidate)
        self.assertIn("education", reason)


    def test_non_islamic_indian_religious_channels_are_rejected(self):
        for name in ("Aastha", "Disha TV", "Shekinah TV", "Santvani Channel", "Calvary TV"):
            attrs = {"group-title": "Religious", "tvg-country": "IN", "tvg-id": "SampleChannel.in"}
            with self.subTest(name=name):
                self.assertIsNotNone(prohibited_channel(attrs, name, iptv_discovery=True))


    def test_indian_sports_are_allowed_even_with_country_metadata_mismatch(self):
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
                self.assertIsNotNone(candidate, reason)

    def test_indian_cricket_and_football_sports_channels_are_allowed(self):
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
                self.assertIsNotNone(candidate, reason)

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

    def test_explicit_pakistani_queue_rows_are_purged_from_iptv_discovery(self):
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
        self.assertEqual(removed, ["ARY Music", "Madani Channel", "Gopal Bhar"])
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


    def test_existing_indian_kids_remain_allowed_in_curated_playlist(self):
        playlist = (Path(__file__).resolve().parents[1] / "IPTV-Playlist.m3u").read_text(encoding="utf-8")
        expected = ["Disney Channel", "Green Gold TV", "WOW Kidz Hindi", "WOW Kidz Tamil", "WOW Kidz Telugu", "ZB Cartoon"]
        for name in expected:
            with self.subTest(name=name):
                self.assertRegex(playlist, rf'tvg-name="{re.escape(name)}".*group-title="Kids"|group-title="Kids".*tvg-name="{re.escape(name)}"')
                attrs = {"tvg-id": "SampleChannel.in", "tvg-country": "IN", "group-title": "Kids"}
                self.assertIsNone(prohibited_channel(attrs, name))
                self.assertIn("kids", prohibited_channel(attrs, name, iptv_discovery=True))

    def test_bollywood_old_is_consolidated_under_hindi_movie_classic_and_not_rediscovered(self):
        from stream_url_identity import stream_endpoint_family_key
        a = {"tvg-id": "mov.bollywood.old.in", "channel-id": "mov.bollywood.old.in"}
        b = {"tvg-id": "new.hindi.movie.classic.24", "channel-id": "new.hindi.movie.classic.24"}
        self.assertTrue(channel_identity_keys(a, "Bollywood OLD") & channel_identity_keys(b, "Hindi Movie Classic 24"))
        url_old = "https://vods2.aynaott.com/hindimovies/tracks-v1a1/mono.ts.m3u8"
        url_master = "https://vods2.aynaott.com/hindimovies/index.m3u8"
        self.assertEqual(stream_endpoint_family_key(url_old), stream_endpoint_family_key(url_master))

        playlist = (Path(__file__).resolve().parents[1] / "IPTV-Playlist.m3u").read_text(encoding="utf-8")
        rows = parse(playlist)
        matching = [(attrs, name, url) for attrs, name, url in rows
                    if channel_identity_keys(attrs, name) & channel_identity_keys(a, "Bollywood OLD")]
        self.assertEqual(len(matching), 1)
        attrs, name, url = matching[0]
        self.assertEqual(name, "Hindi Movie Classic 24")
        self.assertEqual(attrs.get("tvg-name"), "Hindi Movie Classic 24")
        self.assertEqual(url, url_master)
        self.assertEqual(attrs.get("group-title"), "Indian Movies")

    def test_r_plus_gold_is_not_classified_as_indian_news(self):
        attrs = {"tvg-id": "RPlusGold.in@SD", "channel-id": "RPlusGold.in@SD", "tvg-country": "IN", "tvg-language": "ben", "group-title": "Indian Bangla"}
        self.assertIsNone(known_indian_forbidden_category(attrs, "R Plus Gold"))
        self.assertIsNone(prohibited_channel(attrs, "R Plus Gold", iptv_discovery=True))
        playlist = (Path(__file__).resolve().parents[1] / "IPTV-Playlist.m3u").read_text(encoding="utf-8")
        self.assertRegex(playlist, r'tvg-name="R Plus Gold".*group-title="Indian Bangla"|group-title="Indian Bangla".*tvg-name="R Plus Gold"')



if __name__ == "__main__":
    unittest.main()
