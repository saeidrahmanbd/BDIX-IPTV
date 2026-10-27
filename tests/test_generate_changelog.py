import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_changelog import compare, parse


class ChangelogTests(unittest.TestCase):
    def test_parser_handles_commas_inside_quoted_attributes(self):
        rows = parse(
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="Channel24.bd" tvg-name="Channel 24" '
            'group-title="News, Bangladesh",Channel 24 HD\n'
            'https://example.invalid/live.m3u8\n'
        )
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["id"], "Channel24.bd")
        self.assertEqual(rows[0]["group"], "News, Bangladesh")
        self.assertEqual(rows[0]["name"], "Channel 24")

    def test_compare_reports_new_channel_and_added_stream(self):
        old = (
            '#EXTINF:-1 tvg-id="Channel24.bd" tvg-name="Channel 24" group-title="Bangladesh",Channel 24\n'
            'https://example.invalid/one.m3u8\n'
        )
        new = old + (
            '#EXTINF:-1 tvg-id="NewsNow.bd" tvg-name="News Now" group-title="Bangladesh",News Now\n'
            'https://example.invalid/two.m3u8\n'
        )
        summary = compare(old, new)
        self.assertEqual(summary["added_channels"], 1)
        self.assertEqual(summary["added_urls"], 1)
        self.assertEqual(summary["removed_channels"], 0)

    def test_backup_url_replacement_is_not_counted_as_new_channel(self):
        old = (
            '#EXTINF:-1 tvg-id="Channel24.bd" tvg-name="Channel 24" group-title="Backup",Channel 24\n'
            'https://example.invalid/old.m3u8\n'
        )
        new = (
            '#EXTINF:-1 tvg-id="Channel24.bd" tvg-name="Channel 24" group-title="Backup",Channel 24\n'
            'https://example.invalid/new.m3u8\n'
        )
        summary = compare(old, new)
        self.assertEqual(summary["added_channels"], 0)
        self.assertEqual(summary["backup_updates"], 1)
        self.assertEqual(summary["added_urls"], 1)
        self.assertEqual(summary["removed_urls"], 1)


if __name__ == "__main__":
    unittest.main()
