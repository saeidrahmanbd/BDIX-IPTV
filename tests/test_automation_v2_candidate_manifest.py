import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"automation/core"))
from candidate_manifest import CandidateManifest, validate_manifest

class CandidateManifestTests(unittest.TestCase):
    def test_iptv_engine_cannot_touch_international_playlist(self):
        manifest=CandidateManifest("iptv","a"*40,("International-Playlist.m3u",),{"International-Playlist.m3u":"b"*64})
        self.assertTrue(any("outside engine allowlist" in x for x in validate_manifest(manifest)))

    def test_international_engine_can_only_declare_its_playlist_and_report(self):
        paths=("International-Playlist.m3u","reports/automation-v2/run-report.json")
        fingerprints={path:"c"*64 for path in paths}
        manifest=CandidateManifest("international","a"*40,paths,fingerprints)
        self.assertEqual(validate_manifest(manifest),[])

    def test_parent_traversal_and_absolute_paths_are_rejected(self):
        paths=("../IPTV-Playlist.m3u","/IPTV-Playlist.m3u")
        manifest=CandidateManifest("iptv","a"*40,paths,{p:"d"*64 for p in paths})
        self.assertTrue(validate_manifest(manifest))

    def test_invalid_hash_is_rejected(self):
        path="IPTV-Playlist.m3u"
        manifest=CandidateManifest("iptv","a"*40,(path,),{path:"not-a-hash"})
        self.assertTrue(validate_manifest(manifest))

    def test_epg_engine_cannot_touch_playlists(self):
        path="IPTV-Playlist.m3u"
        manifest=CandidateManifest("epg","a"*40,(path,),{path:"e"*64})
        self.assertTrue(validate_manifest(manifest))

if __name__=="__main__":
    unittest.main()
