import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "epg-refresh.yml"
REQUIRED_OUTPUTS = (
    "reports/epg-iptv-coverage.json",
    "reports/epg-research-inventory.csv",
    "reports/epg-research-inventory.md",
)


def run_script(workflow):
    scripts = []
    for job in workflow.get("jobs", {}).values():
        for step in job.get("steps", []):
            if "run" in step:
                scripts.append(step["run"])
    return "\n".join(scripts)


class IptvOnlyEpgWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = WORKFLOW.read_text(encoding="utf-8")
        cls.workflow = yaml.safe_load(cls.text)
        cls.runs = run_script(cls.workflow)

    def test_iptv_only_generators_run_after_the_mapping_producer(self):
        coverage = self.runs.index("python scripts/update_epg_published_coverage.py")
        inventory = self.runs.index("python scripts/epg_research_inventory.py")
        self.assertLess(coverage, inventory)
        last_producer = self.runs.rindex("python scripts/epg_coverage.py")
        self.assertLess(last_producer, coverage)

    def test_all_iptv_outputs_are_required_and_committed(self):
        for output in REQUIRED_OUTPUTS:
            with self.subTest(output=output):
                self.assertIn(output, self.runs)
                self.assertIn(output, self.text)
        commit_line = next(line for line in self.runs.splitlines() if line.strip().startswith("git add -f epg/epg.xml"))
        for output in REQUIRED_OUTPUTS:
            self.assertIn(output, commit_line)

    def test_epg_freshness_is_validated_after_generation(self):
        self.assertIn("python scripts/validate_report_freshness.py --mode epg", self.runs)
        self.assertLess(
            self.runs.index("python scripts/epg_research_inventory.py"),
            self.runs.rindex("python scripts/validate_report_freshness.py --mode epg"),
        )

    def test_international_playlist_is_not_a_refresh_trigger_or_change_guard(self):
        push_paths = self.workflow[True]["push"]["paths"] if True in self.workflow else self.workflow["on"]["push"]["paths"]
        self.assertNotIn("International-Playlist.m3u", push_paths)
        for line in self.text.splitlines():
            if "CHANGED_INPUTS=" in line:
                self.assertNotIn("International-Playlist", line)

    def test_international_playlist_is_not_in_the_iptv_outputs_commit(self):
        commit_line = next(line for line in self.runs.splitlines() if line.strip().startswith("git add -f epg/epg.xml"))
        self.assertNotIn("International-Playlist", commit_line)


if __name__ == "__main__":
    unittest.main()
