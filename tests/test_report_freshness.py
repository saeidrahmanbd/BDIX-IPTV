import hashlib
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_report_freshness import check_reports, stream_url_inventory_sha256


class ReportFreshnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.now = datetime(2026, 10, 20, 12, 0, tzinfo=timezone.utc)
        self.timestamp = "2026-10-20T11:00:00+00:00"
        (self.root / "IPTV-Playlist.m3u").write_text(
            "#EXTM3U\n#EXTINF:-1 tvg-id=\"sample.bd\",Sample\nhttps://example.invalid/live.m3u8\n",
            encoding="utf-8",
        )
        (self.root / "International-Playlist.m3u").write_text(
            "#EXTM3U\n#EXTINF:-1 tvg-id=\"intl.sample\",International Sample\nhttps://intl.example.invalid/live.m3u8\n",
            encoding="utf-8",
        )
        self.hashes = {
            name: hashlib.sha256((self.root / name).read_bytes()).hexdigest()
            for name in ("IPTV-Playlist.m3u", "International-Playlist.m3u")
        }
        report_dir = self.root / "reports"
        report_dir.mkdir()
        one = self.hashes["IPTV-Playlist.m3u"]
        two = self.hashes["International-Playlist.m3u"]
        epg = f"Generated: **{self.timestamp}**\n- IPTV-Playlist.m3u SHA-256: **{one}**\n- International-Playlist.m3u SHA-256: **{two}**\n"
        reports = {
            "iptv-playlist-audit.md": f"Generated: **{self.timestamp}**\nSource playlist SHA-256: **{one}**\n",
            "pre-publish-gate.md": f"Generated: **{self.timestamp}**\nSource playlist SHA-256: **{one}**\n",
            "epg-coverage.md": epg, "epg-playlist-audit.md": epg, "epg-unmapped-audit.md": epg,
            "iptv-metadata-backfill.md": f"Generated: **{self.timestamp}**\nPlaylist SHA-256: **{one}**\n",
            "iptv-fragile-streams.md": f"Generated: **{self.timestamp}**\nIPTV-Playlist.m3u SHA-256: **{one}**\n",
            "stream-risk-review.md": f"Generated: **{self.timestamp}**\nIPTV-Playlist.m3u SHA-256: **{one}**\n",
            "epg-publish-freshness.md": f"Checked: **{self.timestamp}**\nStatus: **PASS**\n",
            "logo-provenance-review.md": epg,
            "logo-asset-quality-audit.md": epg,
            "playlist-metadata-backfill.md": epg,
            "iptv-channel-discovery.md": f"# IPTV Channel Discovery\n\nGenerated: **{self.timestamp}**\n",
            "metadata-normalization.md": f"Generated: **{self.timestamp}**\nSource playlist SHA-256: **{one}**\n",
            "Update Report.md": f"_Last generated: **{self.timestamp}**_\n\nSource playlist SHA-256: **{one}**\n",
            "maintenance-report.md": f"_Generated: **{self.timestamp}**_\n\nSource playlist SHA-256: **{one}**\n",
            "playlist-logo-repair-results.md": f"Generated: **{self.timestamp}**\nSource playlist SHA-256: **{one}**\n",
            "stream-health.md": f"Generated: **{self.timestamp}**\nStream URL inventory SHA-256: **{stream_url_inventory_sha256(self.root / 'IPTV-Playlist.m3u')}**\n",
        }
        for name, content in reports.items():
            (report_dir / name).write_text(content, encoding="utf-8")
        (report_dir / "logo-authenticity-manifest.json").write_text(
            json.dumps({"generated_at_utc": self.timestamp, "source_sha256_by_playlist": self.hashes}),
            encoding="utf-8",
        )
        # IPTV-only EPG research outputs, consistent with the fixture's playlist and guide.
        (self.root / "epg").mkdir()
        (self.root / "epg" / "epg.xml").write_text('<tv><channel id="sample.bd"/></tv>\n', encoding="utf-8")
        (report_dir / "epg-research-inventory.csv").write_text("category,tvg_id\nNO_SOURCE_MAPPING_ID,sample.bd\n", encoding="utf-8")
        csv_sha = hashlib.sha256((report_dir / "epg-research-inventory.csv").read_bytes()).hexdigest()
        (report_dir / "epg-research-inventory.md").write_text(
            f"# EPG Research Inventory\n\nGenerated: **{self.timestamp}**\n\n"
            f"- IPTV-Playlist.m3u SHA-256: **{self.hashes['IPTV-Playlist.m3u']}**\n"
            "- Usable now: **0**\n- Channels needing research: **1** (check: 1 − 0 = 1)\n",
            encoding="utf-8",
        )
        (report_dir / "epg-iptv-coverage.json").write_text(
            json.dumps({
                "generated_at": self.timestamp,
                "inventory_sha256": self.hashes["IPTV-Playlist.m3u"],
                "guide_sha256": hashlib.sha256((self.root / "epg" / "epg.xml").read_bytes()).hexdigest(),
                "research_inventory_records": 1,
                "research_inventory_usable_now": 0,
                "research_inventory_csv_sha256": csv_sha,
            }),
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_current_reports_match_both_core_playlists(self):
        self.assertEqual(check_reports(self.root, now=self.now), [])

    def test_generated_mode_also_requires_current_stream_health(self):
        self.assertEqual(check_reports(self.root, now=self.now, mode="generated"), [])
        report = self.root / "reports" / "stream-health.md"
        report.write_text(report.read_text(encoding="utf-8").replace(self.timestamp, "2026-10-17T08:00:00+00:00"), encoding="utf-8")
        errors = check_reports(self.root, now=self.now, mode="generated")
        self.assertTrue(any("stream-health.md: stale report" in item for item in errors))

    def test_playlist_change_invalidates_its_fingerprinted_reports(self):
        with (self.root / "IPTV-Playlist.m3u").open("a", encoding="utf-8") as stream:
            stream.write("# metadata-only change\n")
        errors = check_reports(self.root, now=self.now)
        self.assertTrue(any("fingerprint does not match current IPTV-Playlist.m3u" in item for item in errors))

    def test_international_change_does_not_invalidate_iptv_epg_coverage_reports(self):
        # EPG headline coverage is IPTV-only; International changes must not gate those reports.
        with (self.root / "International-Playlist.m3u").open("a", encoding="utf-8") as stream:
            stream.write("# change\n")
        errors = check_reports(self.root, now=self.now, epg_publication_approved=False)
        self.assertFalse(any("epg-coverage.md" in item and "International-Playlist.m3u" in item for item in errors))
        self.assertFalse(any("epg-playlist-audit.md" in item and "International-Playlist.m3u" in item for item in errors))
        self.assertTrue(any("logo-authenticity-manifest.json: fingerprint does not match current International-Playlist.m3u" in item for item in errors))

    def test_stale_epg_report_is_reported(self):
        report = self.root / "reports" / "epg-coverage.md"
        report.write_text(report.read_text(encoding="utf-8").replace(self.timestamp, "2026-10-17T08:00:00+00:00"), encoding="utf-8")
        errors = check_reports(self.root, now=self.now, epg_publication_approved=True)
        self.assertTrue(any("epg-coverage.md: stale report" in item for item in errors))

    def test_epg_mode_checks_reports_without_legacy_approval_flag(self):
        errors = check_reports(self.root, now=self.now, mode="epg", epg_publication_approved=False)
        self.assertEqual(errors, [])
        report = self.root / "reports" / "epg-unmapped-audit.md"
        report.write_text(report.read_text(encoding="utf-8").replace(self.timestamp, "2026-10-17T08:00:00+00:00"), encoding="utf-8")
        errors = check_reports(self.root, now=self.now, mode="epg", epg_publication_approved=False)
        self.assertTrue(any("epg-unmapped-audit.md: stale report" in item for item in errors))
        self.assertFalse(any("logo-authenticity-manifest.json" in item for item in errors))

    def test_metadata_read_only_report_marker_is_accepted(self):
        report = self.root / "reports" / "iptv-metadata-backfill.md"
        report.write_text(f"Generated: **{self.timestamp}**\nPlaylist SHA-256: **{self.hashes['IPTV-Playlist.m3u']}**\n", encoding="utf-8")
        errors = check_reports(self.root, now=self.now)
        self.assertFalse(any("iptv-metadata-backfill.md" in error and "fingerprint" in error for error in errors))

    def test_discovery_report_must_match_current_bangladesh_date_even_within_48_hours(self):
        report = self.root / "reports" / "iptv-channel-discovery.md"
        report.write_text(
            "# IPTV Channel Discovery\n\nGenerated: **2026-10-19T10:00:00+00:00**\n",
            encoding="utf-8",
        )
        errors = check_reports(self.root, now=self.now, mode="discovery")
        self.assertTrue(any(
            "iptv-channel-discovery.md: discovery report was not regenerated for the current Bangladesh date" in item
            for item in errors
        ))

    def test_discovery_mode_checks_only_discovery_owned_reports(self):
        self.assertEqual(check_reports(self.root, now=self.now, mode="discovery"), [])
        # Stream-health belongs to playlist maintenance; discovery must not fail
        # because that separate report has not yet been regenerated.
        health = self.root / "reports" / "stream-health.md"
        health.write_text("Generated: **2026-10-20T11:00:00+00:00**\nStream URL inventory SHA-256: **" + ("0" * 64) + "**\n", encoding="utf-8")
        self.assertEqual(check_reports(self.root, now=self.now, mode="discovery"), [])
        with (self.root / "IPTV-Playlist.m3u").open("a", encoding="utf-8") as stream:
            stream.write("# discovery changed final playlist bytes\n")
        errors = check_reports(self.root, now=self.now, mode="discovery")
        self.assertTrue(any("metadata-normalization.md: fingerprint does not match" in item for item in errors))
        self.assertTrue(any("logo-asset-quality-audit.md: fingerprint does not match" in item for item in errors))
        self.assertTrue(any("playlist-logo-repair-results.md: fingerprint does not match" in item for item in errors))
        self.assertTrue(any("logo-authenticity-manifest.json: fingerprint does not match" in item for item in errors))
        self.assertFalse(any("stream-health.md" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
