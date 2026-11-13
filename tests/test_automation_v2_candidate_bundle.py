import sys
import unittest
import json
import tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.core.candidate_bundle import build_candidate_bundle, write_candidate_bundle

class CandidateBundleTests(unittest.TestCase):
    def test_valid_bundle_is_ready_for_review_but_never_published(self):
        result=build_candidate_bundle("iptv","a"*40,{"IPTV-Playlist.m3u":"before"},{"IPTV-Playlist.m3u":"after"},{"IPTV-Playlist.m3u":True})
        self.assertTrue(result.decision.ready_for_owner_review)
        self.assertFalse(result.publish)
        self.assertFalse(result.decision.publish)

    def test_failed_validator_blocks_bundle(self):
        result=build_candidate_bundle("iptv","a"*40,{"IPTV-Playlist.m3u":"before"},{"IPTV-Playlist.m3u":"after"},{"IPTV-Playlist.m3u":False})
        self.assertFalse(result.decision.ready_for_owner_review)
        self.assertFalse(result.publish)

    def test_path_set_mismatch_rejected(self):
        with self.assertRaisesRegex(ValueError,"path sets"):
            build_candidate_bundle("iptv","a"*40,{"IPTV-Playlist.m3u":"before"},{"International-Playlist.m3u":"after"},{"International-Playlist.m3u":True})

    def test_missing_validator_evidence_rejected(self):
        with self.assertRaisesRegex(ValueError,"validator result"):
            build_candidate_bundle("iptv","a"*40,{"IPTV-Playlist.m3u":"before"},{"IPTV-Playlist.m3u":"after"},{})

    def test_candidate_bundle_cannot_be_empty(self):
        with self.assertRaisesRegex(ValueError,"cannot be empty"):
            build_candidate_bundle("iptv","a"*40,{}, {}, {})

    def test_ready_bundle_written_as_one_candidate_directory(self):
        contents={"IPTV-Playlist.m3u":"#EXTM3U\n"}
        bundle=build_candidate_bundle("iptv","a"*40,{"IPTV-Playlist.m3u":"#EXTM3U\n"},contents,{"IPTV-Playlist.m3u":True})
        with tempfile.TemporaryDirectory() as temp:
            path=write_candidate_bundle(temp,"run-123",bundle,contents)
            self.assertEqual((path/"IPTV-Playlist.m3u").read_text(encoding="utf-8"),"#EXTM3U\n")
            self.assertFalse(json.loads((path/"candidate-bundle.json").read_text())["publish"])

    def test_tampered_candidate_content_is_rejected(self):
        contents={"IPTV-Playlist.m3u":"after"}
        bundle=build_candidate_bundle("iptv","a"*40,{"IPTV-Playlist.m3u":"before"},contents,{"IPTV-Playlist.m3u":True})
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError,"fingerprint changed"):
                write_candidate_bundle(temp,"run-123",bundle,{"IPTV-Playlist.m3u":"tampered"})

    def test_symlinked_candidate_directory_is_rejected(self):
        from pathlib import Path
        contents={"IPTV-Playlist.m3u":"after"}
        bundle=build_candidate_bundle("iptv","a"*40,{"IPTV-Playlist.m3u":"before"},contents,{"IPTV-Playlist.m3u":True})
        with tempfile.TemporaryDirectory() as temp, tempfile.TemporaryDirectory() as outside:
            root=Path(temp)
            parent=root/"reports"/"automation-v2"
            parent.mkdir(parents=True)
            (parent/"candidates").symlink_to(outside,target_is_directory=True)
            with self.assertRaisesRegex(ValueError,"escapes"):
                write_candidate_bundle(root,"run-123",bundle,contents)

    def test_symlinked_candidate_parent_is_rejected(self):
        import tempfile
        from pathlib import Path
        from automation.core.candidate_bundle import write_candidate_bundle
        with tempfile.TemporaryDirectory() as temp, tempfile.TemporaryDirectory() as outside:
            root=Path(temp)
            (root/"reports").symlink_to(outside,target_is_directory=True)
            contents={"IPTV-Playlist.m3u":"after"}
            bundle=build_candidate_bundle("iptv","a"*40,{"IPTV-Playlist.m3u":"before"},contents,{"IPTV-Playlist.m3u":True})
            with self.assertRaisesRegex(ValueError,"symlink"):
                write_candidate_bundle(root,"run-123",bundle,contents)

    def test_blocked_bundle_is_not_written(self):
        contents={"IPTV-Playlist.m3u":"after"}
        bundle=build_candidate_bundle("iptv","a"*40,{"IPTV-Playlist.m3u":"before"},contents,{"IPTV-Playlist.m3u":False})
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError,"passed all gates"):
                write_candidate_bundle(temp,"run-123",bundle,contents)

if __name__=="__main__":
    unittest.main()
