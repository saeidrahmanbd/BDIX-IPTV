import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from backfill_cross_playlist_metadata import backfill_text, build_indexes


class CrossPlaylistMetadataTests(unittest.TestCase):
    def test_exact_id_backfill_preserves_stream_url_and_existing_fields(self):
        text = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="BBCNews.uk" tvg-name="BBC News" tvg-logo="bbc.png" tvg-chno="11" group-title="International",BBC News\n'
            'https://example.test/bbc.m3u8\n'
        )
        updated, counts = backfill_text(text, {
            "BBCNews.uk": {"country": "GB", "language": "eng"}
        }, {})
        self.assertIn('tvg-country="GB"', updated)
        self.assertIn('tvg-language="eng"', updated)
        self.assertIn('tvg-chno="11"', updated)
        self.assertIn('https://example.test/bbc.m3u8', updated)
        self.assertEqual(counts["country_fields_filled"], 1)
        self.assertEqual(counts["language_fields_filled"], 1)

    def test_existing_metadata_is_never_overwritten(self):
        text = (
            '#EXTINF:-1 tvg-id="BBCNews.uk" tvg-name="BBC News" tvg-country="GB" tvg-language="eng" group-title="International",BBC News\n'
            'https://example.test/bbc.m3u8\n'
        )
        updated, counts = backfill_text(text, {
            "BBCNews.uk": {"country": "US", "language": "hin"}
        }, {})
        self.assertEqual(updated, text)
        self.assertEqual(counts["entries_changed"], 0)

    def test_backup_entries_are_untouched(self):
        text = (
            '#EXTINF:-1 tvg-id="BBCNews.uk" tvg-name="BBC News" group-title="Backup",BBC News Backup\n'
            'https://example.test/bbc-backup.m3u8\n'
        )
        updated, counts = backfill_text(text, {
            "BBCNews.uk": {"country": "GB", "language": "eng"}
        }, {})
        self.assertEqual(updated, text)
        self.assertEqual(counts["entries_changed"], 0)

    def test_name_propagation_index_requires_unique_id(self):
        a = Path("IPTV-Playlist.m3u")
        b = Path("BDIX-Playlist.m3u")
        first = (
            '#EXTINF:-1 tvg-id="BBCNews.uk" tvg-name="BBC News" tvg-country="GB" tvg-language="eng" group-title="International",BBC News\n'
            'https://example.test/a.m3u8\n'
        )
        second = (
            '#EXTINF:-1 tvg-id="BBCNews.uk" tvg-name="BBC News" tvg-country="GB" tvg-language="eng" group-title="International",BBC News\n'
            'https://example.test/b.m3u8\n'
        )
        by_id, by_name = build_indexes({a: first, b: second})
        self.assertEqual(by_id["BBCNews.uk"]["country"], "GB")
        self.assertEqual(by_name["bbc news"]["country"], "GB")


if __name__ == "__main__":
    unittest.main()
