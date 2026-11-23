import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from pre_publish_gate import primary_channel_number_collisions


def row(number, name, group, url):
    info = f'#EXTINF:-1 tvg-chno="{number}" tvg-name="{name}" group-title="{group}",{name}'
    return (info, {"tvg-chno": str(number), "tvg-name": name, "group-title": group}, url)


class PrimaryChannelNumberCollisionTests(unittest.TestCase):
    def test_unchanged_preexisting_collision_is_detected_for_warning_only(self):
        baseline = [
            row("618", "Fashion&LifeStyle", "International", "https://example.test/fashion.m3u8"),
            row("618", "DD Sports", "Sports", "https://example.test/ddsports.m3u8"),
        ]
        current = list(baseline)
        old_collisions = primary_channel_number_collisions(baseline)
        new_collisions = primary_channel_number_collisions(current)

        self.assertEqual(set(new_collisions), {"618"})
        self.assertEqual(old_collisions["618"], new_collisions["618"])

    def test_new_duplicate_number_is_detected(self):
        baseline = [
            row("618", "Fashion&LifeStyle", "International", "https://example.test/fashion.m3u8"),
        ]
        current = baseline + [
            row("618", "DD Sports", "Sports", "https://example.test/ddsports.m3u8"),
        ]
        old_collisions = primary_channel_number_collisions(baseline)
        new_collisions = primary_channel_number_collisions(current)

        self.assertIn("618", new_collisions)
        self.assertNotEqual(old_collisions.get("618"), new_collisions["618"])

    def test_changed_member_of_existing_collision_is_detected(self):
        baseline = [
            row("619", "FashionTV", "International", "https://example.test/fashion.m3u8"),
            row("619", "DraftKings Network", "Sports", "https://example.test/draftkings.m3u8"),
        ]
        current = [
            baseline[0],
            row("619", "Different Channel", "Sports", "https://example.test/different.m3u8"),
        ]
        old_collisions = primary_channel_number_collisions(baseline)
        new_collisions = primary_channel_number_collisions(current)

        self.assertNotEqual(old_collisions.get("619"), new_collisions["619"])

    def test_single_number_reused_in_backup_does_not_count_as_primary_collision(self):
        entries = [
            row("620", "Primary", "International", "https://example.test/primary.m3u8"),
            row("620", "Alternate", "Backup", "https://example.test/backup.m3u8"),
        ]
        self.assertEqual(primary_channel_number_collisions(entries), {})


if __name__ == "__main__":
    unittest.main()
