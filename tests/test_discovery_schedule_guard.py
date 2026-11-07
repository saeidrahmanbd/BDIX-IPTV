"""Tests for daily discovery scheduling and duplicate-run protection."""
from datetime import date
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import discovery_schedule_guard as guard


class DiscoveryScheduleGuardTests(unittest.TestCase):
    def setUp(self):
        self.today = date(2026, 11, 7)

    def test_bangladesh_day_boundary_is_applied_to_utc_timestamps(self):
        self.assertEqual(
            guard.bangladesh_date("2026-11-06T18:00:00Z"),
            date(2026, 11, 7),
        )
        self.assertEqual(
            guard.bangladesh_date("2026-11-07T17:59:59Z"),
            date(2026, 11, 7),
        )
        self.assertEqual(
            guard.bangladesh_date("2026-11-07T18:00:00Z"),
            date(2026, 11, 8),
        )

    def test_any_existing_run_prevents_watchdog_redispatch(self):
        runs = [
            {
                "id": 10,
                "event": "workflow_dispatch",
                "status": "completed",
                "conclusion": "success",
                "created_at": "2026-11-07T01:20:00Z",
            },
            {
                "id": 11,
                "event": "schedule",
                "status": "queued",
                "conclusion": None,
                "created_at": "2026-11-06T18:30:00Z",
            },
            {
                "id": 12,
                "event": "push",
                "status": "completed",
                "conclusion": "failure",
                "created_at": "2026-11-06T17:50:00Z",
            },
        ]
        todays = guard.runs_for_date(runs, self.today)
        self.assertEqual({run["id"] for run in todays}, {10, 11})
        self.assertEqual(guard.first_run_id(todays), 11)

    def test_only_the_first_run_of_the_bangladesh_day_executes(self):
        runs = [
            {"id": 20, "created_at": "2026-11-07T01:10:00Z"},
            {"id": 21, "created_at": "2026-11-07T01:05:00Z"},
            {"id": 22, "created_at": "2026-11-06T17:59:59Z"},
        ]
        self.assertTrue(guard.should_current_run_execute(runs, 21, self.today))
        self.assertFalse(guard.should_current_run_execute(runs, 20, self.today))
        self.assertFalse(guard.should_current_run_execute(runs, 22, self.today))

    def test_pending_or_failed_earliest_run_still_prevents_a_second_discovery(self):
        runs = [
            {
                "id": 30,
                "event": "schedule",
                "status": "queued",
                "conclusion": None,
                "created_at": "2026-11-07T01:00:00Z",
            },
            {
                "id": 31,
                "event": "workflow_dispatch",
                "status": "completed",
                "conclusion": "success",
                "created_at": "2026-11-07T01:20:00Z",
            },
        ]
        self.assertTrue(guard.should_current_run_execute(runs, 30, self.today))
        self.assertFalse(guard.should_current_run_execute(runs, 31, self.today))

    def test_no_run_for_date_fails_closed(self):
        self.assertIsNone(guard.first_run_id([]))
        self.assertFalse(guard.should_current_run_execute([], 40, self.today))


if __name__ == "__main__":
    unittest.main()
