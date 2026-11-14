from __future__ import annotations

import unittest
from datetime import date, datetime, timedelta, timezone

from automation.core.run_ledger import LedgerEntry
from scripts.reconcile_automation_v2_stale_bundle_lock import is_stale_bundle_reservation


class StaleBundleReservationRecoveryTests(unittest.TestCase):
    def entry(self, engine="bundle", status="running", started_at=None):
        return LedgerEntry("a" * 64, engine, date(2026, 11, 14), "b" * 40,
                           status, 1, started_at)

    def test_missing_timestamp_is_recoverable_only_for_bundle_running_entry(self):
        now = datetime(2026, 11, 14, 10, 0, tzinfo=timezone.utc)
        self.assertTrue(is_stale_bundle_reservation(self.entry(), now))
        self.assertFalse(is_stale_bundle_reservation(self.entry(engine="iptv"), now))
        self.assertFalse(is_stale_bundle_reservation(self.entry(status="failed"), now))

    def test_live_lease_is_not_recovered(self):
        now = datetime(2026, 11, 14, 10, 0, tzinfo=timezone.utc)
        started = now - timedelta(minutes=20)
        self.assertFalse(is_stale_bundle_reservation(self.entry(started_at=started), now))

    def test_expired_lease_is_recovered(self):
        now = datetime(2026, 11, 14, 10, 0, tzinfo=timezone.utc)
        started = now - timedelta(minutes=131)
        self.assertTrue(is_stale_bundle_reservation(self.entry(started_at=started), now))


if __name__ == "__main__":
    unittest.main()
