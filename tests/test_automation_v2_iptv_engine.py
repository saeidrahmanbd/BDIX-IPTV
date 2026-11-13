import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.iptv.candidate_engine import DiscoveryCandidate, build_candidate

BASE = '#EXTM3U\n#EXTINF:-1 tvg-chno="1" group-title="Bangladesh",A\nhttps://a.example/a.m3u8\n'

class IptvCandidateEngineTests(unittest.TestCase):
    def test_discovery_appends_to_manual_queue(self):
        item=DiscoveryCandidate('#EXTINF:-1 group-title="New Channels",B','https://b.example/b.m3u8')
        result=build_candidate(BASE,[item])
        self.assertTrue(result.startswith(BASE))
        self.assertIn('group-title="New Channels"',result)

    def test_backup_discovery_uses_backup_queue(self):
        item=DiscoveryCandidate('#EXTINF:-1 group-title="New Backups",B','https://b.example/b.m3u8',True)
        self.assertIn('New Backups',build_candidate(BASE,[item]))

    def test_existing_url_is_not_duplicated(self):
        item=DiscoveryCandidate('#EXTINF:-1 group-title="New Channels",A','https://a.example/a.m3u8')
        self.assertEqual(build_candidate(BASE,[item]),BASE)

    def test_duplicate_new_url_is_added_once(self):
        item=DiscoveryCandidate('#EXTINF:-1 group-title="New Channels",B','https://b.example/b.m3u8')
        self.assertEqual(build_candidate(BASE,[item,item]).count('https://b.example/b.m3u8'),1)

    def test_wrong_queue_rejected(self):
        item=DiscoveryCandidate('#EXTINF:-1 group-title="Bangladesh",B','https://b.example/b.m3u8')
        with self.assertRaisesRegex(ValueError,"New Channels"):
            build_candidate(BASE,[item])

    def test_missing_m3u_header_rejected(self):
        item=DiscoveryCandidate('#EXTINF:-1 group-title="New Channels",B','https://b.example/b.m3u8')
        with self.assertRaisesRegex(ValueError,"#EXTM3U"):
            build_candidate("not a playlist", [item])

    def test_non_http_url_rejected(self):
        item=DiscoveryCandidate('#EXTINF:-1 group-title="New Channels",B','file:///tmp/a')
        with self.assertRaises(ValueError):
            build_candidate(BASE,[item])

if __name__=="__main__":
    unittest.main()
