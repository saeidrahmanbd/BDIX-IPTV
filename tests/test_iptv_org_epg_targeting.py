import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from fetch_iptv_org_epg import active_playlist_ids, target_channel_ids, build_target_channels_xml


class TargetedIptvOrgEpgTests(unittest.TestCase):
    def test_only_active_ids_from_three_playlists_are_targets(self):
        main = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="BBCNews.uk" tvg-name="BBC News" group-title="International",BBC News\n'
            'https://example.test/bbc.m3u8\n'
            '#EXTINF:-1 tvg-id="Private.Test" tvg-name="Test" group-title="Test",Test\n'
            'https://example.test/test.m3u8\n'
            '#EXTINF:-1 tvg-id="BackupOnly.uk" tvg-name="Backup Only" group-title="Backup",Backup Only\n'
            'https://example.test/backup.m3u8\n'
        )
        bdix = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="ZeeBangla.in@SD" tvg-name="Zee Bangla" group-title="Bangla",Zee Bangla\n'
            'https://example.test/zee.m3u8\n'
        )
        intl = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="SomeIntl.us" tvg-name="Some Intl" group-title="International",Some Intl\n'
            'https://example.test/intl.m3u8\n'
        )
        active = active_playlist_ids([main, bdix, intl])
        self.assertEqual(active, {"BBCNews.uk", "ZeeBangla.in@SD", "SomeIntl.us"})

    def test_mapping_source_ids_are_included_only_for_active_targets(self):
        main = (
            '#EXTINF:-1 tvg-id="BBCNews.uk" tvg-name="BBC News" group-title="International",BBC News\n'
            'https://example.test/bbc.m3u8\n'
        )
        mapping = (
            'group,channel,tvg_id,epg_id,source,status,note\n'
            'International,BBC News,BBCNews.uk,bbc.news.xmltv|bbc.alt,source,MAPPED,\n'
            'Backup,Backup Only,BackupOnly.uk,backup.xmltv,source,MAPPED,\n'
        )
        self.assertEqual(
            target_channel_ids([main], mapping),
            {"BBCNews.uk", "bbc.news.xmltv", "bbc.alt"},
        )

    def test_catalogue_is_filtered_by_exact_xmltv_id_and_preserves_site_fields(self):
        catalogue = '''<?xml version="1.0"?>
<channels>
  <channel site="dishtv.in" site_id="11" lang="en" xmltv_id="BBCNews.uk">BBC News</channel>
  <channel site="dishtv.in" site_id="12" lang="en" xmltv_id="Other.uk">Other</channel>
  <channel site="dishtv.in" site_id="13" lang="hi" xmltv_id="bbc.news.xmltv">BBC News Hindi provider</channel>
</channels>'''
        generated = build_target_channels_xml([catalogue], {"BBCNews.uk", "bbc.news.xmltv"})
        root = ET.fromstring(generated)
        self.assertEqual([c.attrib["xmltv_id"] for c in root.findall("channel")], ["BBCNews.uk", "bbc.news.xmltv"])
        self.assertEqual(root.find("channel").attrib["site_id"], "11")
        self.assertEqual(root.find("channel").attrib["site"], "dishtv.in")

    def test_empty_target_match_returns_valid_empty_channels_catalogue(self):
        generated = build_target_channels_xml(
            ['<channels><channel site="x" site_id="1" lang="en" xmltv_id="Other.uk">Other</channel></channels>'],
            {"Missing.uk"},
        )
        root = ET.fromstring(generated)
        self.assertEqual(root.tag, "channels")
        self.assertEqual(root.findall("channel"), [])


if __name__ == "__main__":
    unittest.main()
