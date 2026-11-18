"""Regression tests for logo provenance classification (the The Movie Club +2 failure)."""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import logo_provenance as prov  # noqa: E402
import repair_playlist_logos as repair  # noqa: E402
from generate_logo_authenticity_manifest import provenance_for  # noqa: E402
from logo_test_support import (  # noqa: E402
    FALLBACK_NOTE, IPTV, SAMSUNG_URL, extinf, fallback_record, playlist, verified_record, write_png,
)

MOVIE_CLUB = "The Movie Club +2"
MOVIE_CLUB_ID = "TheMovieClub.in@Plus2"
FB_SVG = "logos/generated-fallback-the-movie-club-plus-2-c82c401f.svg"
FB_PNG = "logos/generated-fallback-the-movie-club-plus-2-c82c401f.png"
CANDIDATE = {
    "url": SAMSUNG_URL, "format": "PNG", "page": SAMSUNG_URL,
    "license": "IPTV-org public logo dataset",
    "license_url": "https://github.com/iptv-org/database",
}


def key(logo, playlist_name=IPTV, tvg_id=MOVIE_CLUB_ID, name=MOVIE_CLUB):
    return f"{playlist_name}|{tvg_id}|{name}|{logo}"


class RunRepairInTempTree:
    """Run the real repair main() offline against a one-channel playlist."""

    def __init__(self, test, candidate_side_effect, download):
        self.test, self.candidate, self.download = test, candidate_side_effect, download

    def __enter__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.old_cwd = os.getcwd()
        os.chdir(self.tmp.name)
        Path("logos").mkdir()
        Path("reports").mkdir()
        Path("reports/logo-source-registry.json").write_text("{}", encoding="utf-8")
        Path(IPTV).write_text(playlist(extinf(MOVIE_CLUB, MOVIE_CLUB_ID)), encoding="utf-8")
        return self

    def run(self):
        patches = [
            patch.object(repair.source, "load_iptv_org_indexes", return_value={}),
            patch.object(repair.source, "load_historical_logo_index", return_value={}),
            patch.object(repair, "candidate_for", return_value=self.candidate),
            patch.object(repair, "download_exact_asset", **self.download),
            patch.object(repair, "PLAYLISTS", [IPTV]),
            patch.object(sys, "argv", ["repair_playlist_logos.py"]),
        ]
        for item in patches:
            item.start()
        try:
            repair.main()
        finally:
            for item in reversed(patches):
                item.stop()
        return json.loads(Path("reports/logo-source-registry.json").read_text(encoding="utf-8"))

    def __exit__(self, *exc):
        os.chdir(self.old_cwd)
        self.tmp.cleanup()


class ExactMovieClubFailureTests(unittest.TestCase):
    def test_failed_candidate_download_does_not_make_fallback_third_party_verified(self):
        # IPTV-org supplies a Samsung URL, the download fails ("not a valid supported
        # image"), then a fallback is generated. Before the fix the stale candidate
        # won the if/elif and the fallback was recorded as third_party_verified.
        with RunRepairInTempTree(
            self, (dict(CANDIDATE), "IPTV-org public logo dataset"),
            {"side_effect": ValueError("source response is not a valid supported image")},
        ) as ctx:
            registry = ctx.run()
        # Production policy forbids fabricated artwork when an exact source fails.
        self.assertEqual(registry, {})
        self.assertNotIn("generated-fallback-", Path(IPTV).read_text(encoding="utf-8"))

    def test_provenance_survives_svg_to_png_conversion_and_classifies_as_fallback(self):
        registry = {key(FB_SVG): prov.canonical_fallback_record()}
        record, match = provenance_for(registry, IPTV, {"tvg-id": MOVIE_CLUB_ID}, MOVIE_CLUB, FB_PNG)
        self.assertEqual(match, "same-asset-stem-format-conversion")
        verdict = prov.classify_logo(record, match, FB_PNG)
        self.assertEqual(verdict["status"], "generated_fallback")
        self.assertTrue(verdict["fallback_is_disclosed"])
        self.assertEqual(verdict["problems"], [])

    def test_stale_third_party_record_cannot_override_fallback_asset(self):
        stale = {
            "status": "third_party_verified", "source_url": SAMSUNG_URL,
            "notes": "Generated fallback artwork (unofficial; no exact logo source found) "
                     "IPTV-org public logo dataset Source page: " + SAMSUNG_URL,
        }
        record, match = provenance_for({key(FB_SVG): stale}, IPTV, {"tvg-id": MOVIE_CLUB_ID}, MOVIE_CLUB, FB_PNG)
        self.assertEqual(match, "same-asset-stem-format-conversion")
        verdict = prov.classify_logo(record, match, FB_PNG)
        self.assertEqual(verdict["status"], "generated_fallback")
        self.assertEqual(verdict["source_url"], "")
        self.assertFalse(verdict["fallback_is_disclosed"])
        self.assertEqual(verdict["problems"], [prov.PROBLEM_STATUS_CONFLICT])
        self.assertEqual(verdict["reason"], prov.FALLBACK_DISCLOSURE_NOTE)

    def test_successful_candidate_download_is_still_third_party_verified(self):
        def fake_download(channel, candidate, canonical_name=False):
            write_png(Path("logos") / "the-movie-club-plus-2-abc123.png")
            return "the-movie-club-plus-2-abc123.png"

        with RunRepairInTempTree(
            self, (dict(CANDIDATE), "IPTV-org public logo dataset"), {"side_effect": fake_download},
        ) as ctx:
            registry = ctx.run()
        record = registry[key("logos/the-movie-club-plus-2-abc123.png")]
        self.assertEqual(record["status"], "third_party_verified")
        self.assertEqual(record["source_url"], SAMSUNG_URL)
        self.assertIn("IPTV-org public logo dataset", record["notes"])


class BuildRegistryRecordTests(unittest.TestCase):
    def test_fallback_takes_precedence_over_candidate(self):
        record = prov.build_registry_record(
            generated_fallback=True, candidate=dict(CANDIDATE), source_name="IPTV-org exact ID")
        self.assertEqual(record, prov.canonical_fallback_record())

    def test_candidate_without_fallback_is_third_party_verified(self):
        record = prov.build_registry_record(
            generated_fallback=False, candidate=dict(CANDIDATE), source_name="IPTV-org exact ID")
        self.assertEqual(record["status"], "third_party_verified")
        self.assertEqual(record["source_url"], SAMSUNG_URL)

    def test_nothing_known_produces_no_record(self):
        self.assertIsNone(prov.build_registry_record(generated_fallback=False))

    def test_canonical_note_contains_required_disclosure_phrases(self):
        notes = prov.canonical_fallback_record()["notes"].casefold()
        self.assertIn("unofficial fallback", notes)
        self.assertIn("not an official broadcaster logo", notes)


class ResolveProvenanceTests(unittest.TestCase):
    def resolve(self, registry, logo):
        return prov.resolve_provenance(registry, IPTV, "id.1", "Chan", logo)

    def test_exact_key_wins_over_stem_candidates(self):
        registry = {
            f"{IPTV}|id.1|Chan|logos/chan.png": verified_record("https://a.example/x.png"),
            f"{IPTV}|id.1|Chan|logos/chan.svg": verified_record("https://b.example/y.svg"),
        }
        record, match = self.resolve(registry, "logos/chan.png")
        self.assertEqual((match, record["source_url"]), ("exact-key", "https://a.example/x.png"))

    def test_converted_digest_suffix_matches_original_stem(self):
        registry = {f"{IPTV}|id.1|Chan|logos/chan.svg": verified_record()}
        record, match = self.resolve(registry, "logos/chan-converted-0123456789.png")
        self.assertEqual(match, "same-asset-stem-format-conversion")
        self.assertEqual(record["status"], "third_party_verified")

    def test_name_only_match_is_forbidden(self):
        registry = {f"{IPTV}|id.1|Chan|logos/old-image.png": verified_record()}
        self.assertEqual(self.resolve(registry, "logos/different-image.png"), ({}, "none"))

    def test_other_playlist_or_identity_never_matches(self):
        registry = {f"International-Playlist.m3u|id.1|Chan|logos/chan.svg": verified_record()}
        self.assertEqual(self.resolve(registry, "logos/chan.png"), ({}, "none"))
        registry = {f"{IPTV}|id.2|Chan|logos/chan.svg": verified_record()}
        self.assertEqual(self.resolve(registry, "logos/chan.png"), ({}, "none"))

    def test_distinct_conflicting_records_are_ambiguous(self):
        registry = {
            f"{IPTV}|id.1|Chan|logos/chan.svg": verified_record("https://a.example/1.svg"),
            f"{IPTV}|id.1|Chan|logos/chan.jpg": verified_record("https://b.example/2.jpg"),
        }
        self.assertEqual(self.resolve(registry, "logos/chan.png"), ({}, "ambiguous"))

    def test_identical_duplicate_records_are_not_ambiguous(self):
        registry = {
            f"{IPTV}|id.1|Chan|logos/chan.svg": fallback_record(),
            f"{IPTV}|id.1|Chan|logos/chan.jpg": fallback_record(),
        }
        record, match = self.resolve(registry, "logos/chan.png")
        self.assertEqual((match, record["status"]), ("same-asset-stem-format-conversion", "generated_fallback"))

    def test_needs_review_records_never_supply_provenance(self):
        registry = {f"{IPTV}|id.1|Chan|logos/chan.svg": {"status": "needs_review", "notes": "x"}}
        self.assertEqual(self.resolve(registry, "logos/chan.png"), ({}, "none"))

    def test_resolution_is_independent_of_registry_insertion_order(self):
        items = [
            (f"{IPTV}|id.1|Chan|logos/chan.svg", verified_record("https://a.example/1.svg")),
            (f"{IPTV}|id.1|Chan|logos/chan.jpg", verified_record("https://b.example/2.jpg")),
        ]
        self.assertEqual(
            self.resolve(dict(items), "logos/chan.png"),
            self.resolve(dict(reversed(items)), "logos/chan.png"),
        )


class ClassifyLogoTests(unittest.TestCase):
    def classify(self, record, match, logo):
        return prov.classify_logo(record, match, logo)

    def test_genuine_third_party_logo_stays_verified(self):
        verdict = self.classify(verified_record(), "exact-key", "logos/chan.png")
        self.assertEqual((verdict["status"], verdict["problems"]), ("third_party_verified", []))

    def test_conversion_note_is_added_for_stem_matches(self):
        verdict = self.classify(verified_record(), "same-asset-stem-format-conversion", "logos/chan.png")
        self.assertIn("after file-format conversion", verdict["reason"])

    def test_verified_record_without_source_url_needs_review(self):
        verdict = self.classify({"status": "third_party_verified", "notes": "n"}, "exact-key", "logos/chan.png")
        self.assertEqual(verdict["status"], "needs_review")

    def test_missing_logo_needs_review(self):
        self.assertEqual(self.classify({}, "none", "")["status"], "needs_review")

    def test_disclosed_fallback_is_valid(self):
        verdict = self.classify(fallback_record(), "exact-key", "logos/generated-fallback-chan-1.png")
        self.assertEqual((verdict["status"], verdict["fallback_is_disclosed"], verdict["problems"]),
                         ("generated_fallback", True, []))

    def test_fallback_without_record_is_rejected(self):
        for match in ("none", "ambiguous"):
            verdict = self.classify({}, match, "logos/generated-fallback-chan-1.png")
            self.assertEqual(verdict["problems"], [prov.PROBLEM_UNMATCHED])

    def test_fallback_missing_either_disclosure_phrase_is_rejected(self):
        for notes in ("Unofficial fallback artwork.", "Not an official broadcaster logo.", ""):
            verdict = self.classify(fallback_record(notes), "exact-key", "logos/generated-fallback-chan-1.png")
            self.assertEqual(verdict["problems"], [prov.PROBLEM_UNMATCHED], notes)

    def test_fallback_record_carrying_a_source_url_is_rejected(self):
        verdict = self.classify(fallback_record(source_url=SAMSUNG_URL), "exact-key",
                                "logos/generated-fallback-chan-1.png")
        self.assertEqual(verdict["problems"], [prov.PROBLEM_SOURCE_URL])
        self.assertEqual(verdict["source_url"], "")

    def test_official_verified_status_cannot_promote_a_fallback_asset(self):
        record = {"status": "official_verified", "source_url": "https://x.example/l.png", "notes": FALLBACK_NOTE}
        verdict = self.classify(record, "exact-key", "logos/generated-fallback-chan-1.png")
        self.assertEqual(verdict["status"], "generated_fallback")
        self.assertEqual(verdict["problems"], [prov.PROBLEM_STATUS_CONFLICT])

    def test_legacy_fallback_status_without_prefix_is_still_a_fallback(self):
        verdict = self.classify(fallback_record(), "exact-key", "logos/classic-movies-27994c39.png")
        self.assertEqual(verdict["status"], "generated_fallback")


class NormalizeRegistryTests(unittest.TestCase):
    def test_heals_conflicting_fallback_record(self):
        registry = {key(FB_SVG): {"status": "third_party_verified", "source_url": SAMSUNG_URL,
                                  "notes": "Generated fallback artwork (unofficial; no exact logo source found)"}}
        healed_registry, healed = prov.normalize_registry(registry)
        self.assertEqual(healed, [key(FB_SVG)])
        record = healed_registry[key(FB_SVG)]
        self.assertEqual((record["status"], record["source_url"]), ("generated_fallback", ""))
        self.assertTrue(prov.notes_disclose_fallback(record["notes"]))
        self.assertIn("Generated fallback artwork", record["notes"])  # history preserved

    def test_adds_missing_phrase_to_legacy_record_and_is_idempotent(self):
        legacy = "Channel-labelled local fallback artwork; explicitly marked UNOFFICIAL FALLBACK ART."
        registry = {key("logos/generated-fallback-x.svg"): fallback_record(legacy)}
        first, healed = prov.normalize_registry(registry)
        self.assertEqual(len(healed), 1)
        self.assertTrue(first[key("logos/generated-fallback-x.svg")]["notes"].startswith(legacy))
        _, healed_again = prov.normalize_registry(first)
        self.assertEqual(healed_again, [])

    def test_leaves_genuine_verified_records_untouched(self):
        registry = {key("logos/chan.png"): verified_record()}
        before = json.dumps(registry, sort_keys=True)
        prov.normalize_registry(registry)
        self.assertEqual(json.dumps(registry, sort_keys=True), before)


if __name__ == "__main__":
    unittest.main()
