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

    def test_review_removal_fails_during_maintenance(self):
        before = entry("A", "Review", "http://a/1.m3u8")
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

    def test_health_review_entries_remain_in_review_after_reorganization(self):
        playlist = "#EXTM3U\n#PLAYLIST-STUDIO-NAME: Test\n" + entry("World Cinema", "Review", "http://review.example/cinema.m3u8", 'tvg-country="US" tvg-content="Movies" tvg-logo="logos/world-cinema.png" ')
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "International-Playlist.m3u").write_text(playlist, encoding="utf-8")
            Path(tmp, "reports").mkdir()
            Path(tmp, "logos").mkdir()
            Path(tmp, "logos", "world-cinema.png").write_bytes(b"logo")
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "reorganize_international_playlist.py")],
                cwd=tmp, env=dict(os.environ, PYTHONPATH=str(SCRIPTS)), capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            out = Path(tmp, "International-Playlist.m3u").read_text(encoding="utf-8")
        self.assertIn('group-title="Review"', out)
        self.assertIn('tvg-content="Movies"', out)
        self.assertIn('tvg-logo="logos/world-cinema.png"', out)

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


    def test_pakistan_uses_the_same_five_unique_primary_channel_threshold(self):
        header = "#EXTM3U\n#PLAYLIST-STUDIO-NAME: Test\n"
        four = "".join(
            entry(f"Pakistan Channel {i}", "Pakistani", f"http://pk.example/{i}.m3u8", 'tvg-country="PK" ')
            for i in range(1, 5)
        )
        five = "".join(
            entry(f"Pakistan Channel {i}", "Pakistani", f"http://pk5.example/{i}.m3u8", 'tvg-country="PK" ')
            for i in range(1, 6)
        )
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "International-Playlist.m3u").write_text(header + four, encoding="utf-8")
            Path(tmp, "reports").mkdir()
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "reorganize_international_playlist.py")],
                cwd=tmp, env=dict(os.environ, PYTHONPATH=str(SCRIPTS)), capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            four_output = Path(tmp, "International-Playlist.m3u").read_text(encoding="utf-8")

            Path(tmp, "International-Playlist.m3u").write_text(header + five, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "reorganize_international_playlist.py")],
                cwd=tmp, env=dict(os.environ, PYTHONPATH=str(SCRIPTS)), capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            five_output = Path(tmp, "International-Playlist.m3u").read_text(encoding="utf-8")

        self.assertEqual(four_output.count('group-title="International"'), 4)
        self.assertNotIn('group-title="Pakistani"', four_output)
        self.assertEqual(five_output.count('group-title="Pakistani"'), 5)
        self.assertNotIn('group-title="International"', five_output)

    def test_eligible_orphan_backup_is_promoted_and_counts_toward_threshold(self):
        header = "#EXTM3U\n#PLAYLIST-STUDIO-NAME: Test\n"
        four_primary = "".join(
            entry(f"Albania Movie {i}", "International", f"http://al.example/{i}.m3u8",
                  'tvg-country="AL" tvg-content="Movies" ')
            for i in range(1, 5)
        )
        orphan = entry(
            "Albania Movie 5", "Backup", "http://al.example/orphan.m3u8",
            'tvg-country="AL" tvg-content="Movies" '
        )
        same_channel_alternate = entry(
            "Albania Movie 1", "Backup", "http://al.example/alternate.m3u8",
            'tvg-country="AL" tvg-content="Movies" '
        )
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "International-Playlist.m3u").write_text(
                header + four_primary + orphan + same_channel_alternate, encoding="utf-8"
            )
            Path(tmp, "reports").mkdir()
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "reorganize_international_playlist.py")],
                cwd=tmp, env=dict(os.environ, PYTHONPATH=str(SCRIPTS)), capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            output = Path(tmp, "International-Playlist.m3u").read_text(encoding="utf-8")
            audit = Path(tmp, "reports", "international-playlist-audit.md").read_text(encoding="utf-8")

        self.assertEqual(output.count('group-title="Albania"'), 5)
        self.assertEqual(output.count('group-title="Backup"'), 1)
        self.assertIn("http://al.example/orphan.m3u8", output)
        self.assertIn("http://al.example/alternate.m3u8", output)
        self.assertIn("Eligible orphan Backup rows promoted to primary: 1", audit)
        self.assertIn("Matching alternate streams retained in Backup: 1", audit)
        self.assertIn("True orphan Backup rows evaluated: 1", audit)

    def test_adult_orphan_backup_is_restored_to_adult_group(self):
        header = "#EXTM3U\n#PLAYLIST-STUDIO-NAME: Test\n"
        adult_orphan = entry(
            "Pink Erotic 2", "Backup", "http://adult.example/pink-erotic-2.m3u8",
            'tvg-country="US" tvg-content="Adult" '
        )
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "International-Playlist.m3u").write_text(header + adult_orphan, encoding="utf-8")
            Path(tmp, "reports").mkdir()
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "reorganize_international_playlist.py")],
                cwd=tmp, env=dict(os.environ, PYTHONPATH=str(SCRIPTS)), capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            output = Path(tmp, "International-Playlist.m3u").read_text(encoding="utf-8")

        self.assertIn('group-title="Adult"', output)
        self.assertIn('tvg-content="Adult"', output)
        self.assertNotIn('group-title="Backup"', output)

    def test_review_queues_remain_manual_and_follow_regional_policy(self):
        header = "#EXTM3U\n#PLAYLIST-STUDIO-NAME: Test\n"
        rows = (
            entry("Bangladesh News", "New Channels", "http://bd.example/news.m3u8", 'tvg-logo="logos/bangladesh-news.png" tvg-country="BD" ')
            + entry("Indian Sports", "New Channels", "http://in.example/sports.m3u8", 'tvg-logo="logos/indian-sports.png" tvg-country="IN" ')
            + entry("Indian Education TV", "New Channels", "http://in.example/education.m3u8", 'tvg-logo="logos/indian-education-tv.png" tvg-country="IN" ')
            + entry("Indian Cartoon Kids", "New Channels", "http://in.example/kids.m3u8", 'tvg-logo="logos/indian-cartoon-kids.png" tvg-country="IN" ')
            + entry("Foreign Movie", "New Channels", "http://us.example/movie.m3u8", 'tvg-logo="logos/foreign-movie.png" tvg-country="US" tvg-content="Movies" ')
            + entry("Bangladesh Religious Alternate", "New Backups", "http://bd.example/religious-alt.m3u8", 'tvg-logo="logos/bangladesh-religious-alternate.png" tvg-country="BD" ')
        )
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "International-Playlist.m3u").write_text(header + rows, encoding="utf-8")
            Path(tmp, "reports").mkdir()
            Path(tmp, "logos").mkdir()
            for logo_name in (
                "bangladesh-news.png", "indian-sports.png", "indian-education-tv.png",
                "indian-cartoon-kids.png", "foreign-movie.png", "bangladesh-religious-alternate.png",
            ):
                Path(tmp, "logos", logo_name).write_bytes(b"logo")
            r = subprocess.run(
                [sys.executable, str(SCRIPTS / "reorganize_international_playlist.py")],
                cwd=tmp, env=dict(os.environ, PYTHONPATH=str(SCRIPTS)),
                capture_output=True, text=True,
            )
            self.assertEqual(r.returncode, 0, r.stderr)
            out = Path(tmp, "International-Playlist.m3u").read_text(encoding="utf-8")
        self.assertIn('group-title="New Channels" tvg-name="Bangladesh News",Bangladesh News', out)
        self.assertIn('group-title="New Channels" tvg-name="Indian Sports",Indian Sports', out)
        self.assertIn('group-title="New Channels" tvg-name="Foreign Movie",Foreign Movie', out)
        self.assertIn('group-title="New Backups" tvg-name="Bangladesh Religious Alternate",Bangladesh Religious Alternate', out)
        self.assertNotIn("Indian Education TV", out)
        self.assertIn('group-title="New Channels" tvg-name="Indian Cartoon Kids",Indian Cartoon Kids', out)
        self.assertIn('"New Backups"', out)

if __name__ == "__main__":
    unittest.main()
