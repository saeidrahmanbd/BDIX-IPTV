import csv
import hashlib
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_report_freshness import check_reports  # noqa: E402

NOW = datetime(2026, 11, 8, 12, 0, tzinfo=timezone.utc)
STAMP = "2026-11-08T11:00:00+00:00"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class IptvOnlyEpgFreshnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "IPTV-Playlist.m3u").write_text(
            '#EXTM3U\n#EXTINF:-1 tvg-id="sample.bd" group-title="Bangladesh",Sample\nhttps://example.invalid/a.m3u8\n',
            encoding="utf-8")
        (self.root / "International-Playlist.m3u").write_text(
            '#EXTM3U\n#EXTINF:-1 tvg-id="intl.sample",Intl\nhttps://intl.example.invalid/b.m3u8\n', encoding="utf-8")
        (self.root / "epg").mkdir()
        (self.root / "epg" / "epg.xml").write_text(
            '<?xml version="1.0"?><tv><channel id="sample.bd"/></tv>\n', encoding="utf-8")
        (self.root / "reports").mkdir()
        self.write_reports()

    def tearDown(self):
        self.temp.cleanup()

    def iptv(self):
        return sha(self.root / "IPTV-Playlist.m3u")

    def write_reports(self):
        reports = self.root / "reports"
        one = self.iptv()
        epg = f"Generated: **{STAMP}**\n- IPTV-Playlist.m3u SHA-256: **{one}**\n"
        for name in ("epg-coverage.md", "epg-playlist-audit.md", "epg-unmapped-audit.md"):
            (reports / name).write_text(epg, encoding="utf-8")
        (reports / "epg-publish-freshness.md").write_text(f"Checked: **{STAMP}**\nStatus: **PASS**\n", encoding="utf-8")
        (reports / "epg-timing-audit.md").write_text(f"Generated: **{STAMP}**\n", encoding="utf-8")
        rows = [{"category": "NO_SOURCE_MAPPING_ID", "group": "Bangladesh", "channel": "Sample", "tvg_id": "sample.bd"}]
        with (reports / "epg-research-inventory.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        csv_sha = sha(reports / "epg-research-inventory.csv")
        (reports / "epg-research-inventory.md").write_text(
            f"# EPG Research Inventory\n\nGenerated: **{STAMP}**\n\n"
            f"- IPTV-Playlist.m3u SHA-256: **{one}**\n"
            f"- Usable now: **0**\n- Channels needing research: **1** (check: 1 − 0 = 1)\n",
            encoding="utf-8")
        data = {
            "generated_at": STAMP, "inventory_sha256": one, "guide_sha256": sha(self.root / "epg" / "epg.xml"),
            "research_inventory_records": 1, "research_inventory_usable_now": 0,
            "research_inventory_csv_sha256": csv_sha,
        }
        (reports / "epg-iptv-coverage.json").write_text(json.dumps(data), encoding="utf-8")

    def epg_errors(self):
        return check_reports(self.root, now=NOW, mode="epg")

    def test_baseline_passes(self):
        self.assertEqual(self.epg_errors(), [])

    def test_iptv_change_invalidates_iptv_epg_reports(self):
        with (self.root / "IPTV-Playlist.m3u").open("a", encoding="utf-8") as handle:
            handle.write("# change\n")
        errors = self.epg_errors()
        for name in ("epg-coverage.md", "epg-playlist-audit.md", "epg-unmapped-audit.md"):
            self.assertTrue(any(f"{name}: fingerprint does not match current IPTV-Playlist.m3u" in e for e in errors), name)
        self.assertTrue(any("epg-iptv-coverage.json: inventory_sha256" in e for e in errors))

    def test_international_change_does_not_invalidate_iptv_epg_reports(self):
        with (self.root / "International-Playlist.m3u").open("a", encoding="utf-8") as handle:
            handle.write("# change\n")
        self.assertEqual(self.epg_errors(), [])

    def test_missing_international_playlist_does_not_break_epg_validation(self):
        (self.root / "International-Playlist.m3u").unlink()
        self.assertEqual(self.epg_errors(), [])

    def test_missing_research_inventory_fails(self):
        (self.root / "reports" / "epg-research-inventory.csv").unlink()
        errors = self.epg_errors()
        self.assertTrue(any("epg-research-inventory.csv: missing" in e for e in errors))

    def test_stale_research_json_fails(self):
        data = json.loads((self.root / "reports" / "epg-iptv-coverage.json").read_text(encoding="utf-8"))
        data["generated_at"] = "2026-10-01T00:00:00+00:00"
        (self.root / "reports" / "epg-iptv-coverage.json").write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(any("epg-iptv-coverage.json: stale" in e for e in self.epg_errors()))

    def test_json_and_markdown_counts_must_match_csv(self):
        data = json.loads((self.root / "reports" / "epg-iptv-coverage.json").read_text(encoding="utf-8"))
        data["research_inventory_records"] = 2
        (self.root / "reports" / "epg-iptv-coverage.json").write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(any("research_inventory_records does not match CSV" in e for e in self.epg_errors()))

    def test_markdown_count_mismatch_fails(self):
        md = self.root / "reports" / "epg-research-inventory.md"
        md.write_text(md.read_text(encoding="utf-8").replace("**1** (check", "**5** (check"), encoding="utf-8")
        self.assertTrue(any("channel count does not match CSV" in e for e in self.epg_errors()))

    def test_guide_change_without_regeneration_fails(self):
        (self.root / "epg" / "epg.xml").write_text("<tv><channel id=\"other\"/></tv>\n", encoding="utf-8")
        self.assertTrue(any("guide_sha256 does not match" in e for e in self.epg_errors()))


if __name__ == "__main__":
    unittest.main()
