"""Tests for narrowly scoped permanent channel removals and queue protection."""
from contextlib import redirect_stderr
import io
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
    def test_allowlists_cover_exactly_the_thirteen_requested_names(self):
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
            ]) + "\n", encoding="utf-8")
            sorter.sort_playlist(path)
            content = path.read_text(encoding="utf-8")
            self.assertLess(content.index('tvg-name="Alpha"'), content.index('tvg-name="Zulu"'))
            primary = [line for line in content.splitlines() if line.startswith("#EXTINF:") and 'group-title="Bangladesh"' in line]
            nums = [int(re.search(r'tvg-chno="(\d+)"', line).group(1)) for line in primary]
            self.assertEqual(nums, [1, 2])
            backup = next(line for line in content.splitlines() if line.startswith("#EXTINF:") and 'group-title="Backup"' in line)
            self.assertNotIn("tvg-chno", backup)

if __name__ == "__main__":
    unittest.main()
