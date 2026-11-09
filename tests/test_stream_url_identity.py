import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from stream_url_identity import stream_url_key


class StreamUrlIdentityTests(unittest.TestCase):
    def test_scheme_and_host_are_case_insensitive(self):
        self.assertEqual(
            stream_url_key("HTTP://EXAMPLE.COM/Live/index.m3u8"),
            stream_url_key("http://example.com/Live/index.m3u8"),
        )

    def test_path_case_is_preserved(self):
        upper = "https://stream.example/Tunes6music/live/video.m3u8"
        lower = "https://stream.example/tunes6music/live/video.m3u8"
        self.assertNotEqual(stream_url_key(upper), stream_url_key(lower))

    def test_query_case_is_preserved(self):
        upper = "https://stream.example/live.m3u8?Token=AbC"
        lower = "https://stream.example/live.m3u8?token=AbC"
        self.assertNotEqual(stream_url_key(upper), stream_url_key(lower))


    def test_audit_and_pre_publish_gate_use_canonical_stream_identity(self):
        root = Path(__file__).resolve().parents[1]
        audit = (root / "scripts" / "audit_playlist.py").read_text(encoding="utf-8")
        gate = (root / "scripts" / "pre_publish_gate.py").read_text(encoding="utf-8")
        self.assertIn("urls[stream_url_key(url)]", audit)
        self.assertIn("old_urls = Counter(stream_url_key(url)", audit)
        self.assertIn("new_urls = Counter(stream_url_key(url)", audit)
        self.assertIn("cur_urls=Counter(stream_url_key(u)", gate)
        self.assertIn("cur_all_groups[stream_url_key(u)]", gate)
        self.assertNotIn("urls[url.lower()]", audit)
        self.assertNotIn("cur_urls=Counter(u.lower()", gate)

    def test_empty_and_malformed_values_are_safe(self):
        self.assertEqual(stream_url_key(""), "")
        malformed = "https://[not-a-valid-host/live"
        self.assertEqual(stream_url_key(malformed), malformed)
