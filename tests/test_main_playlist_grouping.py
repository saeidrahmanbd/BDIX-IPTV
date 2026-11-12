import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "reclassify_main_playlist_groups.py"


def entry(name, group, url, country, language="", content="", channel_id=None):
    cid = channel_id or f"{name.replace(' ', '')}.{country.lower()}"
    return (
        f'#EXTINF:-1 tvg-id="{cid}" tvg-name="{name}" tvg-country="{country}" '
        f'tvg-language="{language}" tvg-content="{content}" tvg-logo="logos/{name.replace(" ", "-").lower()}.png" '
        f'group-title="{group}",{name}\n{url}\n'
    )


class MainPlaylistGroupingTests(unittest.TestCase):
    def run_script(self, playlist_rows):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "IPTV-Playlist.m3u").write_text("#EXTM3U\n" + playlist_rows, encoding="utf-8")
            Path(tmp, "International-Playlist.m3u").write_text("#EXTM3U\n", encoding="utf-8")
            Path(tmp, "reports").mkdir()
            result = subprocess.run(
                [sys.executable, str(SCRIPT)], cwd=tmp,
                env=dict(os.environ, PYTHONPATH=str(ROOT / "scripts")),
                capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            return Path(tmp, "IPTV-Playlist.m3u").read_text(encoding="utf-8"), Path(tmp, "reports", "iptv-grouping-corrections.md").read_text(encoding="utf-8")

    def test_evidence_backed_bangladesh_and_indian_grouping(self):
        source = (
            entry("Somoy TV", "International", "https://bd.example/somoy.m3u8", "BD", "ben")
            + entry("Star Jalsha Movies", "Indian Entertainment", "https://in.example/movies.m3u8", "IN", "ben", "Movies")
            + entry("9XM Music", "Indian Entertainment", "https://in.example/music.m3u8", "IN", "hin", "Music")
            + entry("Pogo Kids", "Indian Entertainment", "https://in.example/kids.m3u8", "IN", "hin", "Kids")
            + entry("Star Sports 1", "Indian Entertainment", "https://in.example/sports.m3u8", "IN", "hin", "Sports")
        )
        out, report = self.run_script(source)
        self.assertIn('group-title="Bangladesh"', out)
        self.assertIn('group-title="Indian Movies"', out)
        self.assertIn('group-title="Indian Music"', out)
        self.assertIn('group-title="Kids"', out)
        self.assertIn('group-title="Sports"', out)
        for url in ("https://bd.example/somoy.m3u8", "https://in.example/movies.m3u8",
                    "https://in.example/music.m3u8", "https://in.example/kids.m3u8",
                    "https://in.example/sports.m3u8"):
            self.assertIn(url, out)
        self.assertIn("Verified primary rows reclassified: **5**", report)

    def test_indian_policy_excluded_stream_stays_out_of_review(self):
        source = entry("Indian Quran Channel", "Indian Entertainment", "https://in.example/quran.m3u8", "IN", "hin")
        out, report = self.run_script(source)
        self.assertIn('group-title="Indian Entertainment"', out)
        self.assertNotIn('group-title="Review"', out)
        self.assertIn("https://in.example/quran.m3u8", out)
        self.assertIn("policy-excluded", report)

    def test_manual_queues_and_adult_are_untouched(self):
        source = (
            entry("Review Movie", "Review", "https://x/review.m3u8", "IN", "hin", "Movies")
            + entry("Backup Movie", "Backup", "https://x/backup.m3u8", "IN", "hin", "Movies")
            + entry("New Sports", "New Channels", "https://x/new.m3u8", "IN", "hin", "Sports")
            + entry("Adult Channel", "Adult", "https://x/adult.m3u8", "US", "eng")
        )
        out, _ = self.run_script(source)
        for group, url in (("Review", "review"), ("Backup", "backup"),
                           ("New Channels", "new"), ("Adult", "adult")):
            self.assertIn(f'group-title="{group}"', out)
            self.assertIn(f"https://x/{url}.m3u8", out)

    def test_unverified_country_is_not_guessed(self):
        source = entry("Unknown Channel", "International", "https://x/unknown.m3u8", "US", "eng")
        out, report = self.run_script(source)
        self.assertIn('group-title="International"', out)
        self.assertIn("not conclusively verified", report)

    def test_group_repair_changes_only_group_title_and_keeps_every_url(self):
        source = entry("Somoy TV", "International", "https://bd.example/somoy.m3u8", "BD", "ben")
        before = source.splitlines()
        out, _ = self.run_script(source)
        after = out.splitlines()
        original_info = before[0].replace('group-title="International"', 'group-title="__GROUP__"')
        corrected_info = after[1].replace('group-title="Bangladesh"', 'group-title="__GROUP__"')
        self.assertEqual(original_info, corrected_info)
        self.assertEqual(before[1], after[2])
        self.assertIn('group-title="Bangladesh"', after[1])


if __name__ == "__main__":
    unittest.main()
