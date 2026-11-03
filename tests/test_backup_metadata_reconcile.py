"""Tests for exact-ID-only Backup country/language reconciliation."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from reconcile_backup_metadata_exact_id import reconcile_text


class BackupMetadataReconciliationTests(unittest.TestCase):
    def test_fills_language_and_corrects_country_from_exact_primary_id(self):
        text = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="DiscoveryKids.au" tvg-name="Discovery Kids" tvg-language="eng" tvg-country="AU" group-title="Kids",Discovery Kids\n'
            'https://stream.example/primary.m3u8\n'
            '#EXTINF:-1 tvg-id="DiscoveryKids.au" tvg-name="Discovery Kids" tvg-country="IN" group-title="Backup",Discovery Kids\n'
            'https://stream.example/backup.m3u8\n'
        )
        updated, languages, countries, ambiguous, unmatched = reconcile_text(text)
        self.assertEqual(len(languages), 1)
        self.assertEqual(len(countries), 1)
        self.assertIn('tvg-country="AU"', updated)
        self.assertIn('tvg-language="eng" group-title="Backup"', updated)
        self.assertEqual(ambiguous, [])
        self.assertEqual(unmatched, [])

    def test_does_not_overwrite_ambiguous_country(self):
        text = (
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-country="IN" tvg-language="hin" group-title="Indian Entertainment",Example\n'
            'https://stream.example/one.m3u8\n'
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-country="PK" tvg-language="urd" group-title="Pakistani",Example\n'
            'https://stream.example/two.m3u8\n'
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-country="GB" group-title="Backup",Example\n'
            'https://stream.example/backup.m3u8\n'
        )
        updated, languages, countries, ambiguous, unmatched = reconcile_text(text)
        self.assertEqual(updated, text)
        self.assertEqual(languages, [])
        self.assertEqual(countries, [])
        self.assertEqual(len(ambiguous), 1)
        self.assertEqual(unmatched, [])

    def test_does_not_guess_conflicting_language(self):
        text = (
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-country="IN" tvg-language="ben" group-title="Indian Bangla",Example\n'
            'https://stream.example/one.m3u8\n'
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-country="IN" tvg-language="eng" group-title="Indian Entertainment",Example\n'
            'https://stream.example/two.m3u8\n'
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-country="IN" group-title="Backup",Example\n'
            'https://stream.example/backup.m3u8\n'
        )
        updated, languages, countries, ambiguous, unmatched = reconcile_text(text)
        self.assertEqual(updated, text)
        self.assertEqual(languages, [])
        self.assertEqual(countries, [])
        self.assertEqual(len(ambiguous), 1)

    def test_preserves_existing_backup_language(self):
        text = (
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-country="IN" tvg-language="hin" group-title="Indian Entertainment",Example\n'
            'https://stream.example/primary.m3u8\n'
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-country="IN" tvg-language="eng" group-title="Backup",Example\n'
            'https://stream.example/backup.m3u8\n'
        )
        updated, languages, countries, _, _ = reconcile_text(text)
        self.assertEqual(updated, text)
        self.assertEqual(languages, [])
        self.assertEqual(countries, [])

    def test_stream_urls_are_preserved(self):
        text = (
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-country="IN" tvg-language="hin" group-title="Indian Entertainment",Example\n'
            'https://stream.example/primary.m3u8\n'
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" group-title="Backup",Example\n'
            'https://stream.example/backup.m3u8\n'
        )
        updated, _, _, _, _ = reconcile_text(text)
        before = [line for line in text.splitlines() if line.startswith("https://")]
        after = [line for line in updated.splitlines() if line.startswith("https://")]
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
