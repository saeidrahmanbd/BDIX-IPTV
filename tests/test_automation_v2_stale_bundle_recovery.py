from __future__ import annotations

import unittest
from datetime import date, datetime, timezone

from automation.core.run_ledger import LedgerEntry
from scripts.reconcile_automation_v2_stale_bundle_lock import is_orphaned_bundle_reservation


class StaleBundleReservationRecoveryTests(unittest.TestCase):
    def entry(self, engine="bundle", status="running", started_at=None):
        return LedgerEntry("a" * 64, engine, date(2026, 11, 14), "b" * 40,
                           status, 1, started_at)

    def test_running_bundle_entry_is_recoverable_even_when_recent(self):
        recent = datetime(2026, 11, 14, 9, 40, tzinfo=timezone.utc)
        self.assertTrue(is_orphaned_bundle_reservation(self.entry(started_at=recent)))

    def test_missing_timestamp_is_recoverable(self):
        self.assertTrue(is_orphaned_bundle_reservation(self.entry()))

    def test_other_engines_and_terminal_entries_are_preserved(self):
        self.assertFalse(is_orphaned_bundle_reservation(self.entry(engine="iptv")))
        self.assertFalse(is_orphaned_bundle_reservation(self.entry(status="failed")))
        self.assertFalse(is_orphaned_bundle_reservation(self.entry(status="succeeded")))


if __name__ == "__main__":
    unittest.main()
