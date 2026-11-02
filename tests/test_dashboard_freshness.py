import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_dashboard import (parse, playlist_counts, url_inventory_sha, epg_report_fingerprints_match, epg_audit_headers_ok)
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


    def test_epg_report_uses_exact_playlist_fingerprints(self):
        with tempfile.TemporaryDirectory() as directory:
            paths = []
            report_lines = []
            for name, content in (
                ("IPTV-Playlist.m3u", "#EXTM3U\nA\n"),
                ("International-Playlist.m3u", "#EXTM3U\nC\n"),
            ):
                path = Path(directory) / name
                path.write_text(content, encoding="utf-8")
                paths.append((name, path))
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                report_lines.append(f"- {name} SHA-256: **{digest}**")
            report = "\n".join(report_lines)
            self.assertTrue(epg_report_fingerprints_match(report, paths))
            paths[1][1].write_text("#EXTM3U\nchanged\n", encoding="utf-8")
            self.assertFalse(epg_report_fingerprints_match(report, paths))

    def test_epg_audit_requires_both_headers_ok(self):
        report = (
            "| IPTV-Playlist.m3u | 10 | 5 | OK |\n"
            "| International-Playlist.m3u | 20 | 12 | OK |\n"
        )
        self.assertTrue(epg_audit_headers_ok(report))
        self.assertFalse(epg_audit_headers_ok(report.replace(
            "International-Playlist.m3u | 20 | 12 | OK",
            "International-Playlist.m3u | 20 | 12 | MISMATCH",
        )))


if __name__ == "__main__":
    unittest.main()
