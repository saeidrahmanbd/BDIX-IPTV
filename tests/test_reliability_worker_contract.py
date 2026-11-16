import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKER = ROOT / "automation/reliability/worker"

class ReliabilityWorkerContractTests(unittest.TestCase):
    def test_worker_is_shadow_only_and_never_dispatches(self):
        source = (WORKER / "src/index.js").read_text(encoding="utf-8")
        self.assertIn('mode: "shadow"', source)
        self.assertIn('dispatched: 0', source)
        self.assertNotIn("workflow_dispatch", source)
        self.assertNotIn("api.github.com", source)

    def test_cron_and_d1_binding_are_declared(self):
        config = (WORKER / "wrangler.toml").read_text(encoding="utf-8")
        self.assertIn('crons = ["* * * * *"]', config)
        self.assertIn('binding = "RELIABILITY_DB"', config)
        self.assertNotIn("REPLACE_WITH_YOUR_CLOUDFLARE_D1_DATABASE_ID", config)
        database_id = next(line.split("=", 1)[1].strip().strip("\\\"") for line in config.splitlines() if line.startswith("database_id"))
        self.assertRegex(database_id, r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")

    def test_registry_and_worker_share_schedule_field(self):
        registry = json.loads((ROOT / "automation/reliability/workflow_registry.json").read_text(encoding="utf-8"))
        source = (WORKER / "src/index.js").read_text(encoding="utf-8")
        self.assertEqual(len(registry["workflows"]), 6)
        self.assertIn("workflow.expected_local_time", source)

    def test_d1_migration_has_idempotent_obligation_key(self):
        sql = (WORKER / "migrations/0001_reliability_ledger.sql").read_text(encoding="utf-8")
        self.assertIn("UNIQUE (workflow_id, business_date)", sql)
        self.assertIn("CREATE TABLE IF NOT EXISTS reliability_events", sql)

if __name__ == "__main__":
    unittest.main()
