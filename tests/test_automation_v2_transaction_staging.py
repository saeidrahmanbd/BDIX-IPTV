import sys
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.core.candidate_manifest import CandidateManifest
from automation.core.transaction_gate import ArtifactEvidence
from automation.core.transaction_staging import stage_transaction_bundle

BASE="a"*40

def evidence(path,before,after):
    return ArtifactEvidence(path,hashlib.sha256(before.encode()).hexdigest(),
        hashlib.sha256(after.encode()).hexdigest(),hashlib.sha256(before.encode()).hexdigest(),
        hashlib.sha256(after.encode()).hexdigest(),True)

class TransactionStagingTests(unittest.TestCase):
    def setUp(self):
        self.before={"IPTV-Playlist.m3u":"old playlist","epg/epg.xml":"old guide"}
        self.after={"IPTV-Playlist.m3u":"new candidate playlist","epg/epg.xml":"new candidate guide"}
        self.manifests=[
            CandidateManifest("iptv",BASE,("IPTV-Playlist.m3u",),{"IPTV-Playlist.m3u":hashlib.sha256(self.after["IPTV-Playlist.m3u"].encode()).hexdigest()}),
            CandidateManifest("epg",BASE,("epg/epg.xml",),{"epg/epg.xml":hashlib.sha256(self.after["epg/epg.xml"].encode()).hexdigest()}),
        ]
        self.artifacts=[evidence(path,self.before[path],self.after[path]) for path in self.before]

    def test_stages_multiple_engines_as_one_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            path=stage_transaction_bundle(temp,"tx-001",self.manifests,self.artifacts,self.after,BASE)
            self.assertEqual((path/"IPTV-Playlist.m3u").read_text(),"new candidate playlist")
            self.assertEqual((path/"epg"/"epg.xml").read_text(),"new candidate guide")
            metadata=json.loads((path/"transaction-bundle.json").read_text())
            self.assertEqual(metadata["engines"],["epg","iptv"])
            self.assertFalse(metadata["publish"])

    def test_changed_content_fingerprint_blocks_staging(self):
        with tempfile.TemporaryDirectory() as temp:
            bad=dict(self.after);bad["epg/epg.xml"]="tampered"
            with self.assertRaisesRegex(ValueError,"fingerprint mismatch"):
                stage_transaction_bundle(temp,"tx-001",self.manifests,self.artifacts,bad,BASE)
            self.assertFalse((Path(temp)/"reports/automation-v2/candidates/transactions/tx-001").exists())

    def test_failed_validator_blocks_staging(self):
        with tempfile.TemporaryDirectory() as temp:
            bad=[self.artifacts[0],ArtifactEvidence(**{**self.artifacts[1].__dict__,"validator_passed":False})]
            with self.assertRaisesRegex(ValueError,"passed all gates"):
                stage_transaction_bundle(temp,"tx-001",self.manifests,bad,self.after,BASE)

    def test_overlapping_engine_paths_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            overlapping=self.manifests+[CandidateManifest("international",BASE,("IPTV-Playlist.m3u",),{"IPTV-Playlist.m3u":hashlib.sha256(self.after["IPTV-Playlist.m3u"].encode()).hexdigest()})]
            with self.assertRaisesRegex(ValueError,"overlapping"):
                stage_transaction_bundle(temp,"tx-001",overlapping,self.artifacts,self.after,BASE)

    def test_symlinked_transaction_parent_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp, tempfile.TemporaryDirectory() as outside:
            root=Path(temp)
            (root/"reports").symlink_to(outside,target_is_directory=True)
            with self.assertRaisesRegex(ValueError,"symlink"):
                stage_transaction_bundle(root,"tx-001",self.manifests,self.artifacts,self.after,BASE)

    def test_candidate_path_set_must_match(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError,"paths"):
                stage_transaction_bundle(temp,"tx-001",self.manifests,self.artifacts,{"IPTV-Playlist.m3u":self.after["IPTV-Playlist.m3u"]},BASE)

    def test_atomic_publish_failure_cleans_partial_staging_directory(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as temp:
            with patch("automation.core.transaction_staging.os.replace", side_effect=OSError("injected rename failure")):
                with self.assertRaisesRegex(OSError, "injected rename failure"):
                    stage_transaction_bundle(temp,"tx-fail",self.manifests,self.artifacts,self.after,BASE)
            parent=Path(temp)/"reports/automation-v2/candidates/transactions"
            self.assertFalse((parent/"tx-fail").exists())
            self.assertEqual(list(parent.glob(".staging-*")), [])


if __name__=="__main__":
    unittest.main()
