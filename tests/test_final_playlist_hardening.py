"""Regression tests for final playlist hardening edge cases."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import final_playlist_hardening as hardening


class FinalPlaylistHardeningTests(unittest.TestCase):
    def test_canonical_channel_s_uk_archive_in_not_playing_is_preserved(self):
        rows = [
            "#EXTM3U",
            '#EXTINF:-1 tvg-id="ChannelS.uk@679aa9" tvg-name="Channel S UK" tvg-chno="21" channel-id="ChannelS.uk@679aa9" group-title="Bangladesh",Channel S UK',
            "https://example.invalid/channel-s-main.m3u8",
            '#EXTINF:-1 tvg-id="ChannelS.uk@679aa9" tvg-name="Channel S UK" channel-id="ChannelS.uk@679aa9" group-title="Backup",Channel S UK',
            "https://example.invalid/channel-s-backup.m3u8",
            '#EXTINF:-1 tvg-id="ChannelS.uk@679aa9" tvg-name="Channel S UK" channel-id="ChannelS.uk@679aa9" group-title="Not Playing",Channel S UK',
            "https://example.invalid/channel-s-archive.m3u8",
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "IPTV-Playlist.m3u"
            path.write_text("\n".join(rows) + "\n", encoding="utf-8")
            hardening.process(path)
            result = path.read_text(encoding="utf-8")
        self.assertIn('group-title="Bangladesh",Channel S UK', result)
        self.assertIn('group-title="Backup",Channel S UK', result)
        self.assertIn('group-title="Not Playing",Channel S UK', result)
        registry_line = next(line for line in result.splitlines() if line.startswith("#PLAYLIST-STUDIO-CATEGORIES:"))
        registry = json.loads(registry_line.split(":", 1)[1])
        self.assertEqual(registry, hardening.PLAYLIST_ORDERS["IPTV-Playlist.m3u"])
        self.assertEqual(registry[-3:], ["New Channels", "New Backups", "Backup"])

    def test_bangladesh_all_genres_are_retained_and_prohibited_indian_categories_are_demoted(self):
        rows = [
            "#EXTM3U",
            '#EXTINF:-1 tvg-id="MadaniTV.bd" tvg-name="Madani TV" tvg-country="BD" tvg-chno="1" group-title="Bangladesh",Madani TV',
            "https://example.invalid/bd-madani.m3u8",
            '#EXTINF:-1 tvg-id="AajTak.in" tvg-name="Aaj Tak" tvg-country="IN" group-title="Indian Entertainment",Aaj Tak',
            "https://example.invalid/in-news.m3u8",
            '#EXTINF:-1 tvg-id="CartoonNetwork.in" tvg-name="Cartoon Network" tvg-country="IN" group-title="Indian Entertainment",Cartoon Network',
            "https://example.invalid/in-kids.m3u8",
            '#EXTINF:-1 tvg-id="DDSports.in" tvg-name="DD Sports" tvg-country="IN" group-title="Sports",DD Sports',
            "https://example.invalid/in-sports.m3u8",
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "IPTV-Playlist.m3u"
            path.write_text("\n".join(rows) + "\n", encoding="utf-8")
            hardening.process(path)
            result = path.read_text(encoding="utf-8")
        self.assertIn('group-title="Bangladesh",Madani TV', result)
        self.assertIn('group-title="Backup",Aaj Tak', result)
        self.assertIn('group-title="Backup",Cartoon Network', result)
        self.assertIn('group-title="Sports",DD Sports', result)

    def test_channel_s_uk_with_wrong_identity_still_fails(self):
        rows = [
            "#EXTM3U",
            '#EXTINF:-1 tvg-id="Wrong.uk@sd" tvg-name="Channel S UK" channel-id="Wrong.uk@sd" group-title="Not Playing",Channel S UK',
            "https://example.invalid/wrong.m3u8",
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "IPTV-Playlist.m3u"
            path.write_text("\n".join(rows) + "\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                hardening.process(path)


if __name__ == "__main__":
    unittest.main()
