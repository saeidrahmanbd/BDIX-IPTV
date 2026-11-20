import json
import re
import sqlite3
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "automation" / "reliability" / "workflow_registry.json"
SCHEMA_PATH = ROOT / "automation" / "reliability" / "schema.sql"
WORKFLOWS = ROOT / ".github" / "workflows"

EXPECTED = {
    "iptv_new_channel_discovery": ("new-channel-discovery.yml", "05:07", "7 23 * * *", "discover"),
    "international_channel_discovery": ("international-channel-discovery.yml", "05:17", "17 23 * * *", "discover"),
    "playlist_logo_localization": ("playlist-logo-localization.yml", "05:27", "27 23 * * *", "localize"),
    "international_stream_health": ("international-stream-health.yml", "05:37", "37 23 * * *", "check"),
    "iptv_playlist_maintenance": ("iptv-maintenance.yml", "05:47", "47 23 * * *", "maintain"),
    "epg_refresh": ("epg-refresh.yml", "06:07", "7 0 * * *", "refresh"),
}


class ReliabilityFoundationTests(unittest.TestCase):
    def test_registry_has_six_unique_stable_workflow_ids(self):
        data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        self.assertEqual(data["timezone"], "Asia/Dhaka")
        workflows = data["workflows"]
        self.assertEqual(len(workflows), 6)
        ids = [item["id"] for item in workflows]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), set(EXPECTED))

    def test_registry_matches_live_workflow_schedules_and_job_ids(self):
        data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        for item in data["workflows"]:
            filename, local_time, cron, job_id = EXPECTED[item["id"]]
            self.assertEqual(item["workflow_file"], filename)
            self.assertEqual(item["expected_local_time"], local_time)
            self.assertEqual(item["expected_utc_cron"], cron)
            self.assertEqual(item["required_job_id"], job_id)
            source = (WORKFLOWS / filename).read_text(encoding="utf-8")
            self.assertIn(f"cron: '{cron}'", source)
            self.assertRegex(source, rf"(?m)^  {re.escape(job_id)}:")

    def test_every_registered_workflow_uses_the_shared_playlist_writer_lock(self):
        data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        for item in data["workflows"]:
            source = (WORKFLOWS / item["workflow_file"]).read_text(encoding="utf-8")
            self.assertIn("group: iptv-playlist-main-writer-v5", source)

    def test_registry_does_not_authorize_playlist_policy_changes(self):
        data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        for item in data["workflows"]:
            self.assertEqual(item["completion_contract"], "bdix-automation-completion-v1")
        docs = (ROOT / "docs" / "automation-reliability" / "architecture.md").read_text(encoding="utf-8")
        self.assertIn("IPTV-Playlist.m3u", docs)
        self.assertIn("missed day resets", docs)

    def test_d1_schema_applies_and_enforces_unique_daily_obligations(self):
        connection = sqlite3.connect(":memory:")
        connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        connection.execute(
            """INSERT INTO reliability_executions
            (execution_key, workflow_id, business_date, registry_version, expected_at_utc,
             state, created_at_utc, updated_at_utc)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            ("key-1", "iptv_new_channel_discovery", "2026-11-16", "v1",
             "2026-11-15T23:00:00Z", "EXPECTED", "2026-11-15T23:00:00Z", "2026-11-15T23:00:00Z"),
        )
        with self.assertRaises(sqlite3.IntegrityError):
            connection.execute(
                """INSERT INTO reliability_executions
                (execution_key, workflow_id, business_date, registry_version, expected_at_utc,
                 state, created_at_utc, updated_at_utc)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                ("key-2", "iptv_new_channel_discovery", "2026-11-16", "v1",
                 "2026-11-15T23:00:00Z", "EXPECTED", "2026-11-15T23:00:00Z", "2026-11-15T23:00:00Z"),
            )
        connection.close()


if __name__ == "__main__":
    unittest.main()
