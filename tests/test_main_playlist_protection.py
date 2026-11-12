import json
import tempfile
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import protect_main_playlist as guard

class MainPlaylistProtectionTests(unittest.TestCase):
    def write(self, path, rows):
        path.write_text("#EXTM3U\n" + "".join(f'#EXTINF:-1 group-title="{g}" tvg-name="{n}",{n}\n{u}\n' for g,n,u in rows), encoding="utf-8")

    def test_metadata_changes_and_new_rows_are_allowed(self):
        with tempfile.TemporaryDirectory() as d:
            p, s = Path(d)/"IPTV-Playlist.m3u", Path(d)/"state.json"
            self.write(p, [("Bangladesh","A","https://a"),("Indian Movies","B","https://b")])
            guard.snapshot(p,s)
            self.write(p, [("Bangladesh","A HD","https://a"),("Bangladesh","New","https://new"),("Indian Movies","B HD","https://b")])
            guard.verify(p,s)

    def test_existing_group_move_is_blocked(self):
        with tempfile.TemporaryDirectory() as d:
            p, s = Path(d)/"IPTV-Playlist.m3u", Path(d)/"state.json"
            self.write(p, [("Bangladesh","A","https://a")])
            guard.snapshot(p,s)
            self.write(p, [("Indian Movies","A","https://a")])
            with self.assertRaises(SystemExit):
                guard.verify(p,s)

    def test_category_regrouping_is_allowed_when_group_order_is_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            p, s = Path(d)/"IPTV-Playlist.m3u", Path(d)/"state.json"
            self.write(p, [
                ("Bangladesh","A","https://a"),
                ("Sports","X","https://x"),
                ("Bangladesh","B","https://b"),
                ("International","I","https://i"),
                ("Sports","Y","https://y"),
            ])
            guard.snapshot(p,s)
            self.write(p, [
                ("Bangladesh","A","https://a"),
                ("Bangladesh","B","https://b"),
                ("International","I","https://i"),
                ("Sports","X","https://x"),
                ("Sports","Y","https://y"),
            ])
            guard.verify(p,s)

    def test_existing_deletion_is_blocked(self):
        with tempfile.TemporaryDirectory() as d:
            p, s = Path(d)/"IPTV-Playlist.m3u", Path(d)/"state.json"
            self.write(p, [("Bangladesh","A","https://a"),("Bangladesh","B","https://b")])
            guard.snapshot(p,s)
            self.write(p, [("Bangladesh","B","https://b")])
            with self.assertRaises(SystemExit):
                guard.verify(p,s)

    def test_reordering_existing_rows_is_blocked(self):
        with tempfile.TemporaryDirectory() as d:
            p, s = Path(d)/"IPTV-Playlist.m3u", Path(d)/"state.json"
            self.write(p, [("Bangladesh","A","https://a"),("Bangladesh","B","https://b")])
            guard.snapshot(p,s)
            self.write(p, [("Bangladesh","B","https://b"),("Bangladesh","A","https://a")])
            with self.assertRaises(SystemExit):
                guard.verify(p,s)

if __name__ == "__main__":
    unittest.main()
