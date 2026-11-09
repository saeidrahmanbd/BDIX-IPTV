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
    def test_canonical_channel_s_uk_archive_is_preserved_in_review(self):
        rows = [
            "#EXTM3U",
            '#EXTINF:-1 tvg-id="ChannelS.uk@679aa9" tvg-name="Channel S UK" tvg-chno="21" channel-id="ChannelS.uk@679aa9" group-title="Bangladesh",Channel S UK',
            "https://example.invalid/channel-s-main.m3u8",
            '#EXTINF:-1 tvg-id="ChannelS.uk@679aa9" tvg-name="Channel S UK" tvg-country="GB" tvg-language="ben" channel-id="ChannelS.uk@679aa9" group-title="International",Channel S UK',
            "https://example.invalid/channel-s-intl.m3u8",
            '#EXTINF:-1 tvg-id="ChannelS.uk@679aa9" tvg-name="Channel S UK" channel-id="ChannelS.uk@679aa9" group-title="Backup",Channel S UK',
            "https://example.invalid/channel-s-backup.m3u8",
            '#EXTINF:-1 tvg-id="ChannelS.uk@679aa9" tvg-name="Channel S UK" channel-id="ChannelS.uk@679aa9" group-title="Review",Channel S UK',
            "https://example.invalid/channel-s-archive.m3u8",
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "IPTV-Playlist.m3u"
            path.write_text(chr(10).join(rows) + chr(10), encoding="utf-8")
            hardening.process(path)
            result = path.read_text(encoding="utf-8")
        self.assertIn('group-title="Bangladesh",Channel S UK', result)
        self.assertIn('group-title="International",Channel S UK', result)
        self.assertIn('group-title="Backup",Channel S UK', result)
        self.assertIn('group-title="Review",Channel S UK', result)
        self.assertNotIn('group-title="Not Playing"', result)
        registry_line = next(line for line in result.splitlines() if line.startswith("#PLAYLIST-STUDIO-CATEGORIES:"))
        registry = json.loads(registry_line.split(":", 1)[1])
        self.assertEqual(registry, hardening.PLAYLIST_ORDERS["IPTV-Playlist.m3u"])
        self.assertEqual(registry[-4:], ["Review", "New Channels", "New Backups", "Backup"])

    def test_bangladesh_all_genres_and_indian_kids_sports_are_retained_but_indian_news_is_demoted(self):
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
        self.assertIn('group-title="Indian Entertainment",Cartoon Network', result)
        self.assertIn('group-title="Sports",DD Sports', result)

    def test_missing_bangladesh_channel_numbers_are_filled_without_renumbering_existing(self):
        rows = [
            "#EXTM3U",
            '#EXTINF:-1 tvg-id="Existing.bd" tvg-name="Existing Channel" tvg-country="BD" tvg-chno="7" group-title="Bangladesh",Existing Channel',
            "https://example.invalid/existing.m3u8",
            '#EXTINF:-1 tvg-id="Unnumbered.bd" tvg-name="Unnumbered Channel" tvg-country="BD" group-title="Bangladesh",Unnumbered Channel',
            "https://example.invalid/unnumbered.m3u8",
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "IPTV-Playlist.m3u"
            path.write_text(chr(10).join(rows) + chr(10), encoding="utf-8")
            hardening.process(path)
            result = path.read_text(encoding="utf-8")
        numbered = [
            int(hardening.attrs(line)["tvg-chno"])
            for line in result.splitlines()
            if line.startswith("#EXTINF:") and hardening.attrs(line).get("group-title") == "Bangladesh"
        ]
        self.assertEqual(numbered, [1, 7])
        self.assertIn('tvg-chno="7"', result)

    def test_permanently_banned_channels_are_removed_from_primary_and_backup(self):
        rows = [
            "#EXTM3U",
            '#EXTINF:-1 tvg-id="TVBRICSEnglish.in@SD" tvg-name="TV BRICS English" tvg-country="IN" group-title="Indian Entertainment",TV BRICS English',
            "https://example.invalid/tv-brics.m3u8",
            '#EXTINF:-1 tvg-id="JeevanTV.in@SD" tvg-name="Jeevan TV" tvg-country="IN" group-title="Backup",Jeevan TV',
            "https://example.invalid/jeevan-backup.m3u8",
            '#EXTINF:-1 tvg-id="PulariTV.in@SD" tvg-name="Pulari TV" tvg-country="IN" tvg-language="mal" group-title="Indian Entertainment",Pulari TV',
            "https://example.invalid/pulari.m3u8",
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "IPTV-Playlist.m3u"
            path.write_text("\n".join(rows) + "\n", encoding="utf-8")
            hardening.process(path)
            result = path.read_text(encoding="utf-8")
        self.assertNotIn("TV BRICS English", result)
        self.assertNotIn("Jeevan TV", result)
        self.assertIn('group-title="Indian Entertainment",Pulari TV', result)

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
