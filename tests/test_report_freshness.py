import hashlib
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_report_freshness import check_reports


class ReportFreshnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.now = datetime(2026, 10, 20, 12, 0, tzinfo=timezone.utc)
        (self.root / "IPTV-Playlist.m3u").write_text(
            "#EXTM3U\n#EXTINF:-1 tvg-id=\"sample.bd\",Sample\nhttps://example.invalid/live.m3u8\n",
            encoding="utf-8",
        )
        digest = hashlib.sha256((self.root / "IPTV-Playlist.m3u").read_bytes()).hexdigest()
        (self.root / "reports").mkdir()
        markdown_reports = {
            "playlist-audit.md": f"Generated: **2026-10-20T11:00:00+00:00**\nSource playlist SHA-256: **{digest}**\n",
            "pre-publish-gate.md": f"Generated: **2026-10-20T11:00:00+00:00**\nSource playlist SHA-256: **{digest}**\n",
            "epg-coverage.md": f"Generated: **2026-10-20T11:00:00+00:00**\n- IPTV-Playlist.m3u SHA-256: **{digest}**\n",
            "epg-three-playlist-audit.md": f"Generated: **2026-10-20T11:00:00+00:00**\n- IPTV-Playlist.m3u SHA-256: **{digest}**\n",
        }
        for name, text in markdown_reports.items():
            (self.root / "reports" / name).write_text(text, encoding="utf-8")
        (self.root / "reports" / "logo-authenticity-manifest.json").write_text(
            json.dumps({
                "generated_at_utc": "2026-10-20T11:00:00+00:00",
                "source_sha256_by_playlist": {"IPTV-Playlist.m3u": digest},
            }),
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_current_matching_reports_pass(self):
        self.assertEqual(check_reports(self.root, now=self.now), [])

    def test_playlist_change_invalidates_old_reports(self):
        with (self.root / "IPTV-Playlist.m3u").open("a", encoding="utf-8") as stream:
            stream.write("# metadata-only change\n")
        errors = check_reports(self.root, now=self.now)
        self.assertTrue(any("fingerprint does not match" in item for item in errors))

    def test_stale_epg_report_is_reported(self):
        report = self.root / "reports" / "epg-coverage.md"
        report.write_text(
            report.read_text(encoding="utf-8").replace(
                "2026-10-20T11:00:00+00:00", "2026-10-17T08:00:00+00:00"
            ),
            encoding="utf-8",
        )
        errors = check_reports(self.root, now=self.now)
        self.assertTrue(any("epg-coverage.md: stale report" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
