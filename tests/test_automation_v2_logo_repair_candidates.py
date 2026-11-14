from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.build_automation_v2_logo_repair_candidates import build_proposals


class LogoRepairCandidateTests(unittest.TestCase):
    def _fixture(self, root: Path):
        (root / "logos").mkdir()
        (root / "logos" / "Exact Channel.png").write_bytes(b"image-a")
        (root / "logos" / "Duplicate-Name.svg").write_bytes(b"image-b")
        (root / "logos" / "duplicate name.png").write_bytes(b"image-c")
        (root / "IPTV-Playlist.m3u").write_text(
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-name="Exact Channel" group-title="Bangladesh",Exact Channel\n'
            'https://example.invalid/live\n'
            '#EXTINF:-1 tvg-name="Duplicate Name" group-title="Bangladesh",Duplicate Name\n'
            'https://example.invalid/live2\n'
            '#EXTINF:-1 tvg-name="No Match" group-title="Bangladesh",No Match\n'
            'https://example.invalid/live3\n'
            '#EXTINF:-1 tvg-name="Review Channel" group-title="Review",Review Channel\n'
            'https://example.invalid/review\n', encoding="utf-8")

    def test_unique_match_is_proposal_only_and_source_is_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._fixture(root)
            playlist = root / "IPTV-Playlist.m3u"
            before = playlist.read_bytes()
            report = build_proposals(root)
            self.assertEqual(report["counts"]["unique_exact_match"], 1)
            self.assertEqual(report["proposals"][0]["decision"], "owner_review_required")
            self.assertEqual(playlist.read_bytes(), before)
            self.assertFalse(report["safety"]["automatic_assignment_performed"])

    def test_ambiguous_match_is_never_selected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._fixture(root)
            report = build_proposals(root)
            ambiguous = [p for p in report["proposals"] if p["channel_name"] == "Duplicate Name"]
            self.assertEqual(len(ambiguous), 1)
            self.assertEqual(ambiguous[0]["decision"], "ambiguous_no_change")
            self.assertNotIn("proposed_local_logo", ambiguous[0])

    def test_review_groups_are_excluded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._fixture(root)
            report = build_proposals(root)
            self.assertEqual(report["counts"]["rows_scanned"], 4)
            self.assertEqual(report["counts"]["active_rows"], 3)


if __name__ == "__main__":
    unittest.main()
