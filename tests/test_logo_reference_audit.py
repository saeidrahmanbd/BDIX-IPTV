"""Regression tests for conservative logo reference scanning."""
import sys
import tempfile
import unittest
import random

from PIL import Image
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_logo_references import scan
from repair_logo_asset_technical_quality import repair_one


class LogoReferenceAuditTests(unittest.TestCase):
    def test_generated_reports_do_not_self_reference_assets(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "logos").mkdir()
            (root / "scripts").mkdir()
            (root / "reports").mkdir()
            (root / "logos" / "sample.png").write_bytes(b"test image")
            (root / "scripts" / "consumer.py").write_text(
                'LOGO = "logos/sample.png"\\n', encoding="utf-8"
            )
            (root / "reports" / "logo-reference-audit.json").write_text(
                '{"asset": "logos/sample.png", "missing": "logos/ghost.png"}',
                encoding="utf-8",
            )
            (root / "reports" / "logo-source-registry.json").write_text(
                '{"asset": "logos/sample.png", "future": "logos/registry-only.png"}',
                encoding="utf-8",
            )

            result = scan(root)

            self.assertEqual(result["all_explicitly_referenced_logo_files"], 1)
            self.assertEqual(
                result["all_references"]["logos/sample.png"],
                ["reports/logo-source-registry.json", "scripts/consumer.py"],
            )
            self.assertNotIn("logos/ghost.png", result["missing_explicit_logo_targets"])
            self.assertIn("logos/registry-only.png", result["missing_runtime_logo_targets"])



    def test_non_image_files_are_not_reported_as_large_logo_assets(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "README.md"
            path.write_text("documentation" * 1000, encoding="utf-8")

            result = repair_one(path, fix=False, max_bytes=100)

            self.assertFalse(result["large"])
            self.assertEqual(result["width_before"], 0)
            self.assertEqual(result["height_before"], 0)
            self.assertFalse(result["error"])

    def test_compression_does_not_overwrite_small_logo_when_budget_is_unreachable(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "noise.png"
            rng = random.Random(17)
            pixels = bytes(rng.randrange(256) for _ in range(100 * 100 * 3))
            Image.frombytes("RGB", (100, 100), pixels).save(path, format="PNG")
            original = path.read_bytes()

            result = repair_one(path, fix=True, max_dimension=1600, max_bytes=1000)

            self.assertTrue(result["error"])
            self.assertEqual(path.read_bytes(), original)
            with Image.open(path) as image:
                self.assertEqual(image.size, (100, 100))


if __name__ == "__main__":
    unittest.main()
