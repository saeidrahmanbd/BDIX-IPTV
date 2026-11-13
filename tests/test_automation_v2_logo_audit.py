import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from audit_logo_references import scan

class LogoReferenceAuditTests(unittest.TestCase):
    def test_explicit_reference_and_missing_target(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/"logos").mkdir()
            (root/"logos"/"used.png").write_bytes(b"same")
            (root/"README.md").write_text("tvg-logo=logos/used.png and logos/missing.svg",encoding="utf-8")
            result=scan(root)
            self.assertEqual(result["explicitly_referenced_logo_files"],1)
            self.assertIn("logos/missing.svg",result["missing_explicit_logo_targets"])

    def test_exact_duplicate_assets_are_reported_not_deleted(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/"logos").mkdir()
            (root/"logos"/"a.png").write_bytes(b"identical")
            (root/"logos"/"b.png").write_bytes(b"identical")
            result=scan(root)
            self.assertEqual(result["exact_duplicate_groups"],1)
            self.assertEqual(result["exact_duplicate_files"],1)
            self.assertFalse(result["deletion_performed"])
            self.assertFalse(result["quarantine_performed"])

if __name__=="__main__":
    unittest.main()
