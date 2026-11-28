import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from backfill_cross_playlist_metadata import backfill_text


class CrossPlaylistMetadataBackfillTests(unittest.TestCase):
    def test_dedicated_country_group_fills_country_and_channel_id_from_tvg_id(self):
        source = (
            '#EXTINF:-1 tvg-id="Example.de" tvg-name="Example" group-title="Germany",Example\n'
            'https://example.invalid/live.m3u8\n'
        )
        updated, counts = backfill_text(source, {}, {})
        self.assertIn('tvg-country="DE"', updated)
        self.assertIn('channel-id="Example.de"', updated)
        self.assertIn('tvg-language="und"', updated)
        self.assertEqual(counts["channel_id_fields_filled"], 1)
        self.assertEqual(counts["country_fields_filled_from_group"], 1)
        self.assertIn("https://example.invalid/live.m3u8", updated)

    def test_generic_genre_group_does_not_guess_country(self):
        source = (
            '#EXTINF:-1 tvg-id="Unknown.custom" tvg-name="Unknown" group-title="Sports",Unknown\n'
            'https://example.invalid/sports.m3u8\n'
        )
        updated, _ = backfill_text(source, {}, {})
        self.assertNotIn('tvg-country=', updated)
        self.assertIn('tvg-language="und"', updated)

    def test_review_adult_and_backup_queues_remain_untouched(self):
        source = (
            '#EXTINF:-1 tvg-id="A.custom" tvg-name="A" group-title="Adult",A\n'
            'https://example.invalid/a.m3u8\n'
            '#EXTINF:-1 tvg-id="B.custom" tvg-name="B" group-title="Review",B\n'
            'https://example.invalid/b.m3u8\n'
            '#EXTINF:-1 tvg-id="C.custom" tvg-name="C" group-title="Backup",C\n'
            'https://example.invalid/c.m3u8\n'
        )
        updated, counts = backfill_text(source, {}, {})
        self.assertEqual(updated, source)
        self.assertEqual(counts["entries_changed"], 0)


if __name__ == "__main__":
    unittest.main()
