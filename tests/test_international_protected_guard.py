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

    def test_discovery_policy_scope_is_review_queues_only(self):
        header = "#EXTM3U\n#PLAYLIST-STUDIO-NAME: Test\n"
        legacy = "".join(entry(f"USA Network {i}", "United States", f"http://us.example/{i}.m3u8", 'tvg-country="US" tvg-content="Movies" ') for i in range(6))
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "International-Playlist.m3u").write_text(header + legacy, encoding="utf-8")
            Path(tmp, "reports").mkdir()
            r = subprocess.run([sys.executable, str(SCRIPTS / "reorganize_international_playlist.py")], cwd=tmp,
                               env=dict(os.environ, PYTHONPATH=str(SCRIPTS)), capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            out = Path(tmp, "International-Playlist.m3u").read_text(encoding="utf-8")
        for i in range(6):
            self.assertIn(f"http://us.example/{i}.m3u8", out)


if __name__ == "__main__":
    unittest.main()
