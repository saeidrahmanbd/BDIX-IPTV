#!/usr/bin/env python3
import base64
import io
import struct
import sys
import unittest
import zlib
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from logo_embedded_png import recover_embedded_png_from_svg


def make_png():
    image = Image.new("RGBA", (5, 4), (30, 120, 210, 255))
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()


def corrupt_idat_crc_and_truncate_iend(png):
    damaged = bytearray(png)
    offset = 8
    while offset + 8 <= len(damaged):
        length = struct.unpack(">I", damaged[offset:offset + 4])[0]
        kind = bytes(damaged[offset + 4:offset + 8])
        if kind == b"IDAT":
            crc_position = offset + 8 + length
            damaged[crc_position] ^= 0x01
            break
        offset += 12 + length
    return bytes(damaged[:-3])


def corrupt_idat_length_and_crc(png):
    damaged = bytearray(png)
    offset = 8
    while offset + 8 <= len(damaged):
        length = struct.unpack(">I", damaged[offset:offset + 4])[0]
        kind = bytes(damaged[offset + 4:offset + 8])
        if kind == b"IDAT":
            struct.pack_into(">I", damaged, offset, length + 3)
            crc_position = offset + 8 + length
            damaged[crc_position] ^= 0x01
            break
        offset += 12 + length
    return bytes(damaged)


class EmbeddedPngRecoveryTests(unittest.TestCase):
    def test_repairs_idat_crc_and_truncated_iend_without_changing_pixels(self):
        original = make_png()
        damaged = corrupt_idat_crc_and_truncate_iend(original)
        svg = (
            b'<svg xmlns="http://www.w3.org/2000/svg"><image href="data:image/png;base64,'
            + base64.b64encode(damaged)
            + b'"/></svg>'
        )

        recovered = recover_embedded_png_from_svg(svg)
        self.assertIsNotNone(recovered)
        with Image.open(io.BytesIO(original)) as expected, Image.open(io.BytesIO(recovered)) as actual:
            expected.load()
            actual.load()
            self.assertEqual(actual.size, expected.size)
            self.assertEqual(actual.convert("RGBA").tobytes(), expected.convert("RGBA").tobytes())

    def test_repairs_idat_length_overlapping_complete_iend(self):
        original = make_png()
        damaged = corrupt_idat_length_and_crc(original)
        svg = (
            b'<svg xmlns="http://www.w3.org/2000/svg"><image href="data:image/png;base64,'
            + base64.b64encode(damaged)
            + b'"/></svg>'
        )
        recovered = recover_embedded_png_from_svg(svg)
        self.assertIsNotNone(recovered)
        with Image.open(io.BytesIO(original)) as expected, Image.open(io.BytesIO(recovered)) as actual:
            expected.load()
            actual.load()
            self.assertEqual(actual.size, expected.size)
            self.assertEqual(actual.convert("RGBA").tobytes(), expected.convert("RGBA").tobytes())

    def test_rejects_bad_non_idat_crc(self):
        png = bytearray(make_png())
        png[29] ^= 0x01  # corrupt the IHDR CRC
        svg = b'<svg><image href="data:image/png;base64,' + base64.b64encode(png) + b'"/></svg>'
        self.assertIsNone(recover_embedded_png_from_svg(svg))

    def test_rejects_truncated_pixel_data(self):
        png = make_png()
        svg = b'<svg><image href="data:image/png;base64,' + base64.b64encode(png[:-20]) + b'"/></svg>'
        self.assertIsNone(recover_embedded_png_from_svg(svg))


if __name__ == "__main__":
    unittest.main()
