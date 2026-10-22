import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from repair_logo_asset_technical_quality import repair_one


class LogoAssetTechnicalQualityTests(unittest.TestCase):
    def test_jpeg_stored_as_png_is_reencoded_as_png(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad-extension.png"
            Image.new("RGB", (160, 90), (20, 40, 60)).save(path, format="JPEG")
            before = repair_one(path, fix=False)
            self.assertTrue(before["format_mismatch"])
            result = repair_one(path, fix=True)
            self.assertTrue(result["format_repaired"])
            with Image.open(path) as image:
                self.assertEqual(image.format, "PNG")

    def test_oversized_image_is_resized_without_changing_extension(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "oversized.png"
            Image.new("RGBA", (2000, 1000), (20, 40, 60, 255)).save(path, format="PNG")
            result = repair_one(path, fix=True, max_dimension=1200)
            self.assertTrue(result["resized"])
            with Image.open(path) as image:
                self.assertEqual(image.format, "PNG")
                self.assertEqual(max(image.size), 1200)
                self.assertAlmostEqual(image.width / image.height, 2.0, places=2)


if __name__ == "__main__":
    unittest.main()
