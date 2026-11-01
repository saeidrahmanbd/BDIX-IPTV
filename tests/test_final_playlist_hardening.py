"""Regression tests for final playlist hardening edge cases."""
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
