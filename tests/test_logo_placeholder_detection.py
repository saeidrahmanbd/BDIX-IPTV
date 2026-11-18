from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from scripts.audit_logo_references import scan

BAD_HASH = "9b5936f4006146e4e1e9025b474c02863c0b5614132ad40db4b925a10e8bfbb9"


class LogoPlaceholderDetectionTests(unittest.TestCase):
    def test_known_placeholder_hash_is_reported_when_playlist_references_asset(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "logos").mkdir()
            (root / "logos" / "bad.png").write_bytes(b"placeholder bytes")
            (root / "IPTV-Playlist.m3u").write_text(
                '#EXTM3U\n#EXTINF:-1 tvg-logo="logos/bad.png" group-title="Review",Bad Logo\n'
                'https://example.invalid/live.m3u8\n',
                encoding="utf-8",
            )
            with patch("scripts.audit_logo_references._sha256", return_value=BAD_HASH):
                result = scan(root)

        self.assertEqual(result["known_placeholder_asset_files"], ["logos/bad.png"])
        self.assertEqual(result["playlist_referenced_placeholder_assets"], ["logos/bad.png"])
        self.assertEqual(result["known_placeholder_asset_groups"][0]["reason"], "Imgur missing-image placeholder")


if __name__ == "__main__":
    unittest.main()
