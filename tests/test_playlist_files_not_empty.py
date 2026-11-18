"""Guard against publishing an empty or malformed canonical playlist file."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
PLAYLISTS = ("IPTV-Playlist.m3u", "International-Playlist.m3u")


class PlaylistPublicationGuardTests(unittest.TestCase):
    def test_both_canonical_playlists_are_nonempty_m3u_files(self):
        for filename in PLAYLISTS:
            with self.subTest(playlist=filename):
                path = ROOT / filename
                self.assertTrue(path.is_file(), f"{filename} is missing")
                content = path.read_text(encoding="utf-8-sig")
                lines = [line.strip() for line in content.splitlines() if line.strip()]
                self.assertTrue(lines, f"{filename} is empty")
                self.assertTrue(lines[0].startswith("#EXTM3U"), f"{filename} has no M3U header")
                extinf_count = sum(line.startswith("#EXTINF:") for line in lines)
                stream_count = sum(line.startswith(("http://", "https://")) for line in lines)
                self.assertGreater(extinf_count, 0, f"{filename} has no channel entries")
                self.assertEqual(stream_count, extinf_count, f"{filename} has incomplete channel URL pairs")


if __name__ == "__main__":
    unittest.main()
