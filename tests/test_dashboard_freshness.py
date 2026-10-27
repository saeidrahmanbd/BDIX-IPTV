import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_dashboard import parse, playlist_counts, url_inventory_sha
from stream_health import stream_url_inventory_sha256


class DashboardFreshnessTests(unittest.TestCase):
    def test_inventory_hash_matches_stream_health_generator(self):
        playlist = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-id="A.bd" group-title="Bangladesh",A\n'
            "https://example.invalid/a.m3u8\n"
            '#EXTINF:-1 tvg-id="B.in" group-title="Backup",B\n'
            "http://example.invalid/b.m3u8\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.m3u"
            path.write_text(playlist, encoding="utf-8")
            self.assertEqual(url_inventory_sha(playlist), stream_url_inventory_sha256(path))

    def test_playlist_count_excludes_only_backup_test_and_not_playing_ids(self):
        playlist = (
            "#EXTM3U\n"
            '#EXTINF:-1 tvg-id="A.bd" group-title="Bangladesh",A\n'
            "https://example.invalid/a.m3u8\n"
            '#EXTINF:-1 tvg-id="A.bd" group-title="Backup",A Backup\n'
            "https://example.invalid/a-backup.m3u8\n"
            '#EXTINF:-1 tvg-id="Q.bd" group-title="New Channels",Queue\n'
            "https://example.invalid/queue.m3u8\n"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.m3u"
            path.write_text(playlist, encoding="utf-8")
            rows = parse(path)
            self.assertEqual(len(rows), 3)
            self.assertEqual(playlist_counts(path), (3, 2))


if __name__ == "__main__":
    unittest.main()
