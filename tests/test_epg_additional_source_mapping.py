import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from augment_epg_mapping_from_additional_sources import apply_exact_source_matches


class AdditionalIndianSourceMappingTests(unittest.TestCase):
    def test_appends_unique_provider_ids_and_sources_to_existing_mapping(self):
        rows = [{
            "group": "Indian Bangla",
            "channel": "Colors Bangla",
            "tvg_id": "ColorsBangla.in",
            "epg_id": "legacy.colors.bangla",
            "source": "https://legacy.example/epg.xml",
            "status": "MAPPED",
            "note": "Existing verified mapping.",
        }]
        channels = [{"tvg_id": "ColorsBangla.in", "name": "Colors Bangla"}]
        source_hits = {
            "https://provider-a.example/epg.xml": {
                "colorsbangla": {"ColorsBangla.in@SD"}
            },
            "https://provider-b.example/epg.xml": {
                "colorsbangla": {"ColorsBangla.in@HD"}
            },
            "https://provider-c.example/epg.xml": {
                "colorsbangla": {"ColorsBangla.in@HD"}
            },
        }

        updated, added_ids, updated_channels = apply_exact_source_matches(
            rows, channels, source_hits, locked_targets=set()
        )

        row = updated[0]
        self.assertEqual(
            row["epg_id"],
            "legacy.colors.bangla | ColorsBangla.in@HD | ColorsBangla.in@SD",
        )
        self.assertEqual(
            row["source"],
            "https://legacy.example/epg.xml | "
            "https://provider-a.example/epg.xml | "
            "https://provider-b.example/epg.xml | "
            "https://provider-c.example/epg.xml",
        )
        self.assertEqual(row["status"], "MAPPED")
        self.assertIn("Existing verified mapping.", row["note"])
        self.assertEqual(added_ids, 2)
        self.assertEqual(updated_channels, 1)

    def test_new_exact_match_creates_mapping_without_claiming_schedule_coverage(self):
        rows = [{
            "group": "Indian Movies",
            "channel": "Goldmines Movies",
            "tvg_id": "GoldminesMovies.in@SD",
            "epg_id": "",
            "source": "",
            "status": "NO_GUIDE_HIT",
            "note": "",
        }]
        channels = [{
            "tvg_id": "GoldminesMovies.in@SD",
            "name": "Goldmines Movies",
        }]
        source_hits = {
            "https://provider.example/epg.xml": {
                "goldminesmovies": {"GoldminesMovies.in"}
            }
        }

        updated, added_ids, updated_channels = apply_exact_source_matches(
            rows, channels, source_hits, locked_targets=set()
        )

        self.assertEqual(updated[0]["epg_id"], "GoldminesMovies.in")
        self.assertEqual(updated[0]["status"], "MAPPED_ID_ONLY")
        self.assertEqual(added_ids, 1)
        self.assertEqual(updated_channels, 1)

    def test_strict_locked_identity_is_never_extended(self):
        rows = [{
            "group": "Indian Entertainment",
            "channel": "Locked Channel",
            "tvg_id": "LockedChannel.in",
            "epg_id": "trusted.locked.id",
            "source": "https://trusted.example/epg.xml",
            "status": "MAPPED",
            "note": "Strict identity lock.",
        }]
        channels = [{"tvg_id": "LockedChannel.in", "name": "Locked Channel"}]
        source_hits = {
            "https://other.example/epg.xml": {
                "lockedchannel": {"other.provider.id"}
            }
        }

        updated, added_ids, updated_channels = apply_exact_source_matches(
            rows, channels, source_hits, locked_targets={"LockedChannel.in"}
        )

        self.assertEqual(updated[0]["epg_id"], "trusted.locked.id")
        self.assertEqual(updated[0]["source"], "https://trusted.example/epg.xml")
        self.assertEqual(added_ids, 0)
        self.assertEqual(updated_channels, 0)

    def test_ambiguous_source_name_is_not_added(self):
        rows = [{
            "group": "Indian Entertainment",
            "channel": "Colors",
            "tvg_id": "Colors.in",
            "epg_id": "",
            "source": "",
            "status": "NO_GUIDE_HIT",
            "note": "",
        }]
        channels = [{"tvg_id": "Colors.in", "name": "Colors"}]
        source_hits = {
            "https://ambiguous.example/epg.xml": {
                "colors": {"Colors.in", "ColorsHD.in"}
            }
        }

        updated, added_ids, updated_channels = apply_exact_source_matches(
            rows, channels, source_hits, locked_targets=set()
        )

        self.assertEqual(updated[0]["epg_id"], "")
        self.assertEqual(added_ids, 0)
        self.assertEqual(updated_channels, 0)


if __name__ == "__main__":
    unittest.main()
