from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import reorganize_international_playlist as international_reorg


def playlist_rows(path):
    rows = []
    current = None
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if line.startswith("#EXTINF:"):
            attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', line))
            comma = line.find(",")
            display = line[comma + 1:].strip() if comma >= 0 else ""
            current = {"line": line_number, "attrs": attrs, "display": display, "raw": line}
        elif current and line.strip().startswith(("http://", "https://")):
            rows.append(current)
            current = None
    return rows


class PlaylistMetadataRepairTests(unittest.TestCase):
    def test_all_playlists_advertise_the_public_xmltv_guide(self):
        expected = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml"
        for name in ("IPTV-Playlist.m3u", "International-Playlist.m3u"):
            with self.subTest(playlist=name):
                header = (ROOT / name).read_text(encoding="utf-8-sig").splitlines()[0]
                self.assertIn(f'url-tvg="{expected}"', header)
                self.assertIn(f'x-tvg-url="{expected}"', header)

    def test_main_playlist_has_no_empty_logo_attributes(self):
        rows = playlist_rows(ROOT / "IPTV-Playlist.m3u")
        self.assertGreater(len(rows), 900)
        self.assertFalse([row for row in rows if row["attrs"].get("tvg-logo") == ""])

    def test_foreign_radio_and_vod_names_cannot_be_queued_as_movie_music(self):
        target, kind, reason = international_reorg.classify(
            {"tvg-id": "DismarRadioTV.py@SD", "tvg-content": "Music"},
            "Dismar Radio TV",
            "Paraguay",
            "PY",
        )
        self.assertIsNone(target)
        self.assertEqual(reason, "test/VOD/non-TV name")

    def test_international_backup_groups_use_the_plural_review_queue_contract(self):
        rows = playlist_rows(ROOT / "International-Playlist.m3u")
        # "New Backups" is the canonical plural review queue; only the
        # obsolete standalone "Backups" group is forbidden.
        legacy = [row for row in rows if row["attrs"].get("group-title", "").casefold() == "backups"]
        self.assertEqual(legacy, [])

        organizer = (ROOT / "scripts/reorganize_international_playlist.py").read_text(encoding="utf-8")
        self.assertIn('TAIL = ["Fashion TV", "Documentary & Wildlife", "Kids", "Religious", "Sports", "Adult", "Review", "New Channels", "New Backups", "Backup"]', organizer)
        self.assertIn('return "Backup", None, None', organizer)
        self.assertNotIn('target = "Backups"', organizer)
        self.assertNotIn('emit(row, "Backups"', organizer)
        self.assertIn('emit(row, "New Backups"', organizer)

    def test_international_playlist_names_are_present_and_empty_logos_removed(self):
        rows = playlist_rows(ROOT / "International-Playlist.m3u")
        self.assertGreater(len(rows), 2000)
        missing_names = [row for row in rows if not row["attrs"].get("tvg-name", "").strip()]
        empty_logos = [row for row in rows if row["attrs"].get("tvg-logo") == ""]
        self.assertEqual(missing_names, [])
        self.assertEqual(empty_logos, [])

    def test_main_worker_serves_xmltv_and_keeps_safe_stream_redirects(self):
        expected = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml"
        for name in ("xtream-main",):
            with self.subTest(worker=name):
                source = (ROOT / name / "worker.js").read_text(encoding="utf-8")
                self.assertIn(f'const EPG_URL = "{expected}"', source)
                self.assertRegex(source, r'if\s*\(p\s*===\s*"/xmltv\.php"\)')
                self.assertIn("fetch(EPG_URL", source)
                self.assertIn('"content-type":"application/xml; charset=utf-8"', source)
                self.assertNotIn("Programme guide disabled pending verified redistribution rights", source)
                self.assertIn("url-tvg=", source)
                self.assertIn("status:302", source)
                self.assertIn('"Location":s.url', source)
                self.assertNotRegex(source, r'fetch\(s\.url')
                self.assertIn("function constantTimeEqual", source)
                self.assertIn("function stableId", source)

    def test_adult_entries_are_explicitly_protected_from_maintenance(self):
        normalizer = (ROOT / "scripts/normalize_metadata.py").read_text(encoding="utf-8")
        logo_migration = (ROOT / "scripts/migrate_external_logos_fixed.py").read_text(encoding="utf-8")
        cross_playlist = (ROOT / "scripts/backfill_cross_playlist_metadata.py").read_text(encoding="utf-8")
        self.assertIn('"Adult"', normalizer.split("EXCLUDE=", 1)[1].split("\\n", 1)[0])
        self.assertIn('if g == "Adult":', normalizer)
        self.assertIn('if group == "Adult":', normalizer)
        self.assertIn('casefold() == "adult"', logo_migration)
        self.assertIn('"adult"', cross_playlist.split("REVIEW_GROUPS =", 1)[1].split("\\n", 1)[0])


if __name__ == "__main__":
    unittest.main()
