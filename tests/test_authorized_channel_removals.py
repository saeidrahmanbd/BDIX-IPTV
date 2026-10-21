"""Tests for narrowly scoped permanent channel removals and queue protection."""
from contextlib import redirect_stderr
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import maintenance_helpers as guard
import restore_protected_review as restore


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


if __name__ == "__main__":
    unittest.main()
