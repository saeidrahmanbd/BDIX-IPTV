"""Tests for exact-ID-only Backup language metadata backfill."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from backfill_backup_language_exact_id import backfill_text


class BackupLanguageBackfillTests(unittest.TestCase):
    def test_fills_language_from_exact_primary_id(self):
        text = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-language="ben" tvg-country="IN" group-title="Bangladesh",Example\n'
            'https://stream.example/primary.m3u8\n'
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-country="IN" group-title="Backup",Example\n'
            'https://stream.example/backup.m3u8\n'
        )
        updated, filled, ambiguous, unmatched = backfill_text(text)
        self.assertEqual(len(filled), 1)
        self.assertIn('tvg-language="ben" group-title="Backup"', updated)
        self.assertEqual(ambiguous, [])
        self.assertEqual(unmatched, [])

    def test_does_not_guess_conflicting_language(self):
        text = (
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-language="ben" group-title="Bangladesh",Example\n'
            'https://stream.example/one.m3u8\n'
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-language="eng" group-title="Indian Entertainment",Example\n'
            'https://stream.example/two.m3u8\n'
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" group-title="Backup",Example\n'
            'https://stream.example/backup.m3u8\n'
        )
        updated, filled, ambiguous, unmatched = backfill_text(text)
        self.assertEqual(updated, text)
        self.assertEqual(filled, [])
        self.assertEqual(len(ambiguous), 1)
        self.assertEqual(unmatched, [])

    def test_does_not_change_existing_backup_language(self):
        text = (
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-language="ben" group-title="Bangladesh",Example\n'
            'https://stream.example/primary.m3u8\n'
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-language="eng" group-title="Backup",Example\n'
            'https://stream.example/backup.m3u8\n'
        )
        updated, filled, ambiguous, unmatched = backfill_text(text)
        self.assertEqual(updated, text)
        self.assertEqual(filled, [])

    def test_stream_urls_are_preserved(self):
        text = (
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" tvg-language="hin" group-title="Indian Entertainment",Example\n'
            'https://stream.example/primary.m3u8\n'
            '#EXTINF:-1 tvg-id="X.in" tvg-name="Example" group-title="Backup",Example\n'
            'https://stream.example/backup.m3u8\n'
        )
        updated, _, _, _ = backfill_text(text)
        before = [line for line in text.splitlines() if line.startswith("https://")]
        after = [line for line in updated.splitlines() if line.startswith("https://")]
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
