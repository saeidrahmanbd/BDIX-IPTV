import importlib, sys, unittest
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import ast, types, unicodedata

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"


def load_policy_only(name):
    """Load just the language-policy definitions (the gate script runs on import)."""
    tree = ast.parse((SCRIPTS / f"{name}.py").read_text(encoding="utf-8"))
    keep = [n for n in tree.body if (
        isinstance(n, ast.FunctionDef) and n.name in ("is_english_text_element", "_script_allowed")
    ) or (isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") in (
        "ALLOWED_LANGS", "ALLOWED_LANG_PREFIXES", "ALLOWED_SCRIPTS", "XML_LANG"))]
    mod = types.ModuleType(name)
    mod.unicodedata = unicodedata
    exec(compile(ast.Module(keep, []), name, "exec"), mod.__dict__)
    return mod


MODULES = [load_policy_only(n) for n in ("epg_coverage", "generate_epg", "epg_publish_gate")]
XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"


def el(text, lang=None):
    e = ET.Element("title")
    e.text = text
    if lang:
        e.set(XML_LANG, lang)
    return e


CASES = [
    # (text, lang, expected)
    ("Evening News", None, True),
    ("Evening News", "en", True),
    ("Evening News", "en-GB", True),
    ("সন্ধ্যার খবর", "bn", True),
    ("সন্ধ্যার খবর", None, True),
    ("সন্ধ্যার খবর", "bn-BD", True),
    ("Kusum - কুসুম", "en", True),
    ("Kusum", "bn", True),
    ("Kusum", "zh", False),      # wrong/unsupported tag is still rejected
    ("Kusum", "hi", False),
    ("कुसुम", None, False),       # Devanagari
    ("कुसुम", "hi", False),
    ("خبر", None, False),         # Arabic script
    ("Новости", None, False),     # Cyrillic
    ("新闻", None, False),         # Han
    ("", "fr", True),             # empty text is not judged
]


class LanguagePolicyTests(unittest.TestCase):
    def test_policy_matches_in_every_module(self):
        for mod in MODULES:
            for text, lang, expected in CASES:
                with self.subTest(module=mod.__name__, text=text, lang=lang):
                    self.assertEqual(mod.is_english_text_element(el(text, lang)), expected)

    def test_constants_identical(self):
        ref = MODULES[0]
        for mod in MODULES[1:]:
            self.assertEqual(mod.ALLOWED_LANGS, ref.ALLOWED_LANGS)
            self.assertEqual(mod.ALLOWED_LANG_PREFIXES, ref.ALLOWED_LANG_PREFIXES)
            self.assertEqual(mod.ALLOWED_SCRIPTS, ref.ALLOWED_SCRIPTS)


if __name__ == "__main__":
    unittest.main()
