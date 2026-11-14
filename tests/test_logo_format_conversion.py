"""Regression tests for safe local logo format conversion."""
import base64
import io
import struct
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from convert_referenced_logos_to_png import (
    RAW_BASE,
    convert_referenced_logos,
    image_bytes_to_png,
    without_logo_attributes,
)


def image_bytes(fmt, color=(30, 120, 220)):
    output = io.BytesIO()
    Image.new("RGB", (80, 40), color).save(output, format=fmt)
    return output.getvalue()


class LogoFormatConversionTests(unittest.TestCase):
    def test_jpeg_and_webp_are_converted_to_png(self):
        for extension, fmt in ((".jpg", "JPEG"), (".webp", "WEBP")):
            with self.subTest(extension=extension):
                png = image_bytes_to_png(image_bytes(fmt), extension)
                self.assertTrue(png.startswith(b"\x89PNG\r\n\x1a\n"))
                with Image.open(io.BytesIO(png)) as image:
                    self.assertEqual(image.format, "PNG")
                    self.assertEqual(image.size, (80, 40))

    def test_svg_is_converted_to_png(self):
        svg = b'<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100" viewBox="0 0 200 100"><rect width="200" height="100" fill="#ff0000"/></svg>'
        png = image_bytes_to_png(svg, ".svg")
        self.assertTrue(png.startswith(b"\x89PNG\r\n\x1a\n"))
        with Image.open(io.BytesIO(png)) as image:
            self.assertEqual(image.format, "PNG")
            self.assertEqual(image.size, (1024, 512))

    def test_svg_with_damaged_embedded_png_is_recovered_safely(self):
        embedded = bytearray(image_bytes("PNG", (80, 30, 190)))
        offset = 8
        while offset + 8 <= len(embedded):
            length = struct.unpack(">I", embedded[offset:offset + 4])[0]
            kind = bytes(embedded[offset + 4:offset + 8])
            if kind == b"IDAT":
                embedded[offset + 8 + length] ^= 0x01
                break
            offset += 12 + length
        damaged = bytes(embedded[:-3])
        svg = (
            b'<svg xmlns="http://www.w3.org/2000/svg" width="100" height="50">'
            b'<image href="data:image/png;base64,' + base64.b64encode(damaged)
            + b'" width="100" height="50"/></svg>'
        )
        png = image_bytes_to_png(svg, ".svg")
        with Image.open(io.BytesIO(png)) as image:
            image.load()
            self.assertEqual(image.format, "PNG")
            self.assertEqual(image.size, (1024, 512))
    def test_shared_asset_is_converted_once_and_only_logo_references_change(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            logos = root / "logos"
            logos.mkdir()
            (logos / "shared.jpg").write_bytes(image_bytes("JPEG"))
            line = (
                '#EXTINF:-1 tvg-id="sample.bd" tvg-name="Sample" '
                f'tvg-logo="{RAW_BASE}shared.jpg" tvg-chno="7" group-title="Bangladesh",Sample\n'
                "https://example.invalid/live.m3u8\n"
            )
            for playlist in ("IPTV-Playlist.m3u", "International-Playlist.m3u"):
                (root / playlist).write_text("#EXTM3U\n" + line, encoding="utf-8")
            before = {
                playlist: (root / playlist).read_text(encoding="utf-8")
                for playlist in ("IPTV-Playlist.m3u", "International-Playlist.m3u")
            }
            summary = convert_referenced_logos(root=root)
            self.assertEqual(summary["unique_assets_converted"], 1)
            self.assertEqual(summary["updated_references"], 2)
            self.assertEqual(summary["source_formats"], {"jpg": 1})
            outputs = []
            for playlist in before:
                after = (root / playlist).read_text(encoding="utf-8")
                self.assertEqual(without_logo_attributes(after), without_logo_attributes(before[playlist]))
                logo = after.split('tvg-logo="', 1)[1].split('"', 1)[0]
                self.assertTrue(logo.endswith(".png"))
                outputs.append(logo)
                relative = logo[len(RAW_BASE):]
                png_path = logos / relative
                self.assertTrue(png_path.is_file())
                self.assertTrue(png_path.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))
            self.assertEqual(outputs[0], outputs[1])
            self.assertTrue((logos / "shared.jpg").is_file())

    def test_blocked_generic_png_name_uses_converted_digest_filename(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            logos = root / "logos"
            logos.mkdir()
            (logos / "zee-tv.svg").write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="50"><rect width="100" height="50" fill="#0000ff"/></svg>',
                encoding="utf-8",
            )
            (root / "IPTV-Playlist.m3u").write_text(
                "#EXTM3U\n"
                f'#EXTINF:-1 tvg-logo="{RAW_BASE}zee-tv.svg",Zee TV\n'
                "https://example.invalid/live.m3u8\n",
                encoding="utf-8",
            )
            convert_referenced_logos(root=root, playlist_names=("IPTV-Playlist.m3u",))
            playlist = (root / "IPTV-Playlist.m3u").read_text(encoding="utf-8")
            logo = playlist.split('tvg-logo="', 1)[1].split('"', 1)[0]
            self.assertIn("zee-tv-converted-", logo)
            self.assertTrue(logo.endswith(".png"))
            self.assertFalse(logo.endswith("/zee-tv.png"))

    def test_existing_different_png_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            logos = root / "logos"
            logos.mkdir()
            (logos / "sample.jpg").write_bytes(image_bytes("JPEG", (220, 20, 20)))
            existing = image_bytes_to_png(image_bytes("PNG", (20, 220, 20)), ".png")
            (logos / "sample.png").write_bytes(existing)
            (root / "IPTV-Playlist.m3u").write_text(
                "#EXTM3U\n"
                f'#EXTINF:-1 tvg-logo="{RAW_BASE}sample.jpg",Sample\n'
                "https://example.invalid/live.m3u8\n",
                encoding="utf-8",
            )
            summary = convert_referenced_logos(root=root, playlist_names=("IPTV-Playlist.m3u",))
            self.assertEqual(summary["unique_assets_converted"], 1)
            self.assertEqual((logos / "sample.png").read_bytes(), existing)
            playlist = (root / "IPTV-Playlist.m3u").read_text(encoding="utf-8")
            self.assertIn("sample-", playlist)
            self.assertIn(".png", playlist)


    def test_crlf_playlist_line_endings_are_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            logos = root / "logos"
            logos.mkdir()
            (logos / "line.jpg").write_bytes(image_bytes("JPEG"))
            original = (
                "#EXTM3U\\r\\n"
                f'#EXTINF:-1 tvg-logo="{RAW_BASE}line.jpg",Line\\r\\n'
                "https://example.invalid/live.m3u8\\r\\n"
            )
            playlist = root / "IPTV-Playlist.m3u"
            playlist.write_bytes(original.encode("utf-8"))
            convert_referenced_logos(root=root, playlist_names=("IPTV-Playlist.m3u",))
            converted = playlist.read_bytes()
            self.assertIn(b"\\r\\n", converted)
            self.assertNotIn(b"\\n", converted.replace(b"\\r\\n", b""))

    def test_complete_logo_inventory_is_converted_not_only_referenced_assets(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            logos = root / "logos"
            logos.mkdir()
            (logos / "shikor-tv-canada.svg").write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="120" height="60"><rect width="120" height="60" fill="#123456"/></svg>',
                encoding="utf-8",
            )
            (logos / "ten-tv-prime.svg").write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" width="120" height="60"><rect width="120" height="60" fill="#654321"/></svg>',
                encoding="utf-8",
            )
            (logos / "unused.webp").write_bytes(image_bytes("WEBP"))
            (logos / "notes.md").write_text("not an image", encoding="utf-8")
            playlist = root / "IPTV-Playlist.m3u"
            playlist.write_text(
                "#EXTM3U\n"
                f'#EXTINF:-1 tvg-id="custom.shikortvcanada" tvg-logo="logos/shikor-tv-canada.svg",Shikor TV Canada\n'
                "https://example.invalid/shikor.m3u8\n"
                f'#EXTINF:-1 tvg-id="custom.tentvprime" tvg-logo="logos/ten-tv-prime.svg",Ten TV Prime\n'
                "https://example.invalid/ten.m3u8\n",
                encoding="utf-8",
            )
            summary = convert_referenced_logos(root=root, playlist_names=("IPTV-Playlist.m3u",))
            self.assertEqual(summary["unique_assets_converted"], 3)
            self.assertEqual(summary["remaining_non_png_references"], 0)
            updated = playlist.read_text(encoding="utf-8")
            self.assertIn("logos/shikor-tv-canada.png", updated)
            self.assertIn("logos/ten-tv-prime.png", updated)
            self.assertTrue((logos / "unused.png").is_file())
            self.assertTrue((logos / "shikor-tv-canada.svg").is_file())
            self.assertTrue((logos / "ten-tv-prime.svg").is_file())
            self.assertTrue((logos / "notes.md").is_file())

    def test_external_logo_reference_fails_without_changing_playlist(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "logos").mkdir()
            playlist = root / "IPTV-Playlist.m3u"
            original = (
                '#EXTINF:-1 tvg-logo="https://cdn.example/logo.jpg",Sample\n'
                "https://example.invalid/live.m3u8\n"
            )
            playlist.write_text(original, encoding="utf-8")
            with self.assertRaises(ValueError):
                convert_referenced_logos(root=root, playlist_names=("IPTV-Playlist.m3u",))
            self.assertEqual(playlist.read_text(encoding="utf-8"), original)


if __name__ == "__main__":
    unittest.main()
