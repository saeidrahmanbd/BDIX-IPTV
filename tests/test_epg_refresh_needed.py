import hashlib
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from epg_refresh_needed import PLAYLIST_NAMES, assess_freshness


class EPGRefreshNeededTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.now = datetime(2026, 10, 27, 10, 0, tzinfo=timezone.utc)
        timestamp = (self.now - timedelta(minutes=30)).isoformat(timespec="seconds")
        self.hashes = {}
        for index, name in enumerate(PLAYLIST_NAMES):
            path = self.root / name
            path.write_text(f"#EXTM3U\n# playlist {index}\n", encoding="utf-8")
            self.hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        reports = self.root / "reports"
        reports.mkdir()
        report = "Generated: **" + timestamp + "**\n" + "".join(
            f"- {name} SHA-256: **{self.hashes[name]}**\n" for name in PLAYLIST_NAMES
        )
        for name in ("epg-coverage.md", "epg-three-playlist-audit.md"):
            (reports / name).write_text(report, encoding="utf-8")
        (reports / "epg-publish-freshness.md").write_text(
            f"Checked: **{timestamp}**\nStatus: **PASS**\n", encoding="utf-8"
        )
        guide = self.root / "epg"
        guide.mkdir()
        (guide / "epg.xml").write_text(
            '<?xml version="1.0"?><tv><channel id="sample"/><programme start="20261027090000 +0000" stop="20261027100000 +0000" channel="sample"><title>News</title></programme></tv>',
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_fresh_current_guide_skips_duplicate_refresh(self):
        skip, reasons = assess_freshness(self.root, now=self.now, max_age_hours=8)
        self.assertTrue(skip, reasons)

    def test_playlist_change_requires_refresh(self):
        with (self.root / PLAYLIST_NAMES[0]).open("a", encoding="utf-8") as stream:
            stream.write("# changed playlist\n")
        skip, reasons = assess_freshness(self.root, now=self.now, max_age_hours=8)
        self.assertFalse(skip)
        self.assertTrue(any("fingerprint does not match current IPTV-Playlist.m3u" in x for x in reasons))

    def test_stale_freshness_report_requires_refresh(self):
        freshness = self.root / "reports" / "epg-publish-freshness.md"
        old = (self.now - timedelta(hours=9)).isoformat(timespec="seconds")
        freshness.write_text(f"Checked: **{old}**\nStatus: **PASS**\n", encoding="utf-8")
        skip, reasons = assess_freshness(self.root, now=self.now, max_age_hours=8)
        self.assertFalse(skip)
        self.assertTrue(any("epg-publish-freshness.md: stale report" in x for x in reasons))

    def test_failed_freshness_status_requires_refresh(self):
        freshness = self.root / "reports" / "epg-publish-freshness.md"
        freshness.write_text(freshness.read_text(encoding="utf-8").replace("PASS", "FAIL"), encoding="utf-8")
        skip, reasons = assess_freshness(self.root, now=self.now, max_age_hours=8)
        self.assertFalse(skip)
        self.assertTrue(any("status is not PASS" in x for x in reasons))

    def test_missing_programme_entries_requires_refresh(self):
        (self.root / "epg" / "epg.xml").write_text("<tv><channel id=\"sample\"/></tv>", encoding="utf-8")
        skip, reasons = assess_freshness(self.root, now=self.now, max_age_hours=8)
        self.assertFalse(skip)
        self.assertTrue(any("contains no programme entries" in x for x in reasons))

    def test_stale_playlist_report_requires_refresh(self):
        stale = (self.now - timedelta(hours=9)).isoformat(timespec="seconds")
        report = "Generated: **" + stale + "**\n" + "".join(
            f"- {name} SHA-256: **{self.hashes[name]}**\n" for name in PLAYLIST_NAMES
        )
        (self.root / "reports" / "epg-coverage.md").write_text(report, encoding="utf-8")
        skip, reasons = assess_freshness(self.root, now=self.now, max_age_hours=8)
        self.assertFalse(skip)
        self.assertTrue(any("epg-coverage.md: stale report" in x for x in reasons))


if __name__ == "__main__":
    unittest.main()
