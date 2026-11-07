#!/usr/bin/env python3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import international_adult_guard as guard
import reorganize_international_playlist as reorg
import validate_international_playlist as intl_validator

class InternationalAdultGuardTests(unittest.TestCase):
    def test_restore_reinserts_exact_adult_blocks_and_keeps_other_updates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "International-Playlist.m3u"
            snapshot = root / "adult.json"
            original = """#EXTM3U
#PLAYLIST-STUDIO-CATEGORIES:["Sports", "Adult", "Review", "Backup"]
#PLAYLIST-STUDIO-NAME:"International Playlist"
#EXTINF:-1 tvg-id="sports.id" group-title="Sports",Sports Channel
https://sports.example/live.m3u8
#EXTINF:-1 tvg-name="VOD Adult Test 1080p" tvg-logo="https://invalid.example/logo.png" group-title="Adult",VOD Adult Test 1080p
#EXTVLCOPT:http-user-agent=keep-this
https://adult.example/stream.m3u8
#EXTINF:-1 tvg-name="Another Adult Service" group-title="Adult",Another Adult Service
https://adult.example/second.m3u8
#EXTINF:-1 tvg-id="review.id" group-title="Review",Review Channel
https://review.example/live.m3u8
"""
            playlist.write_text(original, encoding="utf-8")
            guard.snapshot(playlist, snapshot)
            mutated = original.replace('group-title="Adult"', 'group-title="Backup"', 1)
            mutated = mutated.replace(
                '#EXTINF:-1 tvg-name="Another Adult Service" group-title="Adult",Another Adult Service\nhttps://adult.example/second.m3u8\n', ""
            )
            mutated = mutated.replace("https://sports.example/live.m3u8", "https://sports.example/updated.m3u8")
            playlist.write_text(mutated, encoding="utf-8")
            guard.restore(playlist, snapshot)
            _, before = guard.parse_playlist(original)
            _, after = guard.parse_playlist(playlist.read_text(encoding="utf-8"))
            self.assertEqual([r for r in after if guard.group_of(r) == "Adult"], [r for r in before if guard.group_of(r) == "Adult"])
            self.assertIn("https://sports.example/updated.m3u8", playlist.read_text(encoding="utf-8"))
            self.assertEqual([guard.group_of(r) for r in after].index("Adult") + 2, [guard.group_of(r) for r in after].index("Review"))

    def test_reorganizer_and_validator_leave_adult_metadata_untouched(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "International-Playlist.m3u"
            logos = root / "logos"
            logos.mkdir()
            adult = [
                '#EXTINF:-1 tvg-name="VOD Adult Mystery 1080p" tvg-logo="https://invalid.example/logo.png" group-title="Adult",VOD Adult Mystery 1080p',
                "#EXTVLCOPT:http-user-agent=leave-unchanged",
                "https://adult.example/live.m3u8",
            ]
            attribution = [
                "#EXTM3U",
                "#=================================",
                "# Developed by: SAEID RAHMAN",
                "# Facebook: https://www.facebook.com/saeid.rahman.sr",
                "# Email: saeidrahman.mkt@gmail.com",
                "#=================================",
                '#PLAYLIST-STUDIO-NAME:"International Playlist"',
            ]
            playlist.write_text("\n".join(attribution + [
                '#EXTINF:-1 tvg-id="BTV.bd" tvg-name="BTV" tvg-country="BD" group-title="Bangladesh",BTV',
                "https://bd.example/live.m3u8",
                *adult,
            ]) + "\n", encoding="utf-8")
            with patch.object(reorg, "PLAYLIST", playlist), patch.object(reorg, "LOGOS", logos), patch.chdir(root):
                reorg.main()
            _, records = reorg.parse_playlist(playlist.read_text(encoding="utf-8"))
            self.assertEqual([r for r in records if reorg.attrs(reorg.split_info(r[0])[0]).get("group-title") == "Adult"], [adult])
            with patch.object(intl_validator, "PLAYLIST", playlist), patch.object(intl_validator, "LOGOS", logos):
                intl_validator.main()

if __name__ == "__main__":
    unittest.main()
