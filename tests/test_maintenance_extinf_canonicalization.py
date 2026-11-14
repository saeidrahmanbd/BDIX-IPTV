import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import maintenance_helpers


class MaintenanceExtinfCanonicalizationTests(unittest.TestCase):
    def test_final_pass_canonicalizes_attributes_without_reordering_rows(self):
        first = (
            '#EXTINF:-1 tvg-id="one.bd" tvg-name="One" tvg-chno="1" '
            'channel-id="one.bd" tvg-country="BD" tvg-language="ben" '
            'tvg-logo="logos/one.png" group-title="Bangladesh",One'
        )
        second = (
            '#EXTINF:-1 tvg-id="two.in" tvg-name="Two" tvg-chno="2" '
            'channel-id="two.in" tvg-country="IN" tvg-language="hin" '
            'tvg-logo="logos/two.png" group-title="Indian Movies",Two'
        )
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "IPTV-Playlist.m3u"
            playlist.write_text("#EXTM3U\n" + first + "\nhttps://one.test/live.m3u8\n"
                                + second + "\nhttps://two.test/live.m3u8\n", encoding="utf-8")
            with patch.object(maintenance_helpers, "PLAYLIST", playlist):
                changed = maintenance_helpers.canonicalize_extinf()
            result = playlist.read_text(encoding="utf-8")
        self.assertEqual(changed, 2)
        self.assertLess(result.index(",One"), result.index(",Two"))
        self.assertLess(result.index("https://one.test/live.m3u8"), result.index("https://two.test/live.m3u8"))
        self.assertLess(result.index('tvg-logo="logos/one.png"'), result.index('tvg-chno="1"'))
        self.assertIn('group-title="Bangladesh",One', result)
        self.assertIn('group-title="Indian Movies",Two', result)

    def test_second_pass_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "IPTV-Playlist.m3u"
            playlist.write_text(
                '#EXTM3U\n#EXTINF:-1 tvg-id="one.bd" tvg-name="One" '
                'tvg-logo="logos/one.png" tvg-chno="1" channel-id="one.bd" '
                'tvg-country="BD" tvg-language="ben" group-title="Bangladesh",One\n'
                'https://one.test/live.m3u8\n',
                encoding="utf-8",
            )
            with patch.object(maintenance_helpers, "PLAYLIST", playlist):
                first = maintenance_helpers.canonicalize_extinf()
                second = maintenance_helpers.canonicalize_extinf()
        self.assertEqual(first, 0)
        self.assertEqual(second, 0)


if __name__ == "__main__":
    unittest.main()
