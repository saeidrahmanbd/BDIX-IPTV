import ast, csv, io, os, re, tempfile, unittest, sys
from datetime import datetime, timezone, timedelta
from unittest.mock import patch
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import generate_epg
import epg_coverage
import official_epg_sources

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
        ]
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

    def test_rtv_schedule_tries_apex_https_then_www_without_disabling_tls(self):
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
            side_effect=[OSError("certificate chain"), io.BytesIO(html.encode("utf-8"))],
        ) as urlopen:
            programmes = official_epg_sources.fetch_rtv_programmes(
                datetime(2026, 10, 29, tzinfo=timezone.utc)
            )
        self.assertTrue(programmes)
        self.assertEqual(
            urlopen.call_args_list[0].args[0].full_url,
            "https://rtvbd.tv/schedule.php",
        )
        self.assertEqual(
            urlopen.call_args_list[1].args[0].full_url,
            "https://www.rtvbd.tv/schedule.php",
        )

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
            ]
            with (
                patch.object(generate_epg, "PLAYLISTS", [main_playlist, international_playlist]),
                patch.object(generate_epg, "MAPPING", mapping),
            ):
                countries = generate_epg.active_playlist_country_codes()
                selected = generate_epg.sources_with_mapped_channels(configured)

        self.assertEqual(countries, {"IN", "PA", "SG", "CN", "GB"})
        self.assertEqual(
            selected,
            [
                "https://iptv-epg.org/files/epg-in.xml.gz",
                "https://free-epg.de/api/epg/pa.xml.gz",
                "https://iptv-epg.org/files/epg-sg.xml.gz",
                "https://free-epg.de/api/epg/cn.xml.gz",
                "https://iptv-epg.org/files/epg-gb.xml.gz",
            ],
        )

    def test_source_country_codes_recognize_public_feed_families(self):
        self.assertEqual(
            generate_epg.source_country_codes("https://iptv-epg.org/files/epg-at.xml.gz"),
            {"AT"},
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
        self.assertIn("https://www.rtvbd.tv/schedule.php", coverage_sources)
        self.assertIn("https://www.rtvbd.tv/schedule.php", generator_sources)
        self.assertIn(official_epg_sources.BTV_SOURCE, coverage_sources)
        self.assertIn(official_epg_sources.BTV_SOURCE, generator_sources)
        self.assertEqual(literal(COV, "EPG_LOCKS")["BTVNational.bd"], ["BTVNational.bd"])

    def test_epg_source_list_has_no_hardcoded_provider_ban(self):
        coverage_sources = literal(COV, "SOURCES")
        generator_sources = literal(GEN, "SOURCES")
        self.assertEqual(len(coverage_sources), len(generator_sources))
        self.assertEqual(coverage_sources, generator_sources)
        self.assertNotIn("EPGPW_SOURCE_IDS", COV + GEN)
        self.assertNotIn("normalize_epgpw_source", COV + GEN)

    def test_new_aliases(self):
        al = literal(COV, "EPG_ALIASES")
        self.assertEqual(al["Hungama.in@SD"], ["143150"])
        self.assertEqual(al["ZBMusic.in@HD"], ["jtv3319"])
        self.assertEqual(al["DeenTV.uk"], ["1235", "DeenTV.uk"])
        self.assertNotIn("ZBBhakti.in@HD", al)

    def test_m3u4u_exact_ids_are_enabled_without_weakening_bangladesh_matching(self):
        locks = literal(COV, "EPG_LOCKS")
        self.assertEqual(locks["ATNBanglaUK.uk"], ["6753", "ATNBanglaUK.uk"])
        self.assertEqual(locks["IqraBangla.uk"], ["3914", "IqraBangla.uk"])
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

    def test_alias_ids_exist_in_playlist(self):
        pl = (ROOT / "IPTV-Playlist.m3u").read_text(encoding="utf-8-sig")
        for tid in ("Hungama.in@SD", "ZBMusic.in@HD"):
            self.assertIn(f'tvg-id="{tid}"', pl)
        self.assertNotIn('tvg-id="ZBBhakti.in@HD"', pl)

    def test_epg_refresh_follows_successful_playlist_writer_workflows(self):
        workflow = (ROOT / ".github" / "workflows" / "epg-refresh.yml").read_text(encoding="utf-8")
        self.assertIn("workflow_run:", workflow)
        for name in (
            "IPTV Playlist Update",
            "IPTV New Channel Discovery",
            "International Channel Discovery",
            "Playlist Logo Repair and Localization",
        ):
            self.assertIn(f'"{name}"', workflow)
        self.assertIn("github.event.workflow_run.conclusion == 'success'", workflow)
        self.assertIn("# 09:00 Asia/Dhaka (UTC+6)", workflow)


    def test_epg_refresh_does_not_cancel_active_generation(self):
        workflow = (ROOT / ".github" / "workflows" / "epg-refresh.yml").read_text(encoding="utf-8")
        self.assertIn("cancel-in-progress: false", workflow)
        self.assertIn("Skip superseded queued EPG refresh", workflow)


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
        self.assertIn("And.Pictures.HD.in", al["Picture.in"])

    def test_new_alias_ids_exist_in_playlist(self):
        pl = (ROOT / "IPTV-Playlist.m3u").read_text(encoding="utf-8-sig")
        for tid in ("AmarBanglaDigital.in", "EpicBhojpuriDigital.in", "Picture.in"):
            self.assertIn(f'tvg-id="{tid}"', pl)


if __name__ == "__main__":
    unittest.main()
