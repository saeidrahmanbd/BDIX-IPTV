import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"


def workflow_text(name):
    return (WORKFLOWS / name).read_text(encoding="utf-8")


def concurrency_group(source):
    match = re.search(
        r"(?ms)^concurrency:\s*\n\s+group:\s*([^\n]+)\n\s+cancel-in-progress:\s*false\s*$",
        source,
    )
    if not match:
        raise AssertionError("workflow must declare a non-cancelling concurrency group")
    return match.group(1).strip()


class WorkflowSafetyTests(unittest.TestCase):
    def test_candidate_and_state_writers_share_one_non_cancelling_lock(self):
        candidate = workflow_text("automation-v2-candidate-bundle.yml")
        state_check = workflow_text("automation-v2-state-store-check.yml")
        self.assertEqual(concurrency_group(candidate), "automation-v2-state-store")
        self.assertEqual(concurrency_group(state_check), "automation-v2-state-store")

    def test_publication_and_rollback_pr_preparers_share_one_lock(self):
        publication = workflow_text("automation-v2-prepare-publication-pr.yml")
        rollback = workflow_text("automation-v2-prepare-rollback-pr.yml")
        self.assertEqual(concurrency_group(publication), "automation-v2-publication-pr")
        self.assertEqual(concurrency_group(rollback), "automation-v2-publication-pr")

    def test_candidate_bundle_has_no_production_push_or_pull_request_authority(self):
        source = workflow_text("automation-v2-candidate-bundle.yml")
        runner = (ROOT / "scripts" / "run_automation_v2_candidate_bundle.py").read_text(encoding="utf-8")
        self.assertIn('"publish": False', runner)
        self.assertNotIn("git push", source.lower())
        self.assertNotIn("gh pr create", source.lower())

    def test_publication_pr_requires_explicit_confirmation_and_never_auto_merges(self):
        source = workflow_text("automation-v2-prepare-publication-pr.yml")
        self.assertIn("PREPARE PUBLISH PR", source)
        self.assertIn("refs/heads/main", source)
        self.assertNotIn("--auto", source)

    def test_rollback_pr_requires_explicit_confirmation_and_never_auto_merges(self):
        source = workflow_text("automation-v2-prepare-rollback-pr.yml")
        self.assertIn("PREPARE ROLLBACK PR", source)
        self.assertIn("refs/heads/main", source)
        self.assertNotIn("--auto", source)
        self.assertIn("git push --set-upstream origin", source)


if __name__ == "__main__":
    unittest.main()
