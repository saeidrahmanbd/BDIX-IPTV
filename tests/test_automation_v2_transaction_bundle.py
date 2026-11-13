import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.core.candidate_manifest import CandidateManifest
from automation.core.transaction_gate import ArtifactEvidence
from automation.core.transaction_bundle import evaluate_bundle

class TransactionBundleTests(unittest.TestCase):
    def setUp(self):
        self.baseline="a"*40
        self.iptv=CandidateManifest("iptv",self.baseline,("IPTV-Playlist.m3u",),{"IPTV-Playlist.m3u":"b"*64})
        self.epg=CandidateManifest("epg",self.baseline,("epg/epg.xml",),{"epg/epg.xml":"c"*64})
        self.evidence=[
            ArtifactEvidence("IPTV-Playlist.m3u","d"*64,"b"*64,"d"*64,"b"*64,True),
            ArtifactEvidence("epg/epg.xml","e"*64,"c"*64,"e"*64,"c"*64,True),
        ]

    def test_multi_engine_bundle_ready_but_not_published(self):
        result=evaluate_bundle([self.iptv,self.epg],self.evidence,self.baseline)
        self.assertTrue(result.ready_for_owner_review)
        self.assertFalse(result.publish)

    def test_global_transaction_lock_blocks_bundle(self):
        result=evaluate_bundle([self.iptv],self.evidence[:1],self.baseline,"tx-active")
        self.assertFalse(result.ready_for_owner_review)
        self.assertTrue(any("global lock" in e for e in result.errors))

    def test_duplicate_engine_manifests_rejected(self):
        result=evaluate_bundle([self.iptv,self.iptv],self.evidence[:1],self.baseline)
        self.assertTrue(any("duplicate engine" in e for e in result.errors))

    def test_overlapping_shared_report_path_rejected(self):
        a=CandidateManifest("iptv",self.baseline,("IPTV-Playlist.m3u","reports/automation-v2/run-report.json"),{"IPTV-Playlist.m3u":"b"*64,"reports/automation-v2/run-report.json":"f"*64})
        b=CandidateManifest("epg",self.baseline,("epg/epg.xml","reports/automation-v2/run-report.json"),{"epg/epg.xml":"c"*64,"reports/automation-v2/run-report.json":"1"*64})
        result=evaluate_bundle([a,b],self.evidence,self.baseline)
        self.assertTrue(any("overlapping output paths" in e for e in result.errors))

    def test_mixed_baseline_commits_rejected(self):
        other=CandidateManifest("epg","f"*40,("epg/epg.xml",),{"epg/epg.xml":"c"*64})
        result=evaluate_bundle([self.iptv,other],self.evidence,self.baseline)
        self.assertTrue(any("same approved baseline" in e for e in result.errors))

    def test_missing_artifact_evidence_rejected(self):
        result=evaluate_bundle([self.iptv,self.epg],self.evidence[:1],self.baseline)
        self.assertTrue(any("evidence does not exactly match" in e for e in result.errors))

if __name__=="__main__":
    unittest.main()
