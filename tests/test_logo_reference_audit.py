"""Regression tests for conservative logo reference scanning."""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_logo_references import scan


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


if __name__ == "__main__":
    unittest.main()
