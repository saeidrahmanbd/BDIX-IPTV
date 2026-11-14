import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import fetch_iptv_org_epg as fetcher
from fetch_iptv_org_epg import active_playlist_ids, target_channel_ids, build_target_channels_xml, grab_command


class TargetedIptvOrgEpgTests(unittest.TestCase):
    def test_upstream_checkout_uses_an_immutable_commit(self):
        self.assertRegex(fetcher.UPSTREAM_COMMIT, r"^[0-9a-f]{40}$")
        with patch.object(fetcher, "run") as run:
            fetcher.checkout_upstream()
        calls = [call.args for call in run.call_args_list]
        self.assertIn(("git", "-C", str(fetcher.WORK), "fetch", "--depth", "1", "origin", fetcher.UPSTREAM_COMMIT), calls)
        self.assertIn(("git", "-C", str(fetcher.WORK), "checkout", "--detach", "FETCH_HEAD"), calls)
        self.assertFalse(any("clone" in args for args in calls))

    def test_grab_command_does_not_filter_out_bengali_or_other_languages(self):
        args = grab_command()
        self.assertNotIn("--lang=en", args)
        self.assertFalse(any(arg.startswith("--lang=") for arg in args))
        self.assertIn("--days=2", args)
        self.assertIn("--delay=100", args)
        self.assertTrue(any(arg.startswith("--channels=") for arg in args))

    def test_only_active_ids_from_three_core_playlists_are_targets(self):
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
            'International,BBC News,BBCNews.uk,bbc.news.xmltv|bbc.alt,source,MAPPED_ID_ONLY,\n'
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

    def test_explicit_aliases_are_targeted_only_for_active_playlist_ids(self):
        playlist = (
            '#EXTINF:-1 tvg-id="Star.Jalsha.in" tvg-name="Star Jalsha" group-title="Indian Bangla",Star Jalsha\n'
            'https://example.test/star.m3u8\n'
            '#EXTINF:-1 tvg-id="BackupOnly.in" tvg-name="Backup Only" group-title="Backups",Backup Only\n'
            'https://example.test/backup.m3u8\n'
        )
        explicit = {
            "Star.Jalsha.in": ["StarJalsha.in@SD"],
            "BackupOnly.in": ["BackupOnly.in@SD"],
        }
        self.assertEqual(
            target_channel_ids([playlist], "", explicit),
            {"Star.Jalsha.in", "StarJalsha.in@SD"},
        )

    def test_sky_catalogue_rows_require_a_normalized_name_match(self):
        catalogue = '''<channels>
  <channel site="sky.com" site_id="GB#1" lang="en" xmltv_id="SanskarTV.in@SD">Sanskar</channel>
  <channel site="sky.com" site_id="GB#2" lang="en" xmltv_id="MasalaTV.pk@SD">HUM News</channel>
  <channel site="sky.com" site_id="GB#3" lang="en" xmltv_id="MasalaTV.pk@SD">Masala TV</channel>
</channels>'''
        generated = build_target_channels_xml(
            [catalogue],
            {"SanskarTV.in@SD", "MasalaTV.pk@SD"},
            {
                "SanskarTV.in@SD": {"sanskar"},
                "MasalaTV.pk@SD": {"masala"},
            },
        )
        root = ET.fromstring(generated)
        pairs = [(channel.attrib["site_id"], channel.attrib["xmltv_id"]) for channel in root.findall("channel")]
        self.assertEqual(
            pairs,
            [("GB#1", "SanskarTV.in@SD"), ("GB#3", "MasalaTV.pk@SD")],
        )

    def test_curated_sky_site_ids_allow_short_diaspora_labels_only_for_locked_channels(self):
        catalogue = '''<channels>
  <channel site="sky.com" site_id="GB#6753" lang="en" xmltv_id="ATNBanglaUK.uk@SD">ATN</channel>
  <channel site="sky.com" site_id="GB#9999" lang="en" xmltv_id="ATNBanglaUK.uk@SD">ATN</channel>
  <channel site="sky.com" site_id="GB#4540" lang="en" xmltv_id="NTVEurope.bd@SD">NTV</channel>
</channels>'''
        explicit = {
            "ATNBanglaUK.uk": ["6753", "ATNBanglaUK.uk@SD"],
            "NTVEurope.bd": ["4540", "NTVEurope.bd@SD"],
        }
        generated = build_target_channels_xml(
            [catalogue],
            {"ATNBanglaUK.uk@SD", "NTVEurope.bd@SD"},
            {
                "ATNBanglaUK.uk": {"atnbanglauk"},
                "NTVEurope.bd": {"ntveurope"},
            },
            explicit_mappings=explicit,
        )
        pairs = [(c.attrib["site_id"], c.attrib["xmltv_id"]) for c in ET.fromstring(generated).findall("channel")]
        self.assertEqual(
            pairs,
            [("GB#6753", "ATNBanglaUK.uk@SD"), ("GB#4540", "NTVEurope.bd@SD")],
        )

    def test_tv24_blank_id_uses_only_curated_site_id_and_exact_name(self):
        catalogue = '''<channels>
  <channel site="tv24.co.uk" site_id="iqra-bangla" lang="en" xmltv_id="">IQRA BANGLA</channel>
  <channel site="tv24.co.uk" site_id="ntv" lang="en" xmltv_id="">NTV</channel>
</channels>'''
        generated = build_target_channels_xml(
            [catalogue],
            {"IqraBangla.uk"},
            {"IqraBangla.uk": {"iqrabangla"}},
        )
        rows = ET.fromstring(generated).findall("channel")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].attrib["site_id"], "iqra-bangla")
        self.assertEqual(rows[0].attrib["xmltv_id"], "IqraBangla.uk")

    def test_strict_epg_locks_replace_the_playlist_id(self):
        playlist = (
            '#EXTINF:-1 tvg-id="ColorsCineplex.in@SD" tvg-name="Colors Cineplex" group-title="Indian Movies",Colors Cineplex\n'
            'https://example.test/colors.m3u8\n'
        )
        self.assertEqual(
            target_channel_ids(
                [playlist],
                "",
                {"ColorsCineplex.in@SD": ["543298"]},
                {"ColorsCineplex.in@SD": ["543298"]},
            ),
            {"543298"},
        )

    def test_currently_covered_channels_are_not_re_fetched(self):
        playlist = (
            '#EXTINF:-1 tvg-id="Covered.in" tvg-name="Covered" group-title="Indian Entertainment",Covered\n'
            'https://example.test/covered.m3u8\n'
            '#EXTINF:-1 tvg-id="Missing.in" tvg-name="Missing" group-title="Indian Entertainment",Missing\n'
            'https://example.test/missing.m3u8\n'
        )
        mapping = (
            'group,channel,tvg_id,epg_id,source,status,note\n'
            'Indian Entertainment,Covered,Covered.in,Covered.in@SD,feed,MAPPED,\n'
            'Indian Entertainment,Missing,Missing.in,legacy.source.id,feed,MAPPED_ID_ONLY,\n'
        )
        explicit = {"Covered.in": ["Covered.in@HD"], "Missing.in": ["Missing.in@SD"]}
        self.assertEqual(
            target_channel_ids([playlist], mapping, explicit),
            {"Missing.in", "legacy.source.id", "Missing.in@SD"},
        )


    def test_rate_limited_polish_site_is_skipped_while_other_regions_remain(self):
        self.assertNotIn("programtv.onet.pl", fetcher.SITES)
        self.assertTrue({"m.tv.sms.cz", "mujtvprogram.cz", "tv.mail.ru", "epg.iptvx.one"}.issubset(set(fetcher.SITES)))

    def test_selected_upstream_sites_cover_regional_and_fast_catalogues(self):
        self.assertTrue({
            "jiotv.com", "distro.tv", "plex.tv", "pluto.tv", "xumo.tv",
            "tvpassport.com", "tvguide.com", "m.tv.sms.cz", "mujtvprogram.cz",
            "tv.mail.ru", "tv24.co.uk", "guidatv.sky.it", "superguidatv.it",
            "epg.iptvx.one",
        }.issubset(set(fetcher.SITES)))

    def test_jio_catalogue_blank_xmltv_id_maps_only_to_unique_exact_target_name(self):
        catalogue = '''<channels>
  <channel site="jiotv.com" site_id="154" lang="en" xmltv_id="">Sony SAB HD</channel>
</channels>'''
        generated = build_target_channels_xml(
            [catalogue],
            {"SonySAB.in@HD"},
            target_name_to_ids={"sonysab": {"SonySAB.in@HD"}},
        )
        root = ET.fromstring(generated)
        self.assertEqual(len(root.findall("channel")), 1)
        self.assertEqual(root.find("channel").attrib["xmltv_id"], "SonySAB.in@HD")
        self.assertEqual(root.find("channel").attrib["site_id"], "154")

    def test_jio_blank_id_mapping_rejects_ambiguous_playlist_names(self):
        catalogue = '''<channels>
  <channel site="jiotv.com" site_id="154" lang="en" xmltv_id="">Sony SAB HD</channel>
</channels>'''
        generated = build_target_channels_xml(
            [catalogue],
            {"SonySAB.in@HD", "SonySAB.in@SD"},
            target_name_to_ids={"sonysab": {"SonySAB.in@HD", "SonySAB.in@SD"}},
        )
        self.assertEqual(ET.fromstring(generated).findall("channel"), [])

    def test_jio_name_index_only_uses_active_indian_targets_from_both_playlists(self):
        with tempfile.TemporaryDirectory() as tmp:
            iptv = Path(tmp) / "IPTV-Playlist.m3u"
            international = Path(tmp) / "International-Playlist.m3u"
            iptv.write_text(
                '#EXTM3U\n'
                '#EXTINF:-1 tvg-id="SonySAB.in@HD" tvg-name="Sony SAB" group-title="Indian Entertainment",Sony SAB\n'
                'https://example.test/sony.m3u8\n',
                encoding="utf-8",
            )
            international.write_text(
                '#EXTM3U\n'
                '#EXTINF:-1 tvg-id="SonySAB.uk@HD" tvg-name="Sony SAB" group-title="United Kingdom",Sony SAB\n'
                'https://example.test/sony-uk.m3u8\n',
                encoding="utf-8",
            )
            with patch.object(fetcher, "PLAYLISTS", (iptv, international)):
                index = fetcher.read_active_target_name_to_ids(
                    {"SonySAB.in@HD", "SonySAB.uk@HD"}
                )
        self.assertEqual(index, {"sonysab": {"SonySAB.in@HD"}})

    def test_selected_catalogue_texts_loads_all_plex_region_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            directory = work / "sites" / "plex.tv"
            directory.mkdir(parents=True)
            (directory / "plex.tv_uk.channels.xml").write_text("<channels><channel>UK</channel></channels>", encoding="utf-8")
            (directory / "plex.tv_us.channels.xml").write_text("<channels><channel>US</channel></channels>", encoding="utf-8")
            with patch.object(fetcher, "WORK", work), patch.object(fetcher, "SITES", ("plex.tv",)):
                texts = fetcher.selected_catalogue_texts()
        self.assertEqual(len(texts), 2)
        self.assertTrue(any(">UK<" in value for value in texts))
        self.assertTrue(any(">US<" in value for value in texts))


if __name__ == "__main__":
    unittest.main()
