import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from iptv_metadata_backfill import parse_catalogue, update_playlist, active_gaps


class MetadataBackfillTests(unittest.TestCase):
    def setUp(self):
        self.catalogue = parse_catalogue(
            "id,name,country,languages\n"
            "Example.in,Example,IN,hin\n"
            "Multi.in,Multi,IN,eng;hin\n"
            "Preserve.in,Preserve,IN,hin\n"
        )

    def test_exact_quality_suffix_match_fills_blank_fields(self):
        playlist = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-id="Example.in@HD" tvg-name="Example" group-title="Indian Movies",Example\n'
            "https://example.invalid/a.m3u8\n"
        )
        updated, metrics = update_playlist(playlist, self.catalogue)
        self.assertIn('tvg-country="IN"', updated)
        self.assertIn('tvg-language="hin"', updated)
        self.assertIn("https://example.invalid/a.m3u8", updated)
        self.assertEqual(metrics["entries_changed"], 1)
        self.assertEqual(metrics["country_fields_filled"], 1)
        self.assertEqual(metrics["language_fields_filled"], 1)

    def test_multilanguage_does_not_guess_primary_language(self):
        playlist = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-id="Multi.in" tvg-name="Multi" group-title="International",Multi\n'
            "https://example.invalid/multi.m3u8\n"
        )
        updated, metrics = update_playlist(playlist, self.catalogue)
        self.assertIn('tvg-country="IN"', updated)
        self.assertNotIn('tvg-language="', updated)
        self.assertEqual(metrics["language_fields_filled"], 0)

    def test_existing_metadata_is_never_overwritten(self):
        playlist = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-id="Preserve.in" tvg-name="Preserve" tvg-country="FR" tvg-language="fra" group-title="International",Preserve\n'
            "https://example.invalid/preserve.m3u8\n"
        )
        updated, metrics = update_playlist(playlist, self.catalogue)
        self.assertIn('tvg-country="FR"', updated)
        self.assertIn('tvg-language="fra"', updated)
        self.assertEqual(metrics["entries_changed"], 0)

    def test_protected_groups_and_unknown_ids_are_unchanged(self):
        playlist = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-id="Example.in" tvg-name="Backup" group-title="Backup",Backup\n'
            "https://example.invalid/backup.m3u8\n"
            '#EXTINF:-1 tvg-id="Unknown.custom" tvg-name="Unknown" group-title="International",Unknown\n'
            "https://example.invalid/unknown.m3u8\n"
            '#EXTINF:-1 tvg-id="Example.in" tvg-name="Review" group-title="Not Playing",Review\n'
            "https://example.invalid/review.m3u8\n"
        )
        updated, metrics = update_playlist(playlist, self.catalogue)
        self.assertEqual(updated, playlist)
        self.assertEqual(metrics["entries_changed"], 0)
        self.assertEqual(metrics["country_fields_filled"], 0)
        self.assertEqual(metrics["language_fields_filled"], 0)

    def test_all_original_urls_and_entry_count_are_preserved(self):
        playlist = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-id="Example.in" tvg-name="Example" group-title="Indian Movies",Example\n'
            "https://example.invalid/a.m3u8\n"
            '#EXTINF:-1 tvg-id="Unknown.custom" tvg-name="Unknown" group-title="International",Unknown\n'
            "https://example.invalid/b.m3u8\n"
        )
        updated, metrics = update_playlist(playlist, self.catalogue)
        self.assertEqual(
            [x for x in playlist.splitlines() if x.startswith(("http://", "https://"))],
            [x for x in updated.splitlines() if x.startswith(("http://", "https://"))],
        )
        self.assertEqual(
            sum(x.startswith("#EXTINF:") for x in playlist.splitlines()),
            sum(x.startswith("#EXTINF:") for x in updated.splitlines()),
        )
        self.assertEqual(len(active_gaps(updated)), 1)


if __name__ == "__main__":
    unittest.main()
