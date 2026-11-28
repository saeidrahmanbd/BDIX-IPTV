"""Regression tests for active IPTV ordering and contiguous channel numbering."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from renumber_active_channels import normalize_playlist_text


class ActiveChannelNumberingTests(unittest.TestCase):
    def setUp(self):
        self.sample = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="b" tvg-name="Zeta" tvg-chno="99" group-title="Bangladesh",Zeta\n'
            'https://stream.example/zeta.m3u8\n'
            '#EXTINF:-1 tvg-id="a" tvg-name="Alpha" tvg-chno="12" group-title="Bangladesh",Alpha\n'
            'https://stream.example/alpha.m3u8\n'
            '#EXTINF:-1 tvg-id="q" tvg-name="Queue B" tvg-chno="700" group-title="Backup",Queue B\n'
            'https://stream.example/queue-b.m3u8\n'
            '#EXTINF:-1 tvg-id="n" tvg-name="New B" tvg-chno="701" group-title="New Channels",New B\n'
            'https://stream.example/new-b.m3u8\n'
            '#EXTINF:-1 tvg-id="nb" tvg-name="New Backup B" tvg-chno="702" group-title="New Backups",New Backup B\n'
            'https://stream.example/new-backup-b.m3u8\n'
            '#EXTINF:-1 tvg-id="r" tvg-name="Review Existing" tvg-chno="703" group-title="Review",Review Existing\n'
            'https://stream.example/review-existing.m3u8\n'
            '#EXTINF:-1 tvg-id="rm" tvg-name="Review Missing" group-title="Review",Review Missing\n'
            'https://stream.example/review-missing.m3u8\n'
            '#EXTINF:-1 tvg-id="m" tvg-name="Movie" group-title="Indian Movies",Movie\n'
            'https://stream.example/movie.m3u8\n'
        )

    def test_only_missing_active_numbers_are_filled_and_existing_numbers_are_preserved(self):
        updated, count = normalize_playlist_text(self.sample)
        self.assertEqual(count, 3)
        self.assertIn('tvg-name="Zeta" tvg-chno="99"', updated)
        self.assertIn('tvg-name="Alpha" tvg-chno="12"', updated)
        self.assertIn('tvg-name="Movie" tvg-chno="1"', updated)
        self.assertLess(updated.index(",Zeta"), updated.index(",Alpha"))
        self.assertLess(updated.index(",Alpha"), updated.index(",Movie"))

    def test_review_and_discovery_queues_preserve_existing_numbers_without_filling_missing_ones(self):
        updated, _ = normalize_playlist_text(self.sample)
        self.assertLess(updated.index(",Queue B"), updated.index(",New B"))
        self.assertLess(updated.index(",New B"), updated.index(",New Backup B"))
        self.assertIn('tvg-chno="700"', updated)
        self.assertIn('tvg-chno="701"', updated)
        self.assertIn('tvg-chno="702"', updated)
        self.assertIn('tvg-chno="703"', updated)
        review_missing = next(
            line for line in updated.splitlines()
            if line.startswith("#EXTINF:") and 'tvg-name="Review Missing"' in line
        )
        self.assertNotIn("tvg-chno=", review_missing)

    def test_stream_url_inventory_is_unchanged(self):
        updated, _ = normalize_playlist_text(self.sample)
        before = [line for line in self.sample.splitlines() if line.startswith("http")]
        after = [line for line in updated.splitlines() if line.startswith("http")]
        self.assertEqual(sorted(before), sorted(after))

    def test_operation_is_idempotent(self):
        updated, _ = normalize_playlist_text(self.sample)
        again, count = normalize_playlist_text(updated)
        self.assertEqual(again, updated)
        self.assertEqual(count, 3)


if __name__ == "__main__":
    unittest.main()
