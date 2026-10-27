import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from pre_publish_gate import referenced_logo_file, referenced_logo_relative_path, RAW_BASE


class PrePublishLogoPathTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "logos"
        self.root.mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def test_nested_logo_asset_preserves_subdirectory_and_query_is_ignored(self):
        path = self.root / "international" / "music" / "channel.png"
        path.parent.mkdir(parents=True)
        path.write_bytes(b"png")
        url = RAW_BASE + "international/music/channel.png?raw=1"
        self.assertEqual(referenced_logo_relative_path(url), Path("international/music/channel.png"))
        self.assertEqual(referenced_logo_file(url, self.root), path.resolve())

    def test_root_level_logo_still_resolves(self):
        path = self.root / "channel.png"
        path.write_bytes(b"png")
        url = RAW_BASE + "channel.png"
        self.assertEqual(referenced_logo_file(url, self.root), path.resolve())

    def test_encoded_filename_is_decoded(self):
        path = self.root / "channel logo.png"
        path.write_bytes(b"png")
        url = RAW_BASE + "channel%20logo.png"
        self.assertEqual(referenced_logo_file(url, self.root), path.resolve())

    def test_path_traversal_is_rejected(self):
        self.assertIsNone(referenced_logo_relative_path(RAW_BASE + "../secrets.txt"))
        self.assertIsNone(referenced_logo_file(RAW_BASE + "../secrets.txt", self.root))

    def test_non_repository_logo_is_not_resolved_as_local(self):
        self.assertIsNone(referenced_logo_file("https://example.invalid/logos/channel.png", self.root))


if __name__ == "__main__":
    unittest.main()
