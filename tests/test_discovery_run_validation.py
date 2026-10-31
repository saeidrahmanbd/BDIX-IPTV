import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_discovery_run import NEWS_RE, append_section, classify_response, consolidate_international_country_groups, ensure_local_logo, parse_playlist


class DiscoveryRunValidationTests(unittest.TestCase):
    def test_news_filter_does_not_misclassify_ndtv_good_times(self):
        self.assertFalse(NEWS_RE.search("NDTV Good Times"))
        self.assertTrue(NEWS_RE.search("NDTV 24x7"))

    def test_hls_manifest_is_verified(self):
        status, _ = classify_response(200, {"Content-Type": "application/vnd.apple.mpegurl"}, b"#EXTM3U\n#EXT-X-VERSION:3\n", "https://example.test/live.m3u8")
        self.assertEqual(status, "verified")

    def test_dash_manifest_is_verified(self):
        status, _ = classify_response(200, {"Content-Type": "application/dash+xml"}, b"<MPD></MPD>", "https://example.test/live.mpd")
        self.assertEqual(status, "verified")

    def test_not_found_is_dead(self):
        self.assertEqual(classify_response(404, {}, b"", "https://example.test/dead.m3u8")[0], "dead")

    def test_access_denied_is_unknown_not_dead(self):
        self.assertEqual(classify_response(403, {}, b"", "https://example.test/live.m3u8")[0], "unknown")

    def test_html_error_page_is_not_a_live_stream(self):
        self.assertEqual(classify_response(200, {"Content-Type": "text/html"}, b"<html>error</html>", "https://example.test/live.m3u8")[0], "dead")

    def test_final_validation_keeps_stream_verification_section(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "report.md"
            report.write_text("# Report\\n\\n## Stream verification\\n\\n- Verified streams: 2\\n", encoding="utf-8")
            append_section(report, "Final validation", "- Validation status: PASS")
            content = report.read_text(encoding="utf-8")
            self.assertIn("## Stream verification", content)
            self.assertIn("Verified streams: 2", content)
            self.assertIn("## Final validation", content)

    def test_country_group_is_promoted_when_five_primary_identities_exist_after_probe(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "International-Playlist.m3u"
            rows = [
                f'#EXTINF:-1 tvg-id="MK{i}.mk" tvg-country="MK" group-title="North Macedonia",MK {i}\nhttps://example.org/mk{i}.m3u8'
                for i in range(4)
            ]
            rows.append('#EXTINF:-1 tvg-id="MK5.mk" tvg-country="MK" group-title="New Channels",MK 5\nhttps://example.org/mk5.m3u8')
            playlist.write_text("#EXTM3U\n" + "\n".join(rows) + "\n", encoding="utf-8")
            moved = consolidate_international_country_groups(playlist)
            content = playlist.read_text(encoding="utf-8")
            self.assertEqual(len(moved), 1)
            self.assertEqual(content.count('group-title="North Macedonia"'), 5)
            self.assertNotIn('group-title="New Channels"', content)

    def test_country_group_below_five_is_consolidated_into_new_channels_after_probe(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "International-Playlist.m3u"
            rows = [
                f'#EXTINF:-1 tvg-id="MK{i}.mk" tvg-country="MK" group-title="North Macedonia",MK {i}\nhttps://example.org/under{i}.m3u8'
                for i in range(4)
            ]
            playlist.write_text("#EXTM3U\n" + "\n".join(rows) + "\n", encoding="utf-8")
            moved = consolidate_international_country_groups(playlist)
            content = playlist.read_text(encoding="utf-8")
            self.assertEqual(len(moved), 4)
            self.assertNotIn('group-title="North Macedonia"', content)
            self.assertEqual(content.count('group-title="New Channels"'), 4)

    def test_empty_logo_attribute_is_removed_when_no_authentic_asset_exists(self):
        extinf = '#EXTINF:-1 tvg-name="Definitely Missing Channel" tvg-logo="",Definitely Missing Channel'
        entry = {"extinf": extinf, "logo": "", "name": "Definitely Missing Channel"}
        updated, localized, cleared = ensure_local_logo(entry)
        self.assertNotIn('tvg-logo=""', updated)
        self.assertTrue(cleared)

    def test_parser_detects_malformed_extinf_pair(self):
        _, entries, malformed = parse_playlist('#EXTM3U\n#EXTINF:-1 group-title="New Channels",Example\n')
        self.assertEqual(entries, [])
        self.assertEqual(len(malformed), 1)

if __name__ == "__main__":
    unittest.main()
