import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import protect_main_playlist as guard


class MainPlaylistProtectionTests(unittest.TestCase):
    def write(self, path, rows, categories=None):
        categories = categories or guard.CATEGORY_ORDER
        text = "#EXTM3U\n#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(categories) + "\n"
        for group, name, url, number, channel_id in rows:
            number_attr = f' tvg-chno="{number}"' if number else ""
            id_attr = f' tvg-id="{channel_id}" channel-id="{channel_id}"' if channel_id else ""
            text += f'#EXTINF:-1{number_attr}{id_attr} tvg-name="{name}" group-title="{group}",{name}\n{url}\n'
        path.write_text(text, encoding="utf-8")

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
            with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                with self.assertRaises(SystemExit):
                    guard.verify(playlist, state)

    def test_metadata_repairs_and_new_discovery_rows_are_allowed(self):
        self.run_guard(
            [("Bangladesh", "A", "https://a", "1", "a.bd"),
             ("Indian Movies", "B", "https://b", "2", "b.in")],
            [("Bangladesh", "A Updated", "https://a", "1", "a.bd"),
             ("Indian Movies", "B Updated", "https://b", "2", "b.in"),
             ("New Channels", "New discovery", "https://new", "", "new.in"),
             ("New Backups", "Alternate discovery", "https://alternate", "", "alternate.in")],
        )

    def test_unapproved_existing_group_change_is_blocked(self):
        self.assert_guard_blocks(
            [("International", "A", "https://a", "1", "a.us")],
            [("Indian Movies", "A", "https://a", "1", "a.us")],
        )

    def test_exact_url_approved_queue_migration_is_allowed(self):
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "IPTV-Playlist.m3u"
            state = Path(directory) / "state.json"
            approvals = Path(directory) / "approvals.json"
            self.write(playlist, [("New Channels", "Movies Now", "https://a", "", "moviesnow.in")])
            guard.snapshot(playlist, state)
            approvals.write_text(json.dumps([{
                "url": "https://a", "source_group": "New Channels",
                "target_group": "Indian Movies", "allow_metadata": True
            }]), encoding="utf-8")
            self.write(playlist, [("Indian Movies", "Movies Now", "https://a", "1", "moviesnow.in")])
            with patch.object(guard, "OWNER_APPROVALS", approvals):
                guard.verify(playlist, state)

    def test_review_cannot_be_promoted_by_cleanup(self):
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "IPTV-Playlist.m3u"
            state = Path(directory) / "state.json"
            approvals = Path(directory) / "approvals.json"
            self.write(playlist, [("Review", "Broken candidate", "https://a", "", "broken.in")])
            guard.snapshot(playlist, state)
            approvals.write_text(json.dumps([{
                "url": "https://a", "source_group": "Review",
                "target_group": "Indian Movies", "allow_metadata": True
            }]), encoding="utf-8")
            self.write(playlist, [("Indian Movies", "Broken candidate", "https://a", "1", "broken.in")])
            with patch.object(guard, "OWNER_APPROVALS", approvals):
                with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                    with self.assertRaises(SystemExit):
                        guard.verify(playlist, state)

    def test_canonical_group_sorting_is_blocked_during_routine_maintenance(self):
        self.assert_guard_blocks(
            [("Indian Movies", "B", "https://b", "2", "b.in"),
             ("Bangladesh", "A", "https://a", "1", "a.bd")],
            [("Bangladesh", "A", "https://a", "1", "a.bd"),
             ("Indian Movies", "B", "https://b", "2", "b.in")],
        )

    def test_primary_renumbering_is_blocked_during_routine_maintenance(self):
        self.assert_guard_blocks(
            [("Bangladesh", "A", "https://a", "12", "a.bd"),
             ("Bangladesh", "B", "https://b", "23", "b.bd")],
            [("Bangladesh", "A", "https://a", "1", "a.bd"),
             ("Bangladesh", "B", "https://b", "2", "b.bd")],
        )

    def test_preexisting_numbered_backup_and_unnumbered_primary_are_preserved(self):
        self.run_guard(
            [("Backup", "A alternate", "https://a", "501", "a.bd"),
             ("Bangladesh", "B", "https://b", "", "b.bd")],
            [("Backup", "A alternate metadata fixed", "https://a", "501", "a.bd"),
             ("Bangladesh", "B metadata fixed", "https://b", "", "b.bd")],
        )

    def test_owner_approved_migration_can_reassemble_groups_and_fill_only_missing_numbers(self):
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "IPTV-Playlist.m3u"
            state = Path(directory) / "state.json"
            approvals = Path(directory) / "approvals.json"
            self.write(
                playlist,
                [("Indian Movies", "B", "https://b", "23", "b.in"),
                 ("Bangladesh", "A", "https://a", "", "a.bd")],
            )
            guard.snapshot(playlist, state)
            approvals.write_text("[]", encoding="utf-8")
            self.write(
                playlist,
                [("Bangladesh", "A", "https://a", "1", "a.bd"),
                 ("Indian Movies", "B", "https://b", "23", "b.in")],
            )
            with patch.object(guard, "OWNER_APPROVALS", approvals):
                guard.verify(playlist, state)

    def test_owner_migration_cannot_renumber_existing_primary_channels(self):
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "IPTV-Playlist.m3u"
            state = Path(directory) / "state.json"
            approvals = Path(directory) / "approvals.json"
            self.write(
                playlist,
                [("Bangladesh", "A", "https://a", "12", "a.bd"),
                 ("Bangladesh", "B", "https://b", "23", "b.bd")],
            )
            guard.snapshot(playlist, state)
            approvals.write_text(json.dumps([{
                "url": "https://a", "source_group": "Bangladesh",
                "target_group": "Bangladesh", "allow_metadata": True
            }]), encoding="utf-8")
            self.write(
                playlist,
                [("Bangladesh", "A", "https://a", "1", "a.bd"),
                 ("Bangladesh", "B", "https://b", "2", "b.bd")],
            )
            with patch.object(guard, "OWNER_APPROVALS", approvals):
                with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
                    with self.assertRaises(SystemExit):
                        guard.verify(playlist, state)

    def test_non_primary_rows_must_be_unnumbered(self):
        self.assert_guard_blocks(
            [("Backup", "A alternate", "https://a", "", "a.bd")],
            [("Backup", "A alternate", "https://a", "1", "a.bd")],
        )

    def test_primary_number_gap_is_blocked(self):
        self.assert_guard_blocks(
            [("Bangladesh", "A", "https://a", "1", "a.bd"),
             ("Bangladesh", "B", "https://b", "2", "b.bd")],
            [("Bangladesh", "A", "https://a", "1", "a.bd"),
             ("Bangladesh", "B", "https://b", "7", "b.bd")],
        )

    def test_category_registry_must_be_canonical(self):
        rows = [("Bangladesh", "A", "https://a", "1", "a.bd")]
        self.assert_guard_blocks(rows, rows, guard.CATEGORY_ORDER, list(reversed(guard.CATEGORY_ORDER)))

    def test_new_rows_outside_discovery_queues_are_blocked(self):
        self.assert_guard_blocks(
            [("Bangladesh", "A", "https://a", "1", "a.bd")],
            [("Bangladesh", "A", "https://a", "1", "a.bd"),
             ("Indian Movies", "Unreviewed discovery", "https://new", "2", "new.in")],
        )

    def test_existing_deletion_is_blocked(self):
        self.assert_guard_blocks(
            [("Bangladesh", "A", "https://a", "1", "a.bd"),
             ("Bangladesh", "B", "https://b", "2", "b.bd")],
            [("Bangladesh", "B", "https://b", "1", "b.bd")],
        )

    def test_existing_url_replacement_is_blocked(self):
        self.assert_guard_blocks(
            [("Bangladesh", "A", "https://a", "1", "a.bd")],
            [("Bangladesh", "A", "https://replacement", "1", "a.bd")],
        )

    def test_duplicate_new_discovery_url_is_blocked(self):
        self.assert_guard_blocks(
            [("Bangladesh", "A", "https://a", "1", "a.bd")],
            [("Bangladesh", "A", "https://a", "1", "a.bd"),
             ("New Channels", "Discovery A", "https://new", "", "new.in"),
             ("New Backups", "Discovery B", "https://new", "", "new.in")],
        )

    def test_duplicate_url_occurrence_is_blocked(self):
        self.assert_guard_blocks(
            [("Bangladesh", "A", "https://same", "1", "a.bd")],
            [("Bangladesh", "A", "https://same", "1", "a.bd"),
             ("New Backups", "Duplicate URL", "https://same", "", "a.bd")],
        )


if __name__ == "__main__":
    unittest.main()
