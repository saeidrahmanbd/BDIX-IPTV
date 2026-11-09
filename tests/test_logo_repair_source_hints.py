"""Source regression tests for exact active-channel logo repairs."""
import re
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_playlist_logos as logo_repair
import logo_source_catalog as logo_source_catalog


class LogoRepairSourceTests(unittest.TestCase):
    @patch("logo_source_catalog.fetch_bytes")
    def test_find_page_logo_parses_img_attributes(self, fetch_bytes):
        fetch_bytes.return_value = (
            b'<html><img src="/assets/shikor-logo.png" alt="Shikor TV Canada logo"></html>',
            "text/html",
        )
        self.assertEqual(
            logo_source_catalog.find_page_logo("https://example.org/channel"),
            "https://example.org/assets/shikor-logo.png",
        )

    @patch("logo_source_catalog.fetch_bytes")
    def test_find_page_logo_parses_open_graph_attributes(self, fetch_bytes):
        fetch_bytes.return_value = (
            b'<html><head><meta property="og:image" content="/assets/channel-logo.png"></head></html>',
            "text/html",
        )
        self.assertEqual(
            logo_source_catalog.find_page_logo("https://example.org/channel", allow_og_image=True),
            "https://example.org/assets/channel-logo.png",
        )

    def test_logo_only_render_preserves_nonlogo_content_and_trailing_newlines(self):
        for original in (
            "#EXTM3U\n#EXTINF:-1 tvg-name=\"Channel\" group-title=\"Review\",Channel\nhttps://example.org/live.m3u8\n",
            "#EXTM3U\n#EXTINF:-1 tvg-name=\"Channel\" group-title=\"Review\",Channel\nhttps://example.org/live.m3u8\n\n",
        ):
            lines = original.splitlines()
            output = [
                logo_repair.set_logo(line, "https://raw.githubusercontent.com/example/logos/channel.png")
                if line.startswith("#EXTINF:") else line
                for line in lines
            ]
            updated = logo_repair.render_updated_playlist(output, original)
            strip_logo = lambda value: re.sub(r'\s+tvg-logo="[^"]*"', "", value)
            self.assertEqual(strip_logo(updated), strip_logo(original))
            self.assertEqual(len(updated) - len(updated.rstrip("\n")), len(original) - len(original.rstrip("\n")))

    def test_alone_uses_a_direct_validated_commons_asset_url(self):
        hint = logo_repair.EXTRA_DIRECT_HINTS["Alone"]
        self.assertTrue(hint["url"].startswith("https://upload.wikimedia.org/wikipedia/commons/"))
        self.assertIn("Alone_%28Leftfield_Pictures_TV_series%29_logo.svg", hint["url"])
        self.assertIn("commons.wikimedia.org/wiki/File:Alone_", hint["page"])
        self.assertIn("history.com/shows/alone", hint["license_url"])

    def test_zainabia_logo_source_is_identity_attributed(self):
        hint = logo_repair.EXTRA_DIRECT_HINTS["Zainabia Channel"]
        self.assertIn("ZAINABIA", hint["license"].upper())
        self.assertIn("zainabiachannel.co.in", hint["license_url"])
        self.assertIn("shialivetv.com", hint["url"])

    def test_channel16_ru_asset_is_quarantined_from_general_reuse(self):
        self.assertIn("16-a308b78988.png", logo_repair.BAD_ASSETS)

    def test_generated_fallback_art_is_disabled_by_default(self):
        self.assertFalse(logo_repair.ALLOW_GENERATED_FALLBACKS)

    def test_adult_backup_channels_are_exempt_from_logo_repair(self):
        for name in ("Evil Angel", "Pink Erotic 2", "Pink Erotic 3", "Pink Erotic 5", "Pink Erotic 7", "Pink Erotic 8"):
            with self.subTest(channel=name):
                self.assertTrue(
                    logo_repair.is_adult_playlist_entry(
                        "International-Playlist.m3u", "Backup", "custom." + logo_repair.norm_key(name), logo_repair.norm_key(name)
                    )
                )
        self.assertFalse(
            logo_repair.is_adult_playlist_entry(
                "International-Playlist.m3u", "Backup", "custom.news", logo_repair.norm_key("MBC Mood")
            )
        )


if __name__ == "__main__":
    unittest.main()
