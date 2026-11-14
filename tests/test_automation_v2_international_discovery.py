import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.international.discovery import build_international_discovery_batch, fetch_international_source

BASE='#EXTM3U\n#EXTINF:-1 tvg-id="existing.bd" tvg-name="Existing",Existing\nhttps://existing.example/live.m3u8\n'
FEED='#EXTM3U\n#EXTINF:-1 tvg-id="bdnews.bd" tvg-name="Bangladesh News" tvg-country="BD" group-title="News",Bangladesh News\nhttps://bdnews.example/live.m3u8\n#EXTINF:-1 tvg-id="insport.in" tvg-name="India Cricket Sports" tvg-country="IN" group-title="Sports",India Cricket Sports\nhttps://insport.example/live.m3u8\n#EXTINF:-1 tvg-id="foreignmovie.us" tvg-name="US Movie Channel" tvg-country="US" group-title="Movies",US Movie Channel\nhttps://movie.example/live.m3u8\n#EXTINF:-1 tvg-id="foreignnews.us" tvg-name="US News" tvg-country="US" group-title="News",US News\nhttps://news.example/live.m3u8\n#EXTINF:-1 tvg-id="unknown" tvg-name="Unknown Country Channel",Unknown Country Channel\nhttps://unknown.example/live.m3u8\n'

class InternationalDiscoveryAdapterTests(unittest.TestCase):
    def test_bd_and_india_are_not_excluded_by_genre(self):
        with tempfile.TemporaryDirectory() as temp:
            result=build_international_discovery_batch(BASE,FEED,temp)
        names=[item.extinf.split(",",1)[-1] for item in result.candidates]
        self.assertIn("Bangladesh News",names)
        self.assertIn("India Cricket Sports",names)

    def test_other_countries_remain_movie_music_only(self):
        with tempfile.TemporaryDirectory() as temp:
            result=build_international_discovery_batch(BASE,FEED,temp)
        names=[item.extinf.split(",",1)[-1] for item in result.candidates]
        self.assertIn("US Movie Channel",names)
        self.assertNotIn("US News",names)
        self.assertTrue(any("news is outside" in reason for reason,count in result.rejected_reasons))

    def test_unknown_country_is_warning_not_a_discovery_gate(self):
        with tempfile.TemporaryDirectory() as temp:
            result=build_international_discovery_batch(BASE,FEED,temp)
        names=[item.extinf.split(",",1)[-1] for item in result.candidates]
        self.assertIn("Unknown Country Channel",names)
        self.assertTrue(any("country could not be verified" in warning for warning in result.warnings))

    def test_conflicting_country_metadata_is_warning_only(self):
        feed='#EXTM3U\n#EXTINF:-1 tvg-id="conflict.in" tvg-name="India News" tvg-country="US" group-title="News",India News\nhttps://conflict.example/live.m3u8\n'
        with tempfile.TemporaryDirectory() as temp:
            result=build_international_discovery_batch(BASE,feed,temp)
        self.assertEqual(len(result.candidates),1)
        self.assertTrue(any("conflicts with channel ID" in warning for warning in result.warnings))

    def test_logo_path_must_be_a_real_asset_inside_logos_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/"logos").mkdir()
            (root/"elsewhere").mkdir()
            (root/"elsewhere"/"inside-repo.png").write_bytes(b"not a logo")
            (root/"logos"/"valid.png").write_bytes(b"valid")
            (root/"logos"/"linked.png").symlink_to(root/"elsewhere"/"inside-repo.png")
            feed='#EXTM3U\n'
            feed += '#EXTINF:-1 tvg-id="valid.in" tvg-name="Valid" tvg-logo="logos/valid.png",Valid\nhttps://valid.example/live.m3u8\n'
            feed += '#EXTINF:-1 tvg-id="linked.in" tvg-name="Linked" tvg-logo="logos/linked.png",Linked\nhttps://linked.example/live.m3u8\n'
            feed += '#EXTINF:-1 tvg-id="traversal.in" tvg-name="Traversal" tvg-logo="logos/../elsewhere/inside-repo.png",Traversal\nhttps://traversal.example/live.m3u8\n'
            result=build_international_discovery_batch(BASE,feed,root)
        rows={item.extinf.split(",",1)[-1]:item.extinf for item in result.candidates}
        self.assertIn("Valid",rows)
        self.assertIn("Linked",rows)
        self.assertIn("Traversal",rows)
        self.assertIn('tvg-logo="logos/valid.png"',rows["Valid"])
        self.assertNotIn("tvg-logo=",rows["Linked"])
        self.assertNotIn("tvg-logo=",rows["Traversal"])

    def test_missing_or_external_logo_does_not_block_discovery(self):
        with tempfile.TemporaryDirectory() as temp:
            result=build_international_discovery_batch(BASE,FEED,temp)
        row=next(item for item in result.candidates if "Bangladesh News" in item.extinf)
        self.assertNotIn("tvg-logo=",row.extinf)

    def test_duplicate_identity_becomes_new_backup(self):
        feed='#EXTM3U\n#EXTINF:-1 tvg-id="existing.bd" tvg-name="Existing",Existing\nhttps://backup.example/live.m3u8\n'
        with tempfile.TemporaryDirectory() as temp:
            result=build_international_discovery_batch(BASE,feed,temp)
        self.assertEqual(len(result.candidates),1)
        self.assertTrue(result.candidates[0].backup)
        self.assertIn('group-title="New Backups"',result.candidates[0].extinf)

    @patch("automation.engines.international.discovery.urlopen")
    def test_fetch_only_approved_international_source(self,mock):
        response=MagicMock()
        response.__enter__.return_value.read.return_value=b"#EXTM3U\n"
        mock.return_value=response
        from automation.engines.international.discovery import _policy_module
        self.assertEqual(fetch_international_source(),"#EXTM3U\n")
        with self.assertRaisesRegex(ValueError,"not approved"):
            fetch_international_source("https://example.com/other.m3u")

if __name__=="__main__":
    unittest.main()
