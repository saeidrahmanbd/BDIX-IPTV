import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from stream_url_identity import stream_url_key, stream_endpoint_family_key


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

    def test_near_duplicate_hls_rendition_urls_share_endpoint_family(self):
        self.assertEqual(
            stream_endpoint_family_key("https://tvsen7.aynaott.com/ssport2hd/index.m3u8"),
            stream_endpoint_family_key("https://tvsen7.aynaott.com/ssport2hd/tracks-v1a1/mono.ts.m3u8"),
        )
        self.assertEqual(
            stream_endpoint_family_key("http://live.playmax.live/matribhumi/index.m3u8"),
            stream_endpoint_family_key("https://live.playmax.live/matribhumi/playlist.m3u8"),
        )

    def test_endpoint_family_preserves_case_sensitive_paths_and_distinct_hosts(self):
        self.assertNotEqual(
            stream_endpoint_family_key("https://stream.example/Tunes6music/index.m3u8"),
            stream_endpoint_family_key("https://stream.example/tunes6music/index.m3u8"),
        )
        self.assertNotEqual(
            stream_endpoint_family_key("https://a.example/live/index.m3u8"),
            stream_endpoint_family_key("https://b.example/live/index.m3u8"),
        )

    def test_retired_endpoint_registry_covers_removed_star_sports_endpoint_family(self):
        import json
        root = Path(__file__).resolve().parents[1]
        registry = json.loads((root / "config" / "discovery-retired-endpoints.json").read_text(encoding="utf-8"))
        retired = set(registry["endpoint_keys"])
        self.assertIn(
            stream_endpoint_family_key("https://tvsen7.aynaott.com/ssport2hd/index.m3u8"),
            retired,
        )
        self.assertIn(
            stream_endpoint_family_key("https://tvsen7.aynaott.com/ssport2hd/tracks-v1a1/mono.ts.m3u8"),
            retired,
        )

    def test_static_scn_route_token_is_not_treated_as_opaque_credential(self):
        from urllib.parse import parse_qs, urlsplit
        query = parse_qs(urlsplit("http://103.114.11.37:8081/Star-sports-1/index.m3u8?token=scn").query)
        self.assertEqual(query, {"token": ["scn"]})

    def test_empty_and_malformed_values_are_safe(self):
        self.assertEqual(stream_url_key(""), "")
        self.assertEqual(stream_endpoint_family_key(""), "")
        malformed = "https://[not-a-valid-host/live"
        self.assertEqual(stream_url_key(malformed), malformed)
