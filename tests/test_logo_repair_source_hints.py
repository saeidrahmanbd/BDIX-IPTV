"""Source regression tests for exact active-channel logo repairs."""
import re
import sys
import unittest
import tempfile
import hashlib
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

    def test_wow_kidz_tamil_uses_official_brand_wordmark_without_hindi_suffix(self):
        hint = logo_repair.EXTRA_DIRECT_HINTS["WOW Kidz Tamil"]
        self.assertIn("yt3.ggpht.com", hint["url"])
        self.assertIn("youtube.com/channel/", hint["page"])
        self.assertIn("without the incorrect Hindi-language suffix", hint["license"])

    def test_channel_52_uses_published_original_logo_source(self):
        hint = logo_repair.EXTRA_DIRECT_HINTS["Channel 52"]
        self.assertEqual(hint["url"], "https://wsrv.nl/?url=cdn.risingbd.com%2Fmedia%2FimgAll%2F2013December%2F4420131228144155.jpg")
        self.assertIn("risingbd.com", hint["page"])
        self.assertIn("logo", hint["license"].casefold())

    def test_superseded_placeholder_assets_are_quarantined_but_verified_channel_52_is_allowed(self):
        self.assertNotIn("channel-52.png", logo_repair.BAD_ASSETS)
        for name in ("channel-52-converted-56518832e7.png", "jtv-bangla.png", "classic-movies-27994c39.png", "wow-kidz-tamil.png"):
            with self.subTest(asset=name):
                self.assertIn(name, logo_repair.BAD_ASSETS)

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

    @patch("repair_playlist_logos.file_is_valid", return_value=True)
    @patch("logo_source_catalog.valid_image", return_value=True)
    @patch("logo_source_catalog.fetch_bytes")
    def test_canonical_name_collision_preserves_existing_asset_and_uses_digest_name(
        self, fetch_bytes, valid_image, file_is_valid
    ):
        raw = b"\\x89PNG\\r\\n\\x1a\\nverified-new-logo-bytes"
        fetch_bytes.return_value = (raw, "image/png")
        with tempfile.TemporaryDirectory() as directory:
            logo_repair.LOGOS = Path(directory)
            canonical = Path(directory) / "colors-gujarati.png"
            canonical.write_bytes(b"existing-different-logo")
            result = logo_repair.download_exact_asset(
                "Colors Gujarati", {"url": "https://example.org/logo.png", "format": "PNG"},
                canonical_name=True,
            )
            self.assertNotEqual(result, canonical.name)
            self.assertTrue(result.startswith("colors-gujarati-"))
            self.assertEqual(canonical.read_bytes(), b"existing-different-logo")
            self.assertEqual((Path(directory) / result).read_bytes(), raw)

    def test_image_extension_is_sniffed_when_source_uses_octet_stream(self):
        self.assertEqual(
            logo_repair.detected_image_extension(b"\xff\xd8\xff" + b"jpeg", "application/octet-stream"),
            ".jpg",
        )
        self.assertEqual(
            logo_repair.detected_image_extension(b"RIFF0000WEBP" + b"webp", "application/octet-stream"),
            ".webp",
        )
        self.assertEqual(
            logo_repair.detected_image_extension(b"\x89PNG\r\n\x1a\n" + b"png", "application/octet-stream"),
            ".png",
        )

    def test_international_logo_sources_are_exact_and_attributed(self):
        expected = {
            "Diema": (
                "https://upload.wikimedia.org/wikipedia/commons/d/d5/Diema_Bulgaria_logo.svg",
                "https://commons.wikimedia.org/wiki/File:Diema_Bulgaria_logo.svg",
            ),
            "MBC Mood": (
                "https://upload.wikimedia.org/wikipedia/commons/1/12/MBC_Mood_Logo.png",
                "https://commons.wikimedia.org/wiki/File:MBC_Mood_Logo.png",
            ),
            "Tarab": (
                "https://assets.mbcmood.com/channels/1738059679TARAB_Logo.png",
                "https://github.com/iptv-org/database/issues/15624",
            ),
            "Cinecanal Panregional": (
                "https://upload.wikimedia.org/wikipedia/commons/e/e6/CinecanalLA.png",
                "https://commons.wikimedia.org/wiki/File:CinecanalLA.png",
            ),
        }
        for channel, (asset_url, source_page) in expected.items():
            with self.subTest(channel=channel):
                hint = logo_repair.EXTRA_DIRECT_HINTS[channel]
                self.assertEqual(hint["url"], asset_url)
                self.assertEqual(hint["page"], source_page)
                self.assertTrue(hint["license"])

    def test_wwe_superstar_central_uses_exact_trademark_image_asset(self):
        hint = logo_repair.EXTRA_DIRECT_HINTS["WWE Superstar Central"]
        self.assertEqual(hint["url"], "https://static.trademarkia.com/images/99048431")
        self.assertIn("ww-superstar-central-99048431", hint["page"])
        self.assertIn("World Wrestling Entertainment", hint["license"])

    def test_shikor_prefers_explicit_logo_on_official_site_then_partner_page(self):
        hints = logo_source_catalog.DIRECT_PAGE_HINTS["Shikor TV Canada"]
        self.assertEqual(hints[0], ("https://shikortvcanada.com/", False))
        self.assertEqual(hints[1], ("https://www.jagobd.com/shikortv", True))

    def test_channel16_ru_asset_is_quarantined_from_general_reuse(self):
        self.assertIn("16-a308b78988.png", logo_repair.BAD_ASSETS)

    def test_generated_fallback_art_is_enabled_as_disclosed_last_resort(self):
        self.assertTrue(logo_repair.ALLOW_GENERATED_FALLBACKS)
        self.assertIn("UNOFFICIAL FALLBACK ART", logo_repair.make_generated_fallback.__doc__.upper())

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

    def test_existing_logo_replacement_preserves_noncanonical_attribute_order(self):
        line = (
            '#EXTINF:-1 group-title="International" tvg-language="eng" '
            'tvg-logo="https://old.example/logo.jpg" tvg-name="Diema" '
            'tvg-id="Diema.bg@SD",Diema'
        )
        updated = logo_repair.set_logo(
            line, "https://raw.githubusercontent.com/example/logos/diema.png"
        )
        strip_logo = lambda value: re.sub(r'\s+tvg-logo="[^"]*"', "", value)
        self.assertEqual(strip_logo(updated), strip_logo(line))
        self.assertLess(updated.index('group-title="'), updated.index('tvg-language="'))
        self.assertLess(updated.index('tvg-name="'), updated.index('tvg-id="'))
        self.assertIn('tvg-logo="https://raw.githubusercontent.com/example/logos/diema.png"', updated)

    def test_new_logo_attribute_preserves_existing_attribute_order(self):
        line = '#EXTINF:-1 group-title="International" tvg-name="Diema" tvg-id="Diema.bg@SD",Diema'
        updated = logo_repair.set_logo(
            line, "https://raw.githubusercontent.com/example/logos/diema.png"
        )
        strip_logo = lambda value: re.sub(r'\s+tvg-logo="[^"]*"', "", value)
        self.assertEqual(strip_logo(updated), strip_logo(line))
        self.assertLess(updated.index('group-title="'), updated.index('tvg-name="'))
        self.assertLess(updated.index('tvg-name="'), updated.index('tvg-id="'))

    def test_render_updated_playlist_preserves_crlf_endings(self):
        original = (
            "#EXTM3U\r\n"
            '#EXTINF:-1 group-title="International" tvg-name="Diema",Diema\r\n'
            "https://example.invalid/live.m3u8\r\n"
        )
        lines = original.splitlines()
        lines[1] = logo_repair.set_logo(
            lines[1], "https://raw.githubusercontent.com/example/logos/diema.png"
        )
        updated = logo_repair.render_updated_playlist(lines, original)
        self.assertEqual(updated.count("\r\n"), original.count("\r\n"))
        self.assertNotIn("\n", updated.replace("\r\n", ""))

    def test_new_logo_attribute_is_inserted_before_group_title(self):
        line = '#EXTINF:-1 tvg-id="sample.bd" tvg-name="Sample TV" group-title="New Channels",Sample TV'
        updated = logo_repair.set_logo(
            line, "https://raw.githubusercontent.com/example/logos/sample.png"
        )
        keys = re.findall(r'([A-Za-z0-9_-]+)="([^"]*)"', updated)
        self.assertEqual([key for key, _ in keys], ["tvg-id", "tvg-name", "tvg-logo", "group-title"])


if __name__ == "__main__":
    unittest.main()
