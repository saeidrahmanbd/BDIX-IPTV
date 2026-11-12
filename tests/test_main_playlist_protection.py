import json
import tempfile
import unittest
from collections import Counter
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import protect_main_playlist as guard


class MainPlaylistProtectionTests(unittest.TestCase):
    def write(self, path, rows):
        path.write_text(
            "#EXTM3U\n" + "".join(
                f'#EXTINF:-1 group-title="{g}" tvg-name="{n}",{n}\n{u}\n'
                for g, n, u in rows
            ),
            encoding="utf-8",
        )

    def run_guard(self, before, after):
        with tempfile.TemporaryDirectory() as d:
            p, s = Path(d) / "IPTV-Playlist.m3u", Path(d) / "state.json"
            self.write(p, before)
            guard.snapshot(p, s)
            self.write(p, after)
            guard.verify(p, s)

    def test_metadata_changes_and_new_rows_are_allowed(self):
        self.run_guard(
            [("Bangladesh", "A", "https://a"), ("Indian Movies", "B", "https://b")],
            [("Bangladesh", "A HD", "https://a"), ("Bangladesh", "New", "https://new"),
             ("Indian Movies", "B HD", "https://b")],
        )

    def test_verified_existing_group_correction_is_allowed(self):
        self.run_guard(
            [("International", "Bangla Movie", "https://a")],
            [("Indian Movies", "Bangla Movie", "https://a")],
        )

    def test_category_regrouping_and_existing_row_reordering_are_allowed(self):
        self.run_guard(
            [("Bangladesh", "A", "https://a"), ("Sports", "X", "https://x"),
             ("Bangladesh", "B", "https://b"), ("International", "I", "https://i"),
             ("Sports", "Y", "https://y")],
            [("Sports", "Y", "https://y"), ("Bangladesh", "B", "https://b"),
             ("International", "I", "https://i"), ("Sports", "X", "https://x"),
             ("Bangladesh", "A", "https://a")],
        )

    def test_existing_deletion_is_blocked(self):
        with tempfile.TemporaryDirectory() as d:
            p, s = Path(d) / "IPTV-Playlist.m3u", Path(d) / "state.json"
            self.write(p, [("Bangladesh", "A", "https://a"), ("Bangladesh", "B", "https://b")])
            guard.snapshot(p, s)
            self.write(p, [("Bangladesh", "B", "https://b")])
            with self.assertRaises(SystemExit):
                guard.verify(p, s)

    def test_existing_url_replacement_is_blocked(self):
        with tempfile.TemporaryDirectory() as d:
            p, s = Path(d) / "IPTV-Playlist.m3u", Path(d) / "state.json"
            self.write(p, [("Bangladesh", "A", "https://a")])
            guard.snapshot(p, s)
            self.write(p, [("Bangladesh", "A", "https://replacement")])
            with self.assertRaises(SystemExit):
                guard.verify(p, s)

    def test_duplicate_url_occurrence_is_not_silently_dropped(self):
        with tempfile.TemporaryDirectory() as d:
            p, s = Path(d) / "IPTV-Playlist.m3u", Path(d) / "state.json"
            self.write(p, [("Bangladesh", "A", "https://same"), ("Backup", "A alt", "https://same")])
            guard.snapshot(p, s)
            self.write(p, [("Bangladesh", "A", "https://same")])
            with self.assertRaises(SystemExit):
                guard.verify(p, s)


if __name__ == "__main__":
    unittest.main()
