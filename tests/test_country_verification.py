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

    def test_queue_errors(self):
        good = ({"tvg-id": "A.in", "tvg-country": "IN", "group-title": "New Channels"}, "A", "https://x/a.m3u8")
        unnormalized = ({"tvg-id": "B.bd", "group-title": "New Backup"}, "B", "https://x/b.m3u8")
        foreign = ({"tvg-id": "C.us", "tvg-country": "US", "group-title": "New Channels"}, "C", "https://x/c.m3u8")
        errs = cv.queue_errors([good, unnormalized, foreign], ref())
        self.assertEqual(len(errs), 2)
        self.assertFalse(any(e.startswith("A:") for e in errs))


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

    def test_evaluate_normalizes_country_and_rejects_foreign(self):
        url = "https://cdn.example.com/live/index.m3u8"
        a, why = disc.evaluate("India", {"tvg-id": "Star Utsav.in@SD"}, "Star Utsav", url)
        self.assertEqual(why, "")
        self.assertEqual(a["tvg-country"], "IN")
        line = disc.extinf(a, "Star Utsav", "New Channels", "India")
        self.assertIn('tvg-country="IN"', line)
        self.assertIsNone(disc.evaluate("India", {"tvg-id": "Star Utsav.us"}, "Star Utsav", url)[0])
        self.assertIsNone(disc.evaluate("India", {}, "Star Utsav", url)[0])
        self.assertIsNone(disc.evaluate("Bangladesh", {"tvg-id": "X.in"}, "X", url)[0])
        # Indian News is prohibited by repository policy, independent of country verification.
        self.assertIsNone(disc.evaluate("India", {"tvg-id": "Latest News.in@SD"}, "Latest News", url)[0])

    def test_extinf_refuses_unverified_country(self):
        self.assertIsNone(disc.extinf({"tvg-id": "X.in"}, "X", "New Channels", "India"))


if __name__ == "__main__":
    unittest.main()
