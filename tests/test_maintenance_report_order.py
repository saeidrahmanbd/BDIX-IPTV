"""Guard the maintenance ordering that keeps report fingerprints current."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "iptv-maintenance.yml"


class MaintenanceReportOrderTests(unittest.TestCase):
    def test_final_playlist_backfill_precedes_all_final_fingerprinted_reports(self):
        workflow = WORKFLOW.read_text(encoding="utf-8")
        # The last backfill must occur after the optional repair/correction pass.
        backfill = workflow.rfind("python scripts/iptv_metadata_backfill.py")
        self.assertGreaterEqual(backfill, 0)

        def next_pos(needle, start):
            pos = workflow.find(needle, start)
            self.assertGreaterEqual(pos, 0, f"missing workflow step: {needle}")
            return pos

        guard = next_pos(
            "python scripts/maintenance_helpers.py verify-no-unauthorized-removals",
            backfill,
        )
        audit = next_pos("python scripts/audit_playlist.py", guard)
        gate = next_pos("python scripts/pre_publish_gate.py", audit)
        history = next_pos("python scripts/record_maintenance_history.py", gate)
        epg = next_pos("python scripts/epg_coverage.py", history)
        logos = next_pos("python scripts/generate_logo_authenticity_manifest.py", epg)
        freshness = next_pos("python scripts/validate_report_freshness.py", logos)

        self.assertLess(backfill, guard)
        self.assertLess(guard, audit)
        self.assertLess(audit, gate)
        self.assertLess(gate, history)
        self.assertLess(history, epg)
        self.assertLess(epg, logos)
        self.assertLess(logos, freshness)


if __name__ == "__main__":
    unittest.main()
