import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.epg.candidate_engine import build_epg_candidate
from automation.engines.epg.alias_apply import ApprovedAlias

PLAYLIST='#EXTM3U\n#EXTINF:-1 tvg-id="target" group-title="Bangladesh",Target\nhttps://target.example/live\n'
BASE='<tv><channel id="source"><display-name>Target</display-name></channel><programme channel="source" start="20261113090000 +0600" stop="20261113100000 +0600"/></tv>'
AS_OF=datetime(2026,11,13,2,0,tzinfo=timezone.utc)

class EpgCandidateEngineTests(unittest.TestCase):
    def test_approved_alias_improves_active_channel_mapping(self):
        result=build_epg_candidate(PLAYLIST,BASE,approved_aliases=[ApprovedAlias("source","target","verified provider match",True)],as_of=AS_OF)
        self.assertTrue(result.decision.accepted)
        self.assertFalse(result.publish)
        self.assertIn('channel="target"',result.xml_text)

    def test_unapproved_alias_is_rejected(self):
        with self.assertRaisesRegex(ValueError,"explicit approval"):
            build_epg_candidate(PLAYLIST,BASE,approved_aliases=[ApprovedAlias("source","target","",False)],as_of=AS_OF)

    def test_candidate_schedule_regression_is_rejected(self):
        playlist='#EXTM3U\n#EXTINF:-1 tvg-id="a" group-title="Bangladesh",A\nhttps://a.example/a\n'
        baseline='<tv><channel id="a"/><programme channel="a" start="20261113090000 +0600" stop="20261113100000 +0600"/></tv>'
        candidate='<tv><channel id="a"/><programme channel="a" start="20261112090000 +0600" stop="20261112100000 +0600"/></tv>'
        result=build_epg_candidate(playlist,baseline,candidate,as_of=AS_OF)
        self.assertFalse(result.decision.accepted)
        self.assertIn("freshness regressed",result.decision.reason)

    def test_candidate_engine_never_publishes(self):
        result=build_epg_candidate(PLAYLIST,BASE,as_of=AS_OF)
        self.assertFalse(result.publish)
        self.assertIn("publication remains disabled",result.decision.reason)

if __name__=="__main__":
    unittest.main()
