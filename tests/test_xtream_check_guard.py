"""Tests for Xtream health-check deduplication."""
from datetime import datetime, timezone
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import xtream_check_guard as guard


class XtreamCheckGuardTests(unittest.TestCase):
    def setUp(self):
        self.sha = "a" * 40
        self.current = {
            "id": 20, "head_sha": self.sha, "event": "workflow_run",
            "status": "in_progress", "conclusion": None,
            "created_at": "2026-11-07T03:30:00Z",
        }
        self.success = {
            "id": 19, "head_sha": self.sha, "event": "workflow_run",
            "status": "completed", "conclusion": "success",
            "created_at": "2026-11-07T03:20:00Z",
            "jobs": [{
                "name": "check", "status": "completed", "conclusion": "success",
                "steps": [{"name": "Check main IPTV Xtream gateway", "conclusion": "success"}],
            }],
        }

    def test_successful_same_revision_check_suppresses_duplicate(self):
        self.assertFalse(guard.should_current_run_execute(
            [self.success, self.current], self.current, "workflow_run"
        ))

    def test_newer_source_revision_gets_a_new_check(self):
        previous = dict(self.success, head_sha="b" * 40)
        self.assertTrue(guard.should_current_run_execute(
            [previous, self.current], self.current, "workflow_run"
        ))

    def test_same_revision_on_new_bangladesh_date_gets_a_new_daily_check(self):
        previous = dict(self.success, created_at="2026-11-06T03:20:00Z")
        self.assertTrue(guard.should_current_run_execute(
            [previous, self.current], self.current, "workflow_run"
        ))

    def test_failed_same_revision_check_can_be_retried(self):
        previous = dict(self.success, conclusion="failure")
        self.assertTrue(guard.should_current_run_execute(
            [previous, self.current], self.current, "workflow_run"
        ))

    def test_active_same_revision_check_blocks_overlap(self):
        previous = dict(self.current, id=18, created_at="2026-11-07T03:10:00Z")
        self.assertFalse(guard.should_current_run_execute(
            [previous, self.current], self.current, "workflow_run"
        ))

    def test_manual_dispatch_can_repeat_completed_success(self):
        self.assertTrue(guard.should_current_run_execute(
            [self.success, self.current], self.current, "workflow_dispatch"
        ))

    def test_rerun_attempt_can_repeat_completed_success(self):
        self.assertTrue(guard.should_current_run_execute(
            [self.success, self.current], self.current, "workflow_run", run_attempt=2
        ))

    def test_missing_source_sha_fails_closed(self):
        current = dict(self.current, head_sha="bad")
        with self.assertRaises(ValueError):
            guard.should_current_run_execute([self.success], current)

    def test_only_successful_required_check_step_counts_as_success(self):
        incomplete = dict(self.success, jobs=[{
            "name": "check", "status": "completed", "conclusion": "success",
            "steps": [{"name": "Check main IPTV Xtream gateway", "conclusion": "skipped"}],
        }])
        self.assertTrue(guard.should_current_run_execute(
            [incomplete, self.current], self.current, "workflow_run"
        ))

    def test_bangladesh_date_boundary_is_respected(self):
        late_utc = dict(self.success, created_at="2026-11-07T17:59:00Z")
        self.assertTrue(guard.same_day(late_utc, self.current))
        next_bd_day = dict(self.success, created_at="2026-11-07T18:00:00Z")
        self.assertFalse(guard.same_day(next_bd_day, self.current))


if __name__ == "__main__":
    unittest.main()
