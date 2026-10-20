import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_logo_authenticity_manifest import provenance_for


class LogoAuthenticityManifestTests(unittest.TestCase):
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
