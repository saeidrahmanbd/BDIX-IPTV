import sys
import unittest
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import generate_epg
import epg_coverage


def rows(*titles):
    return [{"title": t} for t in titles]


class FillerTitleTests(unittest.TestCase):
    def test_no_data_placeholders_score_zero(self):
        for title in ("No Data", "no information", "N/A", "None", "No Schedule Available"):
            with self.subTest(title=title):
                self.assertEqual(generate_epg.title_score(title), 0)

    def test_blank_slot_labels_are_placeholders(self):
        for title in ("Program @ 5:00 AM", "programme @ 11:30 PM", "Show @ 9:00 PM"):
            with self.subTest(title=title):
                self.assertEqual(generate_epg.title_score(title), 0)
        # Real titles that merely start with the same word are untouched.
        self.assertGreater(generate_epg.title_score("Programming Hour"), 0)
        self.assertGreater(generate_epg.title_score("Show Me the Money"), 0)

        candidates = {"ch": rows("Program @ 5:00 AM", "Ayur Shakthi", "Program @ 6:00 AM")}
        self.assertEqual(generate_epg.filter_generic_candidates(candidates), 2)
        self.assertEqual([r["title"] for r in candidates["ch"]], ["Ayur Shakthi"])

    def test_placeholder_only_channel_is_dropped_entirely(self):
        candidates = {"filler": rows("No Data", "No Data"), "real": rows("Evening News")}
        removed = generate_epg.filter_generic_candidates(candidates)
        self.assertEqual(removed, 2)
        self.assertEqual(candidates["filler"], [])
        self.assertEqual([r["title"] for r in candidates["real"]], ["Evening News"])

    def test_generic_only_channel_is_still_retained(self):
        # Existing behaviour: generic labels other than Movie/Movies are kept
        # when a channel has nothing better.
        candidates = {"live_only": rows("Live TV", "Live TV")}
        removed = generate_epg.filter_generic_candidates(candidates)
        self.assertEqual(removed, 0)
        self.assertEqual(len(candidates["live_only"]), 2)

    def test_self_titled_rows_removed_when_channel_names_given(self):
        names = {"DhoomMusic.in@SD": "Dhoom Music Bangla"}
        candidates = {"DhoomMusic.in@SD": rows("Dhoom Music Bangla", "Dhoom Music Bangla")}
        removed = generate_epg.filter_generic_candidates(candidates, names)
        self.assertEqual(removed, 2)
        self.assertEqual(candidates["DhoomMusic.in@SD"], [])

    def test_real_programme_sharing_the_channel_name_is_kept(self):
        # BBC News legitimately airs a bulletin called "BBC News"; a varied
        # schedule is not name-filled, so nothing is removed.
        names = {"BBCNews.uk": "BBC News"}
        candidates = {"BBCNews.uk": rows("Newsday", "Business Today", "BBC News", "BBC Sport")}
        removed = generate_epg.filter_generic_candidates(candidates, names)
        self.assertEqual(removed, 0)
        self.assertEqual(len(candidates["BBCNews.uk"]), 4)

    def test_name_filler_threshold_is_share_based(self):
        names = {"A.in": "Alpha TV", "B.in": "Beta TV"}
        candidates = {
            "A.in": rows(*["Alpha TV"] * 4, "Real Show"),   # 80% -> name-filled
            "B.in": rows(*["Beta TV"] * 3, "Real Show", "Other"),  # 60% -> kept
        }
        removed = generate_epg.filter_generic_candidates(candidates, names)
        self.assertEqual(removed, 4)
        self.assertEqual([r["title"] for r in candidates["A.in"]], ["Real Show"])
        self.assertEqual(len(candidates["B.in"]), 5)

    def test_quality_tag_and_punctuation_ignored_when_matching_channel_name(self):
        names = {"7XMusic.in@SD": "7x music (360p)"}
        candidates = {"7XMusic.in@SD": rows("7X Music")}
        self.assertEqual(generate_epg.filter_generic_candidates(candidates, names), 1)

    def test_single_show_channels_keep_name_titles(self):
        names = {"Mythbusters.us": "Mythbusters"}
        candidates = {"Mythbusters.us": rows("Mythbusters", "Mythbusters")}
        removed = generate_epg.filter_generic_candidates(candidates, names)
        self.assertEqual(removed, 0)
        self.assertEqual(len(candidates["Mythbusters.us"]), 2)

    def test_self_title_filter_is_off_without_channel_names(self):
        candidates = {"X.in": rows("Some Channel")}
        self.assertEqual(generate_epg.filter_generic_candidates(candidates), 0)

    def test_name_filler_rows_do_not_make_a_channel_count_as_named(self):
        # Name-filled rows are not real titles, so a generic label alongside
        # them is retained (existing generic-only behaviour) rather than being
        # dropped as redundant next to a "named" programme.
        names = {"Ch.in": "My Channel"}
        candidates = {"Ch.in": rows(*["My Channel"] * 4, "Live TV")}
        removed = generate_epg.filter_generic_candidates(candidates, names)
        self.assertEqual(removed, 4)
        self.assertEqual([r["title"] for r in candidates["Ch.in"]], ["Live TV"])


class SlotLabelAndSpellingVariantTests(unittest.TestCase):
    def test_scheduling_slot_labels_are_placeholders(self):
        for title in ("Slot", "Commercial Slot", "FILLER", "Filler", "Brak zaplanowanych emisji", "Sin programación"):
            with self.subTest(title=title):
                self.assertEqual(generate_epg.title_score(title), 0)
                self.assertTrue(epg_coverage.is_filler_title(title))
        # Real titles that only contain the same words stay valid.
        for title in ("Slot Machine Hour", "The Filler Episode", "Commercial Break Special"):
            with self.subTest(title=title):
                self.assertGreater(generate_epg.title_score(title), 0)

    def test_slot_rows_are_dropped_even_without_other_titles(self):
        candidates = {"Raj.in": rows("Slot", "Commercial Slot", "Filler", "Raj News")}
        removed = generate_epg.filter_generic_candidates(candidates)
        self.assertEqual(removed, 3)
        self.assertEqual([r["title"] for r in candidates["Raj.in"]], ["Raj News"])

    def test_teleshopping_is_a_real_programme_and_is_kept(self):
        candidates = {"Ch.in": rows("Teleshopping", "Paid Programming", "Evening News")}
        self.assertEqual(generate_epg.filter_generic_candidates(candidates), 0)

    def test_spelling_variant_of_channel_name_is_name_filler(self):
        # Playlist says "Amar Bangla"; the feed titles every row "Amar Bangla TV".
        names = {"AamarBangla.in": "Amar Bangla"}
        candidates = {"AamarBangla.in": rows(*["Amar Bangla TV"] * 6)}
        self.assertEqual(generate_epg.filter_generic_candidates(candidates, names), 6)
        self.assertEqual(candidates["AamarBangla.in"], [])

    def test_identity_stem_catches_filler_when_playlist_names_disagree(self):
        # The same tvg-id carries different names across playlists, so the stored
        # name may not match the feed; the tvg-id's own name part still does.
        names = {"ZeeBanglaSonar.in@SD": "Zee Bangla Cinema"}
        candidates = {"ZeeBanglaSonar.in@SD": rows(*["Zee Bangla Sonar"] * 7, "Sonar Special")}
        self.assertEqual(generate_epg.filter_generic_candidates(candidates, names), 7)
        self.assertEqual([r["title"] for r in candidates["ZeeBanglaSonar.in@SD"]], ["Sonar Special"])

    def test_similar_but_different_programmes_are_not_name_filler(self):
        self.assertFalse(generate_epg.repeats_channel_name("BBC Sport", "BBC News", "BBCNews.uk"))
        self.assertFalse(generate_epg.repeats_channel_name("Newsday", "BBC News", "BBCNews.uk"))
        self.assertFalse(generate_epg.repeats_channel_name("Sony Pal Special", "Sony Pal", "SonyPal.in@SD"))

    def test_varied_schedule_with_one_similar_title_is_untouched(self):
        names = {"AamarBangla.in": "Amar Bangla"}
        candidates = {"AamarBangla.in": rows("Amar Bangla TV", "Evening News", "Drama Hour", "Music Time", "Talk Show")}
        self.assertEqual(generate_epg.filter_generic_candidates(candidates, names), 0)

    def test_single_show_channels_are_still_exempt(self):
        names = {"AxMen.us": "Ax Men"}
        candidates = {"AxMen.us": rows(*["Ax Men"] * 5)}
        self.assertEqual(generate_epg.filter_generic_candidates(candidates, names), 0)


class SourceOffsetPatternTests(unittest.TestCase):
    def test_feed_with_repeated_identical_offsets_is_flagged(self):
        events = [("Feed A", f"Ch{i}.in", timedelta(hours=-5.5)) for i in range(5)]
        events.append(("Feed B", "Other.in", timedelta(hours=-24)))
        lines = generate_epg.source_offset_patterns(events)
        self.assertEqual(len(lines), 1)
        self.assertIn("Feed A", lines[0])
        self.assertIn("-5.5", lines[0])
        self.assertIn("5 channels", lines[0])

    def test_same_channel_repeated_does_not_count_as_a_pattern(self):
        events = [("Feed A", "Ch.in", timedelta(hours=-5.5))] * 8
        self.assertEqual(generate_epg.source_offset_patterns(events), [])

    def test_mixed_offsets_below_threshold_are_not_flagged(self):
        events = [("Feed A", f"Ch{i}.in", timedelta(hours=-5.5 if i % 2 else -24)) for i in range(8)]
        self.assertEqual(generate_epg.source_offset_patterns(events), [])


class CoverageFillerTests(unittest.TestCase):
    def test_coverage_report_ignores_filler_titles(self):
        for title in ("No Data", "Movie", "movies", "Program @ 5:00 AM"):
            with self.subTest(title=title):
                self.assertTrue(epg_coverage.is_filler_title(title))
        for title in ("Evening News", "Live TV", "Programming Hour", "संध्या समाचार"):
            with self.subTest(title=title):
                self.assertFalse(epg_coverage.is_filler_title(title))


if __name__ == "__main__":
    unittest.main()
