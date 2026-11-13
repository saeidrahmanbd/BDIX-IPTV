import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import scripts.run_automation_v2_candidate_bundle as runner


class CandidateBundleScriptTests(unittest.TestCase):
    def test_failure_always_writes_machine_readable_diagnostics(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            argv = [
                "run_automation_v2_candidate_bundle.py",
                "--baseline-commit", "a" * 40,
            ]
            output = io.StringIO()
            with (
                patch.object(runner, "ROOT", root),
                patch.object(runner, "store_from_environment", return_value=object()),
                patch.object(runner, "run_candidate_bundle", side_effect=ValueError("EPG gate rejected candidate")),
                patch.object(sys, "argv", argv),
                contextlib.redirect_stdout(output),
            ):
                exit_code = runner.main()

            report_path = root / "reports" / "automation-v2" / "candidate-run.json"
            self.assertEqual(exit_code, 1)
            self.assertTrue(report_path.is_file())
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["status"], "failed")
            self.assertEqual(report["error_type"], "ValueError")
            self.assertIn("EPG gate rejected candidate", report["reason"])
            self.assertFalse(report["publish"])
            self.assertFalse(report["production_files_modified"])


if __name__ == "__main__":
    unittest.main()
