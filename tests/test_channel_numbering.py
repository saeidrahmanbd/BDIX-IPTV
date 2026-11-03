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
            '#EXTINF:-1 tvg-id="m" tvg-name="Movie" group-title="Indian Movies",Movie\n'
            'https://stream.example/movie.m3u8\n'
        )

    def test_active_entries_are_sorted_and_numbered_gaplessly(self):
        updated, count = normalize_playlist_text(self.sample)
        self.assertEqual(count, 3)
        self.assertIn('tvg-name="Alpha" tvg-chno="1"', updated)
        self.assertIn('tvg-name="Zeta" tvg-chno="2"', updated)
        self.assertIn('tvg-name="Movie" tvg-chno="3"', updated)
        self.assertLess(updated.index(",Alpha"), updated.index(",Zeta"))
        self.assertLess(updated.index(",Zeta"), updated.index(",Movie"))

    def test_review_queues_are_unnumbered_and_keep_internal_order(self):
        updated, _ = normalize_playlist_text(self.sample)
        self.assertLess(updated.index(",New B"), updated.index(",Queue B"))
        self.assertNotIn('tvg-chno="700"', updated)
        self.assertNotIn('tvg-chno="701"', updated)

    def test_stream_url_inventory_is_unchanged(self):
        updated, _ = normalize_playlist_text(self.sample)
        before = [line for line in self.sample.splitlines() if line.startswith("http")]
        after = [line for line in updated.splitlines() if line.startswith("http")]
        self.assertEqual(before, after)

    def test_operation_is_idempotent(self):
        updated, _ = normalize_playlist_text(self.sample)
        again, count = normalize_playlist_text(updated)
        self.assertEqual(again, updated)
        self.assertEqual(count, 3)


if __name__ == "__main__":
    unittest.main()
