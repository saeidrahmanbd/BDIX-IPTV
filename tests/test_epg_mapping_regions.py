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

    def test_coverage_and_generator_share_the_same_region_policy(self):
        self.assertIs(epg_coverage.mapping_id_region_compatible, mapping_id_region_compatible)
        self.assertIs(generate_epg.mapping_id_region_compatible, mapping_id_region_compatible)


if __name__ == "__main__":
    unittest.main()
