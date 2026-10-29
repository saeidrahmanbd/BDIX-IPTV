"""migrate_external_logos_fixed.force_local must never write an empty tvg-logo attribute."""
import ast
import re
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / "scripts" / "migrate_external_logos_fixed.py"


def load_force_local():
    # The script executes network/playlist work at import time, so load only the helper.
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "force_local")
    namespace = {"re": re}
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(SOURCE), "exec"), namespace)
    return namespace["force_local"]


class ForceLocalTests(unittest.TestCase):
    def setUp(self):
        self.force_local = load_force_local()

    def test_unset_removes_existing_attribute(self):
        line = '#EXTINF:-1 tvg-id="A.in" tvg-logo="https://x/y.png" tvg-chno="3" group-title="Kids",A'
        out = self.force_local(line, "")
        self.assertNotIn("tvg-logo", out)
        self.assertEqual(out, '#EXTINF:-1 tvg-id="A.in" tvg-chno="3" group-title="Kids",A')

    def test_unset_without_attribute_is_a_noop(self):
        line = '#EXTINF:-1 tvg-id="A.in" group-title="Kids",A'
        self.assertEqual(self.force_local(line, ""), line)

    def test_replacement_still_sets_or_adds_logo(self):
        base = "https://raw.githubusercontent.com/o/r/main/logos/a.png"
        replaced = self.force_local('#EXTINF:-1 tvg-id="A.in" tvg-logo="old" group-title="Kids",A', base)
        self.assertIn(f'tvg-logo="{base}"', replaced)
        added = self.force_local('#EXTINF:-1 tvg-id="A.in" group-title="Kids",A', base)
        self.assertIn(f'tvg-logo="{base}"', added)
        self.assertTrue(added.endswith(",A"))


if __name__ == "__main__":
    unittest.main()
