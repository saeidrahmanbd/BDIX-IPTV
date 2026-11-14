import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_logo_authenticity_manifest import asset_stem, provenance_for


class LogoAuthenticityManifestTests(unittest.TestCase):

    def test_converted_digest_suffix_retains_exact_asset_provenance(self):
        registry = {
            "IPTV-Playlist.m3u|custom.sample|Sample|logos/sample.svg": {
                "status": "third_party_verified",
                "source_url": "https://example.com/sample-logo.svg",
                "notes": "Exact sample asset source.",
            }
        }
        converted_logo = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/sample-converted-0123456789.png"
        source, match = provenance_for(
            registry, "IPTV-Playlist.m3u", {"tvg-id": "custom.sample"},
            "Sample", converted_logo
        )
        self.assertEqual(asset_stem(converted_logo), "sample")
        self.assertEqual(match, "same-asset-stem-format-conversion")
        self.assertEqual(source.get("status"), "third_party_verified")

    def test_classic_movies_fallback_is_explicitly_unofficial(self):
        registry = json.loads(
            (ROOT / "reports" / "logo-source-registry.json").read_text(encoding="utf-8")
        )
        logo = (
            "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/"
            "logos/classic-movies-27994c39.png"
        )
        metadata = {"tvg-id": "custom.classic.movies"}
        source, match = provenance_for(
            registry, "IPTV-Playlist.m3u", metadata, "Classic Movies", logo
        )

        self.assertEqual(match, "exact-key")
        self.assertEqual(source.get("status"), "generated_fallback")
        self.assertFalse(source.get("source_url"))
        self.assertIn("unofficial fallback", source.get("notes", "").casefold())


if __name__ == "__main__":
    unittest.main()
