import unittest
from datetime import datetime
from zoneinfo import ZoneInfo

from scripts.recover_automation_v2_candidate_run import decide_dispatch

BD = ZoneInfo("Asia/Dhaka")
SHA = "a" * 40


class V2MissedRunRecoveryTests(unittest.TestCase):
    def test_missing_run_dispatches(self):
        dispatch, reason = decide_dispatch([], SHA, datetime(2026, 11, 14, tzinfo=BD).date())
        self.assertTrue(dispatch)
        self.assertIn("no candidate-bundle run", reason)

    def test_successful_current_main_run_suppresses_dispatch(self):
        runs = [{
            "created_at": "2026-11-14T03:35:00Z", "head_sha": SHA,
            "run_number": 10, "status": "completed", "conclusion": "success",
        }]
        dispatch, _ = decide_dispatch(runs, SHA, datetime(2026, 11, 14, 10, 0, tzinfo=BD).date())
        self.assertFalse(dispatch)

    def test_failed_current_main_run_dispatches_retry(self):
        runs = [{
            "created_at": "2026-11-14T03:35:00Z", "head_sha": SHA,
            "run_number": 10, "status": "completed", "conclusion": "failure",
        }]
        dispatch, reason = decide_dispatch(runs, SHA, datetime(2026, 11, 14, 10, 0, tzinfo=BD).date())
        self.assertTrue(dispatch)
        self.assertIn("retry is due", reason)

    def test_in_progress_run_is_never_overlapped(self):
        runs = [{
            "created_at": "2026-11-14T03:35:00Z", "head_sha": SHA,
            "run_number": 10, "status": "in_progress", "conclusion": None,
        }]
        dispatch, _ = decide_dispatch(runs, SHA, datetime(2026, 11, 14, 10, 0, tzinfo=BD).date())
        self.assertFalse(dispatch)

    def test_old_main_success_does_not_suppress_new_commit(self):
        runs = [{
            "created_at": "2026-11-14T03:35:00Z", "head_sha": "b" * 40,
            "run_number": 10, "status": "completed", "conclusion": "success",
        }]
        dispatch, _ = decide_dispatch(runs, SHA, datetime(2026, 11, 14, 10, 0, tzinfo=BD).date())
        self.assertTrue(dispatch)

    def test_utc_timestamp_is_compared_using_bangladesh_date(self):
        runs = [{
            "created_at": "2026-11-13T19:00:00Z", "head_sha": SHA,
            "run_number": 10, "status": "completed", "conclusion": "success",
        }]
        dispatch, _ = decide_dispatch(runs, SHA, datetime(2026, 11, 14, 1, 30, tzinfo=BD).date())
        self.assertFalse(dispatch)


if __name__ == "__main__":
    unittest.main()
