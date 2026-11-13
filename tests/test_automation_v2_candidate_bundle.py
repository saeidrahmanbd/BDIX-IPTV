import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.core.candidate_bundle import build_candidate_bundle

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

if __name__=="__main__":
    unittest.main()
