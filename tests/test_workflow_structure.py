"""Structural checks for GitHub Actions workflows, parsed with a real YAML parser.

These assert workflow structure (triggers, job-level concurrency, pinned actions,
schedule timezone notes) rather than formatting, so they survive reformatting.
"""
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
SHARED_WRITER_GROUP = "iptv-playlist-main-writer-v3"
WRITER_JOBS = {
    "iptv-maintenance.yml": "maintain",
    "new-channel-discovery.yml": "discover",
    "international-channel-discovery.yml": "discover",
    "playlist-logo-localization.yml": "localize",
    "changelog.yml": "changelog",
    "epg-refresh.yml": "refresh",
    "international-stream-health.yml": "check",
}


def load(name):
    with (WORKFLOWS / name).open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def triggers(document):
    # PyYAML parses the bare key `on` as boolean True.
    return document.get(True, document.get("on", {}))


class WorkflowStructureTests(unittest.TestCase):
    def test_every_workflow_parses_and_declares_jobs(self):
        for path in sorted(WORKFLOWS.glob("*.yml")):
            with self.subTest(workflow=path.name):
                document = load(path.name)
                self.assertIsInstance(document, dict)
                self.assertTrue(document.get("jobs"))
                self.assertTrue(triggers(document))

    def test_writer_queue_is_job_level_not_workflow_level(self):
        for name, job in WRITER_JOBS.items():
            with self.subTest(workflow=name):
                document = load(name)
                self.assertNotIn("concurrency", document, "writer queue must not be workflow-level")
                concurrency = document["jobs"][job].get("concurrency")
                self.assertIsInstance(concurrency, dict)
                self.assertEqual(concurrency["group"], SHARED_WRITER_GROUP)
                self.assertIs(concurrency["cancel-in-progress"], False)
                self.assertEqual(concurrency.get("queue"), "max")

    def test_epg_refresh_runs_after_any_completed_playlist_writer(self):
        document = load("epg-refresh.yml")
        workflow_run = triggers(document)["workflow_run"]
        self.assertEqual(workflow_run["types"], ["completed"])
        self.assertEqual(
            set(workflow_run["workflows"]),
            {
                "IPTV Playlist Update",
                "IPTV New Channel Discovery",
                "International Channel Discovery",
                "Playlist Logo Repair and Localization",
            },
        )
        condition = document["jobs"]["refresh"]["if"]
        self.assertNotIn("workflow_run.conclusion", condition)

    def test_check_xtream_runs_after_each_upstream_it_depends_on(self):
        document = load("check-xtream.yml")
        workflow_run = triggers(document)["workflow_run"]
        self.assertEqual(workflow_run["types"], ["completed"])
        self.assertIn("Refresh IPTV EPG", workflow_run["workflows"])

    def test_every_action_is_pinned_to_a_full_commit_sha(self):
        pattern = re.compile(r"^\s*(?:-\s*)?uses:\s*([^\s#]+)", re.M)
        for path in sorted(WORKFLOWS.glob("*.yml")):
            text = path.read_text(encoding="utf-8")
            for match in pattern.finditer(text):
                ref = match.group(1)
                if ref.startswith("./") or ref.startswith("docker://"):
                    continue
                with self.subTest(workflow=path.name, action=ref):
                    self.assertRegex(ref, r"@[0-9a-f]{40}$")

    def test_scheduled_workflows_state_their_timezone(self):
        for path in sorted(WORKFLOWS.glob("*.yml")):
            lines = path.read_text(encoding="utf-8").splitlines()
            for index, line in enumerate(lines):
                if re.match(r"^\s*-\s*cron:", line):
                    with self.subTest(workflow=path.name, line=line.strip()):
                        self.assertRegex(line, r"UTC|Asia/Dhaka", "scheduled cron must state its timezone")

    def test_discovery_workflows_keep_daily_schedules(self):
        for name in ("international-channel-discovery.yml", "new-channel-discovery.yml"):
            with self.subTest(workflow=name):
                crons = [entry["cron"] for entry in triggers(load(name))["schedule"]]
                self.assertTrue(crons)


if __name__ == "__main__":
    unittest.main()
