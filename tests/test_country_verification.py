import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import country_verification as cv
import discover_bd_in_new_queues as disc


def ref(*rows):
    return cv.build_reference(rows)


class CountryVerificationTests(unittest.TestCase):
    def test_valid_id_is_verified(self):
        v = cv.verify_country({"tvg-id": "Somoy.bd@SD"}, "Somoy TV", None, "BD")
        self.assertEqual((v.country, v.basis), ("BD", "id"))
        self.assertEqual(cv.verify_country({"tvg-id": "Zee.in"}, "Zee", None, "IN").country, "IN")

    def test_ten_tv_prime_custom_id_is_verified_as_indian(self):
        a = {
            "tvg-id": "custom.tentvprime",
            "channel-id": "custom.tentvprime",
            "tvg-country": "IN",
            "tvg-language": "ben",
        }
        verdict = cv.verify_country(a, "Ten TV Prime")
        self.assertEqual((verdict.country, verdict.basis), ("IN", "curated-exact-id-override"))
        self.assertFalse(cv.verify_country({**a, "tvg-country": "BD"}, "Ten TV Prime").ok)
        self.assertFalse(cv.verify_country(a, "Ten TV Prime", feed_country="BD").ok)
        self.assertFalse(cv.verify_country({**a, "tvg-id": "custom.other", "channel-id": "custom.other"}, "Ten TV Prime").ok)

    def test_indian_bangla_primary_playlist_classification(self):
        root = Path(__file__).resolve().parent.parent
        expected = {
            "JTV Bangla": ("JTVBangla.in@SD", "IN", "Indian Bangla"),
            "Ten TV Prime": ("custom.tentvprime", "IN", "Indian Bangla"),
        }
        for channel, (channel_id, country, group) in expected.items():
            matches = []
            for line in (root / "IPTV-Playlist.m3u").read_text(encoding="utf-8").splitlines():
                if line.startswith("#EXTINF:") and f'tvg-name="{channel}"' in line:
                    matches.append(line)
            self.assertEqual(len(matches), 1, channel)
            self.assertIn(f'tvg-id="{channel_id}"', matches[0])
            self.assertIn(f'channel-id="{channel_id}"', matches[0])
            self.assertIn(f'tvg-country="{country}"', matches[0])
            self.assertIn(f'group-title="{group}"', matches[0])

    def test_id_conflicts_are_held(self):
        self.assertFalse(cv.verify_country({"tvg-id": "X.in"}, "X", None, "BD").ok)          # feed mismatch
        self.assertFalse(cv.verify_country({"tvg-id": "X.us"}, "X", None, "IN").ok)          # foreign id
        self.assertFalse(cv.verify_country({"tvg-id": "X.in", "channel-id": "X.bd"}, "X").ok)
        self.assertFalse(cv.verify_country({"tvg-id": "X.in", "tvg-country": "BD"}, "X").ok)
        self.assertFalse(cv.verify_country({"tvg-id": "X.in", "tvg-country": "US"}, "X").ok)

    def test_missing_id_needs_repository_evidence(self):
        self.assertFalse(cv.verify_country({}, "Mystery TV", None, "IN").ok)  # feed alone is not enough
        r = ref(({"tvg-id": "Star Jalsha.in@SD", "group-title": "Indian Bangla"}, "Star Jalsha"))
        v = cv.verify_country({"tvg-id": "bad id!"}, "Star Jalsha HD", r, "IN")
        self.assertEqual((v.country, v.tvg_id, v.basis), ("IN", "Star Jalsha.in@SD", "repository-mapping"))
        self.assertFalse(cv.verify_country({}, "Star Jalsha", r, "BD").ok)  # feed conflict

    def test_international_look_alike_is_never_accepted(self):
        r = ref(({"tvg-id": "Star Jalsha.in@SD", "group-title": "Indian Bangla"}, "Star Jalsha"),
                ({"tvg-id": "Star Jalsha.us", "group-title": "International"}, "Star Jalsha"))
        self.assertFalse(cv.verify_country({}, "Star Jalsha", r, "IN").ok)
        r2 = ref(({"tvg-id": "Foo.us@SD", "group-title": "International"}, "Foo TV"))
        self.assertFalse(cv.verify_country({}, "Foo TV", r2, "IN").ok)

    def test_ambiguous_bd_in_mapping_is_held(self):
        r = ref(({"tvg-id": "A.bd"}, "Alpha"), ({"tvg-id": "A.in"}, "Alpha"))
        self.assertFalse(cv.verify_country({}, "Alpha", r).ok)

    def test_queue_rows_are_not_evidence(self):
        r = ref(({"tvg-id": "Q.in", "group-title": "New Channels"}, "Queue TV"))
        self.assertFalse(cv.verify_country({}, "Queue TV", r).ok)

    def test_country_metadata_warnings_do_not_block_manual_review_queues(self):
        good = ({"tvg-id": "A.in", "tvg-country": "IN", "group-title": "New Channels"}, "A", "https://x/a.m3u8")
        unnormalized = ({"tvg-id": "B.bd", "group-title": "New Backup"}, "B", "https://x/b.m3u8")
        foreign = ({"tvg-id": "C.us", "tvg-country": "US", "group-title": "New Channels"}, "C", "https://x/c.m3u8")
        errs = cv.queue_errors([good, unnormalized, foreign], ref())
        warnings = cv.queue_metadata_warnings([good, unnormalized, foreign], ref())
        self.assertEqual(errs, [])
        self.assertEqual(len(warnings), 2)


class DiscoveryTests(unittest.TestCase):
    def test_whole_word_bad_words(self):
        self.assertIsNone(disc.BAD_RE.search("latest news"))
        self.assertIsNone(disc.BAD_RE.search("contest tv"))
        self.assertIsNone(disc.BAD_RE.search("protest.in"))
        self.assertIsNotNone(disc.BAD_RE.search("test channel"))
        self.assertIsNotNone(disc.BAD_RE.search("news (vod)"))
        self.assertIsNotNone(disc.BAD_RE.search("demo_feed"))

    def test_norm_preserves_combining_marks(self):
        self.assertNotEqual(disc.norm("কি"), disc.norm("কু"))
        self.assertNotEqual(disc.norm("कि"), disc.norm("कु"))
        self.assertTrue(disc.norm("সংবাদ"))
        self.assertEqual(disc.norm("Somoy TV HD"), disc.norm("somoy_tv (SD)"))

    def test_country_metadata_is_preserved_without_verification_or_rewriting(self):
        url = "https://cdn.example.com/live/index.m3u8"
        cases = [
            ({"tvg-id": "CartoonNetwork.us", "channel-id": "CartoonNetwork.us",
              "tvg-country": "US"}, "Cartoon Network"),
            ({"tvg-id": "ColorsCineplex.uk", "channel-id": "ColorsCineplex.uk",
              "tvg-country": "GB"}, "Colors Cineplex [UK]"),
        ]
        for attrs, name in cases:
            with self.subTest(name=name):
                candidate, reason = disc.evaluate("India", attrs, name, url)
                self.assertEqual(reason, "")
                self.assertEqual(candidate, attrs)
        self.assertEqual(disc.evaluate(
            "Bangladesh", cases[0][0], cases[0][1], url)[0], cases[0][0])

    def test_evaluate_retains_country_and_identity_metadata_for_manual_review(self):
        url = "https://cdn.example.com/live/index.m3u8"
        original = {"tvg-id": "Star Utsav.in@SD"}
        candidate, why = disc.evaluate("India", original, "Star Utsav", url)
        self.assertEqual(why, "")
        self.assertEqual(candidate, original)
        self.assertNotIn("tvg-country", candidate)
        line = disc.extinf(candidate, "Star Utsav", "New Channels", "India")
        self.assertNotIn("tvg-country=", line)
        foreign, why = disc.evaluate("India", {"tvg-id": "Star Utsav.us"}, "Star Utsav", url)
        self.assertEqual(why, "")
        self.assertEqual(foreign["tvg-id"], "Star Utsav.us")
        no_ids, why = disc.evaluate("India", {}, "Unmapped Channel", url)
        self.assertEqual(why, "")
        self.assertEqual(no_ids, {})
        mismatch, why = disc.evaluate("Bangladesh", {"tvg-id": "X.in"}, "X", url)
        self.assertEqual(why, "")
        self.assertEqual(mismatch["tvg-id"], "X.in")
        self.assertIsNone(disc.evaluate("India", {"tvg-id": "Latest News.us"}, "Latest News", url)[0])

    def test_extinf_accepts_missing_identity_fields(self):
        line = disc.extinf({}, "Unidentified Candidate", "New Channels", "India")
        self.assertIn('tvg-name="Unidentified Candidate"', line)
        self.assertIn('group-title="New Channels"', line)


if __name__ == "__main__":
    unittest.main()
