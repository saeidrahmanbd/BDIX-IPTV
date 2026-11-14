import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from restore_protected_review import authorized_backup_migration_target


class ProtectedMigrationMetadataInputTests(unittest.TestCase):
    def test_parsed_attribute_dict_is_accepted_by_backup_migration_gate(self):
        attributes = {
            "tvg-name": "7X Punjabi",
            "group-title": "Backup",
        }
        url = "https://cdn2.in/7xPunjabihls/live.m3u8"
        self.assertEqual(
            authorized_backup_migration_target(attributes, url),
            "Indian Music",
        )

    def test_unapproved_url_stays_blocked_for_parsed_attribute_dict(self):
        attributes = {"tvg-name": "7X Punjabi", "group-title": "Backup"}
        self.assertIsNone(
            authorized_backup_migration_target(
                attributes, "https://example.invalid/other.m3u8"
            )
        )

    def test_extinf_string_input_remains_supported(self):
        info = (
            '#EXTINF:-1 tvg-name="7X Punjabi" '
            'group-title="Backup",7X Punjabi'
        )
        self.assertEqual(
            authorized_backup_migration_target(
                info, "https://cdn2.in/7xPunjabihls/live.m3u8"
            ),
            "Indian Music",
        )


if __name__ == "__main__":
    unittest.main()
