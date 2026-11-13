import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.epg.alias_suggestions import suggest_aliases, normalize_name

def playlist(rows):
    return "#EXTM3U\n" + "".join(f'#EXTINF:-1 tvg-id="{i}" tvg-name="{n}" group-title="Bangladesh",{n}\nhttps://x.example/{i}\n' for i,n in rows)

def guide(rows):
    channels="".join(f'<channel id="{i}"><display-name>{n}</display-name></channel>' for i,n in rows)
    programmes="".join(f'<programme channel="{i}" start="20261113090000" stop="20261113100000"><title>Test</title></programme>' for i,n in rows)
    return f"<tv>{channels}{programmes}</tv>"

class EpgAliasSuggestionTests(unittest.TestCase):
    def test_name_normalization_is_case_and_punctuation_insensitive(self):
        self.assertEqual(normalize_name("Star Jalsha HD"),"starjalshahd")

    def test_normalized_id_suggestion_requires_manual_review(self):
        result=suggest_aliases(playlist([("Star.Jalsha.in","Star Jalsha")]),guide([("starjalshain","Star Jalsha")]))
        self.assertEqual(result["normalized_id_suggestions"],1)
        self.assertEqual(result["suggestions"][0]["status"],"manual_review_required")
        self.assertFalse(result["auto_applied"])

    def test_exact_display_name_suggestion(self):
        result=suggest_aliases(playlist([("missing.id","Star Jalsha")]),guide([("epg.id","Star Jalsha")]))
        self.assertEqual(result["suggestion_count"],1)
        self.assertEqual(result["suggestions"][0]["match_type"],"exact_name")
        self.assertEqual(result["suggestions"][0]["confidence"],1.0)

    def test_fuzzy_name_suggestion_is_manual_only(self):
        result=suggest_aliases(playlist([("missing.id","Star Jalsha HD")]),guide([("epg.id","Star Jalsha")]))
        self.assertTrue(result["suggestions"])
        self.assertEqual(result["suggestions"][0]["status"],"manual_review_required")

    def test_ambiguous_duplicate_names_are_not_suggested(self):
        result=suggest_aliases(playlist([("missing.id","Star Jalsha")]),guide([("epg.a","Star Jalsha"),("epg.b","Star Jalsha")]))
        self.assertEqual(result["suggestion_count"],0)
        self.assertEqual(result["ambiguous_count"],1)

    def test_unmatched_channel_is_reported_without_alias(self):
        result=suggest_aliases(playlist([("missing.id","Unrelated Channel")]),guide([("epg.id","Other Name")]))
        self.assertEqual(result["unmatched_count"],1)
        self.assertEqual(result["suggestion_count"],0)

if __name__=="__main__":
    unittest.main()
