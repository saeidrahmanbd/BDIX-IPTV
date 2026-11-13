import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "automation/core"))
sys.path.insert(0, str(ROOT / "automation/validators"))
from playlist_contract import assert_iptv_existing_rows_preserved, validate_discovery_queues
from policy_conformance import validate_policy

def row(name, url, group="Bangladesh", number="1", logo="logos/test.png"):
    return f'#EXTINF:-1 tvg-name="{name}" tvg-logo="{logo}" tvg-chno="{number}" group-title="{group}",{name}\n{url}\n'

class AutomationV2PolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = json.loads((ROOT / "automation/policy/policy.json").read_text(encoding="utf-8"))

    def test_central_policy_conforms(self):
        self.assertEqual(validate_policy(self.policy), [])

    def test_policy_rejects_weakening_url_protection(self):
        policy = json.loads(json.dumps(self.policy))
        policy["playlists"]["IPTV-Playlist.m3u"]["existing_rows"]["stream_urls"] = "mutable"
        self.assertTrue(validate_policy(policy))

    def test_metadata_and_logo_repairs_are_allowed(self):
        before = "#EXTM3U\n" + row("Channel A", "https://a.example/live.m3u8")
        after = "#EXTM3U\n" + row("Channel A HD", "https://a.example/live.m3u8", logo="logos/new.png")
        assert_iptv_existing_rows_preserved(before, after)

    def test_removal_is_rejected(self):
        before = "#EXTM3U\n" + row("Channel A", "https://a.example/live.m3u8")
        with self.assertRaisesRegex(ValueError, "URL occurrences removed"):
            assert_iptv_existing_rows_preserved(before, "#EXTM3U\n")

    def test_url_replacement_is_rejected(self):
        before = "#EXTM3U\n" + row("Channel A", "https://a.example/live.m3u8")
        after = "#EXTM3U\n" + row("Channel A", "https://a.example/other.m3u8")
        with self.assertRaises(ValueError):
            assert_iptv_existing_rows_preserved(before, after)

    def test_group_change_is_rejected(self):
        before = "#EXTM3U\n" + row("Channel A", "https://a.example/live.m3u8")
        after = "#EXTM3U\n" + row("Channel A", "https://a.example/live.m3u8", group="Backup")
        with self.assertRaisesRegex(ValueError, "group changed"):
            assert_iptv_existing_rows_preserved(before, after)

    def test_renumbering_is_rejected(self):
        before = "#EXTM3U\n" + row("Channel A", "https://a.example/live.m3u8", number="1")
        after = "#EXTM3U\n" + row("Channel A", "https://a.example/live.m3u8", number="9")
        with self.assertRaisesRegex(ValueError, "channel number changed"):
            assert_iptv_existing_rows_preserved(before, after)

    def test_reordering_is_rejected(self):
        before = "#EXTM3U\n" + row("A", "https://a.example/a.m3u8") + row("B", "https://b.example/b.m3u8", number="2")
        after = "#EXTM3U\n" + row("B", "https://b.example/b.m3u8", number="2") + row("A", "https://a.example/a.m3u8")
        with self.assertRaisesRegex(ValueError, "reordered"):
            assert_iptv_existing_rows_preserved(before, after)

    def test_appended_discovery_row_is_allowed(self):
        before = "#EXTM3U\n" + row("A", "https://a.example/a.m3u8")
        after = before + row("Candidate", "https://new.example/new.m3u8", group="New Channels")
        assert_iptv_existing_rows_preserved(before, after)

    def test_baseline_playlists_parse_without_losing_rows(self):
        from playlist_contract import parse_rows
        for filename in ("IPTV-Playlist.m3u", "International-Playlist.m3u"):
            text = (ROOT / filename).read_text(encoding="utf-8-sig")
            expected = sum(line.startswith("#EXTINF:") for line in text.splitlines())
            parsed = parse_rows(text)
            self.assertEqual(len(parsed), expected, filename)
            self.assertTrue(all(row.url.startswith(("http://", "https://")) for row in parsed), filename)

    def test_discovery_queues_are_not_xtream_publishable(self):
        with self.assertRaisesRegex(ValueError, "excluded from Xtream"):
            validate_discovery_queues("#EXTM3U\n" + row("Candidate", "https://new.example/live.m3u8", group="New Channels"))

if __name__ == "__main__":
    unittest.main()
