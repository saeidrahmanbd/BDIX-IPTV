import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))
import verify_international_protected as guard  # noqa: E402


def entry(name, group, url, extra=""):
    return f'#EXTINF:-1 tvg-id="{name}.xx" tvg-name="{name}" {extra}group-title="{group}",{name}\n{url}\n'


class ProtectedGuardTests(unittest.TestCase):
    def run_guard(self, before, after, command_after=None):
        with tempfile.TemporaryDirectory() as tmp:
            old = Path.cwd()
            os.chdir(tmp)
            try:
                guard.PLAYLIST = Path("International-Playlist.m3u")
                guard.BASELINE = Path("baseline.json")
                Path("International-Playlist.m3u").write_text("#EXTM3U\n" + before, encoding="utf-8")
                self.assertEqual(guard.main(["g", "snapshot"]), 0)
                Path("International-Playlist.m3u").write_text("#EXTM3U\n" + after, encoding="utf-8")
                return guard.main(["g", "verify"])
            finally:
                os.chdir(old)

    def test_removal_of_backup_stream_fails(self):
        before = entry("A", "Backup", "http://a/1.m3u8") + entry("B", "Backup", "http://b/1.m3u8")
        self.assertEqual(self.run_guard(before, entry("A", "Backup", "http://a/1.m3u8")), 1)

    def test_not_playing_removal_fails(self):
        before = entry("A", "Not Playing", "http://a/1.m3u8")
        self.assertEqual(self.run_guard(before, ""), 1)

    def test_unprotected_removal_and_attribute_changes_pass(self):
        before = entry("A", "Backup", "http://a/1.m3u8") + entry("N", "New Channels", "http://n/1.m3u8")
        after = entry("A", "Backup", "http://a/1.m3u8", extra='tvg-country="IN" ')
        self.assertEqual(self.run_guard(before, after), 0)


class ReorganizePreservesProtectedTests(unittest.TestCase):
    def test_policy_does_not_delete_backup_entries(self):
        playlist = "#EXTM3U\n#PLAYLIST-STUDIO-NAME: Test\n" + entry("CNN", "Backup", "http://news.example/cnn.m3u8", 'tvg-country="US" ') \
            + entry("Hum TV Extra", "Backup", "http://orphan.example/hum.m3u8", 'tvg-country="PK" ') \
            + entry("RTSH Shqip", "New Channels", "http://rtsh.example/1.m3u8", 'tvg-country="AL" tvg-content="Movies" ')
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "International-Playlist.m3u").write_text(playlist, encoding="utf-8")
            Path(tmp, "reports").mkdir()
            env = dict(os.environ, PYTHONPATH=str(SCRIPTS))
            r = subprocess.run([sys.executable, str(SCRIPTS / "reorganize_international_playlist.py")],
                               cwd=ROOT if False else tmp, env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            out = Path(tmp, "International-Playlist.m3u").read_text(encoding="utf-8")
        self.assertIn("http://news.example/cnn.m3u8", out)
        self.assertIn("http://orphan.example/hum.m3u8", out)
        self.assertNotIn("http://rtsh.example/1.m3u8", out)

    def test_foreign_country_groups_accept_movie_music_only(self):
        header = "#EXTM3U\n#PLAYLIST-STUDIO-NAME: Test\n"
        legacy = "".join(entry(f"Cinema World {i}", "United States", f"http://us.example/{i}.m3u8", 'tvg-country="US" tvg-content="Movies" ') for i in range(6))
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "International-Playlist.m3u").write_text(header + legacy, encoding="utf-8")
            Path(tmp, "reports").mkdir()
            r = subprocess.run([sys.executable, str(SCRIPTS / "reorganize_international_playlist.py")], cwd=tmp,
                               env=dict(os.environ, PYTHONPATH=str(SCRIPTS)), capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            out = Path(tmp, "International-Playlist.m3u").read_text(encoding="utf-8")
        for i in range(6):
            self.assertIn(f"http://us.example/{i}.m3u8", out)

    def test_candidates_remain_in_manual_review_queues_and_follow_regional_rules(self):
        header = "#EXTM3U\n#PLAYLIST-STUDIO-NAME: Test\n"
        rows = "".join([
            entry("World Cinema", "New Channels", "http://world.example/movie.m3u8", 'tvg-country="US" tvg-content="Movies" '),
            entry("World Cinema Alternate", "New Backups", "http://world.example/backup.m3u8", 'tvg-country="US" tvg-content="Movies" '),
            entry("Channel 24", "New Channels", "http://bd.example/news.m3u8", 'tvg-country="BD" '),
            entry("DD Sports", "New Channels", "http://in.example/sports.m3u8", 'tvg-country="IN" '),
            entry("Aaj Tak", "New Channels", "http://in.example/news.m3u8", 'tvg-country="IN" '),
            entry("Madani TV", "New Channels", "http://in.example/religious.m3u8", 'tvg-country="IN" '),
            entry("Gyan Darshan", "New Channels", "http://in.example/education.m3u8", 'tvg-country="IN" '),
            entry("Disney Junior", "New Channels", "http://in.example/kids.m3u8", 'tvg-country="IN" '),
            entry("World News", "New Channels", "http://us.example/news.m3u8", 'tvg-country="US" tvg-content="Movies" '),
        ])
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "International-Playlist.m3u").write_text(header + rows, encoding="utf-8")
            Path(tmp, "reports").mkdir()
            r = subprocess.run([sys.executable, str(SCRIPTS / "reorganize_international_playlist.py")],
                               cwd=tmp, env=dict(os.environ, PYTHONPATH=str(SCRIPTS)),
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            out = Path(tmp, "International-Playlist.m3u").read_text(encoding="utf-8")
        self.assertIn('group-title="New Channels",World Cinema', out)
        self.assertIn('group-title="New Backups",World Cinema Alternate', out)
        self.assertIn('group-title="New Channels",Channel 24', out)
        self.assertIn('group-title="New Channels",DD Sports', out)
        for prohibited in ("Aaj Tak", "Madani TV", "Gyan Darshan", "Disney Junior", "World News"):
            self.assertNotIn(prohibited, out)

    def test_country_group_requires_five_unique_primary_names_and_ignores_backup(self):
        header = "#EXTM3U\n#PLAYLIST-STUDIO-NAME: Test\n"
        four = "".join(
            entry(f"Albania Movie {i}", "International", f"http://al.example/{i}.m3u8", 'tvg-country="AL" tvg-content="Movies" ')
            for i in range(1, 5)
        )
        duplicate_backup = entry("Albania Movie 1", "Backup", "http://al.example/backup.m3u8", 'tvg-country="AL" tvg-content="Movies" ')
        five = "".join(
            entry(f"Belarus Music {i}", "International", f"http://by.example/{i}.m3u8", 'tvg-country="BY" tvg-content="Music" ')
            for i in range(1, 6)
        )
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "International-Playlist.m3u").write_text(header + four + duplicate_backup + five, encoding="utf-8")
            Path(tmp, "reports").mkdir()
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "reorganize_international_playlist.py")],
                cwd=tmp, env=dict(os.environ, PYTHONPATH=str(SCRIPTS)), capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            output = Path(tmp, "International-Playlist.m3u").read_text(encoding="utf-8")
        self.assertEqual(output.count('group-title="International"'), 4)
        self.assertEqual(output.count('group-title="Belarus"'), 5)
        self.assertEqual(output.count('group-title="Backup"'), 1)
        self.assertNotIn('group-title="Albania"', output)
        self.assertIn('"Belarus"', output)
        self.assertIn('"International"', output)


if __name__ == "__main__":
    unittest.main()
