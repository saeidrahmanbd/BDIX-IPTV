"""Regression tests for stable contiguous category regrouping in IPTV-Playlist.m3u."""
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from sort_playlists import sort_playlist


def rows(text):
    result = []
    current = None
    for line in text.splitlines():
        if line.startswith("#EXTINF:"):
            if current is not None:
                result.append(current)
            attrs = dict(__import__("re").findall(r'([A-Za-z0-9_-]+)="([^"]*)"', line))
            current = {"info": line, "attrs": attrs, "url": ""}
        elif current is not None and line.strip().startswith(("http://", "https://")):
            current["url"] = line.strip()
    if current is not None:
        result.append(current)
    return result


class SortPlaylistsTests(unittest.TestCase):
    def sample(self):
        return (
            "#EXTM3U\n"
            '#PLAYLIST-STUDIO-CATEGORIES:["Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani","International","Documentary & Wildlife","Kids","Religious","Sports","Backup","New Channels","New Backups","Review"]\n'
            '#EXTINF:-1 group-title="Sports" tvg-name="Sports Zulu" tvg-id="sports.zulu" tvg-chno="3",Sports Zulu\n'
            "https://stream.example/sports-zulu.m3u8\n"
            '#EXTINF:-1 group-title="Bangladesh" tvg-name="Bangla Zulu" tvg-id="bd.zulu" tvg-chno="1",Bangla Zulu\n'
            "https://stream.example/bangla-zulu.m3u8\n"
            '#EXTINF:-1 group-title="Review" tvg-name="Review Row" tvg-id="review.row" tvg-chno="88",Review Row\n'
            "https://stream.example/review.m3u8\n"
            '#EXTINF:-1 group-title="Sports" tvg-name="Sports Alpha" tvg-id="sports.alpha" tvg-chno="4",Sports Alpha\n'
            "https://stream.example/sports-alpha.m3u8\n"
            '#EXTINF:-1 group-title="Bangladesh" tvg-name="Bangla Alpha" tvg-id="bd.alpha" tvg-chno="2",Bangla Alpha\n'
            "https://stream.example/bangla-alpha.m3u8\n"
            '#EXTINF:-1 group-title="International" tvg-name="International Row" tvg-id="intl.row" tvg-chno="5",International Row\n'
            "https://stream.example/international.m3u8\n"
            '#EXTINF:-1 group-title="Backup" tvg-name="Backup Row" tvg-id="backup.row" tvg-chno="1",Backup Row\n'
            "https://stream.example/backup.m3u8\n"
        )

    def test_regroups_categories_stably_without_changing_numbers_or_streams(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "IPTV-Playlist.m3u"
            original = self.sample()
            path.write_text(original, encoding="utf-8")
            before = rows(original)

            sort_playlist(path)

            updated = path.read_text(encoding="utf-8")
            after = rows(updated)
            group_sequence = []
            for entry in after:
                group = entry["attrs"].get("group-title", "")
                if not group_sequence or group_sequence[-1] != group:
                    group_sequence.append(group)

            self.assertEqual(
                group_sequence,
                ["Bangladesh", "International", "Sports", "Backup", "Review"],
            )
            self.assertEqual(len(before), len(after))
            self.assertEqual(
                sorted(row["url"] for row in before),
                sorted(row["url"] for row in after),
            )
            before_by_url = {row["url"]: row["attrs"] for row in before}
            for entry in after:
                old = before_by_url[entry["url"]]
                self.assertEqual(entry["attrs"].get("tvg-chno"), old.get("tvg-chno"))
                self.assertEqual(entry["attrs"].get("group-title"), old.get("group-title"))
                self.assertEqual(entry["attrs"].get("tvg-id"), old.get("tvg-id"))

            groups = {}
            for entry in after:
                groups.setdefault(entry["attrs"]["group-title"], []).append(entry["attrs"]["tvg-name"])
            self.assertEqual(groups["Bangladesh"], ["Bangla Zulu", "Bangla Alpha"])
            self.assertEqual(groups["Sports"], ["Sports Zulu", "Sports Alpha"])

    def test_regrouping_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "IPTV-Playlist.m3u"
            path.write_text(self.sample(), encoding="utf-8")
            sort_playlist(path)
            once = path.read_text(encoding="utf-8")
            sort_playlist(path)
            self.assertEqual(path.read_text(encoding="utf-8"), once)


if __name__ == "__main__":
    unittest.main()
