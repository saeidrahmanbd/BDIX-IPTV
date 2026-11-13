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

    def test_combined_candidate_preserves_existing_rows_and_appends_discovery(self):
        import tempfile
        from pathlib import Path
        from automation.engines.iptv.metadata_repair import MetadataPatch
        from automation.engines.iptv.candidate_engine import build_iptv_candidate
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/"logos").mkdir()
            (root/"logos"/"new.png").write_bytes(b"logo")
            patch=MetadataPatch(0,"official channel identity",True,tvg_name="A Official",tvg_logo="logos/new.png",display_name="A Official")
            discovery=DiscoveryCandidate('#EXTINF:-1 group-title="New Channels",B','https://b.example/b.m3u8')
            result=build_iptv_candidate(BASE,[discovery],[patch],root)
            self.assertFalse(result.publish)
            self.assertEqual((result.baseline_rows,result.candidate_rows),(1,2))
            self.assertIn('tvg-name="A Official"',result.text)
            self.assertIn('group-title="New Channels"',result.text)

    def test_combined_candidate_rejects_unapproved_metadata_patch(self):
        import tempfile
        from automation.engines.iptv.metadata_repair import MetadataPatch
        from automation.engines.iptv.candidate_engine import build_iptv_candidate
        with tempfile.TemporaryDirectory() as temp:
            patch=MetadataPatch(0,"",False,tvg_name="A changed")
            with self.assertRaisesRegex(ValueError,"approval and evidence"):
                build_iptv_candidate(BASE,[],[patch],temp)

    def test_non_http_url_rejected(self):
        item=DiscoveryCandidate('#EXTINF:-1 group-title="New Channels",B','file:///tmp/a')
        with self.assertRaises(ValueError):
            build_candidate(BASE,[item])

if __name__=="__main__":
    unittest.main()
