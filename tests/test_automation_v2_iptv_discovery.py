import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.iptv.discovery import build_discovery_batch, fetch_source_feed

BASE='#EXTM3U\n#EXTINF:-1 tvg-id="existing.in" tvg-name="Existing",Existing\nhttps://existing.example/live.m3u8\n'
BD_FEED='#EXTM3U\n#EXTINF:-1 tvg-id="newbd.bd" tvg-name="New BD" tvg-country="IN" group-title="Sports",New BD\nhttps://newbd.example/live.m3u8\n'
IN_FEED='#EXTM3U\n#EXTINF:-1 tvg-id="cricket.in" tvg-name="Cricket Sports" group-title="Sports",Cricket Sports\nhttps://cricket.example/live.m3u8\n#EXTINF:-1 tvg-id="news.in" tvg-name="India News",India News\nhttps://news.example/live.m3u8\n'

class IptvDiscoveryAdapterTests(unittest.TestCase):
    def test_unknown_or_conflicting_country_and_missing_logo_do_not_block_discovery(self):
        with tempfile.TemporaryDirectory() as temp:
            result=build_discovery_batch(BASE,{"Bangladesh":BD_FEED},temp)
        self.assertEqual(len(result.candidates),1)
        self.assertIn('group-title="New Channels"',result.candidates[0].extinf)
        self.assertNotIn("tvg-logo=",result.candidates[0].extinf)
        self.assertTrue(any("country conflicts" in warning for warning in result.warnings))
        self.assertTrue(any("no authentic local logo" in warning for warning in result.warnings))

    def test_indian_cricket_and_sports_allowed_but_news_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            result=build_discovery_batch(BASE,{"India":IN_FEED},temp)
        self.assertEqual(len(result.candidates),1)
        self.assertIn("Cricket Sports",result.candidates[0].extinf)
        self.assertTrue(any("Indian news channel is prohibited" in reason for reason,count in result.rejected_reasons))

    def test_duplicate_channel_identity_becomes_new_backup(self):
        feed='#EXTM3U\n#EXTINF:-1 tvg-id="existing.in" tvg-name="Existing",Existing\nhttps://backup.example/live.m3u8\n'
        with tempfile.TemporaryDirectory() as temp:
            result=build_discovery_batch(BASE,{"India":feed},temp)
        self.assertEqual(len(result.candidates),1)
        self.assertTrue(result.candidates[0].backup)
        self.assertIn('group-title="New Backups"',result.candidates[0].extinf)

    def test_external_logo_is_never_retained(self):
        feed='#EXTM3U\n#EXTINF:-1 tvg-id="new.in" tvg-name="New" tvg-logo="https://cdn.example/logo.png",New\nhttps://new.example/live.m3u8\n'
        with tempfile.TemporaryDirectory() as temp:
            result=build_discovery_batch(BASE,{"India":feed},temp)
        self.assertEqual(len(result.candidates),1)
        self.assertNotIn("https://cdn.example/logo.png",result.candidates[0].extinf)

    def test_unsupported_source_country_is_warning_not_a_candidate(self):
        with tempfile.TemporaryDirectory() as temp:
            result=build_discovery_batch(BASE,{"Nepal":IN_FEED},temp)
        self.assertEqual(result.candidates,())
        self.assertTrue(any("Unrecognized source country" in warning for warning in result.warnings))

    @patch("automation.engines.iptv.discovery.urlopen")
    def test_fetch_source_uses_approved_source_registry(self,mock):
        response=MagicMock()
        response.__enter__.return_value.read.return_value=b"#EXTM3U\n"
        mock.return_value=response
        from automation.engines.iptv.discovery import _legacy_policy
        source=_legacy_policy().SOURCES[0][1]
        self.assertEqual(fetch_source_feed(source),"#EXTM3U\n")
        with self.assertRaisesRegex(ValueError,"approved source registry"):
            fetch_source_feed("https://example.com/evil.m3u")

if __name__=="__main__":
    unittest.main()
