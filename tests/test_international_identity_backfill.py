import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from repair_international_playlist import build_primary_id_index, backfill_exact_tvg_id


class InternationalTvgIdBackfillTests(unittest.TestCase):
    def test_exact_unique_primary_name_is_backfilled(self):
        reference = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="BBCNews.uk" tvg-name="BBC News" group-title="International",BBC News\n'
            'https://example.test/bbc.m3u8\n'
            '#EXTINF:-1 tvg-id="BBCNews.uk" tvg-name="BBC News" group-title="Backup",BBC News Backup\n'
            'https://example.test/bbc-backup.m3u8\n'
        )
        ids = build_primary_id_index([reference])
        updated, changed = backfill_exact_tvg_id(
            '#EXTINF:-1 tvg-name="bbc news" group-title="International",bbc news',
            "International",
            ids,
        )
        self.assertTrue(changed)
        self.assertIn('tvg-id="BBCNews.uk"', updated)

    def test_conflicting_exact_name_ids_are_not_backfilled(self):
        a = (
            '#EXTINF:-1 tvg-id="News.uk" tvg-name="News One" group-title="International",News One\n'
            'https://example.test/news-a.m3u8\n'
        )
        b = (
            '#EXTINF:-1 tvg-id="News.in" tvg-name="News One" group-title="Indian Entertainment",News One\n'
            'https://example.test/news-b.m3u8\n'
        )
        ids = build_primary_id_index([a, b])
        original = '#EXTINF:-1 tvg-name="News One" group-title="International",News One'
        updated, changed = backfill_exact_tvg_id(original, "International", ids)
        self.assertFalse(changed)
        self.assertEqual(updated, original)

    def test_similar_names_with_different_qualifiers_are_not_merged(self):
        reference = (
            '#EXTINF:-1 tvg-id="StudioOne.uk" tvg-name="Studio One" group-title="International",Studio One\n'
            'https://example.test/studio-one.m3u8\n'
        )
        ids = build_primary_id_index([reference])
        original = '#EXTINF:-1 tvg-name="Studio One +" group-title="International",Studio One +'
        updated, changed = backfill_exact_tvg_id(original, "International", ids)
        self.assertFalse(changed)
        self.assertEqual(updated, original)

    def test_backup_and_existing_ids_are_preserved(self):
        reference = (
            '#EXTINF:-1 tvg-id="BBCNews.uk" tvg-name="BBC News" group-title="International",BBC News\n'
            'https://example.test/bbc.m3u8\n'
        )
        ids = build_primary_id_index([reference])
        backup = '#EXTINF:-1 tvg-name="BBC News" group-title="Backup",BBC News'
        updated, changed = backfill_exact_tvg_id(backup, "Backup", ids)
        self.assertFalse(changed)
        self.assertEqual(updated, backup)
        existing = '#EXTINF:-1 tvg-id="Custom.BBC" tvg-name="BBC News" group-title="International",BBC News'
        updated, changed = backfill_exact_tvg_id(existing, "International", ids)
        self.assertFalse(changed)
        self.assertEqual(updated, existing)


if __name__ == "__main__":
    unittest.main()
