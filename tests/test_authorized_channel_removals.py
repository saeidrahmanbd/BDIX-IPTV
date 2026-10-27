"""Tests for narrowly scoped permanent channel removals and queue protection."""
from contextlib import redirect_stderr, redirect_stdout
import io
import json
import re
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import maintenance_helpers as guard
import restore_protected_review as restore
import sort_playlists as sorter
import final_playlist_hardening as hardening


TARGET_NAMES = {
    "AccuWeather",
    "America's Got Talent",
    "American Idol",
    "Baraza Music TV",
    "Oscar Movies Bhojpuri",
    "The Walking Dead Universe",
    "Popflix",
    "60 Days In",
    "Deadly Women",
    "Highway Thru Hell",
    "MINI",
    "Mundial",
    "TVC Arabic Kids",
    "Grace Network",
    "Joshua TV",
    "King TV",
    "Jeremiah TV",
    "CBN TV USA",
    "Dios Te Ve Kids",
    "ZB Bhakti",
    "Aaj Tak",
    "GNT",
    "Good News Today",
    "Network 10",
    "Angel TV",
    "Calvary TV",
    "Hosanna TV",
    "Hosanna TV Hindi",
    "Prarthana TV",
    "Santvani Channel",
    "Sharnam TV",
}


def channel(name, group, url):
    return f'#EXTINF:-1 tvg-name="{name}" group-title="{group}",{name}\n{url}'


def remove_named_record(text, name):
    lines = text.replace("\r", "").rstrip("\n").split("\n")
    preamble, records = [], []
    current = None
    for line in lines:
        if line.startswith("#EXTINF:"):
            if current is not None:
                records.append(current)
            current = [line]
        elif current is None:
            preamble.append(line)
        else:
            current.append(line)
    if current is not None:
        records.append(current)
    target = guard._canonical_channel_name(name)
    keep = [
        record for record in records
        if guard._canonical_channel_name(guard._name(record[0])) != target
    ]
    return "\n".join(preamble + [line for record in keep for line in record]) + "\n"


class AuthorizedChannelRemovalTests(unittest.TestCase):
    def test_allowlists_cover_all_explicitly_approved_channel_identities(self):
        expected = {guard._canonical_channel_name(name) for name in TARGET_NAMES}
        self.assertEqual(
            {guard._canonical_channel_name(name) for name in guard.PERMANENTLY_REMOVED_NAMES},
            expected,
        )
        self.assertEqual(
            {restore.normalize_name(name) for name in restore.PERMANENTLY_REMOVED_NAMES},
            expected,
        )
        for name in TARGET_NAMES:
            info = channel(name, "Backup", "https://example.invalid/stream.m3u8").splitlines()[0]
            self.assertTrue(guard._is_permanently_removed(info), name)
            self.assertTrue(restore.is_permanently_removed(info), name)

    def test_new_prohibited_channel_names_are_enforced_by_hardening(self):
        prohibited_names = {
            "Aaj Tak", "GNT", "Good News Today", "Network 10",
            "Angel TV", "Calvary TV", "Hosanna TV", "Hosanna TV Hindi",
            "Prarthana TV", "Santvani Channel", "Sharnam TV",
        }
        self.assertEqual(
            {hardening.normalize_name(name) for name in prohibited_names},
            hardening.PROHIBITED_RELIGIOUS_CHANNELS,
        )

    def _run_guard(self, removed_names):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            playlist = root / "IPTV-Playlist.m3u"
            baseline = root / "baseline.json"
            protected = root / "protected.m3u"
            report = root / "proposed-removals.md"
            original = "\n".join([
                "#EXTM3U",
                channel("AccuWeather", "Backup", "https://example.invalid/accuweather.m3u8"),
                channel("Reliable Backup", "Backup", "https://example.invalid/reliable.m3u8"),
                channel("Channel One", "Bangladesh", "https://example.invalid/channel-one.m3u8"),
            ]) + "\n"
            playlist.write_text(original, encoding="utf-8")
            with (
                patch.object(guard, "PLAYLIST", playlist),
                patch.object(guard, "BASELINE", baseline),
                patch.object(guard, "PROTECTED_SNAPSHOT", protected),
                patch.object(guard, "REMOVAL_REPORT", report),
            ):
                guard.snapshot_playlist()
                guard.snapshot_protected()
                current = playlist.read_text(encoding="utf-8")
                for name in removed_names:
                    current = remove_named_record(current, name)
                playlist.write_text(current, encoding="utf-8")
                with redirect_stderr(io.StringIO()):
                    return guard.verify_no_unauthorized_removals()

    def test_explicitly_authorized_deletion_passes_guard(self):
        self.assertEqual(self._run_guard(["AccuWeather"]), 0)

    def test_unrelated_protected_deletion_still_fails_guard(self):
        self.assertEqual(self._run_guard(["AccuWeather", "Reliable Backup"]), 1)

    def test_reintroduced_allowlisted_channel_is_blocked(self):
        self.assertEqual(self._run_guard([]), 1)


    def test_protected_snapshot_ignores_only_attribute_order(self):
        url = "https://example.invalid/reliable.m3u8"
        first = (
            '#EXTINF:-1 tvg-name="Reliable Backup" group-title="Backup" '
            'tvg-country="BD" tvg-language="ben",Reliable Backup\n' + url
        )
        second = (
            '#EXTINF:-1 tvg-language="ben" tvg-country="BD" '
            'group-title="Backup" tvg-name="Reliable Backup",Reliable Backup\n' + url
        )
        self.assertEqual(guard._protected_text(first), guard._protected_text(second))

    def test_exact_sparkle_duplicate_is_authorized_only_as_backup(self):
        info = '#EXTINF:-1 tvg-name="Sparkle Movies" group-title="Backup",Sparkle Movies'
        url = (
            "https://61fc4f1a40a342daa23f92141853b7b4.mediatailor.us-east-1.amazonaws.com"
            "/v1/master/04fd913bb278d8775298c26fdca9d9841f37601f/Samsung-gb_SparkleMovies/"
            "playlist.m3u8?ads.wurl_channel=1019&ads.wurl_name=SparkleMovies"
        )
        self.assertTrue(guard._is_authorized_removal(info, url))
        self.assertFalse(guard._is_authorized_removal(
            info.replace('group-title="Backup"', 'group-title="International"'), url
        ))
        self.assertFalse(guard._is_authorized_removal(
            info, url.replace("61fc4f1a40a342daa23f92141853b7b4", "different")
        ))

    def test_sorting_renumbers_primary_entries_and_leaves_review_groups_unnumbered(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "IPTV-Playlist.m3u"
            path.write_text("\n".join([
                "#EXTM3U",
                '#EXTINF:-1 tvg-name="Zulu" group-title="Bangladesh" tvg-chno="91",Zulu',
                "https://example.invalid/zulu.m3u8",
                '#EXTINF:-1 group-title="Backup" tvg-name="Backup One" tvg-chno="501",Backup One',
                "https://example.invalid/backup.m3u8",
                '#EXTINF:-1 tvg-chno="4" tvg-name="Alpha" group-title="Bangladesh",Alpha',
                "https://example.invalid/alpha.m3u8",
                '#EXTINF:-1 tvg-name="Sport One" group-title="Sports" tvg-chno="1",Sport One',
                "https://example.invalid/sport-one.m3u8",
                '#EXTINF:-1 tvg-name="Quiet Review" group-title="Not Playing" tvg-chno="3",Quiet Review',
                "https://example.invalid/quiet-review.m3u8",
            ]) + "\n", encoding="utf-8")
            sorter.sort_playlist(path)
            content = path.read_text(encoding="utf-8")
            self.assertLess(content.index('tvg-name="Alpha"'), content.index('tvg-name="Zulu"'))
            primary = [line for line in content.splitlines() if line.startswith("#EXTINF:") and 'group-title="Bangladesh"' in line]
            nums = [int(re.search(r'tvg-chno="(\d+)"', line).group(1)) for line in primary]
            self.assertEqual(nums, [1, 2])
            sport = next(line for line in content.splitlines() if line.startswith("#EXTINF:") and 'group-title="Sports"' in line)
            self.assertEqual(re.search(r'tvg-chno="(\\d+)"', sport).group(1), "3")
            primary_numbers = [
                int(re.search(r'tvg-chno="(\\d+)"', line).group(1))
                for line in content.splitlines()
                if line.startswith("#EXTINF:")
                and 'group-title="' in line
                and not any(f'group-title="{group}"' in line for group in {"Backup", "New Channels", "New Backup", "Not Playing"})
                and re.search(r'tvg-chno="(\\d+)"', line)
            ]
            self.assertEqual(primary_numbers, [1, 2, 3])
            backup = next(line for line in content.splitlines() if line.startswith("#EXTINF:") and 'group-title="Backup"' in line)
            self.assertNotIn("tvg-chno", backup)
            not_playing = next(line for line in content.splitlines() if line.startswith("#EXTINF:") and 'group-title="Not Playing"' in line)
            self.assertNotIn("tvg-chno", not_playing)


    def test_authorized_backup_migration_requires_exact_channel_and_url(self):
        cases = [
            ("7X Punjabi", "https://cdn2.in/7xPunjabihls/live.m3u8", "Indian Music"),
            ("Bangla Cinema", "http://103.151.60.162:2122/play/a02m/index.m3u8", "Indian Movies"),
            ("FASHION ONE", "https://b01c02nl.mediatriple.net/videoonlylive/mtkgeuihrlfwlive/u_stream_5c9e2ee6997cb_1/playlist.m3u8", "International"),
            ("PTV Sports", "http://103.135.253.32:8080/PTV-SPORTS/tracks-v1a1/mono.m3u8", "Pakistani"),
            ("Star Sports Select 1", "http://103.135.253.32:8080/STAR-SPORTS-SELECT-1/index.m3u8", "Sports"),
            ("Channel 52", "http://str24.l9574.com/503.stream/tracks-v1a1/mono.m3u8", "Bangladesh"),
        ]
        for name, url, target in cases:
            info = channel(name, "Backup", url).splitlines()[0]
            self.assertEqual(restore.authorized_backup_migration_target(info, url), target, name)
            self.assertIsNone(restore.authorized_backup_migration_target(info, url + "?changed=1"), name)

    def test_restore_keeps_exactly_authorized_backup_migration_and_other_queue(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            playlist = root / "IPTV-Playlist.m3u"
            snapshot = root / "protected.m3u"
            baseline = root / "baseline.json"
            migrated_url = "https://cdn2.in/7xPunjabihls/live.m3u8"
            safe_url = "https://example.invalid/safe-backup.m3u8"
            old_migrated = channel("7X Punjabi", "Backup", migrated_url).splitlines()
            safe_backup = channel("Safe Backup", "Backup", safe_url).splitlines()
            current_migrated = channel("7X Punjabi", "Indian Music", migrated_url).splitlines()
            current_safe = channel("Safe Backup", "Backup", safe_url).splitlines()

            playlist.write_text("#EXTM3U\n" + "\n".join(current_migrated + current_safe) + "\n", encoding="utf-8")
            snapshot.write_text("\n".join(old_migrated + safe_backup) + "\n", encoding="utf-8")
            baseline.write_text(json.dumps([
                {"info": old_migrated[0], "url": migrated_url, "group": "Backup", "stable": migrated_url, "name": "7X Punjabi"},
                {"info": safe_backup[0], "url": safe_url, "group": "Backup", "stable": safe_url, "name": "Safe Backup"},
            ]), encoding="utf-8")

            with (
                patch.object(restore, "PLAYLIST", playlist),
                patch.object(restore, "SNAPSHOT", snapshot),
                patch.object(restore, "BASELINE", baseline),
                redirect_stdout(io.StringIO()),
            ):
                restore.restore()

            final = playlist.read_text(encoding="utf-8")
            self.assertEqual(final.count(migrated_url), 1)
            self.assertEqual(final.count(safe_url), 1)
            self.assertIn('tvg-name="7X Punjabi" group-title="Indian Music"', final)
            self.assertIn('tvg-name="Safe Backup" group-title="Backup"', final)
            self.assertEqual(final.count('tvg-name="7X Punjabi"'), 1)


    def test_restore_preserves_explicit_not_playing_to_bangladesh_migration(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            playlist = root / "IPTV-Playlist.m3u"
            snapshot = root / "protected.m3u"
            baseline = root / "baseline.json"
            migrated_url = "http://str24.l9574.com/503.stream/tracks-v1a1/mono.m3u8"
            safe_url = "https://example.invalid/safe-not-playing.m3u8"
            old_channel52 = channel("Channel 52", "Not Playing", migrated_url).splitlines()
            safe_review = channel("Keep Reviewing", "Not Playing", safe_url).splitlines()
            current_channel52 = channel("Channel 52", "Bangladesh", migrated_url).splitlines()
            current_safe = channel("Keep Reviewing", "Not Playing", safe_url).splitlines()

            playlist.write_text("#EXTM3U\n" + "\n".join(current_channel52 + current_safe) + "\n", encoding="utf-8")
            snapshot.write_text("\n".join(old_channel52 + safe_review) + "\n", encoding="utf-8")
            baseline.write_text(json.dumps([
                {"info": old_channel52[0], "url": migrated_url, "group": "Not Playing", "stable": migrated_url, "name": "Channel 52"},
                {"info": safe_review[0], "url": safe_url, "group": "Not Playing", "stable": safe_url, "name": "Keep Reviewing"},
            ]), encoding="utf-8")

            with (
                patch.object(restore, "PLAYLIST", playlist),
                patch.object(restore, "SNAPSHOT", snapshot),
                patch.object(restore, "BASELINE", baseline),
                redirect_stdout(io.StringIO()),
            ):
                restore.restore()

            final = playlist.read_text(encoding="utf-8")
            self.assertEqual(final.count(migrated_url), 1)
            self.assertEqual(final.count(safe_url), 1)
            self.assertIn('tvg-name="Channel 52" group-title="Bangladesh"', final)
            self.assertIn('tvg-name="Keep Reviewing" group-title="Not Playing"', final)
            self.assertEqual(final.count('tvg-name="Channel 52"'), 1)


    def test_authorized_primary_to_backup_migration_requires_exact_identity_url_and_source(self):
        url = (
            "https://cdn-ue1-prod.tsv2.amagi.tv/linear/"
            "amg00143-younghollywoodl-younghollywood-xiaomi/playlist.m3u8"
        )
        info = channel("Young Hollywood", "Backup", url).splitlines()[0]
        self.assertTrue(restore.is_authorized_primary_to_backup_migration(info, url, "International"))
        self.assertFalse(restore.is_authorized_primary_to_backup_migration(info, url + "?changed=1", "International"))
        self.assertFalse(restore.is_authorized_primary_to_backup_migration(info, url, "Pakistani"))
        wrong_name = channel("Hollywood One", "Backup", url).splitlines()[0]
        self.assertFalse(restore.is_authorized_primary_to_backup_migration(wrong_name, url, "International"))
        wrong_group = info.replace('group-title="Backup"', 'group-title="Not Playing"')
        self.assertFalse(restore.is_authorized_primary_to_backup_migration(wrong_group, url, "International"))

    def test_restore_keeps_only_the_exact_authorized_young_hollywood_backup_migration(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            playlist_path = root / "IPTV-Playlist.m3u"
            snapshot = root / "protected.m3u"
            baseline = root / "baseline.json"
            main_url = (
                "https://amg00143-younghollywoodl-younghollywood-xiaomi-8k5gd.amagi.tv/"
                "playlist/amg00143-younghollywoodl-younghollywood-xiaomi/playlist.m3u8"
            )
            backup_url = (
                "https://cdn-ue1-prod.tsv2.amagi.tv/linear/"
                "amg00143-younghollywoodl-younghollywood-xiaomi/playlist.m3u8"
            )
            safe_backup_url = "https://example.invalid/safe-backup.m3u8"
            safe_np_url = "https://example.invalid/not-playing.m3u8"
            main_info = (
                '#EXTINF:-1 tvg-id="custom.young.hollywood" tvg-name="Young Hollywood" '
                'tvg-chno="471" group-title="International",Young Hollywood'
            )
            old_backup_info = (
                '#EXTINF:-1 tvg-id="custom.young.hollywood" tvg-name="Young Hollywood" '
                'tvg-chno="472" group-title="International",Young Hollywood'
            )
            new_backup_info = (
                '#EXTINF:-1 tvg-id="custom.young.hollywood" tvg-name="Young Hollywood" '
                'group-title="Backup",Young Hollywood'
            )
            safe_backup = channel("Safe Backup", "Backup", safe_backup_url).splitlines()
            safe_np = channel("Review Stream", "Not Playing", safe_np_url).splitlines()
            current = "\n".join([
                "#EXTM3U",
                main_info, main_url,
                new_backup_info, backup_url,
                *safe_backup, *safe_np,
            ]) + "\n"
            snapshot_text = "\n".join([*safe_backup, *safe_np]) + "\n"
            baseline_records = [
                {"info": main_info, "url": main_url, "group": "International"},
                {"info": old_backup_info, "url": backup_url, "group": "International"},
                {"info": safe_backup[0], "url": safe_backup_url, "group": "Backup"},
                {"info": safe_np[0], "url": safe_np_url, "group": "Not Playing"},
            ]
            playlist_path.write_text(current, encoding="utf-8")
            snapshot.write_text(snapshot_text, encoding="utf-8")
            baseline.write_text(json.dumps(baseline_records), encoding="utf-8")
            with (
                patch.object(restore, "PLAYLIST", playlist_path),
                patch.object(restore, "SNAPSHOT", snapshot),
                patch.object(restore, "BASELINE", baseline),
                redirect_stdout(io.StringIO()),
            ):
                restore.restore()
            result = playlist_path.read_text(encoding="utf-8")
            self.assertIn('tvg-id="custom.young.hollywood" tvg-name="Young Hollywood" tvg-chno="471" group-title="International"', result)
            backup_records = [
                line for line in result.splitlines()
                if line.startswith("#EXTINF:") and 'group-title="Backup"' in line
            ]
            moved = [line for line in backup_records if 'tvg-id="custom.young.hollywood"' in line]
            self.assertEqual(len(moved), 1)
            self.assertNotIn("tvg-chno", moved[0])
            self.assertEqual(result.count(main_url), 1)
            self.assertEqual(result.count(backup_url), 1)
            self.assertIn(safe_backup_url, result)
            self.assertIn(safe_np_url, result)

if __name__ == "__main__":
    unittest.main()
