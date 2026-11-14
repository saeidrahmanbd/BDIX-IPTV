import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.iptv.metadata_repair import MetadataPatch, apply_metadata_patches

BASE='#EXTM3U\n#EXTINF:-1 tvg-id="old.id" tvg-name="Old Name" tvg-logo="logos/old.png" tvg-chno="12" group-title="Bangladesh",Old Name\nhttps://a.example/live.m3u8\n'

class IptvMetadataRepairTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        (self.root/"logos").mkdir()
        (self.root/"logos"/"old.png").write_bytes(b"old")
        (self.root/"logos"/"new.png").write_bytes(b"new")

    def tearDown(self):
        self.temp.cleanup()

    def test_approved_metadata_repair_preserves_protected_fields(self):
        patch=MetadataPatch(0,"official channel source",True,tvg_name="New Name",tvg_id="new.id",display_name="New Name")
        result=apply_metadata_patches(BASE,[patch],self.root)
        self.assertIn('tvg-name="New Name"',result)
        self.assertIn('tvg-id="new.id"',result)
        self.assertIn('tvg-chno="12"',result)
        self.assertIn('group-title="Bangladesh"',result)
        self.assertIn("https://a.example/live.m3u8",result)

    def test_only_existing_local_logo_can_be_used(self):
        patch=MetadataPatch(0,"verified local broadcaster logo",True,tvg_logo="logos/new.png")
        result=apply_metadata_patches(BASE,[patch],self.root)
        self.assertIn('tvg-logo="logos/new.png"',result)

    def test_backslash_logo_path_rejected(self):
        patch=MetadataPatch(0,"source",True,tvg_logo="logos\\\\..\\\\secret.png")
        with self.assertRaises(ValueError):
            apply_metadata_patches(BASE,[patch],self.root)

    def test_remote_logo_rejected(self):
        patch=MetadataPatch(0,"source URL",True,tvg_logo="https://example.com/logo.png")
        with self.assertRaisesRegex(ValueError,"repository-local"):
            apply_metadata_patches(BASE,[patch],self.root)

    def test_missing_local_logo_rejected(self):
        patch=MetadataPatch(0,"source",True,tvg_logo="logos/missing.png")
        with self.assertRaisesRegex(ValueError,"existing supported"):
            apply_metadata_patches(BASE,[patch],self.root)

    def test_path_traversal_rejected(self):
        patch=MetadataPatch(0,"source",True,tvg_logo="logos/../secret.png")
        with self.assertRaisesRegex(ValueError,"traversal"):
            apply_metadata_patches(BASE,[patch],self.root)

    def test_unapproved_or_evidenceless_patch_rejected(self):
        with self.assertRaisesRegex(ValueError,"approval and evidence"):
            apply_metadata_patches(BASE,[MetadataPatch(0,"",False,tvg_name="New")],self.root)

    def test_duplicate_and_out_of_range_patches_rejected(self):
        patch=MetadataPatch(0,"evidence",True,tvg_name="New")
        with self.assertRaisesRegex(ValueError,"duplicate"):
            apply_metadata_patches(BASE,[patch,patch],self.root)
        with self.assertRaisesRegex(ValueError,"out of range"):
            apply_metadata_patches(BASE,[MetadataPatch(1,"evidence",True,tvg_name="New")],self.root)

    def test_invalid_text_value_rejected(self):
        patch=MetadataPatch(0,"evidence",True,tvg_name='Bad"Name')
        with self.assertRaisesRegex(ValueError,"quotes"):
            apply_metadata_patches(BASE,[patch],self.root)

    def test_no_patches_returns_identical_text(self):
        self.assertEqual(apply_metadata_patches(BASE,[],self.root),BASE)


    def test_symlinked_logos_root_rejected(self):
        import tempfile as tempfile_module
        with tempfile_module.TemporaryDirectory() as outside:
            external = Path(outside)
            (external / "new.png").write_bytes(b"external")
            (self.root / "logos").rename(self.root / "logos-original")
            (self.root / "logos").symlink_to(external, target_is_directory=True)
            patch = MetadataPatch(0, "evidence", True, tvg_logo="logos/new.png")
            with self.assertRaisesRegex(ValueError, "real repository directory"):
                apply_metadata_patches(BASE, [patch], self.root)

    def test_symlinked_logo_target_rejected(self):
        external = self.root / "outside.png"
        external.write_bytes(b"external")
        (self.root / "logos" / "linked.png").symlink_to(external)
        patch = MetadataPatch(0, "evidence", True, tvg_logo="logos/linked.png")
        with self.assertRaisesRegex(ValueError, "cannot contain symlinks"):
            apply_metadata_patches(BASE, [patch], self.root)

if __name__=="__main__":
    unittest.main()
