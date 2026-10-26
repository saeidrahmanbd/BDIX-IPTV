import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import generate_epg


def rows(*titles):
    return [{"title": t} for t in titles]


class FillerTitleTests(unittest.TestCase):
    def test_no_data_placeholders_score_zero(self):
        for title in ("No Data", "no information", "N/A", "None", "No Schedule Available"):
            with self.subTest(title=title):
                self.assertEqual(generate_epg.title_score(title), 0)

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


if __name__ == "__main__":
    unittest.main()
