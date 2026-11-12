import json
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import protect_main_playlist as guard


class MainPlaylistProtectionTests(unittest.TestCase):
    def write(self, path, rows, categories=None):
        if categories is None:
            categories = ["Bangladesh", "Indian Movies", "Backup", "New Channels", "New Backups", "Review"]
        path.write_text(
            "#EXTM3U\n#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(categories) + "\n" + "".join(
                f'#EXTINF:-1 tvg-chno="{number}" group-title="{group}" tvg-name="{name}",{name}\n{url}\n'
                for group, name, url, number in rows
            ),
            encoding="utf-8",
        )

    def run_guard(self, before, after):
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "IPTV-Playlist.m3u"
            state = Path(directory) / "state.json"
            self.write(playlist, before)
            guard.snapshot(playlist, state)
            self.write(playlist, after)
            guard.verify(playlist, state)

    def assert_guard_blocks(self, before, after, before_categories=None, after_categories=None):
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "IPTV-Playlist.m3u"
            state = Path(directory) / "state.json"
            self.write(playlist, before, before_categories)
            guard.snapshot(playlist, state)
            self.write(playlist, after, after_categories if after_categories is not None else before_categories)
            with self.assertRaises(SystemExit):
                guard.verify(playlist, state)

    def test_metadata_repairs_and_manual_queue_discoveries_are_allowed(self):
        self.run_guard(
            [
                ("Bangladesh", "A", "https://a", "1"),
                ("Indian Movies", "B", "https://b", "2"),
            ],
            [
                ("Bangladesh", "A HD (metadata fixed)", "https://a", "1"),
                ("Indian Movies", "B HD (metadata fixed)", "https://b", "2"),
                ("New Channels", "New discovery", "https://new", ""),
                ("New Backups", "Alternate discovery", "https://alternate", ""),
            ],
        )

    def test_existing_group_change_is_blocked(self):
        self.assert_guard_blocks(
            [("International", "A", "https://a", "1")],
            [("Indian Movies", "A", "https://a", "1")],
        )

    def test_category_registry_change_is_blocked(self):
        rows = [("Bangladesh", "A", "https://a", "1")]
        self.assert_guard_blocks(
            rows,
            rows,
            ["Bangladesh", "Indian Movies", "Backup", "New Channels", "New Backups", "Review"],
            ["Indian Movies", "Bangladesh", "Backup", "New Channels", "New Backups", "Review"],
        )

    def test_existing_row_reordering_is_blocked(self):
        self.assert_guard_blocks(
            [
                ("Bangladesh", "A", "https://a", "1"),
                ("Bangladesh", "B", "https://b", "2"),
            ],
            [
                ("Bangladesh", "B", "https://b", "2"),
                ("Bangladesh", "A", "https://a", "1"),
            ],
        )

    def test_existing_channel_number_change_is_blocked(self):
        self.assert_guard_blocks(
            [("Bangladesh", "A", "https://a", "1")],
            [("Bangladesh", "A", "https://a", "7")],
        )

    def test_new_discoveries_outside_manual_queues_are_blocked(self):
        self.assert_guard_blocks(
            [("Bangladesh", "A", "https://a", "1")],
            [
                ("Bangladesh", "A", "https://a", "1"),
                ("Indian Movies", "Unreviewed discovery", "https://new", ""),
            ],
        )

    def test_existing_deletion_is_blocked(self):
        self.assert_guard_blocks(
            [
                ("Bangladesh", "A", "https://a", "1"),
                ("Bangladesh", "B", "https://b", "2"),
            ],
            [("Bangladesh", "B", "https://b", "2")],
        )

    def test_existing_url_replacement_is_blocked(self):
        self.assert_guard_blocks(
            [("Bangladesh", "A", "https://a", "1")],
            [("Bangladesh", "A", "https://replacement", "1")],
        )

    def test_duplicate_url_occurrence_is_not_silently_added_or_dropped(self):
        self.assert_guard_blocks(
            [
                ("Bangladesh", "A", "https://same", "1"),
                ("Backup", "A alternate", "https://same", ""),
            ],
            [
                ("Bangladesh", "A", "https://same", "1"),
                ("Backup", "A alternate", "https://same", ""),
                ("New Backups", "Duplicate new backup", "https://same", ""),
            ],
        )


if __name__ == "__main__":
    unittest.main()
