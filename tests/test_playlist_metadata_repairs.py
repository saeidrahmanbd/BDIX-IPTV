from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


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
    def test_no_playlist_advertises_the_unapproved_xmltv_guide(self):
        for name in ("IPTV-Playlist.m3u", "BDIX-Playlist.m3u", "International-Playlist.m3u"):
            with self.subTest(playlist=name):
                header = (ROOT / name).read_text(encoding="utf-8-sig").splitlines()[0]
                self.assertNotIn("url-tvg=", header.casefold())
                self.assertNotIn("x-tvg-url=", header.casefold())
                self.assertNotIn("epg.xml", header.casefold())

    def test_main_playlist_has_no_empty_logo_attributes(self):
        rows = playlist_rows(ROOT / "IPTV-Playlist.m3u")
        self.assertGreater(len(rows), 1000)
        self.assertFalse([row for row in rows if row["attrs"].get("tvg-logo") == ""])

    def test_international_playlist_names_are_present_and_empty_logos_removed(self):
        rows = playlist_rows(ROOT / "International-Playlist.m3u")
        self.assertGreater(len(rows), 2000)
        missing_names = [row for row in rows if not row["attrs"].get("tvg-name", "").strip()]
        empty_logos = [row for row in rows if row["attrs"].get("tvg-logo") == ""]
        self.assertEqual(missing_names, [])
        self.assertEqual(empty_logos, [])

    def test_bdix_test_rows_are_quarantined_and_known_names_corrected(self):
        rows = playlist_rows(ROOT / "BDIX-Playlist.m3u")
        self.assertFalse([row for row in rows if row["attrs"].get("group-title") == "Test"])
        expected = {
            "DBCNews.bd": "DBC News",
            "DeshTV.bd": "Desh TV",
            "EkattorTV.bd": "Ekattor TV",
            "News24.bd": "News 24",
        }
        indexed = {row["attrs"].get("tvg-id"): row for row in rows}
        for channel_id, name in expected.items():
            with self.subTest(channel_id=channel_id):
                self.assertIn(channel_id, indexed)
                self.assertEqual(indexed[channel_id]["attrs"].get("tvg-name"), name)
                self.assertEqual(indexed[channel_id]["attrs"].get("group-title"), "Not Playing")

    def test_both_workers_fail_closed_for_xmltv_and_use_redirects(self):
        for name in ("xtream-main", "xtream-bdix"):
            with self.subTest(worker=name):
                source = (ROOT / name / "worker.js").read_text(encoding="utf-8")
                self.assertNotIn("EPG_URL", source)
                self.assertNotIn("epg/epg.xml", source)
                self.assertRegex(source, r'if\s*\(p\s*===\s*"/xmltv\.php"\)')
                self.assertRegex(source, r'Programme guide disabled pending verified redistribution rights')
                self.assertRegex(source, r'xml\("Programme guide disabled pending verified redistribution rights\.",410\)')
                self.assertRegex(source, r'status:\s*302[^}]*Location:\s*s\.url')
                self.assertNotRegex(source, r'fetch\(s\.url')
                self.assertIn("function constantTimeEqual", source)
                self.assertIn("function stableId", source)


if __name__ == "__main__":
    unittest.main()
