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
            (root/"IPTV-Playlist.m3u").write_text('#EXTM3U\n#EXTINF:-1 tvg-logo="logos/used.png",A\nhttps://a.example/a\n#EXTINF:-1 tvg-logo="logos/missing.svg",B\nhttps://b.example/b\n',encoding="utf-8")
            (root/"logos"/"used.png").write_bytes(b"same")
            result=scan(root)
            self.assertEqual(result["playlist_referenced_logo_files"],1)
            self.assertIn("logos/missing.svg",result["missing_runtime_logo_targets"])

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

    def test_inventory_manifests_do_not_self_reference_every_asset(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/"logos").mkdir()
            (root/"docs"/"automation-v2").mkdir(parents=True)
            (root/"logos"/"orphan.png").write_bytes(b"image")
            (root/"docs"/"automation-v2"/"baseline-tree-manifest.json").write_text('{"path":"logos/orphan.png"}',encoding="utf-8")
            (root/"docs"/"automation-v2"/"logo-reference-baseline.json").write_text('{"unused":["logos/orphan.png"]}',encoding="utf-8")
            result=scan(root)
            self.assertEqual(result["all_explicitly_referenced_logo_files"],0)
            self.assertEqual(result["apparently_unreferenced_by_any_text_file"],1)

    def test_report_only_references_do_not_count_as_runtime_references(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/"logos").mkdir()
            (root/"reports").mkdir()
            (root/"scripts").mkdir()
            (root/"logos"/"report.png").write_bytes(b"r")
            (root/"logos"/"script.png").write_bytes(b"s")
            (root/"reports"/"logo-asset-quality-audit.md").write_text("logos/report.png",encoding="utf-8")
            (root/"scripts"/"repair.py").write_text("LOGO = 'logos/script.png'",encoding="utf-8")
            result=scan(root)
            self.assertEqual(result["all_explicitly_referenced_logo_files"],2)
            self.assertEqual(result["runtime_referenced_logo_files"],1)
            self.assertEqual(result["apparently_unreferenced_by_runtime"],1)

if __name__=="__main__":
    unittest.main()
