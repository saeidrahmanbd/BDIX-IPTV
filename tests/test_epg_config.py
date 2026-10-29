import ast, csv, io, os, re, tempfile, unittest, sys
from datetime import datetime, timezone
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
        ]
        for source in expected:
            self.assertIn(source, literal(COV, "SOURCES"))
            self.assertIn(source, literal(GEN, "SOURCES"))

    def test_private_m3u4u_source_is_selected_for_discovery_without_mapping(self):
        with tempfile.TemporaryDirectory() as tmp:
            mapping = Path(tmp) / "mapping.csv"
            mapping.write_text("group,channel,tvg_id,epg_id,source,status,note\n", encoding="utf-8")
            private_url = "https://m3u4u.com/epg/example-private-feed.xml"
            with patch.object(generate_epg, "MAPPING", mapping), patch.dict(os.environ, {"M3U4U_XMLTV_URL": private_url}):
                selected = generate_epg.sources_with_mapped_channels([private_url, "https://example.test/unused.xml"])
        self.assertEqual(selected, [private_url])

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
                generate_epg.HUM_TV_SOURCE, generate_epg.RTV_SOURCE,
            ]
            with patch.object(generate_epg, "MAPPING", mapping):
                selected = generate_epg.sources_with_mapped_channels(configured)
        self.assertEqual(
            selected,
            ["feed-a", "feed-b", "file:///tmp/iptv-org-guide.xml",
             generate_epg.HUM_TV_SOURCE, generate_epg.RTV_SOURCE],
        )

    def test_generator_covers_all_three_core_playlists(self):
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
        self.assertEqual(paths, ["IPTV-Playlist.m3u", "BDIX-Playlist.m3u", "International-Playlist.m3u"])

    def test_rtv_official_schedule_source_is_configured(self):
        coverage_sources = literal(COV, "SOURCES")
        generator_sources = literal(GEN, "SOURCES")
        self.assertIn("https://www.rtvbd.tv/schedule.php", coverage_sources)
        self.assertIn("https://www.rtvbd.tv/schedule.php", generator_sources)

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
        self.assertNotIn("ZBBhakti.in@HD", al)

    def test_no_bangladesh_alias_to_foreign_ids(self):
        for key, ids in literal(COV, "EPG_ALIASES").items():
            if re.search(r"\.bd(@|$)", key):
                self.assertTrue(all(i.endswith(".bd") or i == key for i in ids), key)

    def test_alias_ids_exist_in_playlist(self):
        pl = (ROOT / "IPTV-Playlist.m3u").read_text(encoding="utf-8-sig")
        for tid in ("Hungama.in@SD", "ZBMusic.in@HD"):
            self.assertIn(f'tvg-id="{tid}"', pl)
        self.assertNotIn('tvg-id="ZBBhakti.in@HD"', pl)


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
