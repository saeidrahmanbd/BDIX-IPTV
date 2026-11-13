import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.epg.alias_apply import ApprovedAlias, apply_approved_aliases
from automation.engines.epg.coverage import calculate_coverage

PLAYLIST='#EXTM3U\n#EXTINF:-1 tvg-id="target" group-title="Bangladesh",Target\nhttps://target.example/live\n'
GUIDE='<tv><channel id="source"><display-name>Target</display-name></channel><programme channel="source" start="20261113090000 +0600" stop="20261113100000 +0600"><title>News</title></programme></tv>'

class ApprovedEpgAliasTests(unittest.TestCase):
    def test_approved_alias_clones_channel_and_schedules(self):
        candidate=apply_approved_aliases(PLAYLIST,GUIDE,[ApprovedAlias("source","target","Exact provider and schedule identity",True)])
        root=ET.fromstring(candidate)
        self.assertIsNotNone(root.find('channel[@id="target"]'))
        self.assertIsNotNone(root.find('programme[@channel="target"]'))
        tags=[node.tag for node in root]
        self.assertLess(tags.index("channel"),tags.index("programme"))
        self.assertEqual(calculate_coverage(PLAYLIST,candidate).mapped_channel_ids,1)

    def test_unapproved_alias_rejected(self):
        with self.assertRaisesRegex(ValueError,"explicit approval"):
            apply_approved_aliases(PLAYLIST,GUIDE,[ApprovedAlias("source","target","",False)])

    def test_target_must_be_active_in_playlist(self):
        with self.assertRaisesRegex(ValueError,"not active"):
            apply_approved_aliases(PLAYLIST,GUIDE,[ApprovedAlias("source","other","evidence",True)])

    def test_existing_target_rejected(self):
        guide='<tv><channel id="source"/><channel id="target"/><programme channel="source" start="20261113090000" stop="20261113100000"/></tv>'
        with self.assertRaisesRegex(ValueError,"already exists"):
            apply_approved_aliases(PLAYLIST,guide,[ApprovedAlias("source","target","evidence",True)])

    def test_alias_source_requires_schedule(self):
        guide='<tv><channel id="source"/></tv>'
        with self.assertRaisesRegex(ValueError,"no programmes"):
            apply_approved_aliases(PLAYLIST,guide,[ApprovedAlias("source","target","evidence",True)])

if __name__=="__main__":
    unittest.main()
