import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_discovery_run import append_section, classify_response, parse_playlist


class DiscoveryRunValidationTests(unittest.TestCase):
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

    def test_parser_detects_malformed_extinf_pair(self):
        _, entries, malformed = parse_playlist('#EXTM3U\n#EXTINF:-1 group-title="New Channels",Example\n')
        self.assertEqual(entries, [])
        self.assertEqual(len(malformed), 1)

if __name__ == "__main__":
    unittest.main()
