"""Regression tests for country-safe reconciliation of review-queue IDs."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "reconcile_playlist_consistency.py"


class ReconcilePlaylistCountryIdentityTests(unittest.TestCase):
    def run_reconciliation(self, active_id, active_country, review_id, review_country):
        text = (
            "#EXTM3U\n"
            f'#EXTINF:-1 tvg-id="{active_id}" tvg-name="Discovery Kids" '
            f'channel-id="{active_id}" tvg-country="{active_country}" group-title="Kids",Discovery Kids\n'
            "https://example.invalid/active.m3u8\n"
            f'#EXTINF:-1 tvg-id="{review_id}" tvg-name="Discovery Kids" '
            f'channel-id="{review_id}" tvg-country="{review_country}" group-title="New Backup",Discovery Kids\n'
            "https://example.invalid/review.m3u8\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "IPTV-Playlist.m3u"
            playlist.write_text(text, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT)],
                cwd=directory,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            lines = playlist.read_text(encoding="utf-8").splitlines()
        return [line for line in lines if line.startswith("#EXTINF:")], lines

    def test_review_id_is_not_rewritten_to_a_different_country(self):
        records, lines = self.run_reconciliation(
            "DiscoveryKids.au", "AU", "DiscoveryKids.in@SD", "IN"
        )
        review = next(line for line in records if 'group-title="New Backup"' in line)
        self.assertIn('tvg-id="DiscoveryKids.in@SD"', review)
        self.assertIn('channel-id="DiscoveryKids.in@SD"', review)
        self.assertIn("https://example.invalid/active.m3u8", lines)
        self.assertIn("https://example.invalid/review.m3u8", lines)

    def test_same_country_review_id_still_normalizes(self):
        records, _ = self.run_reconciliation(
            "DiscoveryKids.in@HD", "IN", "DiscoveryKids.in@SD", "IN"
        )
        review = next(line for line in records if 'group-title="New Backup"' in line)
        self.assertIn('tvg-id="DiscoveryKids.in@HD"', review)
        self.assertIn('channel-id="DiscoveryKids.in@HD"', review)


if __name__ == "__main__":
    unittest.main()
