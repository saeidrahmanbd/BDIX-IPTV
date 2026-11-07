import ast, csv, io, os, re, tempfile, unittest, sys
from datetime import datetime, timezone, timedelta
from unittest.mock import patch
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import generate_epg
import epg_coverage
import epg_source_cache
import official_epg_sources
import augment_epg_mapping_from_additional_sources as additional_augment
import augment_epg_mapping_from_iptv_org as iptv_org_augment

COV = (ROOT / "scripts" / "epg_coverage.py").read_text(encoding="utf-8")
GEN = (ROOT / "scripts" / "generate_epg.py").read_text(encoding="utf-8")


def literal(src, name):
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == name for t in node.targets):
            return ast.literal_eval(node.value)
    raise AssertionError(name)


class EpgConfigTests(unittest.TestCase):
    def test_sources_synchronized_and_unique(self):
        a, b = literal(COV, "SOURCES"), literal(GEN, "SOURCES")
        self.assertEqual(a, b)
        self.assertEqual(len(a), len(set(a)))

    def test_epg_pw_is_excluded_from_public_ingestion_without_redistribution_permission(self):
        source = "https://epg.pw/xmltv/epg_IN.xml.gz"
        self.assertNotIn(source, literal(COV, "SOURCES"))
        self.assertNotIn(source, literal(GEN, "SOURCES"))
        augment = (ROOT / "scripts" / "augment_epg_mapping_from_additional_sources.py").read_text(encoding="utf-8")
        self.assertNotIn(source, literal(augment, "SOURCES"))
        self.assertIn('startswith("epgpw:")', COV)
        register = (ROOT / "epg" / "source-rights-register.csv").read_text(encoding="utf-8")
        self.assertIn(source + ",legacy_feed_not_active,PROHIBITED", register)

    def test_added_public_discovery_feeds_are_available_to_mapping_and_generation(self):
        expected = [
            "https://epg.lat/files/in.xml.gz",
            "https://epg.lat/files/us.xml.gz",
            "https://www.free-epg.de/api/epg/in.xml.gz",
            "https://www.free-epg.de/api/epg/us.xml.gz",
            "https://www.open-epg.com/files/india.xml.gz",
            "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
            "https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz",
            "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz",
            "https://www.free-epg.de/api/epg/pk.xml.gz",
            "https://iptv-epg.org/files/epg-in.xml.gz",
            "https://iptv-epg.org/files/epg-at.xml.gz",
            "https://iptv-epg.org/files/epg-au.xml.gz",
            "https://iptv-epg.org/files/epg-cr.xml.gz",
            "https://iptv-epg.org/files/epg-pa.xml.gz",
            "https://iptv-epg.org/files/epg-py.xml.gz",
            "https://iptv-epg.org/files/epg-sg.xml.gz",
            "https://free-epg.de/api/epg/at.xml.gz",
            "https://free-epg.de/api/epg/cn.xml.gz",
            "https://free-epg.de/api/epg/cr.xml.gz",
            "https://free-epg.de/api/epg/ec.xml.gz",
            "https://free-epg.de/api/epg/ee.xml.gz",
            "https://free-epg.de/api/epg/pa.xml.gz",
            "https://free-epg.de/api/epg/sa.xml.gz",
            "https://free-epg.de/api/epg/ua.xml.gz",
            "https://m3u-edit.com/epg-source.php?file=india_dishtv.in.xml",
            "https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz",
            "https://m3u-edit.com/epg-source.php?file=IN1.xml.gz",
            "https://m3u-edit.com/epg-source.php?file=IN4.xml.gz",
            "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/slingtv.xml",
                ]
        self.assertNotIn("https://iptv-epg.org/files/epg-pk.xml.gz", literal(COV, "SOURCES"))
        self.assertNotIn("https://iptv-epg.org/files/epg-pk.xml.gz", literal(GEN, "SOURCES"))
        for source in expected:
            self.assertIn(source, literal(COV, "SOURCES"))
            self.assertIn(source, literal(GEN, "SOURCES"))
        discovery = literal(
            (ROOT / "scripts" / "augment_epg_mapping_from_additional_sources.py").read_text(encoding="utf-8"),
            "SOURCES",
        )
        discovery_expected = [
            "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
            "https://epgshare01.online/epgshare01/epg_ripper_IN2.xml.gz",
            "https://epgshare01.online/epgshare01/epg_ripper_IN4.xml.gz",
            "https://iptv-epg.org/files/epg-in.xml.gz",
            "https://epg.lat/files/in.xml.gz",
            "https://www.free-epg.de/api/epg/in.xml.gz",
            "https://www.open-epg.com/files/india.xml.gz",
            "https://m3u-edit.com/epg-source.php?file=india_dishtv.in.xml",
            "https://m3u-edit.com/epg-source.php?file=india_tataplay.xml.gz",
            "https://m3u-edit.com/epg-source.php?file=IN1.xml.gz",
            "https://m3u-edit.com/epg-source.php?file=IN4.xml.gz",
        ]
        for source in discovery_expected:
            self.assertIn(source, discovery)

    def test_jasonramg_sling_feed_is_classified_as_us_and_region_matched(self):
        sling = "https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/slingtv.xml"
        self.assertEqual(generate_epg.source_country_codes(sling), {"US"})
        self.assertTrue(epg_coverage.source_region_compatible("US", "ShemarooBollywood.us", sling))
        self.assertTrue(epg_coverage.source_region_compatible("US", "SonyKALHindi.us", sling))
        self.assertFalse(epg_coverage.source_region_compatible("IN", "B4UMusic.in", sling))

    def test_private_m3u4u_source_is_selected_for_discovery_without_mapping(self):
        with tempfile.TemporaryDirectory() as tmp:
            mapping = Path(tmp) / "mapping.csv"
            mapping.write_text("group,channel,tvg_id,epg_id,source,status,note\n", encoding="utf-8")
            private_url = "https://m3u4u.com/epg/example-private-feed.xml"
            with patch.object(generate_epg, "MAPPING", mapping), patch.dict(os.environ, {"M3U4U_XMLTV_URL": private_url}):
                selected = generate_epg.sources_with_mapped_channels([private_url, "https://example.test/unused.xml"])
        self.assertEqual(selected, [private_url])

    def test_targeted_iptv_org_guide_is_audited_when_present(self):
        with tempfile.TemporaryDirectory() as tmp:
            guide = Path(tmp) / "iptv-org-guide.xml"
            now = datetime.now(timezone.utc)
            start = (now + timedelta(hours=1)).strftime("%Y%m%d%H%M%S +0000")
            stop = (now + timedelta(hours=2)).strftime("%Y%m%d%H%M%S +0000")
            guide.write_text(
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<tv><channel id="ColorsBangla.in"><display-name>Colors Bangla</display-name></channel>'
                f'<programme channel="ColorsBangla.in" start="{start}" stop="{stop}">'
                '<title lang="bn">আজকের অনুষ্ঠান</title></programme></tv>',
                encoding="utf-8",
            )
            source = guide.as_uri()
            with (
                patch.object(epg_coverage, "IPTV_ORG_LOCAL_GUIDE", guide),
                patch.object(epg_coverage, "IPTV_ORG_LOCAL_SOURCE", source),
            ):
                self.assertIn(source, epg_coverage.configured_sources())
                ids, future, counts, _ = epg_coverage.fetch_source(source)
                self.assertEqual(
                    epg_coverage.source_label(source),
                    "iptv-org/epg (targeted build-time guide)",
                )
        self.assertIn("ColorsBangla.in", ids)
        self.assertIn("ColorsBangla.in", future)
        self.assertEqual(counts["ColorsBangla.in"], 1)
        self.assertEqual(epg_coverage.source_health(ids, future, counts), "OK")

    def test_source_health_flags_channel_only_and_stale_feeds(self):
        self.assertEqual(epg_coverage.source_health({"channel-a"}, set(), {}), "NO_PROGRAMMES")
        self.assertEqual(
            epg_coverage.source_health({"channel-a"}, set(), {"channel-a": 12}),
            "NO_CURRENT_FUTURE",
        )
        self.assertEqual(
            epg_coverage.source_health({"channel-a"}, {"channel-a"}, {"channel-a": 12}),
            "OK",
        )
        self.assertEqual(epg_coverage.source_health(set(), set(), {}), "NO_CHANNELS")

    def test_private_m3u4u_source_is_available_to_final_generation_without_leaking_its_label(self):
        private_url = "https://m3u4u.com/epg/example-private-feed.xml"
        with patch.dict(os.environ, {"M3U4U_XMLTV_URL": private_url}):
            self.assertIn(private_url, generate_epg.configured_sources())
            self.assertNotEqual(generate_epg.source_label(private_url), private_url)

    def test_rtv_schedule_tries_current_daily_then_legacy_https_without_disabling_tls(self):
        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        html = "".join(
            f"<p>{day}</p>"
            f"<p>09:00 AM - Show {day} A</p>"
            f"<p>10:00 AM - Show {day} B</p>"
            f"<p>11:00 AM - Show {day} C</p>"
            for day in weekdays
        )
        with patch.object(
            official_epg_sources.urllib.request,
            "urlopen",
            side_effect=[
                OSError("current daily page unavailable"),
                OSError("legacy apex unavailable"),
                io.BytesIO(html.encode("utf-8")),
            ],
        ) as urlopen:
            programmes = official_epg_sources.fetch_rtv_programmes(
                datetime(2026, 10, 29, tzinfo=timezone.utc)
            )
        self.assertTrue(programmes)
        self.assertEqual(
            urlopen.call_args_list[0].args[0].full_url,
            "https://rtvonline.com/home/",
        )
        self.assertEqual(
            urlopen.call_args_list[1].args[0].full_url,
            "https://rtvbd.tv/schedule.php",
        )
        self.assertEqual(
            urlopen.call_args_list[2].args[0].full_url,
            "https://www.rtvbd.tv/schedule.php",
        )

    def test_rtv_daily_schedule_parses_current_bengali_date_and_times(self):
        homepage = """
        <a href="/entertainment/rtv/413624">আরটিভিতে আজ যা দেখবেন</a>
        <a href="/entertainment/rtv/413846">আরটিভিতে আজ যা দেখবেন</a>
        """
        article = """
        <p>শুক্রবার, ৬ নভেম্বর ২০২৬, ২১ কার্তিক ১৪৩৩। একনজরে জেনে নিন আরটিভির আজকের আয়োজন—</p>
        <p>সকাল ৯টায় টকশো ‘আজ পত্রিকায়’।</p>
        <p>সকাল ৯টা ৪৫ মিনিটে ‘সকালের সংবাদ’</p>
        <p>সকাল ১০টা ১০ মিনিটে বাংলা ছায়াছবি ‘গরীবের বউ’</p>
        <p>দুপুর ২টা ১০ মিনিটে বাংলা ছায়াছবি ‘হুমকির মুখে’</p>
        <p>বিকেল ৫টায় শিশুতোষ অনুষ্ঠান ‘সিসিমপুর’</p>
        <p>সন্ধ্যা ৭টায় অনুষ্ঠান ‘রাতের খবর’</p>
        <p>রাত ৮টায় নাটক ‘প্রতিদিন’</p>
        """
        with patch.object(
            official_epg_sources.urllib.request,
            "urlopen",
            side_effect=[
                io.BytesIO(homepage.encode("utf-8")),
                io.BytesIO(article.encode("utf-8")),
            ],
        ) as urlopen:
            programmes = official_epg_sources.fetch_rtv_programmes(
                datetime(2026, 11, 6, 0, 0, tzinfo=timezone.utc)
            )
        self.assertEqual(
            urlopen.call_args_list[0].args[0].full_url,
            "https://rtvonline.com/home/",
        )
        self.assertEqual(
            urlopen.call_args_list[1].args[0].full_url,
            "https://rtvonline.com/entertainment/rtv/413846",
        )
        self.assertGreaterEqual(len(programmes), 4)
        self.assertTrue(all(p["channel_id"] == "RTV.bd" for p in programmes))
        morning = next(p for p in programmes if p["title"] == "টকশো ‘আজ পত্রিকায়’")
        self.assertEqual(morning["start_dt"], datetime(2026, 11, 6, 3, 0, tzinfo=timezone.utc))
        self.assertEqual(morning["stop_dt"], datetime(2026, 11, 6, 3, 45, tzinfo=timezone.utc))

    def test_rtv_daily_schedule_rejects_yesterday_instead_of_publishing_stale_slots(self):
        stale = "বৃহস্পতিবার, ৫ নভেম্বর ২০২৬, ২১ কার্তিক ১৪৩৩। সকাল ৯টায় অনুষ্ঠান।"
        parsed = official_epg_sources._parse_rtv_daily_programmes(
            stale,
            datetime(2026, 11, 6, 0, 0, tzinfo=timezone.utc),
        )
        self.assertEqual(parsed, [])

    def test_btv_official_schedule_parses_bengali_dates_and_explicit_times(self):
        cards = []
        for index in range(10):
            start_minutes = 8 * 60 + index * 30
            stop_minutes = start_minutes + 25
            sh, sm = divmod(start_minutes, 60)
            eh, em = divmod(stop_minutes, 60)
            cards.append(
                f"<h3>পরীক্ষামূলক অনুষ্ঠান {index}</h3>"
                f"<div>২৯ অক্টো, ২০২৬ · {sh:02d}:{sm:02d} – {eh:02d}:{em:02d}</div>"
            )
        html = "".join(cards)
        with patch.object(
            official_epg_sources.urllib.request,
            "urlopen",
            return_value=io.BytesIO(html.encode("utf-8")),
        ):
            programmes = official_epg_sources.fetch_btv_programmes(
                datetime(2026, 10, 29, tzinfo=timezone.utc)
            )
        self.assertEqual(len(programmes), 10)
        self.assertEqual(programmes[0]["channel_id"], "BTVNational.bd")
        self.assertEqual(programmes[0]["title"], "পরীক্ষামূলক অনুষ্ঠান 0")


    def test_maasranga_official_weekly_schedule_parses_bengali_titles_and_midnight(self):
        days = ["রবিবার", "সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার", "শুক্রবার", "শনিবার"]
        rows = [
            ("07:00am – 09:00", "রাঙা সকাল"),
            ("09:00am – 12:00pm", "বাংলা চলচ্চিত্র"),
            ("12:00pm – 12:10pm", "মাছরাঙা সংবাদ"),
            ("04:30pm – 05:00", "নিনজা হাতোরি"),
            ("11:30pm – 12.00", "বিজনেস রিপোর্ট"),
        ]
        table = ["<table><tr><th>সময়</th>" + "".join(f"<th>{day}</th>" for day in days) + "</tr>"]
        for time_range, title in rows:
            table.append(
                "<tr><td>" + time_range + "</td>"
                + "".join(f"<td>{title}</td>" for _ in days)
                + "</tr>"
            )
        table.append("</table>")
        html = "".join(table)
        with patch.object(
            official_epg_sources.urllib.request,
            "urlopen",
            return_value=io.BytesIO(html.encode("utf-8")),
        ):
            programmes = official_epg_sources.fetch_maasranga_programmes(
                datetime(2026, 11, 4, 0, 0, tzinfo=timezone.utc)
            )
        self.assertGreaterEqual(len(programmes), 30)
        self.assertTrue(all(p["channel_id"] == "MaasrangaTV.bd" for p in programmes))
        morning = next(p for p in programmes if p["title"] == "রাঙা সকাল")
        self.assertEqual(morning["start_dt"], datetime(2026, 11, 4, 1, 0, tzinfo=timezone.utc))
        midnight = next(p for p in programmes if p["title"] == "বিজনেস রিপোর্ট")
        self.assertEqual(midnight["start_dt"], datetime(2026, 11, 4, 17, 30, tzinfo=timezone.utc))
        self.assertEqual(midnight["stop_dt"], datetime(2026, 11, 4, 18, 0, tzinfo=timezone.utc))

    def test_source_audit_is_staged_by_refresh_workflow(self):
        workflow = (ROOT / ".github" / "workflows" / "epg-refresh.yml").read_text(encoding="utf-8")
        self.assertIn("reports/epg-source-audit.md", workflow)
        self.assertIn("reports/bangladesh-epg-source-audit.md", workflow)
        self.assertIn('M3U4U_XMLTV_URL: ${{ secrets.M3U4U_XMLTV_URL }}', workflow)
        self.assertIn('BANGLADESH_SOURCE_AUDIT_REPORT = Path("reports/bangladesh-epg-source-audit.md")', COV)
        self.assertIn("tests/test_epg_config.py", workflow)

    def test_generator_parses_the_payload_for_each_fetched_source(self):
        self.assertIn(
            'data = source_payloads[src]\n            for _, elem in ET.iterparse(io.BytesIO(data), events=("end",)):',
            GEN,
        )

    def test_country_specific_feeds_are_scanned_for_active_playlist_regions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            main_playlist = root / "IPTV-Playlist.m3u"
            international_playlist = root / "International-Playlist.m3u"
            mapping = root / "mapping.csv"
            main_playlist.write_text(
                '#EXTM3U\n'
                '#EXTINF:-1 tvg-id="ColorsBangla.in" tvg-country="IN" group-title="Indian Entertainment" tvg-name="Colors Bangla",Colors Bangla\n'
                'https://example.test/india.m3u8\n',
                encoding="utf-8",
            )
            international_playlist.write_text(
                '#EXTM3U\n'
                '#EXTINF:-1 tvg-id="TVN.pa" tvg-country="PA" group-title="Panama" tvg-name="TVN",TVN\n'
                'https://example.test/panama.m3u8\n'
                '#EXTINF:-1 tvg-id="Channel.sg" group-title="Singapore" tvg-name="Channel",Channel\n'
                'https://example.test/singapore.m3u8\n'
                '#EXTINF:-1 tvg-id="CCTV6.cn@HD" group-title="International" tvg-name="CCTV-6",CCTV-6\n'
                'https://example.test/cctv6.m3u8\n'
                '#EXTINF:-1 tvg-id="KidsChannel.uk@HD" group-title="Kids" tvg-name="Kids Channel",Kids Channel\n'
                'https://example.test/kids.m3u8\n'
                '#EXTINF:-1 tvg-id="CanalBrasil.br" tvg-country="BR" group-title="International" tvg-name="Canal Brasil",Canal Brasil\n'
                'https://example.test/brazil.m3u8\n'
                '#EXTINF:-1 tvg-id="NotACountry.hd" group-title="International" tvg-name="Invalid",Invalid\n'
                'https://example.test/invalid.m3u8\n',
                encoding="utf-8",
            )
            mapping.write_text(
                "group,channel,tvg_id,epg_id,source,status,note\n",
                encoding="utf-8",
            )
            configured = [
                "https://iptv-epg.org/files/epg-in.xml.gz",
                "https://free-epg.de/api/epg/pa.xml.gz",
                "https://iptv-epg.org/files/epg-sg.xml.gz",
                "https://free-epg.de/api/epg/us.xml.gz",
                "https://example.test/unmapped.xml",
                "https://free-epg.de/api/epg/cn.xml.gz",
                "https://iptv-epg.org/files/epg-gb.xml.gz",
                "https://iptv-epg.org/files/epg-br.xml.gz",
            ]
            with (
                patch.object(generate_epg, "PLAYLISTS", [main_playlist, international_playlist]),
                patch.object(generate_epg, "MAPPING", mapping),
            ):
                countries = generate_epg.active_playlist_country_codes()
                selected = generate_epg.sources_with_mapped_channels(configured)

        self.assertEqual(countries, {"IN", "PA", "SG", "CN", "GB", "BR"})
        self.assertEqual(
            selected,
            [
                "https://iptv-epg.org/files/epg-in.xml.gz",
                "https://free-epg.de/api/epg/pa.xml.gz",
                "https://iptv-epg.org/files/epg-sg.xml.gz",
                "https://free-epg.de/api/epg/cn.xml.gz",
                "https://iptv-epg.org/files/epg-gb.xml.gz",
                "https://iptv-epg.org/files/epg-br.xml.gz",
            ],
        )

    def test_playlist_country_inference_blocks_cross_region_name_matches(self):
        with tempfile.TemporaryDirectory() as tmp:
            playlist = Path(tmp) / "IPTV-Playlist.m3u"
            playlist.write_text(
                '#EXTM3U\n'
                '#EXTINF:-1 tvg-id="CCTV6.cn@HD" group-title="International" tvg-name="CCTV-6",CCTV-6\n'
                'https://example.test/cctv6.m3u8\n'
                '#EXTINF:-1 tvg-id="ChannelS.uk@679aa9" group-title="Kids" tvg-name="Channel S",Channel S\n'
                'https://example.test/channels.m3u8\n'
                '#EXTINF:-1 tvg-id="Generic.sg" group-title="International" tvg-name="Singapore TV",Singapore TV\n'
                'https://example.test/singapore.m3u8\n'
                '#EXTINF:-1 tvg-id="NoSuffix" group-title="Singapore" tvg-name="Fallback",Fallback\n'
                'https://example.test/fallback.m3u8\n'
                '#EXTINF:-1 tvg-id="XITEHits.nl@UK" group-title="International" tvg-name="XITE Hits UK",XITE Hits UK\n'
                'https://example.test/xite-uk.m3u8\n'
                '#EXTINF:-1 tvg-id="AdrenalinaPuraTV.us@Brazil" group-title="United States" tvg-name="Adrenalina Pura TV",Adrenalina Pura TV\n'
                'https://example.test/adrenalina-br.m3u8\n'
                '#EXTINF:-1 tvg-id="BBCDrama.uk@US" tvg-country="GB" group-title="United States" tvg-name="BBC Drama",BBC Drama\n'
                'https://example.test/bbc-drama.m3u8\n',
                encoding="utf-8",
            )
            with patch.object(epg_coverage, "PLAYLISTS", [playlist]):
                channels = epg_coverage.parse_playlist()

        countries = {channel["tvg_id"]: channel["country"] for channel in channels}
        self.assertEqual(countries["CCTV6.cn@HD"], "CN")
        self.assertEqual(countries["ChannelS.uk@679aa9"], "GB")
        self.assertEqual(countries["Generic.sg"], "SG")
        self.assertEqual(countries["NoSuffix"], "SG")
        self.assertEqual(countries["XITEHits.nl@UK"], "GB")
        self.assertEqual(countries["AdrenalinaPuraTV.us@Brazil"], "BR")
        self.assertEqual(countries["BBCDrama.uk@US"], "GB")
        self.assertEqual(epg_coverage.source_id_country("ChannelS.uk@679aa9"), "GB")
        self.assertTrue(epg_coverage.source_region_compatible("GB", "ChannelS.uk@679aa9"))
        self.assertFalse(epg_coverage.source_region_compatible("GB", "ChannelS.in@HD"))
        self.assertEqual(generate_epg.playlist_id_country_code("XITEHits.nl@UK"), "GB")
        self.assertEqual(generate_epg.playlist_id_country_code("NatureTime.ca@AU"), "AU")
        self.assertEqual(generate_epg.playlist_id_country_code("WorldPokerTour.us@Poland"), "PL")
        self.assertEqual(generate_epg.playlist_id_country_code("Cinemax.cz@Czechia"), "CZ")
        self.assertEqual(generate_epg.playlist_id_country_code("CCTV6.cn@HD"), "CN")
        self.assertEqual(generate_epg.playlist_id_country_code("MyTimeMovieNetwork.mx@SD"), "MX")

    def test_source_feed_country_blocks_cross_region_exact_name_candidates(self):
        self.assertFalse(
            epg_coverage.source_region_compatible(
                "GB", "generic-channel-id", "https://iptv-epg.org/files/epg-us.xml.gz"
            )
        )
        self.assertTrue(
            epg_coverage.source_region_compatible(
                "GB", "generic-channel-id", "https://iptv-epg.org/files/epg-gb.xml.gz"
            )
        )
        self.assertFalse(
            epg_coverage.source_region_compatible(
                "AU", "NatureTime", "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz"
            )
        )
        self.assertTrue(
            epg_coverage.source_region_compatible(
                "AU", "NatureTime", "https://epgshare01.online/epgshare01/epg_ripper_AU1.xml.gz"
            )
        )
        # Mixed-region/private feeds have no inferred country and remain eligible
        # for exact-name matching; their URL is never emitted by the audit.
        self.assertTrue(
            epg_coverage.source_region_compatible(
                "GB", "generic-channel-id", "M3U4U XMLTV (private Actions secret)"
            )
        )

    def test_mytime_movie_network_east_uses_exact_us_samsung_identity(self):
        self.assertEqual(
            epg_coverage.EPG_ALIASES["MyTimeMovieNetworkEast.us"],
            ["USBC3900018K6"],
        )
        self.assertTrue(
            epg_coverage.source_region_compatible(
                "US", "USBC3900018K6", "https://i.mjh.nz/SamsungTVPlus/us.xml"
            )
        )
        self.assertFalse(
            epg_coverage.source_region_compatible(
                "US", "USBC3900018K6", "https://i.mjh.nz/SamsungTVPlus/in.xml"
            )
        )

    def test_source_country_codes_recognize_public_feed_families(self):
        self.assertEqual(
            generate_epg.source_country_codes("https://iptv-epg.org/files/epg-at.xml.gz"),
            {"AT"},
        )
        self.assertEqual(
            generate_epg.source_country_codes("https://iptv-epg.org/files/epg-pk.xml.gz"),
            {"PK"},
        )
        self.assertEqual(
            generate_epg.source_country_codes("https://www.free-epg.de/api/epg/pk.xml.gz"),
            {"PK"},
        )
        self.assertEqual(
            generate_epg.source_country_codes("https://free-epg.de/api/epg/cn.xml.gz"),
            {"CN"},
        )
        self.assertEqual(
            generate_epg.source_country_codes("https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz"),
            {"GB"},
        )
        self.assertEqual(
            generate_epg.source_country_codes("https://m3u-edit.com/epg-source.php?file=IN4.xml.gz"),
            {"IN"},
        )

    def test_generator_skips_feeds_without_current_mapped_source_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            mapping = Path(tmp) / "mapping.csv"
            with mapping.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=["group", "channel", "tvg_id", "epg_id", "source", "status", "note"],
                )
                writer.writeheader()
                writer.writerow({
                    "group": "Indian Entertainment", "channel": "Demo",
                    "tvg_id": "Demo.in", "epg_id": "feed-a-id",
                    "source": "feed-a | feed-b", "status": "MAPPED", "note": "",
                })
            configured = [
                "feed-a", "feed-b", "feed-c", "file:///tmp/iptv-org-guide.xml",
                generate_epg.HUM_TV_SOURCE, generate_epg.RTV_SOURCE, generate_epg.BTV_SOURCE,
            ]
            with patch.object(generate_epg, "MAPPING", mapping):
                selected = generate_epg.sources_with_mapped_channels(configured)
        self.assertEqual(
            selected,
            ["feed-a", "feed-b", "file:///tmp/iptv-org-guide.xml",
             generate_epg.HUM_TV_SOURCE, generate_epg.RTV_SOURCE, generate_epg.BTV_SOURCE],
        )

    def test_generator_covers_both_maintained_playlists(self):
        tree = ast.parse(GEN)
        playlists = next(
            node.value
            for node in ast.walk(tree)
            if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "PLAYLISTS" for target in node.targets)
        )
        paths = [
            elt.args[0].value
            for elt in playlists.elts
            if isinstance(elt, ast.Call)
            and isinstance(elt.func, ast.Name)
            and elt.func.id == "Path"
            and elt.args
            and isinstance(elt.args[0], ast.Constant)
        ]
        self.assertEqual(paths, ["IPTV-Playlist.m3u", "International-Playlist.m3u"])

    def test_rtv_official_schedule_source_is_configured(self):
        coverage_sources = literal(COV, "SOURCES")
        generator_sources = literal(GEN, "SOURCES")
        self.assertEqual(official_epg_sources.RTV_SOURCE, "https://rtvonline.com/home/")
        self.assertIn(official_epg_sources.RTV_SOURCE, coverage_sources)
        self.assertIn(official_epg_sources.RTV_SOURCE, generator_sources)
        self.assertIn("https://rtvbd.tv/schedule.php", official_epg_sources.RTV_LEGACY_SOURCES)
        self.assertIn("https://www.rtvbd.tv/schedule.php", official_epg_sources.RTV_LEGACY_SOURCES)
        self.assertIn(official_epg_sources.BTV_SOURCE, coverage_sources)
        self.assertIn(official_epg_sources.BTV_SOURCE, generator_sources)
        self.assertEqual(literal(COV, "EPG_LOCKS")["BTVNational.bd"], ["BTVNational.bd"])
        self.assertIn(official_epg_sources.MAASRANGA_SOURCE, coverage_sources)
        self.assertIn(official_epg_sources.MAASRANGA_SOURCE, generator_sources)
        self.assertEqual(literal(COV, "EPG_LOCKS")["MaasrangaTV.bd"], ["MaasrangaTV.bd"])

    def test_epg_source_list_has_no_hardcoded_provider_ban(self):
        coverage_sources = literal(COV, "SOURCES")
        generator_sources = literal(GEN, "SOURCES")
        self.assertEqual(len(coverage_sources), len(generator_sources))
        self.assertEqual(coverage_sources, generator_sources)
        self.assertNotIn("EPGPW_SOURCE_IDS", COV + GEN)
        self.assertNotIn("normalize_epgpw_source", COV + GEN)

    def test_strict_unmapped_aliases_use_region_compatible_schedule_sources(self):
        aliases = epg_coverage.EPG_ALIASES
        self.assertTrue(
            epg_coverage.source_region_compatible(
                "IN", aliases["Vision.in@SD"][0],
                "https://epgshare01.online/epgshare01/epg_ripper_IN1.xml.gz",
            )
        )
        self.assertTrue(
            epg_coverage.source_region_compatible(
                "US", aliases["DePeliculaUS.us@SD"][0],
                "https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz",
            )
        )
        self.assertTrue(
            epg_coverage.source_region_compatible(
                "US", aliases["BBCEarth.uk@US"][0],
                "https://i.mjh.nz/SamsungTVPlus/us.xml",
            )
        )
        iptv = (ROOT / "IPTV-Playlist.m3u").read_text(encoding="utf-8-sig")
        international = (ROOT / "International-Playlist.m3u").read_text(encoding="utf-8-sig")
        self.assertIn('tvg-id="Vision.in@SD"', iptv)
        self.assertIn('tvg-id="DePeliculaUS.us@SD"', international)
        self.assertIn('tvg-id="BBCEarth.uk@US"', international)

    def test_shared_source_cache_reuses_download_without_exposing_private_url(self):
        with tempfile.TemporaryDirectory() as tmp:
            private_url = "https://m3u4u.com/epg/private-feed-token.xml"
            payload = b"<?xml version='1.0'?><tv/>"
            with (
                patch.dict(
                    os.environ,
                    {
                        "EPG_SOURCE_CACHE_DIR": tmp,
                        "EPG_SOURCE_CACHE_TTL_SECONDS": "3600",
                    },
                ),
                patch.object(
                    epg_source_cache.urllib.request,
                    "urlopen",
                    return_value=io.BytesIO(payload),
                ) as urlopen,
            ):
                first = epg_source_cache.fetch_source_bytes(
                    private_url,
                    headers={"User-Agent": "test", "Accept": "application/xml"},
                    timeout=5,
                )
                second = epg_source_cache.fetch_source_bytes(
                    private_url,
                    headers={"User-Agent": "test", "Accept": "application/xml"},
                    timeout=5,
                )
            self.assertEqual(first, payload)
            self.assertEqual(second, payload)
            self.assertEqual(urlopen.call_count, 1)
            cache_files = list(Path(tmp).iterdir())
            self.assertEqual(len(cache_files), 1)
            self.assertNotIn("private-feed-token", cache_files[0].name)

    def test_new_aliases(self):
        al = literal(COV, "EPG_ALIASES")
        self.assertEqual(al["Hungama.in@SD"], ["143150"])
        self.assertEqual(al["ZBMusic.in@HD"], ["jtv3319"])
        self.assertEqual(al["DeenTV.uk"], ["1235", "DeenTV.uk", "DeenTV.uk@SD"])
        self.assertEqual(al["Cinemax.cz@Czechia"], ["Cinemax.cz"])
        self.assertEqual(al["History.cz@SD"], ["History.Channel.cz"])
        self.assertEqual(al["WeatherSpy.in@SD"], ["INBA5100028R4"])
        self.assertEqual(al["Vision.in@SD"], ["Channel.Vision.in", "jtv1762"])
        self.assertEqual(al["DePeliculaUS.us@SD"], ["De.Pelicula.us2"])
        self.assertEqual(al["BBCEarth.uk@US"], ["USBD1700001RW"])
        self.assertNotIn("ZBBhakti.in@HD", al)

    def test_nick_bangla_uses_verified_exact_jiotv_channel_identity(self):
        locks = literal(COV, "EPG_LOCKS")
        self.assertEqual(locks["NickBangla.bd"], ["jtv1341"])
        self.assertIn('NickBangla.bd', (ROOT / "IPTV-Playlist.m3u").read_text(encoding="utf-8-sig"))

    def test_trace_urban_international_uses_verified_french_xmltv_identities(self):
        aliases = literal(COV, "EPG_ALIASES")
        self.assertEqual(
            aliases["TraceUrban.fr@InternationalHD"],
            ["Trace.Urban.fr", "TraceUrban.fr"],
        )
        playlist = (ROOT / "International-Playlist.m3u").read_text(encoding="utf-8-sig")
        self.assertIn('tvg-id="TraceUrban.fr@InternationalHD"', playlist)
        self.assertTrue(
            epg_coverage.source_region_compatible(
                "FR", "Trace.Urban.fr",
                "https://epgshare01.online/epgshare01/epg_ripper_FR1.xml.gz",
            )
        )

    def test_m3u4u_exact_ids_are_enabled_without_weakening_bangladesh_matching(self):
        locks = literal(COV, "EPG_LOCKS")
        self.assertEqual(locks["ATNBanglaUK.uk"], ["6753", "ATNBanglaUK.uk", "ATNBanglaUK.uk@SD"])
        self.assertEqual(locks["IqraBangla.uk"], ["3914", "IqraBangla.uk", "IqraBangla.uk@SD"])
        self.assertEqual(locks["NTVEurope.bd"], ["4540", "NTVEurope.bd", "NTVEurope.bd@SD"])
        self.assertNotIn("News24.in@SD", locks.get("News24.bd", []))

    def test_name_matches_cannot_cross_explicit_country_boundaries(self):
        self.assertEqual(epg_coverage.source_id_country("Discovery.Science.in (src05)"), "IN")
        self.assertEqual(epg_coverage.source_id_country("AMC.us"), "US")
        self.assertEqual(epg_coverage.source_id_country("CartoonNetwork.uk"), "GB")
        self.assertFalse(epg_coverage.source_region_compatible("US", "Discovery.Science.in (src05)"))
        self.assertTrue(epg_coverage.source_region_compatible("IN", "Discovery.Science.in (src05)"))
        self.assertTrue(epg_coverage.source_region_compatible("GB", "CartoonNetwork.uk"))
        self.assertTrue(epg_coverage.source_region_compatible("", "Discovery.Science.in (src05)"))

    def test_no_bangladesh_alias_to_foreign_ids(self):
        for key, ids in literal(COV, "EPG_ALIASES").items():
            if re.search(r"\.bd(@|$)", key):
                self.assertTrue(all(i.endswith(".bd") or i == key for i in ids), key)

    def test_all_alias_and_lock_keys_exist_in_current_playlists(self):
        playlist_ids = set()
        for path in (ROOT / "IPTV-Playlist.m3u", ROOT / "International-Playlist.m3u"):
            playlist_ids.update(re.findall(r'tvg-id="([^"]+)"', path.read_text(encoding="utf-8-sig")))
        for name in ("EPG_ALIASES", "EPG_LOCKS"):
            mapping = literal(COV, name)
            self.assertEqual(
                sorted(set(mapping) - playlist_ids),
                [],
                f"{name} contains keys absent from both maintained playlists",
            )

    def test_alias_ids_exist_in_playlist(self):
        pl = (ROOT / "IPTV-Playlist.m3u").read_text(encoding="utf-8-sig")
        for tid in ("Hungama.in@SD", "ZBMusic.in@HD"):
            self.assertIn(f'tvg-id="{tid}"', pl)
        self.assertNotIn('tvg-id="ZBBhakti.in@HD"', pl)

    def test_epg_refresh_runs_after_completed_playlist_writer_workflows_even_when_blocked(self):
        workflow = (ROOT / ".github" / "workflows" / "epg-refresh.yml").read_text(encoding="utf-8")
        self.assertIn("workflow_run:", workflow)
        for name in (
            "IPTV Playlist Update",
            "IPTV New Channel Discovery",
            "International Channel Discovery",
            "Playlist Logo Repair and Localization",
        ):
            self.assertIn(f'"{name}"', workflow)
        self.assertIn("types: [completed]", workflow)
        self.assertIn("even when a playlist-maintenance", workflow)
        self.assertNotIn("github.event.workflow_run.conclusion == 'success'", workflow)
        self.assertNotIn("github.event.workflow_run.conclusion == 'failure'", workflow)
        self.assertIn("# 09:00 Asia/Dhaka (UTC+6)", workflow)


    def test_epg_refresh_serializes_builds_and_keeps_known_good_guide_safe(self):
        workflow = (ROOT / ".github" / "workflows" / "epg-refresh.yml").read_text(encoding="utf-8")
        self.assertIn("group: iptv-playlist-main-writer-v3", workflow)
        self.assertIn("cancel-in-progress: false", workflow)
        self.assertIn("queue: max", workflow)
        self.assertIn("Skip superseded queued EPG refresh", workflow)
        self.assertIn("refusing to publish stale output", workflow)
        self.assertIn("last known-good public guide", workflow)


class BangladeshRetentionTests(unittest.TestCase):
    @staticmethod
    def helper():
        src = COV[COV.index("def retained_mapping"):COV.index("def main():")]
        ns = {}
        exec(src, ns)
        return ns["retained_mapping"]

    def test_stale_foreign_mapping_is_dropped_for_bangladesh(self):
        f = self.helper()
        self.assertEqual(f(True, "News24.in@SD", ["News24.bd"]), "")
        self.assertEqual(f(True, "LIVETV_LIVETVCHANNEL_TV_24", ["Channel24.bd"]), "")

    def test_lock_alias_or_own_id_is_kept_for_bangladesh(self):
        f = self.helper()
        self.assertEqual(f(True, "6753", ["6753"]), "6753")
        self.assertEqual(f(True, "ATNBangla.bd", ["ATNBangla.bd", "alias"]), "ATNBangla.bd")

    def test_non_bangladesh_mappings_are_still_retained(self):
        self.assertEqual(self.helper()(False, "jtv1962", ["x"]), "jtv1962")

    def test_nothing_retained_when_empty(self):
        self.assertEqual(self.helper()(True, "", ["a"]), "")


class VerifiedAliasTests(unittest.TestCase):
    def test_new_verified_aliases(self):
        al = literal(COV, "EPG_ALIASES")
        self.assertEqual(al["AmarBanglaDigital.in"], ["jtv1962"])
        self.assertNotIn("AamarBangla.in@SD", al)
        self.assertIn("jtv3384", al["EpicBhojpuriDigital.in"])
        self.assertIn("And.Pictures.HD.in", al["AndPictures.in@SD"])
        self.assertIn("And.Pictures.Tv.Channel.Today.in2", al["AndPictures.in@SD"])
        self.assertEqual(al["SonyMax2.in@SD"], ["143801", "LIVETV_LIVETVCHANNEL_SONY_MAX_2", "jtv483"])
        self.assertEqual(al["Enter10Bangla.in"], ["ENTER10.BANGLA.in", "Enterr10Bangla.in", "Enterr10Bangla.in@SD"])
        self.assertEqual(al["StarMovies.in"], ["LIVETV_LIVETVCHANNEL_STAR_MOVIES_HD"])
        self.assertEqual(al["custom.nick-jr-east"], ["Nick.Jr.HD.us2"])
        self.assertEqual(al["DeluxeRap.de"], ["DeluxeRap.de@SD"])
        self.assertEqual(al["DeejayTV.it"], ["Deejay.TV.it", "DeejayTV.it@SD"])
        self.assertEqual(al["R101TV.it"], ["R101tv.it", "R101TV.it@SD"])
        self.assertEqual(al["RadioItaliaTV.it"], ["Radio.Italia.TV.HD.it", "RadioItaliaTV.it@HD", "RadioItaliaTV.it@SD"])
        self.assertEqual(al["RTL1025TV.it"], ["RTL.102.5.HD.it", "RTL1025TV.it@HD"])
        self.assertEqual(al["RusskiyBestseller.ru@SD"], ["RusskiyBestseller.ru"])
        self.assertEqual(al["RusskiyDetektiv.ru@SD"], ["RusskiyDetektiv.ru"])

    def test_verified_international_ids_exist_in_playlist(self):
        pl = (ROOT / "International-Playlist.m3u").read_text(encoding="utf-8-sig")
        for tid in (
            "custom.nick-jr-east", "DeluxeRap.de", "DeejayTV.it", "R101TV.it", "RadioItaliaTV.it",
            "RakutenTVActionMoviesGermany.es", "Kino1.ua", "Kino2.ua", "MTV2.us",
            "RDSSocialTV.it", "RTL1025TV.it", "RusskiyBestseller.ru@SD",
            "RusskiyDetektiv.ru@SD", "RakutenTVFamilyMovies.es",
            "4everMusic.ua", "EUMusic.ua", "30AMusic.us",
        ):
            self.assertIn(f'tvg-id="{tid}"', pl)

    def test_new_alias_ids_exist_in_playlist(self):
        pl = (ROOT / "IPTV-Playlist.m3u").read_text(encoding="utf-8-sig")
        for tid in ("AmarBanglaDigital.in", "EpicBhojpuriDigital.in", "AndPictures.in@SD"):
            self.assertIn(f'tvg-id="{tid}"', pl)



class EpgMappingAugmentationTests(unittest.TestCase):
    def _entry(self, tvg_id, name, group, country=""):
        country_attr = f' tvg-country="{country}"' if country else ""
        return (
            f'#EXTINF:-1 tvg-id="{tvg_id}" tvg-name="{name}"'
            f' group-title="{group}"{country_attr},{name}\n'
            "https://example.test/live.m3u8\n"
        )

    def test_iptv_org_mapping_reads_both_maintained_playlists_and_infers_regions(self):
        with tempfile.TemporaryDirectory() as tmp:
            iptv = Path(tmp) / "IPTV-Playlist.m3u"
            international = Path(tmp) / "International-Playlist.m3u"
            iptv.write_text("#EXTM3U\n" + self._entry("ColorsBangla.in@HD", "Colors Bangla", "Indian Bangla", "IN"), encoding="utf-8")
            international.write_text("#EXTM3U\n" + self._entry("CCTV6.cn@HD", "CCTV6", "China"), encoding="utf-8")
            with patch.object(iptv_org_augment, "PLAYLISTS", (iptv, international)):
                channels = iptv_org_augment.playlist_channels()
        by_id = {channel[0]: channel for channel in channels}
        self.assertEqual(set(by_id), {"ColorsBangla.in@HD", "CCTV6.cn@HD"})
        self.assertEqual(by_id["ColorsBangla.in@HD"][3], "IN")
        self.assertEqual(by_id["CCTV6.cn@HD"][3], "CN")

    def test_indian_provider_discovery_respects_explicit_territory_qualifier(self):
        with tempfile.TemporaryDirectory() as tmp:
            iptv = Path(tmp) / "IPTV-Playlist.m3u"
            international = Path(tmp) / "International-Playlist.m3u"
            iptv.write_text("#EXTM3U\\n", encoding="utf-8")
            international.write_text(
                "#EXTM3U\\n"
                + self._entry("Channel.in@UK", "Channel UK", "Indian Entertainment")
                + self._entry("Channel.in@India", "Channel India", "International"),
                encoding="utf-8",
            )
            with patch.object(additional_augment, "PLAYLISTS", (iptv, international)):
                channels = additional_augment.playlist_channels()
        self.assertEqual([channel["tvg_id"] for channel in channels], ["Channel.in@India"])

    def test_indian_provider_discovery_includes_indian_ids_in_international_playlist(self):
        with tempfile.TemporaryDirectory() as tmp:
            iptv = Path(tmp) / "IPTV-Playlist.m3u"
            international = Path(tmp) / "International-Playlist.m3u"
            iptv.write_text("#EXTM3U\n", encoding="utf-8")
            international.write_text(
                "#EXTM3U\n"
                + self._entry("ColorsBangla.in@HD", "Colors Bangla", "International")
                + self._entry("CCTV6.cn@HD", "CCTV6", "China"),
                encoding="utf-8",
            )
            with patch.object(additional_augment, "PLAYLISTS", (iptv, international)):
                channels = additional_augment.playlist_channels()
        self.assertEqual([channel["tvg_id"] for channel in channels], ["ColorsBangla.in@HD"])

    def test_iptv_org_can_append_a_current_schedule_to_a_stale_existing_mapping(self):
        rows = [{
            "group": "China",
            "channel": "CCTV6",
            "tvg_id": "CCTV6.cn@HD",
            "epg_id": "old.provider.id",
            "source": "https://old.example/guide.xml",
            "status": "MAPPED_NOT_CURRENTLY_FOUND",
            "note": "Retained mapping",
        }]
        channels = [("CCTV6.cn@HD", "CCTV6", "China", "CN")]
        names = {"cctv6": {"CCTV6Provider.cn@HD"}}
        rows, explicit_added, exact_added = iptv_org_augment.apply_iptv_org_matches(
            channels, rows, names, {"CCTV6Provider.cn@HD"}
        )
        self.assertEqual(explicit_added, 0)
        self.assertEqual(exact_added, 1)
        self.assertIn("old.provider.id", rows[0]["epg_id"])
        self.assertIn("CCTV6Provider.cn@HD", rows[0]["epg_id"])
        self.assertEqual(rows[0]["status"], "MAPPED")

    def test_iptv_org_exact_name_match_rejects_cross_country_source(self):
        rows = [{
            "group": "China", "channel": "CCTV6", "tvg_id": "CCTV6.cn@HD",
            "epg_id": "", "source": "", "status": "NO_GUIDE_HIT", "note": "",
        }]
        rows, _, exact_added = iptv_org_augment.apply_iptv_org_matches(
            [("CCTV6.cn@HD", "CCTV6", "China", "CN")],
            rows,
            {"cctv6": {"CCTV6.in@HD"}},
            {"CCTV6.in@HD"},
        )
        self.assertEqual(exact_added, 0)
        self.assertEqual(rows[0]["epg_id"], "")

    def test_iptv_org_never_fuzzy_maps_domestic_bangladesh_identity(self):
        rows = [{
            "group": "Bangladesh", "channel": "NTV", "tvg_id": "NTV.bd",
            "epg_id": "", "source": "", "status": "NO_GUIDE_HIT", "note": "",
        }]
        rows, _, exact_added = iptv_org_augment.apply_iptv_org_matches(
            [("NTV.bd", "NTV", "Bangladesh", "BD")],
            rows,
            {"ntv": {"NTV.in@HD"}},
            {"NTV.in@HD"},
        )
        self.assertEqual(exact_added, 0)
        self.assertEqual(rows[0]["epg_id"], "")


if __name__ == "__main__":
    unittest.main()
