import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from generate_logo_provenance_review import build_report


class LogoProvenanceReviewTests(unittest.TestCase):
    def test_report_explains_unknown_and_unofficial_statuses(self):
        manifest = {
            "status_counts_by_playlist": {
                "IPTV-Playlist.m3u": {"needs_review": 2, "generated_fallback": 1, "third_party_verified": 3, "official_verified": 0},
                "BDIX-Playlist.m3u": {"needs_review": 4, "generated_fallback": 0, "third_party_verified": 0, "official_verified": 0},
            },
            "entries": [
                {"playlist": "IPTV-Playlist.m3u", "channel_name": "Sample TV", "tvg_id": "sample.tv", "logo": "https://example.invalid/logos/sample.png", "status": "needs_review", "reason": "No exact source record."},
                {"playlist": "IPTV-Playlist.m3u", "channel_name": "Fallback", "tvg_id": "fallback.tv", "logo": "https://example.invalid/logos/generated-fallback.png", "status": "generated_fallback", "reason": "Unofficial fallback."},
                {"playlist": "IPTV-Playlist.m3u", "channel_name": "Goldmines", "tvg_id": "Goldmines.in@SD", "logo": "https://example.invalid/logos/goldmines.png", "status": "needs_review", "reason": "Source not documented."},
                {"playlist": "IPTV-Playlist.m3u", "channel_name": "Goldmines 2", "tvg_id": "Goldmines2.in@SD", "logo": "https://example.invalid/logos/goldmines.png", "status": "needs_review", "reason": "Source not documented."},
            ],
        }
        report = build_report(manifest, {"IPTV-Playlist.m3u": "a" * 64, "BDIX-Playlist.m3u": "b" * 64}, "2026-10-20T12:00:00+00:00")
        self.assertIn("does not by itself prove the logo is wrong", report)
        self.assertIn("unofficial fallback artwork", report)
        self.assertIn("a" * 64, report)
        self.assertIn("Sample TV", report)
        self.assertIn("Shared logo assets across distinct channel identities", report)
        self.assertIn("goldmines.png", report)
        self.assertIn("Goldmines 2", report)
        self.assertNotIn("official_verified | 1", report)


if __name__ == "__main__":
    unittest.main()
