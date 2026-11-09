import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from probe_amazeyourself_epg import (  # noqa: E402
    find_exact_matches,
    markdown_cell,
    normalize_name,
    parse_playlist_text,
    parse_xmltv_datetime,
)


class ExternalEpgProbeTests(unittest.TestCase):
    def test_normalize_name_only_removes_formatting_and_quality_suffix(self):
        self.assertEqual(normalize_name("Channel 24 HD"), "channel24")
        self.assertEqual(normalize_name("  OLI-TV "), "olitv")
        self.assertNotEqual(normalize_name("News 24"), normalize_name("News 21"))

    def test_markdown_report_preserves_zero_counts(self):
        self.assertEqual(markdown_cell(0), "0")

    def test_parse_kableone_timestamp_with_t_separator(self):
        value = parse_xmltv_datetime("20261109T040000 +0530")
        self.assertEqual(value, datetime(2026, 11, 8, 22, 30, tzinfo=timezone.utc))

    def test_parse_neotv_timestamp_with_colon_offset(self):
        value = parse_xmltv_datetime("20261109004152 +00:00")
        self.assertEqual(value, datetime(2026, 11, 9, 0, 41, 52, tzinfo=timezone.utc))

    def test_reject_timestamp_without_explicit_timezone(self):
        self.assertIsNone(parse_xmltv_datetime("20261109004152"))

    def test_playlist_parser_excludes_review_and_retains_active_channel(self):
        playlist = """#EXTM3U
#EXTINF:-1 tvg-id="Channel24.bd" tvg-name="Channel 24 HD" group-title="Bangladesh" tvg-country="BD",Channel 24
https://example.test/channel24.m3u8
#EXTINF:-1 tvg-id="ReviewOnly.bd" tvg-name="Review Only" group-title="Review",Review Only
https://example.test/review.m3u8
"""
        channels = parse_playlist_text(playlist, "test.m3u")
        self.assertIn("Channel24.bd", channels)
        self.assertNotIn("ReviewOnly.bd", channels)

    def test_exact_name_match_requires_a_unique_playlist_identity(self):
        playlist = """#EXTM3U
#EXTINF:-1 tvg-id="Channel24.bd" tvg-name="Channel 24" group-title="Bangladesh" tvg-country="BD",Channel 24
https://example.test/one.m3u8
#EXTINF:-1 tvg-id="Other.bd" tvg-name="Other Channel" group-title="Bangladesh" tvg-country="BD",Other Channel
https://example.test/two.m3u8
"""
        targets = parse_playlist_text(playlist, "test.m3u")
        feed_channels = {"channel-24": ["Channel 24 HD"]}
        counts = {"channel-24": {"valid": 3, "window": 3}}
        matches, ambiguous = find_exact_matches(feed_channels, counts, targets)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["playlist_id"], "Channel24.bd")
        self.assertTrue(matches[0]["bangladesh"])
        self.assertEqual(ambiguous, [])

    def test_ambiguous_names_are_not_auto_matched(self):
        playlist = """#EXTM3U
#EXTINF:-1 tvg-id="Channel24.bd" tvg-name="Channel 24" group-title="Bangladesh" tvg-country="BD",Channel 24
https://example.test/one.m3u8
#EXTINF:-1 tvg-id="Channel24.uk" tvg-name="Channel 24" group-title="United Kingdom" tvg-country="GB",Channel 24
https://example.test/two.m3u8
"""
        targets = parse_playlist_text(playlist, "test.m3u")
        # Merge the two playlist identities as load_playlist_channels() does.
        targets["Channel24.uk"] = {
            "id": "Channel24.uk",
            "names": {"Channel 24"},
            "groups": {"United Kingdom"},
            "countries": {"GB"},
            "playlists": {"test.m3u"},
        }
        feed_channels = {"channel-24": ["Channel 24"]}
        counts = {"channel-24": {"valid": 1, "window": 1}}
        matches, ambiguous = find_exact_matches(feed_channels, counts, targets)
        self.assertEqual(matches, [])
        self.assertEqual(len(ambiguous), 1)


if __name__ == "__main__":
    unittest.main()
