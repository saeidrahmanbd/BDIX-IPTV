"""Regression tests for regional EPG source-ID mapping."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from epg_mapping_policy import mapping_id_region_compatible
import epg_coverage
import generate_epg


INDIA_FEED = "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz"


class EpgMappingRegionTests(unittest.TestCase):
    def test_foreign_country_suffix_is_rejected_even_on_exact_id_match(self):
        self.assertFalse(mapping_id_region_compatible("US", "IN", {"IN"}))

    def test_unqualified_numeric_id_from_a_foreign_regional_feed_is_rejected(self):
        self.assertFalse(mapping_id_region_compatible("US", "", {"IN"}))

    def test_id_suffix_matching_the_target_is_authoritative_in_a_mixed_feed(self):
        self.assertTrue(mapping_id_region_compatible("US", "US", {"IN"}))

    def test_target_and_source_id_with_same_region_are_accepted(self):
        self.assertTrue(mapping_id_region_compatible("IN", "IN", {"US"}))

    def test_explicit_curated_global_alias_overrides_region_mismatch(self):
        self.assertTrue(mapping_id_region_compatible("US", "GB", {"GB"}, explicit_override=True))

    def test_coverage_builder_rejects_discovery_channel_india_id_for_us_target(self):
        channel = {"tvg_id": "DiscoveryChannel.us", "country": "US"}
        self.assertFalse(epg_coverage.source_id_mapping_compatible(
            channel, "DISCOVERY.CHANNEL.in", INDIA_FEED
        ))
        self.assertFalse(epg_coverage.source_id_mapping_compatible(
            channel, "100869", INDIA_FEED
        ))

    def test_generator_rejects_discovery_channel_india_id_for_us_target(self):
        countries = {"DiscoveryChannel.us": "US"}
        self.assertFalse(generate_epg.source_mapping_id_compatible(
            "DiscoveryChannel.us", "DISCOVERY.CHANNEL.in", INDIA_FEED, countries
        ))
        self.assertFalse(generate_epg.source_mapping_id_compatible(
            "DiscoveryChannel.us", "100869", INDIA_FEED, countries
        ))

    def test_verified_global_aliases_remain_available(self):
        countries = {"TravelxpEnglish.us": "US", "WorldWarTV.us": "US"}
        uk_feed = "https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz"
        self.assertTrue(generate_epg.source_mapping_id_compatible(
            "TravelxpEnglish.us", "Travelxp.uk", uk_feed, countries
        ))
        self.assertTrue(generate_epg.source_mapping_id_compatible(
            "WorldWarTV.us", "WorldWarTV.uk", uk_feed, countries
        ))

    def test_m3u_edit_targeted_feeds_have_explicit_regions(self):
        cases = {
            "BG1.xml.gz": "BG",
            "FR1.xml.gz": "FR",
            "HU1.xml.gz": "HU",
            "ID1.xml.gz": "ID",
            "LT1.xml.gz": "LT",
            "UA1.xml.gz": "UA",
            "US2.xml.gz": "US",
        }
        for filename, country in cases.items():
            with self.subTest(filename=filename):
                url = f"https://m3u-edit.com/epg-source.php?file={filename}"
                self.assertEqual(generate_epg.source_country_codes(url), {country})

    def test_global_provider_feeds_are_not_assigned_a_country(self):
        for filename in ("BEIN1.xml.gz", "PLEX1.xml.gz"):
            with self.subTest(filename=filename):
                url = f"https://m3u-edit.com/epg-source.php?file={filename}"
                self.assertEqual(generate_epg.source_country_codes(url), set())

    def test_targeted_discovery_feeds_are_retained_for_custom_playlist_ids(self):
        self.assertIn(
            "https://m3u-edit.com/epg-source.php?file=UA1.xml.gz",
            generate_epg.TARGETED_DISCOVERY_SOURCES,
        )
        self.assertIn(
            "https://m3u-edit.com/epg-source.php?file=PLEX1.xml.gz",
            generate_epg.TARGETED_DISCOVERY_SOURCES,
        )

    def test_bhi_channel_news_is_excluded_from_iptv_playlist(self):
        playlist = (ROOT / "IPTV-Playlist.m3u").read_text(encoding="utf-8")
        entries = [
            line for line in playlist.splitlines()
            if line.startswith("#EXTINF:") and 'tvg-id="BHI.Channel.in"' in line
        ]
        self.assertEqual(entries, [], "Indian News BHI Channel must not remain in the IPTV playlist")
    def test_new_channel_aliases_point_to_catalogued_source_ids(self):
        self.assertEqual(
            epg_coverage.EPG_ALIASES["custom.mggtv"],
            ["MGG.TV.fr"],
        )
        self.assertEqual(
            epg_coverage.EPG_ALIASES["custom.sport2ukraine"],
            ["Sport.2.[UA-RU].ua", "Sport.2.[UA-UA].ua"],
        )

    def test_coverage_and_generator_share_the_same_region_policy(self):
        self.assertIs(epg_coverage.mapping_id_region_compatible, mapping_id_region_compatible)
        self.assertIs(generate_epg.mapping_id_region_compatible, mapping_id_region_compatible)


if __name__ == "__main__":
    unittest.main()
