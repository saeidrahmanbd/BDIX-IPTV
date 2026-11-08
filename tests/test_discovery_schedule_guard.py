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

    def test_failed_or_cancelled_attempts_do_not_block_a_retry(self):
        runs = [
            {
                "id": 50, "status": "completed", "conclusion": "failure",
                "created_at": "2026-11-07T00:55:00Z",
            },
            {
                "id": 51, "status": "completed", "conclusion": "cancelled",
                "created_at": "2026-11-07T01:00:00Z",
            },
            {
                "id": 52, "status": "in_progress", "conclusion": None,
                "created_at": "2026-11-07T01:10:00Z",
            },
        ]
        self.assertEqual(guard.first_run_id(runs), 52)
        self.assertTrue(guard.should_current_run_execute(runs, 52, self.today))
        self.assertFalse(guard.run_blocks_retry(runs[0]))
        self.assertFalse(guard.run_blocks_retry(runs[1]))
        self.assertTrue(guard.run_blocks_retry(runs[2]))

    def test_current_run_date_is_anchored_to_created_at_not_queue_start_time(self):
        run = {"id": 70, "created_at": "2026-11-07T17:59:00Z"}
        self.assertEqual(guard.bangladesh_date(run["created_at"]), date(2026, 11, 7))

    def test_directly_fetched_current_run_wins_over_eventually_consistent_list(self):
        listed = [{
            "id": 80, "status": "completed", "conclusion": "success",
            "created_at": "2026-11-07T01:05:00Z",
        }]
        current = {
            "id": 79, "status": "in_progress", "conclusion": None,
            "created_at": "2026-11-07T01:00:00Z",
        }
        merged = {run["id"]: run for run in listed}
        merged[current["id"]] = current
        todays = guard.runs_for_date(list(merged.values()), self.today)
        self.assertEqual(guard.first_run_id(todays), 79)

    def test_watchdog_can_retry_when_all_daily_attempts_failed(self):
        runs = [
            {
                "id": 60, "status": "completed", "conclusion": "failure",
                "created_at": "2026-11-07T01:00:00Z",
            },
            {
                "id": 61, "status": "completed", "conclusion": "timed_out",
                "created_at": "2026-11-07T01:20:00Z",
            },
        ]
        self.assertIsNone(guard.first_run_id(guard.runs_for_date(runs, self.today)))


    def test_completed_success_with_skipped_discover_job_does_not_block_a_retry(self):
        no_op_run = {
            "id": 90,
            "status": "completed",
            "conclusion": "success",
            "created_at": "2026-11-07T01:00:00Z",
            "jobs": [
                {"name": "daily_guard", "status": "completed", "conclusion": "success"},
                {"name": "discover", "status": "completed", "conclusion": "skipped"},
            ],
        }
        self.assertFalse(guard.run_blocks_retry(no_op_run))
        self.assertIsNone(guard.first_run_id([no_op_run]))

    def test_completed_success_with_successful_discover_job_owns_the_day(self):
        successful_run = {
            "id": 91,
            "status": "completed",
            "conclusion": "success",
            "created_at": "2026-11-07T01:00:00Z",
            "jobs": [
                {"name": "daily_guard", "status": "completed", "conclusion": "success"},
                {"name": "discover", "status": "completed", "conclusion": "success"},
            ],
        }
        later_no_op = {
            "id": 92,
            "status": "completed",
            "conclusion": "success",
            "created_at": "2026-11-07T01:10:00Z",
            "jobs": [
                {"name": "daily_guard", "status": "completed", "conclusion": "success"},
                {"name": "discover", "status": "completed", "conclusion": "skipped"},
            ],
        }
        self.assertTrue(guard.run_blocks_retry(successful_run))
        self.assertEqual(guard.first_run_id([later_no_op, successful_run]), 91)

    def test_completed_success_without_discover_job_does_not_own_the_day(self):
        guard_only_run = {
            "id": 93,
            "status": "completed",
            "conclusion": "success",
            "created_at": "2026-11-07T01:00:00Z",
            "jobs": [{"name": "daily_guard", "status": "completed", "conclusion": "success"}],
        }
        self.assertFalse(guard.run_blocks_retry(guard_only_run))

if __name__ == "__main__":
    unittest.main()
