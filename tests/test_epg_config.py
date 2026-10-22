import ast, re, unittest, sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import epg_coverage

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

    def test_generator_covers_all_three_published_playlists(self):
        generator_paths = literal(GEN, "PLAYLISTS")
        self.assertEqual([p.name for p in generator_paths], ["IPTV-Playlist.m3u", "BDIX-Playlist.m3u", "International-Playlist.m3u"])

    def test_rtv_not_configured(self):
        self.assertFalse([u for u in literal(COV, "SOURCES") if "rtvbd.tv" in u])

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
    def test_epgpw_sources_and_locks_are_explicit_and_synchronized(self):
        coverage_sources = literal(COV, "SOURCES")
        generator_sources = literal(GEN, "SOURCES")
        coverage_ids = literal(COV, "EPGPW_SOURCE_IDS")
        generator_ids = literal(GEN, "EPGPW_SOURCE_IDS")
        self.assertEqual(coverage_ids, generator_ids)
        self.assertTrue(set(coverage_ids).issubset(set(coverage_sources)))
        locks = literal(COV, "EPG_LOCKS")
        self.assertEqual(locks["NTVEurope.bd"], ["epgpw:9374"])
        self.assertEqual(locks["ChannelS.uk@679aa9"], ["epgpw:12504"])

    def test_epgpw_normalization_rewrites_only_the_explicit_feed_channel(self):
        xml = b'<tv><channel id="source-id"><display-name>NTV</display-name></channel><programme channel="source-id" start="20261021070000 +0000" stop="20261021073000 +0000"><title>NTV Europe News</title></programme></tv>'
        url = "https://epg.pw/api/epg.xml?channel_id=9374"
        normalized = ET.fromstring(epg_coverage.normalize_epgpw_source(url, xml))
        self.assertEqual(normalized.find("channel").get("id"), "epgpw:9374")
        self.assertEqual(normalized.find("programme").get("channel"), "epgpw:9374")
        untouched = epg_coverage.normalize_epgpw_source("https://example.invalid/guide.xml", xml)
        self.assertEqual(untouched, xml)


if __name__ == "__main__":
    unittest.main()
