import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from pre_publish_gate import referenced_logo_file, referenced_logo_relative_path, review_state, RAW_BASE, EXCLUDE, REVIEW_QUEUES


class PrePublishLogoPathTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "logos"
        self.root.mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def test_plural_new_backups_is_a_protected_review_queue_not_a_primary_group(self):
        self.assertIn("New Backups", EXCLUDE)
        self.assertIn("New Backups", REVIEW_QUEUES)
        self.assertNotIn("New Backup", REVIEW_QUEUES)

    def test_authorized_permanent_removal_is_not_reported_as_review_queue_deletion(self):
        info = '#EXTINF:-1 tvg-name="Aaj Tak" group-title="Not Playing",Aaj Tak'
        entries = [(info, {"tvg-name": "Aaj Tak", "group-title": "Not Playing"}, "https://example.invalid/aajtak.m3u8")]
        self.assertEqual(review_state(entries), {})

    def test_unapproved_review_entry_remains_in_protected_review_state(self):
        info = '#EXTINF:-1 tvg-name="Sample Channel" group-title="Backup",Sample Channel'
        entries = [(info, {"tvg-name": "Sample Channel", "group-title": "Backup"}, "https://example.invalid/sample.m3u8")]
        state = review_state(entries)
        self.assertIn("https://example.invalid/sample.m3u8", state)

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
