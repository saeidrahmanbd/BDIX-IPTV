import csv
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import epg_research_inventory as inventory  # noqa: E402
import update_epg_published_coverage as coverage  # noqa: E402


class IptvOnlyCoverageScopeTests(unittest.TestCase):
    def test_headline_generator_reads_only_iptv_playlist(self):
        self.assertEqual([filename for filename, _ in coverage.PLAYLISTS], ["IPTV-Playlist.m3u"])

    def test_inventory_reads_only_iptv_playlist(self):
        self.assertEqual(inventory.PLAYLIST.name, "IPTV-Playlist.m3u")

    def test_inventory_never_proposes_ids_outside_the_mapping_snapshot(self):
        if not inventory.OUT_CSV.is_file():
            self.skipTest("inventory not generated")
        mapping_ids = set()
        with inventory.MAPPING.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                if (row.get("epg_id") or "").strip():
                    mapping_ids.add(row["epg_id"].strip())
        with inventory.OUT_CSV.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                recorded = row["epg_id_recorded"].strip()
                if recorded and recorded != "UNKNOWN":
                    self.assertIn(recorded, mapping_ids)
                self.assertNotEqual(row["missing_requirement"], "")

    def test_every_inventory_category_has_a_requirement_and_action(self):
        self.assertTrue(set(inventory.CATEGORIES))
        for meaning, requirement, action in inventory.CATEGORIES.values():
            self.assertTrue(meaning.strip() and requirement.strip() and action.strip())


if __name__ == "__main__":
    unittest.main()
