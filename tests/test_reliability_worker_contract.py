import json
import pathlib
import re
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKER = ROOT / "automation/reliability/worker"

class ReliabilityWorkerContractTests(unittest.TestCase):
    def test_worker_keeps_shadow_default_and_guards_dispatch(self):
        source = (WORKER / "src/index.js").read_text(encoding="utf-8")
        config = (WORKER / "wrangler.toml").read_text(encoding="utf-8")
        self.assertIn('env.MODE !== "active"', source)
        self.assertIn("canDispatchSameDay", source)
        self.assertIn('MODE = "shadow"', config)
        self.assertIn("workflow_dispatch", source)
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

    # --- External watchdog trigger -------------------------------------

    def _checkpoints(self):
        source = (WORKER / "src/watchdog-trigger.js").read_text(encoding="utf-8")
        match = re.search(r"export const CHECKPOINTS = \[([^\]]+)\]", source)
        self.assertIsNotNone(match)
        return re.findall(r'"(\d{2}:\d{2})"', match.group(1))

    def test_watchdog_trigger_modes_never_enable_direct_writer_dispatch(self):
        config = (WORKER / "wrangler.toml").read_text(encoding="utf-8")
        production, preview = config.split("[previews.vars]", 1)
        self.assertIn('WATCHDOG_TRIGGER_MODE = "active"', production)
        self.assertIn('WATCHDOG_TRIGGER_MODE = "dry_run"', preview)
        self.assertNotIn('WATCHDOG_TRIGGER_MODE = "active"', preview)
        # The trigger is separate from the reconciler: MODE stays shadow everywhere.
        self.assertEqual(config.count('MODE = "shadow"'), 2)
        self.assertNotIn('MODE = "active"', config.replace("WATCHDOG_TRIGGER_MODE", ""))

    def test_watchdog_trigger_can_only_dispatch_the_watchdog_workflow(self):
        source = (WORKER / "src/watchdog-trigger.js").read_text(encoding="utf-8")
        self.assertEqual(source.count("dispatchWorkflow("), 1)
        self.assertIn('WATCHDOG_WORKFLOW_FILE = "discovery-schedule-watchdog.yml"', source)
        for workflow in (
            "iptv-maintenance.yml", "new-channel-discovery.yml", "international-channel-discovery.yml",
            "playlist-logo-localization.yml", "international-stream-health.yml", "epg-refresh.yml",
            "check-xtream.yml",
        ):
            self.assertNotIn(workflow, source)

    def test_checkpoints_follow_each_guard_recovery_threshold(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import discovery_schedule_guard as guard

        checkpoints = [int(c[:2]) * 60 + int(c[3:]) for c in self._checkpoints()]
        self.assertEqual(checkpoints, sorted(set(checkpoints)))
        for workflow, (hour, minute) in guard.RECOVERY_AFTER_LOCAL.items():
            threshold = hour * 60 + minute
            # A checkpoint must fire soon after each workflow becomes recoverable,
            # otherwise the watchdog would sleep through its own recovery window.
            self.assertTrue(
                any(threshold <= c < threshold + 15 for c in checkpoints),
                f"no checkpoint within 15 minutes after the {workflow} recovery threshold",
            )

    def test_no_credentials_are_committed_with_the_worker(self):
        config = (WORKER / "wrangler.toml").read_text(encoding="utf-8")
        for secret in ("GITHUB_APP_PRIVATE_KEY", "RECONCILE_BEARER_TOKEN", "HEALTHCHECKS_PING_URL"):
            self.assertNotIn(secret, config)
        for path in (WORKER / "src").glob("*.js"):
            text = path.read_text(encoding="utf-8")
            if path.name.endswith(".test.js"):
                continue
            self.assertNotRegex(text, r"-----BEGIN [A-Z ]*PRIVATE KEY-----\s*\S{20,}")
            self.assertNotRegex(text, r"ghp_[A-Za-z0-9]{20,}|ghs_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}")

    def test_scheduled_handler_runs_reconciliation_and_trigger_independently(self):
        source = (WORKER / "src/index.js").read_text(encoding="utf-8")
        self.assertIn("Promise.allSettled([runReconciliationWithHeartbeat(env),runWatchdogTriggerSafely(env)])", source)
        self.assertIn("/watchdog-dispatch", source)

    def test_watchdog_trigger_migration_is_idempotent(self):
        sql = (WORKER / "migrations/0002_watchdog_triggers.sql").read_text(encoding="utf-8")
        self.assertIn("CREATE TABLE IF NOT EXISTS watchdog_triggers", sql)
        self.assertIn("trigger_key TEXT PRIMARY KEY", sql)
        self.assertIn("CREATE INDEX IF NOT EXISTS", sql)


if __name__ == "__main__":
    unittest.main()
