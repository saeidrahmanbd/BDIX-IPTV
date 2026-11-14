from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.apply_automation_v2_approved_logo_candidates import build_candidates


class ApprovedLogoCandidateTests(unittest.TestCase):
    def _fixture(self, root: Path):
        (root / "logos").mkdir()
        asset = root / "logos" / "Exact Channel.png"
        asset.write_bytes(b"verified-local-image")
        playlist = root / "IPTV-Playlist.m3u"
        playlist.write_text(
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-name="Exact Channel" tvg-logo="old.png" group-title="Bangladesh",Exact Channel\n'
            'https://stream.invalid/live\n', encoding="utf-8")
        approval = {
            "playlist": "IPTV-Playlist.m3u", "line": 2,
            "channel_name": "Exact Channel", "expected_current_logo": "old.png",
            "approved_local_logo": "logos/Exact Channel.png",
            "asset_sha256": hashlib.sha256(asset.read_bytes()).hexdigest(),
        }
        manifest = root / "approved.json"
        source_sha = hashlib.sha256(playlist.read_bytes()).hexdigest()
        manifest.write_text(json.dumps({
            "schema_version": 1,
            "source_playlist_sha256": {"IPTV-Playlist.m3u": source_sha},
            "approvals": [approval],
        }), encoding="utf-8")
        return playlist, manifest

    def test_changes_only_isolated_candidate_and_pins_local_asset(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            playlist, manifest = self._fixture(root)
            before = playlist.read_bytes()
            result = build_candidates(root, manifest, root / "reports" / "automation-v2" / "candidate")
            candidate = root / result["changed_playlists"][0]["candidate_path"]
            self.assertIn('tvg-logo="logos/Exact Channel.png"', candidate.read_text())
            self.assertEqual(playlist.read_bytes(), before)
            self.assertFalse(result["safety"]["production_playlists_modified"])
            self.assertFalse(result["safety"]["publication_performed"])

    def test_stale_channel_identity_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            playlist, manifest = self._fixture(root)
            data = json.loads(manifest.read_text())
            data["approvals"][0]["channel_name"] = "Different Channel"
            manifest.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, "channel identity changed"):
                build_candidates(root, manifest, root / "reports" / "automation-v2" / "candidate")
            self.assertEqual(playlist.read_bytes().count(b"old.png"), 1)

    def test_modified_asset_hash_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            playlist, manifest = self._fixture(root)
            (root / "logos" / "Exact Channel.png").write_bytes(b"changed")
            with self.assertRaisesRegex(ValueError, "SHA-256 does not match"):
                build_candidates(root, manifest, root / "reports" / "automation-v2" / "candidate")
            self.assertEqual(playlist.read_bytes().count(b"old.png"), 1)

    def test_stale_source_playlist_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            playlist, manifest = self._fixture(root)
            playlist.write_text(playlist.read_text() + "# changed\n")
            with self.assertRaisesRegex(ValueError, "source playlist SHA-256 changed"):
                build_candidates(root, manifest, root / "reports" / "automation-v2" / "candidate")

    def test_path_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "logos").mkdir()
            manifest = root / "approved.json"
            playlist = root / "IPTV-Playlist.m3u"
            playlist.write_text('#EXTM3U\n#EXTINF:-1, x\nhttps://stream.invalid/x\n')
            manifest.write_text(json.dumps({"schema_version": 1, "source_playlist_sha256": {
                "IPTV-Playlist.m3u": hashlib.sha256(playlist.read_bytes()).hexdigest()
            }, "approvals": [{
                "playlist": "IPTV-Playlist.m3u", "line": 2, "channel_name": "x",
                "expected_current_logo": "", "approved_local_logo": "logos/../../outside.png",
                "asset_sha256": "0" * 64
            }]}))
            with self.assertRaisesRegex(ValueError, "approved logo path is unsafe"):
                build_candidates(root, manifest, root / "reports" / "automation-v2" / "candidate")

    def test_logo_root_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            root = Path(tmp)
            (Path(outside) / "asset.png").write_bytes(b"outside")
            (root / "logos").symlink_to(Path(outside), target_is_directory=True)
            playlist = root / "IPTV-Playlist.m3u"
            playlist.write_text("#EXTM3U\n", encoding="utf-8")
            manifest = root / "approved.json"
            manifest.write_text(json.dumps({"schema_version": 1, "source_playlist_sha256": {},
                                             "approvals": []}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "logos root must not be a symlink"):
                build_candidates(root, manifest, root / "reports" / "automation-v2" / "candidate")

    def test_output_outside_candidate_allowlist_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            playlist, manifest = self._fixture(root)
            with self.assertRaisesRegex(ValueError, "inside reports/automation-v2"):
                build_candidates(root, manifest, root / "reports" / "other")

    def test_symlinked_candidate_output_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            root = Path(tmp)
            playlist, manifest = self._fixture(root)
            reports = root / "reports"
            reports.mkdir()
            (reports / "automation-v2").symlink_to(Path(outside), target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "symlink"):
                build_candidates(root, manifest, reports / "automation-v2" / "candidate")

    def test_unsupported_asset_extension_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "logos").mkdir()
            asset = root / "logos" / "not-an-image.txt"
            asset.write_text("not image", encoding="utf-8")
            playlist = root / "IPTV-Playlist.m3u"
            playlist.write_text('#EXTM3U\n#EXTINF:-1 tvg-name="Exact Channel",Exact Channel\nhttps://stream.invalid/live\n', encoding="utf-8")
            manifest = root / "approved.json"
            manifest.write_text(json.dumps({
                "schema_version": 1,
                "source_playlist_sha256": {"IPTV-Playlist.m3u": hashlib.sha256(playlist.read_bytes()).hexdigest()},
                "approvals": [{"playlist": "IPTV-Playlist.m3u", "line": 2, "channel_name": "Exact Channel",
                               "expected_current_logo": "", "approved_local_logo": "logos/not-an-image.txt",
                               "asset_sha256": hashlib.sha256(asset.read_bytes()).hexdigest()}]
            }), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "supported image extension"):
                build_candidates(root, manifest, root / "reports" / "automation-v2" / "candidate")

    def test_duplicate_approvals_for_one_row_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            playlist, manifest = self._fixture(root)
            data = json.loads(manifest.read_text())
            data["approvals"].append(dict(data["approvals"][0]))
            manifest.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate logo approval"):
                build_candidates(root, manifest, root / "reports" / "automation-v2" / "candidate")


if __name__ == "__main__":
    unittest.main()
