"""Unit tests for exact primary/Backup integrity and Review quarantine."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from enforce_primary_backup_integrity import GROUP_ORDER, repair_playlist_text


LOGO = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/x.png"


def row(cid, name, group, url, *, language="ben", country="BD", number="1", logo=LOGO):
    attrs = (
        f'tvg-id="{cid}" tvg-name="{name}" tvg-logo="{logo}" '
        f'channel-id="{cid}" tvg-country="{country}" tvg-language="{language}" '
        f'group-title="{group}"'
    )
    if number:
        attrs += f' tvg-chno="{number}"'
    return f"#EXTINF:-1 {attrs},{name}\n{url}\n"


class PrimaryBackupIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.sample = (
            "#EXTM3U\n"
            + row("X.bd", "Example TV", "Bangladesh", "https://stream.example/x-primary.m3u8")
            + row("X.bd", "Example TV", "Indian Entertainment", "https://stream.example/x-alt.m3u8")
            + row("X.bd", "Example TV", "Backup", "https://stream.example/x-backup.m3u8", language="")
            + row("ORPHAN.bd", "Orphan Channel", "Backup", "https://stream.example/orphan.m3u8")
            + row("OLD.bd", "Legacy Review", "Not Playing", "https://stream.example/old.m3u8")
            + row("NEW.bd", "New Candidate", "New Channels", "https://stream.example/new.m3u8")
            + row("ALT.bd", "New Alternate", "New Backups", "https://stream.example/new-alt.m3u8")
            + row("UNKNOWN.bd", "Unknown Language", "Bangladesh", "https://stream.example/unknown.m3u8", language="")
        )

    def test_duplicate_primary_demotes_alternate_and_backup_has_primary(self):
        updated, stats, errors = repair_playlist_text(self.sample)
        self.assertEqual(errors, [])
        self.assertEqual(stats["duplicate_primary_demoted"], 1)
        self.assertIn('group-title="Backup"', updated)
        self.assertEqual(updated.count("https://stream.example/x-alt.m3u8"), 1)
        self.assertEqual(updated.count('tvg-id="X.bd"'), 3)
        self.assertEqual(stats["orphan_backups_quarantined"], 1)
        self.assertIn('group-title="Review"', updated)
        orphan_info = updated.split('https://stream.example/orphan.m3u8')[0].split('#EXTINF:')[-1]
        self.assertIn('group-title="Review"', orphan_info)

    def test_orphan_and_legacy_not_playing_are_review_only(self):
        updated, stats, errors = repair_playlist_text(self.sample)
        self.assertEqual(errors, [])
        self.assertIn('group-title="Review"', updated)
        self.assertNotIn('group-title="Not Playing"', updated)
        self.assertEqual(stats["legacy_review_renamed"], 1)
        self.assertEqual(stats["orphan_backups_quarantined"], 1)

    def test_backup_metadata_is_backfilled_from_exact_primary_id(self):
        updated, _, errors = repair_playlist_text(self.sample)
        self.assertEqual(errors, [])
        backup_block = updated.split("https://stream.example/x-backup.m3u8")[0]
        backup_block = backup_block.split("#EXTINF:")[-1]
        self.assertIn('tvg-language="ben"', backup_block)

    def test_unknown_language_is_marked_und_not_guessed(self):
        updated, stats, errors = repair_playlist_text(self.sample)
        self.assertEqual(errors, [])
        unknown = updated.split("https://stream.example/unknown.m3u8")[0].split("#EXTINF:")[-1]
        self.assertIn('tvg-language="und"', unknown)
        self.assertIn("Unknown Language", stats["undetermined_languages"])

    def test_review_and_discovery_groups_are_unnumbered_and_ordered(self):
        updated, _, errors = repair_playlist_text(self.sample)
        self.assertEqual(errors, [])
        self.assertIn("#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(GROUP_ORDER), updated)
        for name in ("Review", "New Channels", "New Backups"):
            self.assertIn(f'group-title="{name}"', updated)
        self.assertNotIn('group-title="Review" tvg-chno=', updated)
        self.assertLess(updated.index('group-title="Backup"'), updated.index('group-title="Review"'))
        self.assertLess(updated.index('group-title="Review"'), updated.index('group-title="New Channels"'))
        self.assertLess(updated.index('group-title="New Channels"'), updated.index('group-title="New Backups"'))

    def test_stream_urls_are_preserved(self):
        updated, _, errors = repair_playlist_text(self.sample)
        self.assertEqual(errors, [])
        before = sorted(line for line in self.sample.splitlines() if line.startswith("https://"))
        after = sorted(line for line in updated.splitlines() if line.startswith("https://"))
        self.assertEqual(before, after)

    def test_duplicate_stream_url_blocks_without_silent_deletion(self):
        duplicated = self.sample + row("OTHER.bd", "Second Row", "Bangladesh", "https://stream.example/x-primary.m3u8")
        updated, _, errors = repair_playlist_text(duplicated)
        self.assertTrue(any("Duplicate stream URL" in error for error in errors))
        self.assertEqual(updated.splitlines().count("https://stream.example/x-primary.m3u8"), 2)


    def test_verified_orphan_candidates_promote_to_their_genre(self):
        sample = (
            "#EXTM3U\n"
            + row("GTCPunjabi.in@UK", "GTC Punjabi UK", "Backup", "https://stream.example/gtc.m3u8", language="pan", country="IN")
            + row("MHOne.in@SD", "MH One", "Backup", "https://stream.example/mhone.m3u8", language="pan", country="IN")
            + row("QTV.in", "Q TV", "Backup", "https://stream.example/qtv.m3u8", language="hin", country="IN")
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertIn('tvg-name="GTC Punjabi UK"', updated)
        self.assertIn('group-title="Indian Entertainment"', updated)
        self.assertIn('tvg-name="MH One"', updated)
        self.assertIn('group-title="Indian Music"', updated)
        self.assertIn('tvg-name="Q TV"', updated)
        self.assertEqual(stats["orphan_backups_promoted"], 3)

    def test_restricted_or_persistently_failing_orphans_stay_in_review(self):
        sample = (
            "#EXTM3U\n"
            + row("ChannelWIN.in@SD", "Channel WIN", "Backup", "https://stream.example/win.m3u8", language="und", country="IN")
            + row("MHOneDilSe.in@SD", "MH One Dil Se", "Backup", "https://stream.example/dilse.m3u8", language="hin", country="IN")
            + row("Pogo.in@SD", "Pogo", "Backup", "https://stream.example/pogo.m3u8", language="eng", country="IN")
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertEqual(updated.count('group-title="Review"'), 3)
        self.assertEqual(stats["restricted_backups_reviewed"], 3)
        self.assertEqual(stats["orphan_backups_promoted"], 0)

    def test_ntv_malayalam_promotion_adds_the_local_logo(self):
        sample = (
            "#EXTM3U\n"
            + row("NTV.in", "NTV Malayalam", "Backup", "https://stream.example/ntv.m3u8", language="mal", country="IN", logo="")
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertIn('tvg-logo="' + "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/ntv-malayalam.svg" + '"', updated)
        self.assertIn('group-title="Indian Entertainment"', updated)
        self.assertEqual(stats["orphan_backups_promoted"], 1)

    def test_jalsha_movies_alias_links_to_the_existing_primary(self):
        sample = (
            "#EXTM3U\n"
            + row("Star.Jalsha.Movies.in", "Jalsha Movies", "Indian Bangla", "https://stream.example/jalsha-primary.m3u8", language="ben", country="IN")
            + row("JalshaMovies.in@HD", "Jalsha Movies", "Backup", "https://stream.example/jalsha-backup.m3u8", language="ben", country="IN")
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertEqual(updated.count('group-title="Indian Bangla"'), 1)
        self.assertIn('tvg-id="Star.Jalsha.Movies.in"', updated)
        self.assertEqual(stats["name_matched_backups_linked"], 1)
        self.assertEqual(stats["orphan_backups_quarantined"], 0)



if __name__ == "__main__":
    unittest.main()
