from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.audit_automation_v2_runtime_dependencies import trace_workflow_shell_entrypoints


class WorkflowShellEntrypointTraceTests(unittest.TestCase):
    def test_links_python_entrypoints_and_keeps_transitive_trace_open(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "scripts").mkdir()
            (root / "scripts" / "candidate.py").write_text("print('candidate')\n", encoding="utf-8")
            detail = (
                "run: |\n"
                "  python scripts/candidate.py --dry-run\n"
                "  python - <<'PY'\n"
                "  print('inline')\n"
                "  PY\n"
            )
            trace = trace_workflow_shell_entrypoints(detail, root)
            self.assertEqual(trace["referenced_python_entrypoints"], ["scripts/candidate.py"])
            self.assertTrue(trace["referenced_python_entrypoints_exist"])
            self.assertTrue(trace["inline_python_heredoc_present"])
            self.assertEqual(trace["trace_status"], "entrypoints_linked_transitive_effects_pending")
            self.assertFalse(trace["trace_complete"])


if __name__ == "__main__":
    unittest.main()
