import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.core.candidate_manifest import CandidateManifest
from automation.core.transaction_gate import ArtifactEvidence, evaluate_transaction

class TransactionGateTests(unittest.TestCase):
    def setUp(self):
        self.path="IPTV-Playlist.m3u"
        self.fingerprint="b"*64
        self.manifest=CandidateManifest("iptv","a"*40,(self.path,),{self.path:self.fingerprint})
        self.evidence=ArtifactEvidence(self.path,"c"*64,self.fingerprint,"c"*64,self.fingerprint,True)

    def test_all_gates_pass_but_publication_stays_disabled(self):
        result=evaluate_transaction(self.manifest,[self.evidence],"a"*40)
        self.assertTrue(result.ready_for_owner_review)
        self.assertFalse(result.publish)

    def test_stale_baseline_rejected(self):
        stale=ArtifactEvidence(self.path,"c"*64,self.fingerprint,"d"*64,self.fingerprint,True)
        result=evaluate_transaction(self.manifest,[stale],"a"*40)
        self.assertFalse(result.ready_for_owner_review)
        self.assertTrue(any("stale baseline" in e for e in result.errors))

    def test_candidate_tampering_rejected(self):
        changed=ArtifactEvidence(self.path,"c"*64,self.fingerprint,"c"*64,"e"*64,True)
        result=evaluate_transaction(self.manifest,[changed],"a"*40)
        self.assertTrue(any("fingerprint mismatch" in e for e in result.errors))

    def test_failed_validator_rejected(self):
        failed=ArtifactEvidence(self.path,"c"*64,self.fingerprint,"c"*64,self.fingerprint,False)
        self.assertFalse(evaluate_transaction(self.manifest,[failed],"a"*40).ready_for_owner_review)

    def test_wrong_baseline_commit_rejected(self):
        result=evaluate_transaction(self.manifest,[self.evidence],"f"*40)
        self.assertTrue(any("baseline commit" in e for e in result.errors))

if __name__=="__main__":
    unittest.main()
