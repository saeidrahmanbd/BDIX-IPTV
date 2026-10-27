import ast, re, unittest, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

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

    def test_generator_parses_the_payload_for_each_fetched_source(self):
        # Regression: using an undefined/stale local variable made every XMLTV
        # feed fail after retrieval; only the separate HUM TV parser survived.
        self.assertIn(
            'data = source_payloads[src]\n            for _, elem in ET.iterparse(io.BytesIO(data), events=("end",)):',
            GEN,
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

    def test_restricted_epg_pw_sources_are_removed(self):
        coverage_sources = literal(COV, "SOURCES")
        generator_sources = literal(GEN, "SOURCES")
        self.assertFalse(any("epg.pw/" in u for u in coverage_sources))
        self.assertFalse(any("epg.pw/" in u for u in generator_sources))
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
    def test_legacy_epgpw_mappings_are_dropped(self):
        source = COV[COV.index("def retained_mapping"):COV.index("def main():")]
        namespace = {}
        exec(source, namespace)
        retain = namespace["retained_mapping"]
        self.assertEqual(retain(False, "epgpw:9374", ["epgpw:9374"]), "")
        self.assertEqual(retain(False, "epgpw:9374 | LegitChannel.uk", ["LegitChannel.uk"]), "LegitChannel.uk")


if __name__ == "__main__":
    unittest.main()
