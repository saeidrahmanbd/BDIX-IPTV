import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import generate_epg
import epg_coverage

XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"


def el(text, lang=None):
    e = ET.Element("title")
    e.text = text
    if lang:
        e.set(XML_LANG, lang)
    return e


class LanguagePolicyTests(unittest.TestCase):
    def test_valid_languages_are_accepted(self):
        cases = [
            ("Evening News", None),
            ("Evening News", "en"),
            ("Evening News", "en-GB"),
            ("Noticias", "es"),
            ("সন্ধ্যার খবর", "bn"),
            ("संध्या समाचार", "hi"),
            ("செய்திகள்", "ta"),
            ("తెలుగు వార్తలు", "te"),
            ("خبر", "ar"),
            ("Новости", "ru"),
            ("新闻", "zh"),
        ]
        for text, lang in cases:
            with self.subTest(text=text, lang=lang):
                self.assertTrue(generate_epg.is_english_text_element(el(text, lang)))
                self.assertTrue(epg_coverage.is_english_text_element(el(text, lang)))

    def test_movie_catalogue_placeholders_are_not_named_programmes(self):
        self.assertEqual(generate_epg.title_score("Movies"), 0)
        self.assertEqual(generate_epg.title_score("Movie"), 0)

        candidates = {
            "movies_only": [{"title": "Movies"}, {"title": "Movies"}],
            "mixed": [
                {"title": "Movies"},
                {"title": "Live TV"},
                {"title": "Evening News"},
            ],
            "proper_title": [{"title": "Movie Night"}],
        }
        removed = generate_epg.filter_generic_candidates(candidates)

        self.assertEqual(removed, 4)
        self.assertEqual(candidates["movies_only"], [])
        self.assertEqual(
            [row["title"] for row in candidates["mixed"]],
            ["Evening News"],
        )
        self.assertEqual(
            [row["title"] for row in candidates["proper_title"]],
            ["Movie Night"],
        )

    def test_empty_text_is_allowed_by_text_policy(self):
        self.assertTrue(generate_epg.is_english_text_element(el("", "fr")))

    def test_language_priority(self):
        self.assertEqual(generate_epg.language_priority(el("Evening News", "en")), 3)
        self.assertEqual(generate_epg.language_priority(el("Evening News", "en-GB")), 3)
        self.assertEqual(generate_epg.language_priority(el("Noticias", "es")), 1)
        self.assertEqual(epg_coverage.language_priority(el("Noticias", "es")), 1)
        self.assertEqual(generate_epg.language_priority(el("সন্ধ্যার খবর", "bn")), 2)
        self.assertEqual(generate_epg.language_priority(el("संध्या समाचार", "hi")), 1)
        self.assertEqual(epg_coverage.language_priority(el("संध्या समाचार", "hi")), 1)
        self.assertEqual(generate_epg.language_priority(el("Evening News")), 3)
        self.assertEqual(generate_epg.language_priority(el("সন্ধ্যার খবর")), 2)

    def test_preferred_title_is_english_then_bengali(self):
        p = ET.Element("programme")
        bn = ET.SubElement(p, "title", {XML_LANG: "bn"})
        bn.text = "সন্ধ্যার খবর"
        hi = ET.SubElement(p, "title", {XML_LANG: "hi"})
        hi.text = "संध्या समाचार"
        en = ET.SubElement(p, "title", {XML_LANG: "en"})
        en.text = "Evening News"
        self.assertIs(generate_epg.preferred_title_element(p), en)

        p.remove(en)
        self.assertIs(generate_epg.preferred_title_element(p), bn)


if __name__ == "__main__":
    unittest.main()
