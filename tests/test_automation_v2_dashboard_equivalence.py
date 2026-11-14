from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.audit_automation_v2_dashboard_equivalence import (
    compute_metrics, sha256, url_inventory_sha,
)

class DashboardEquivalenceTests(unittest.TestCase):
    def build_fixture(self, root: Path) -> dict:
        playlist = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="bd.one" group-title="Bangladesh",Bangla One\n'
            'https://example.test/bd.m3u8\n'
            '#EXTINF:-1 tvg-id="in.one" group-title="Indian Movies",Movie One\n'
            'https://example.test/in.m3u8\n'
            '#EXTINF:-1 tvg-id="in.one" group-title="Backup",Movie One Backup\n'
            'https://example.test/backup.m3u8\n'
            '#EXTINF:-1 tvg-id="new.one" group-title="New Channels",New One\n'
            'https://example.test/new.m3u8\n'
        )
        (root / "IPTV-Playlist.m3u").write_text(playlist, encoding="utf-8")
        (root / "International-Playlist.m3u").write_text(
            '#EXTM3U\n#EXTINF:-1 tvg-id="x" group-title="International",X\nhttps://example.test/x.m3u8\n',
            encoding="utf-8",
        )
        playlist_hash = sha256((root / "IPTV-Playlist.m3u").read_bytes())
        audit = [
            f"Source playlist SHA-256: **{playlist_hash}**",
            "- Healthy/local references: **3**",
        ]
        for label in (
            "Duplicate stream URLs", "Metadata conflicts", "Cross-country backup collisions",
            "Protected primary-entry changes", "Logo exceptions requiring repair",
            "Duplicate primary identities", "Primary channel-number collisions",
            "Primary entries missing channel numbers", "Malformed EXTINF entries",
            "Category block-order issues", "Alphabetical ordering issues",
        ):
            audit.append(f"- {label}: **0**")
        (root / "reports").mkdir()
        (root / "reports/iptv-playlist-audit.md").write_text("\n".join(audit), encoding="utf-8")
        urls_hash = url_inventory_sha(root / "IPTV-Playlist.m3u")
        (root / "reports/stream-health.md").write_text(
            f"Stream URL inventory SHA-256: **{urls_hash}**\n"
            "- Streams tested: **4**\n- Failed this check: **1**\n"
            "- Persistent failures (3+ consecutive): **1**\n"
            "- Near-duplicate URL families: **0**\n",
            encoding="utf-8",
        )
        (root / "reports/pre-publish-gate.md").write_text(
            f"Generated: **2026-11-14T00:00:00+00:00**\n"
            f"Source playlist SHA-256: **{playlist_hash}**\nStatus: **PASS**\n",
            encoding="utf-8",
        )
        epg_detail = (
            "| IPTV-Playlist.m3u | 4 | 2 | 1 | 1 | 1 | 1 | 1 | OK |\n"
            "| International-Playlist.m3u | 1 | 1 | 1 | 1 | 1 | 1 | 0 | OK |\n"
            f"- IPTV-Playlist.m3u SHA-256: **{playlist_hash}**\n"
            f"- International-Playlist.m3u SHA-256: **{sha256((root / 'International-Playlist.m3u').read_bytes())}**\n"
        )
        (root / "reports/epg-playlist-audit.md").write_text(epg_detail, encoding="utf-8")
        (root / "reports/epg-publish-freshness.md").write_text("Status: **PASS**\n", encoding="utf-8")
        (root / "epg").mkdir()
        (root / "epg/epg.xml").write_text(
            '<tv><channel id="bd.one"/><programme channel="bd.one" start="20261114000000 +0000" stop="20261114010000 +0000"><title>News</title></programme></tv>',
            encoding="utf-8",
        )
        return {
            "Streams": 4, "Active Channel Identities": 2, "Active Primary Streams": 2,
            "Bangladesh": 1, "India": 1, "Backup Stream Entries": 1,
            "IPTV Local Logos": "75.0%", "IPTV EPG Programme Coverage": "50%",
            "IPTV EPG Mapping": "50.0%", "Stream Health Tested": 4,
            "Stream Health Failures": 1, "Persistent Failures": 1,
            "Near-Duplicate URL Families": 0, "Audit Blocking Issues": 0,
            "Pre-Publish Gate": "PASS",
            "Pre-Publish Gate Generated": "2026-11-14T00:00:00+00:00",
        }

    def test_independently_recomputes_dashboard_metrics_and_detects_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            expected = self.build_fixture(root)
            report = compute_metrics(root)
            self.assertEqual(report["expected_metrics"], expected)
            self.assertTrue(all(report["inputs_current"].values()))
            self.assertFalse(report["equivalent"])
            dashboard = "\n".join(
                f"| {key} | **{value}** |" for key, value in expected.items()
            )
            (root / "reports/Update Report.md").write_text(dashboard, encoding="utf-8")
            report = compute_metrics(root)
            self.assertEqual(report["status"], "PASS")
            self.assertEqual(report["mismatches"], {})
            self.assertTrue(report["cutover_ready"])
            self.assertEqual(report["cutover_blockers"], [])

    def test_stale_audit_is_not_counted_as_current(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.build_fixture(root)
            audit = root / "reports/iptv-playlist-audit.md"
            audit.write_text(audit.read_text().replace("Source playlist SHA-256:", "Old playlist SHA-256:"), encoding="utf-8")
            report = compute_metrics(root)
            self.assertFalse(report["inputs_current"]["playlist_audit"])
            self.assertEqual(report["expected_metrics"]["IPTV Local Logos"], "STALE")
            self.assertEqual(report["expected_metrics"]["Audit Blocking Issues"], "STALE / UNKNOWN")
            self.assertFalse(report["cutover_ready"])
            self.assertIn("playlist_audit", report["cutover_blockers"])

if __name__ == "__main__":
    unittest.main()
