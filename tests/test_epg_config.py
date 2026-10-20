import ast, re, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
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

    def test_rtv_not_configured(self):
        self.assertFalse([u for u in literal(COV, "SOURCES") if "rtvbd.tv" in u])

    def test_new_aliases(self):
        al = literal(COV, "EPG_ALIASES")
        self.assertEqual(al["Hungama.in@SD"], ["143150"])
        self.assertEqual(al["ZBMusic.in@HD"], ["jtv3319"])
        self.assertEqual(al["ZBBhakti.in@HD"], ["jtv3320"])

    def test_no_bangladesh_alias_to_foreign_ids(self):
        for key, ids in literal(COV, "EPG_ALIASES").items():
            if re.search(r"\.bd(@|$)", key):
                self.assertTrue(all(i.endswith(".bd") or i == key for i in ids), key)

    def test_alias_ids_exist_in_playlist(self):
        pl = (ROOT / "IPTV-Playlist.m3u").read_text(encoding="utf-8-sig")
        for tid in ("Hungama.in@SD", "ZBMusic.in@HD", "ZBBhakti.in@HD"):
            self.assertIn(f'tvg-id="{tid}"', pl)


if __name__ == "__main__":
    unittest.main()
