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
                '#EXTINF:-1 tvg-name="Another Adult Service" group-title="Adult",Another Adult Service\nhttps://adult.example/second.m3u8\n',
                "",
            )
            mutated = mutated.replace(
                "https://sports.example/live.m3u8",
                "https://sports.example/updated.m3u8",
            )
            playlist.write_text(mutated, encoding="utf-8")
            guard.restore(playlist, snapshot)

            _, before_blocks = guard.parse_playlist(original)
            _, after_blocks = guard.parse_playlist(playlist.read_text(encoding="utf-8"))
            before_adult = [block for block in before_blocks if guard.group_of(block) == "Adult"]
            after_adult = [block for block in after_blocks if guard.group_of(block) == "Adult"]
            self.assertEqual(after_adult, before_adult)
            final_text = playlist.read_text(encoding="utf-8")
            self.assertIn("https://sports.example/updated.m3u8", final_text)
            groups = [guard.group_of(block) for block in after_blocks]
            self.assertEqual(groups.index("Adult") + 2, groups.index("Review"))
            self.assertIn('"Adult"', final_text.splitlines()[1])

    def test_international_reorganizer_passes_adult_rows_through_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "International-Playlist.m3u"
            logos = root / "logos"
            logos.mkdir()
            adult_block = [
                '#EXTINF:-1 tvg-name="VOD Adult Mystery 1080p" tvg-logo="https://invalid.example/logo.png" group-title="Adult",VOD Adult Mystery 1080p',
                "#EXTVLCOPT:http-user-agent=leave-unchanged",
                "https://adult.example/live.m3u8",
            ]
            playlist.write_text(
                "\n".join([
                    "#EXTM3U",
                    "#=================================",
                    "# Developed by: SAEID RAHMAN",
                    "# Facebook: https://www.facebook.com/saeid.rahman.sr",
                    "# Email: saeidrahman.mkt@gmail.com",
                    "#=================================",
                    '#PLAYLIST-STUDIO-NAME:"International Playlist"',
                    '#EXTINF:-1 tvg-id="BTV.bd" tvg-name="BTV" tvg-country="BD" group-title="Bangladesh",BTV',
                    "https://bd.example/live.m3u8",
                    *adult_block,
                ]) + "\n",
                encoding="utf-8",
            )
            with patch.object(reorg, "PLAYLIST", playlist), patch.object(reorg, "LOGOS", logos), patch.chdir(root):
                reorg.main()
            _, records = reorg.parse_playlist(playlist.read_text(encoding="utf-8"))
            adult_after = [record for record in records if reorg.attrs(reorg.split_info(record[0])[0]).get("group-title") == "Adult"]
            self.assertEqual(adult_after, [adult_block])
            with patch.object(intl_validator, "PLAYLIST", playlist), patch.object(intl_validator, "LOGOS", logos):
                intl_validator.main()


if __name__ == "__main__":
    unittest.main()
