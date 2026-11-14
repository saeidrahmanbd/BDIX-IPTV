"""Tests for daily discovery scheduling and duplicate-run protection."""
from datetime import date, datetime
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

    def test_github_rerun_attempt_is_treated_as_manual_retry(self):
        self.assertTrue(guard.is_manual_retry("workflow_dispatch", 1))
        self.assertTrue(guard.is_manual_retry("push", 2))
        self.assertTrue(guard.is_manual_retry("schedule", "3"))
        self.assertFalse(guard.is_manual_retry("push", 1))
        self.assertFalse(guard.is_manual_retry("schedule", None))
        self.assertTrue(guard.is_manual_retry(
            "push", 1, "international-channel-discovery.yml",
            "Manual International maintenance [manual-international-discovery]",
        ))
        self.assertFalse(guard.is_manual_retry(
            "push", 1, "new-channel-discovery.yml",
            "Manual International maintenance [manual-international-discovery]",
        ))
        self.assertFalse(guard.is_manual_retry(
            "push", 1, "international-channel-discovery.yml",
            "Routine maintenance commit",
        ))
        self.assertTrue(guard.is_manual_retry(
            "push", 1, "new-channel-discovery.yml",
            "Verify fixed IPTV discovery [manual-new-channel-discovery]",
        ))
        self.assertFalse(guard.is_manual_retry(
            "push", 1, "international-channel-discovery.yml",
            "Verify fixed IPTV discovery [manual-new-channel-discovery]",
        ))

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
                {"name": "discover", "status": "completed", "conclusion": "success", "steps": [{
                    "name": "Discover Bangladesh and India candidates into manual-review queues",
                    "conclusion": "success",
                }]},
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

    def test_stream_health_only_blocks_retry_when_check_job_succeeds(self):
        successful_health = {
            "id": 94, "status": "completed", "conclusion": "success",
            "created_at": "2026-11-07T02:45:00Z",
            "jobs": [
                {
                    "name": "check", "status": "completed", "conclusion": "success",
                    "steps": [{
                        "name": "Probe all International streams and apply three-day policy",
                        "conclusion": "success",
                    }],
                },
            ],
        }
        skipped_health = {
            "id": 95, "status": "completed", "conclusion": "success",
            "created_at": "2026-11-07T03:00:00Z",
            "jobs": [
                {"name": "check", "status": "completed", "conclusion": "skipped"},
            ],
        }
        self.assertTrue(guard.run_blocks_retry(successful_health, workflow_file="international-stream-health.yml"))
        self.assertFalse(guard.run_blocks_retry(skipped_health, workflow_file="international-stream-health.yml"))
        self.assertEqual(
            guard.first_run_id(
                [skipped_health, successful_health],
                workflow_file="international-stream-health.yml",
            ),
            94,
        )

    def test_active_stream_health_run_prevents_duplicate_watchdog_dispatch(self):
        active_health = {
            "id": 96, "status": "in_progress", "conclusion": None,
            "created_at": "2026-11-07T03:15:00Z",
        }
        self.assertTrue(
            guard.run_blocks_retry(
                active_health, workflow_file="international-stream-health.yml"
            )
        )

    def test_completed_success_without_discover_job_does_not_own_the_day(self):
        guard_only_run = {
            "id": 93,
            "status": "completed",
            "conclusion": "success",
            "created_at": "2026-11-07T01:00:00Z",
            "jobs": [{"name": "daily_guard", "status": "completed", "conclusion": "success"}],
        }
        self.assertFalse(guard.run_blocks_retry(guard_only_run))

    def test_manual_dispatch_can_refresh_after_successful_daily_discovery(self):
        successful_daily_run = {
            "id": 100,
            "event": "schedule",
            "status": "completed",
            "conclusion": "success",
            "created_at": "2026-11-07T01:00:00Z",
            "jobs": [
                {"name": "daily_guard", "status": "completed", "conclusion": "success"},
                {"name": "discover", "status": "completed", "conclusion": "success", "steps": [{
                    "name": "Discover Bangladesh and India candidates into manual-review queues",
                    "conclusion": "success",
                }]},
            ],
        }
        manual_run = {
            "id": 101,
            "event": "workflow_dispatch",
            "status": "in_progress",
            "conclusion": None,
            "created_at": "2026-11-07T12:00:00Z",
        }
        runs = [successful_daily_run, manual_run]

        self.assertFalse(
            guard.should_current_run_execute(runs, 101, self.today, event="schedule")
        )
        self.assertTrue(
            guard.should_current_run_execute(
                runs, 101, self.today, event="workflow_dispatch"
            )
        )

    def test_manual_dispatch_does_not_overlap_an_active_discovery_run(self):
        active_run = {
            "id": 110,
            "event": "schedule",
            "status": "in_progress",
            "conclusion": None,
            "created_at": "2026-11-07T01:00:00Z",
        }
        manual_run = {
            "id": 111,
            "event": "workflow_dispatch",
            "status": "in_progress",
            "conclusion": None,
            "created_at": "2026-11-07T01:10:00Z",
        }
        self.assertFalse(
            guard.should_current_run_execute(
                [active_run, manual_run], 111, self.today, event="workflow_dispatch"
            )
        )

    def test_later_scheduled_run_remains_blocked_by_successful_discovery(self):
        successful_run = {
            "id": 120,
            "event": "workflow_dispatch",
            "status": "completed",
            "conclusion": "success",
            "created_at": "2026-11-07T01:00:00Z",
            "jobs": [
                {"name": "daily_guard", "status": "completed", "conclusion": "success"},
                {
                    "name": "discover", "status": "completed", "conclusion": "success",
                    "steps": [{
                        "name": "Discover Bangladesh and India candidates into manual-review queues",
                        "conclusion": "success",
                    }],
                },
            ],
        }
        scheduled_run = {
            "id": 121,
            "event": "schedule",
            "status": "in_progress",
            "conclusion": None,
            "created_at": "2026-11-07T01:20:00Z",
        }
        self.assertFalse(
            guard.should_current_run_execute(
                [successful_run, scheduled_run], 121, self.today, event="schedule"
            )
        )

    def test_successful_health_check_is_the_daily_winner_for_health_workflow(self):
        runs = [{
            "id": 130,
            "event": "schedule",
            "status": "completed",
            "conclusion": "success",
            "created_at": "2026-11-07T02:45:00Z",
            "jobs": [{
                "name": "check", "status": "completed", "conclusion": "success",
                "steps": [{
                    "name": "Probe all International streams and apply three-day policy",
                    "conclusion": "success",
                }],
            }],
        }]
        self.assertEqual(
            guard.first_run_id(runs, workflow_file="international-stream-health.yml"),
            130,
        )
        self.assertIsNone(
            guard.first_run_id(runs, workflow_file="new-channel-discovery.yml")
        )

    def test_watchdog_recovery_uses_workflow_specific_local_grace_time(self):
        before = datetime(2026, 11, 7, 7, 29, tzinfo=guard.BD_TZ)
        after = datetime(2026, 11, 7, 7, 30, tzinfo=guard.BD_TZ)
        self.assertFalse(guard.recovery_is_due("iptv-maintenance.yml", before))
        self.assertTrue(guard.recovery_is_due("iptv-maintenance.yml", after))
        self.assertFalse(guard.recovery_is_due("epg-refresh.yml", after))


    def test_guard_only_success_does_not_count_as_completed_work(self):
        skipped_health = {
            "id": 140, "status": "completed", "conclusion": "success",
            "created_at": "2026-11-07T02:45:00Z",
            "jobs": [{
                "name": "check", "status": "completed", "conclusion": "success",
                "steps": [
                    {"name": "Check whether this queued health revision is current", "conclusion": "success"},
                    {"name": "Probe all International streams and apply three-day policy", "conclusion": "skipped"},
                ],
            }],
        }
        skipped_epg = {
            "id": 141, "status": "completed", "conclusion": "success",
            "created_at": "2026-11-07T03:00:00Z",
            "jobs": [{
                "name": "refresh", "status": "completed", "conclusion": "success",
                "steps": [
                    {"name": "Skip superseded queued EPG refresh", "conclusion": "success"},
                    {"name": "Regenerate, validate and publish XMLTV", "conclusion": "skipped"},
                ],
            }],
        }
        self.assertFalse(guard.run_blocks_retry(skipped_health, workflow_file="international-stream-health.yml"))
        self.assertFalse(guard.run_blocks_retry(skipped_epg, workflow_file="epg-refresh.yml"))

    def test_current_run_owns_day_when_no_other_run_has_completed_work(self):
        current = {"id": 150, "event": "workflow_run", "status": "in_progress",
                   "conclusion": None, "created_at": "2026-11-07T03:00:00Z"}
        self.assertTrue(guard.should_current_run_execute(
            [current], 150, self.today, event="workflow_run", workflow_file="epg-refresh.yml"
        ))

    def test_current_run_is_not_rejected_by_its_own_stale_skipped_job_state(self):
        current = {
            "id": 151, "event": "workflow_run", "status": "completed", "conclusion": "success",
            "created_at": "2026-11-07T03:00:00Z",
            "jobs": [{"name": "refresh", "status": "completed", "conclusion": "skipped",
                      "steps": [{"name": "Regenerate, validate and publish XMLTV", "conclusion": "skipped"}]}],
        }
        self.assertTrue(guard.should_current_run_execute(
            [current], 151, self.today, event="workflow_run", workflow_file="epg-refresh.yml"
        ))

    def test_earlier_active_run_owns_daily_slot(self):
        earlier = {"id": 152, "status": "in_progress", "conclusion": None,
                   "created_at": "2026-11-07T02:59:00Z"}
        current = {"id": 153, "status": "in_progress", "conclusion": None,
                   "created_at": "2026-11-07T03:00:00Z"}
        self.assertFalse(guard.should_current_run_execute(
            [earlier, current], 153, self.today, event="workflow_run", workflow_file="epg-refresh.yml"
        ))
        self.assertTrue(guard.should_current_run_execute(
            [earlier, current], 152, self.today, event="workflow_run", workflow_file="epg-refresh.yml"
        ))

    def test_later_active_run_does_not_displace_earlier_current_run(self):
        current = {"id": 154, "status": "in_progress", "conclusion": None,
                   "created_at": "2026-11-07T03:00:00Z"}
        later = {"id": 155, "status": "in_progress", "conclusion": None,
                 "created_at": "2026-11-07T03:01:00Z"}
        self.assertTrue(guard.should_current_run_execute(
            [current, later], 154, self.today, event="workflow_run", workflow_file="epg-refresh.yml"
        ))
        self.assertFalse(guard.should_current_run_execute(
            [current, later], 155, self.today, event="workflow_run", workflow_file="epg-refresh.yml"
        ))

    def test_scheduled_epg_run_takes_priority_over_earlier_successful_push(self):
        earlier_push = {
            "id": 158, "event": "push", "status": "completed", "conclusion": "success",
            "created_at": "2026-11-07T00:09:00Z",
            "jobs": [{
                "name": "refresh", "status": "completed", "conclusion": "success",
                "steps": [{
                    "name": "Regenerate, validate and publish XMLTV",
                    "conclusion": "success",
                }],
            }],
        }
        scheduled_run = {
            "id": 159, "event": "schedule", "status": "in_progress", "conclusion": None,
            "created_at": "2026-11-07T03:00:00Z",
        }
        self.assertTrue(guard.should_current_run_execute(
            [earlier_push, scheduled_run], 159, self.today,
            event="schedule", workflow_file="epg-refresh.yml",
        ))

    def test_successful_scheduled_epg_run_blocks_later_automatic_events(self):
        scheduled_run = {
            "id": 160, "event": "schedule", "status": "completed", "conclusion": "success",
            "created_at": "2026-11-07T03:00:00Z",
            "jobs": [{
                "name": "refresh", "status": "completed", "conclusion": "success",
                "steps": [{
                    "name": "Regenerate, validate and publish XMLTV",
                    "conclusion": "success",
                }],
            }],
        }
        later_push = {
            "id": 161, "event": "push", "status": "in_progress", "conclusion": None,
            "created_at": "2026-11-07T04:00:00Z",
        }
        self.assertFalse(guard.should_current_run_execute(
            [scheduled_run, later_push], 161, self.today,
            event="push", workflow_file="epg-refresh.yml",
        ))

    def test_prior_successful_epg_writer_blocks_later_workflow_run(self):
        previous = {
            "id": 156, "status": "completed", "conclusion": "success",
            "created_at": "2026-11-07T02:45:00Z",
            "jobs": [{"name": "refresh", "status": "completed", "conclusion": "success",
                      "steps": [{"name": "Regenerate, validate and publish XMLTV", "conclusion": "success"}]}],
        }
        current = {"id": 157, "status": "in_progress", "conclusion": None,
                   "created_at": "2026-11-07T03:00:00Z"}
        self.assertFalse(guard.should_current_run_execute(
            [previous, current], 157, self.today, event="workflow_run", workflow_file="epg-refresh.yml"
        ))


if __name__ == "__main__":
    unittest.main()
