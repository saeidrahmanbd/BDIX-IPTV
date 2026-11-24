"""Tests for the final logo validation, using the production validation module on both playlists."""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import validate_logo_references as validator  # noqa: E402
import repair_playlist_logos as repair  # noqa: E402
from logo_test_support import (  # noqa: E402
    FALLBACK_NOTE, INTL, IPTV, SAMSUNG_URL, extinf, fallback_record, playlist, verified_record, write_png,
)

MC, MC_ID = "The Movie Club +2", "TheMovieClub.in@Plus2"
FB_PNG = "logos/generated-fallback-the-movie-club-plus-2-c82c401f.png"
FB_SVG = FB_PNG[:-4] + ".svg"


def reg_key(playlist_name, tvg_id, name, logo):
    return f"{playlist_name}|{tvg_id}|{name}|{logo}"


class Tree:
    """A throwaway repository tree with both playlists, assets and a registry."""

    def __init__(self, iptv_entries=(), intl_entries=(), registry=None, assets=(), absolute_logos=True):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        # Real playlists carry absolute raw URLs; fixtures are written that way unless a
        # test deliberately exercises the rejected relative form.
        def render(entries):
            text = playlist(*entries)
            return text.replace('tvg-logo="logos/', f'tvg-logo="{repair.RAW_BASE}') if absolute_logos else text
        (self.root / IPTV).write_text(render(iptv_entries), encoding="utf-8")
        (self.root / INTL).write_text(render(intl_entries), encoding="utf-8")
        (self.root / "reports").mkdir()
        (self.root / "reports/logo-source-registry.json").write_text(json.dumps(registry or {}), encoding="utf-8")
        for asset in assets:
            write_png(self.root / asset)

    def run(self, **kwargs):
        out = io.StringIO()
        try:
            with contextlib.redirect_stdout(out):
                summaries = validator.main(["--root", str(self.root)] + kwargs.get("argv", []))
            return summaries, None, out.getvalue()
        except SystemExit as exc:
            return None, str(exc), out.getvalue()

    def close(self):
        self.tmp.cleanup()


class FinalValidationTests(unittest.TestCase):
    def make(self, **kwargs):
        tree = Tree(**kwargs)
        self.addCleanup(tree.close)
        return tree

    def invalid_lines(self, output):
        return [json.loads(line.split(" ", 1)[1]) for line in output.splitlines()
                if line.startswith("INVALID_LOGO_REFERENCE ")]

    def test_exact_the_movie_club_plus_2_failure_is_rejected_with_precise_reason(self):
        stale = {"status": "third_party_verified", "source_url": SAMSUNG_URL,
                 "notes": "Generated fallback artwork (unofficial; no exact logo source found) "
                          "IPTV-org public logo dataset Source page: " + SAMSUNG_URL}
        tree = self.make(
            iptv_entries=[extinf(MC, MC_ID, logo=FB_PNG)],
            registry={reg_key(IPTV, MC_ID, MC, FB_SVG): stale}, assets=[FB_PNG])
        _, error, output = tree.run()
        self.assertIn("Logo validation failed", error)
        (item,) = self.invalid_lines(output)
        self.assertEqual(item["reasons"], ["fallback_registry_status_conflict"])
        self.assertEqual(item["provenance_match"], "same-asset-stem-format-conversion")
        self.assertEqual(item["provenance_status"], "third_party_verified")
        self.assertFalse(item["fallback_is_disclosed"])

    def test_same_channel_with_correct_fallback_record_passes(self):
        tree = self.make(
            iptv_entries=[extinf(MC, MC_ID, logo=FB_PNG)],
            registry={reg_key(IPTV, MC_ID, MC, FB_SVG): fallback_record()}, assets=[FB_PNG])
        summaries, error, _ = tree.run()
        self.assertIsNone(error)
        self.assertEqual(summaries[IPTV]["invalid_or_blocked_refs"], 0)

    def test_valid_third_party_verified_logo_passes(self):
        tree = self.make(
            iptv_entries=[extinf("Real Channel", "real.in", logo="logos/real-channel.png")],
            registry={reg_key(IPTV, "real.in", "Real Channel", "logos/real-channel.png"): verified_record()},
            assets=["logos/real-channel.png"])
        summaries, error, _ = tree.run()
        self.assertIsNone(error)
        self.assertEqual(summaries[IPTV]["entries"], 1)

    def test_canonical_github_raw_logo_url_is_repository_local(self):
        logo = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/real-channel.png"
        tree = self.make(
            iptv_entries=[extinf("Real Channel", "real.in", logo=logo)],
            registry={reg_key(IPTV, "real.in", "Real Channel", logo): verified_record()},
            assets=["logos/real-channel.png"])
        summaries, error, _ = tree.run()
        self.assertIsNone(error)
        self.assertEqual(summaries[IPTV]["nonrepository_logo_refs"], 0)

    def test_undisclosed_or_unmatched_fallbacks_are_rejected(self):
        cases = {
            "no record": {},
            "missing phrase": {reg_key(IPTV, MC_ID, MC, FB_SVG): fallback_record("Unofficial fallback only.")},
            "source url": {reg_key(IPTV, MC_ID, MC, FB_SVG): fallback_record(source_url=SAMSUNG_URL)},
        }
        for label, registry in cases.items():
            with self.subTest(label):
                tree = self.make(iptv_entries=[extinf(MC, MC_ID, logo=FB_PNG)], registry=registry, assets=[FB_PNG])
                _, error, output = tree.run()
                self.assertIsNotNone(error)
                self.assertEqual(len(self.invalid_lines(output)), 1)

    def test_ambiguous_conflicting_records_reject_the_fallback(self):
        registry = {
            reg_key(IPTV, MC_ID, MC, FB_SVG): fallback_record(),
            reg_key(IPTV, MC_ID, MC, FB_PNG[:-4] + ".jpg"): fallback_record(FALLBACK_NOTE + " Different record."),
        }
        tree = self.make(iptv_entries=[extinf(MC, MC_ID, logo=FB_PNG)], registry=registry, assets=[FB_PNG])
        _, error, output = tree.run()
        self.assertIsNotNone(error)
        self.assertEqual(self.invalid_lines(output)[0]["provenance_match"], "ambiguous")

    def test_duplicate_identical_records_do_not_break_a_valid_fallback(self):
        registry = {
            reg_key(IPTV, MC_ID, MC, FB_SVG): fallback_record(),
            reg_key(IPTV, MC_ID, MC, FB_PNG[:-4] + ".jpg"): fallback_record(),
        }
        tree = self.make(iptv_entries=[extinf(MC, MC_ID, logo=FB_PNG)], registry=registry, assets=[FB_PNG])
        self.assertIsNone(tree.run()[1])

    def test_placeholder_generic_and_blocklisted_assets_are_rejected(self):
        for logo, reason in (
            ("logos/placeholder-btv-news.png", "blocked_filename_prefix"),
            ("logos/generic-news.png", "blocked_filename_prefix"),
            ("logos/unknown-chan.png", "blocked_filename_prefix"),
            ("logos/zee-tv.png", "explicit_blocklist"),
            ("logos/chan-generic-logo.png", "placeholder_or_generic_filename"),
        ):
            with self.subTest(logo=logo):
                tree = self.make(iptv_entries=[extinf("Chan", "c.1", logo=logo)], assets=[logo])
                _, error, output = tree.run()
                self.assertIsNotNone(error)
                self.assertIn(reason, self.invalid_lines(output)[0]["reasons"])

    def test_every_repository_generic_asset_is_rejected(self):
        name = sorted(repair.GENERIC_ASSETS)[0]
        logo = "logos/" + name
        tree = self.make(iptv_entries=[extinf("Chan", "c.1", logo=logo)], assets=[logo])
        self.assertIn("explicit_blocklist", self.invalid_lines(tree.run()[2])[0]["reasons"])

    def test_relative_logo_path_is_rejected_even_when_the_file_exists(self):
        tree = self.make(iptv_entries=[extinf("Chan", "c.1", logo="logos/chan.png")],
                         assets=["logos/chan.png"], absolute_logos=False)
        error = tree.run()[1]
        self.assertIsNotNone(error)
        self.assertIn("relative_logo_refs\": 1", tree.run()[2] + (error or ""))

    def test_missing_asset_file_is_rejected(self):
        tree = self.make(iptv_entries=[extinf("Chan", "c.1", logo="logos/gone.png")])
        _, error, output = tree.run()
        self.assertIsNotNone(error)
        self.assertEqual(self.invalid_lines(output)[0]["reasons"], ["missing_asset_file"])

    def test_non_png_external_nvision_and_corrupt_png_are_rejected(self):
        tree = self.make(iptv_entries=[extinf("Chan", "c.1", logo="logos/chan.svg")], assets=["logos/chan.svg"])
        self.assertEqual(tree.run()[1].count("non_png_refs\": 1"), 1)
        tree = self.make(iptv_entries=[extinf("Chan", "c.1", logo="https://example.com/chan.png")])
        self.assertIn("\"nonrepository_logo_refs\": 1", tree.run()[1])
        tree = self.make(iptv_entries=[extinf("Chan", "c.1", logo="logos/nvisionbd-chan.png")],
                         assets=["logos/nvisionbd-chan.png"])
        self.assertIn("\"nvision_refs\": 1", tree.run()[1])
        tree = self.make(iptv_entries=[extinf("Chan", "c.1", logo="logos/fake.png")])
        (tree.root / "logos").mkdir()
        (tree.root / "logos/fake.png").write_bytes(b"<html>not a png</html>" * 10)
        self.assertIn("invalid_png_signature", self.invalid_lines(tree.run()[2])[0]["reasons"])

    def test_review_and_missing_logos_are_counted_not_failed(self):
        tree = self.make(
            iptv_entries=[
                extinf("Active", "a.1"),
                extinf("Queued", "q.1", group="Review"),
            ],
            intl_entries=[extinf("Adult item", "adult.1", group="Adult")],
        )
        summaries, error, _ = tree.run()
        self.assertIsNone(error)
        self.assertEqual(summaries[IPTV]["missing_logo_metadata"], 1)
        self.assertEqual(summaries[IPTV]["review_missing_logo_metadata"], 1)
        self.assertEqual(summaries[IPTV]["adult_missing_logo_metadata"], 0)
        self.assertEqual(summaries[INTL]["adult_missing_logo_metadata"], 1)
        self.assertEqual(summaries[INTL]["adult_entries_ignored"], 1)

    def test_both_playlists_are_validated_even_when_the_first_fails(self):
        tree = self.make(
            iptv_entries=[extinf("Chan", "c.1", logo="logos/gone.png")],
            intl_entries=[extinf("Intl", "i.1", logo="logos/also-gone.png")])
        _, error, output = tree.run()
        self.assertIn(IPTV, error)
        self.assertIn(INTL, error)
        self.assertEqual({item["playlist"] for item in self.invalid_lines(output)}, {IPTV, INTL})

    def test_international_playlist_fallback_is_validated_with_its_own_record(self):
        intl_entry = extinf(MC, MC_ID, logo=FB_PNG)
        good = self.make(intl_entries=[intl_entry], assets=[FB_PNG],
                         registry={reg_key(INTL, MC_ID, MC, FB_SVG): fallback_record()})
        self.assertIsNone(good.run()[1])
        # A record belonging to the other playlist must not satisfy this playlist.
        wrong = self.make(intl_entries=[intl_entry], assets=[FB_PNG],
                          registry={reg_key(IPTV, MC_ID, MC, FB_SVG): fallback_record()})
        self.assertIsNotNone(wrong.run()[1])


class NonLogoContentProtectionTests(unittest.TestCase):
    def test_non_logo_content_must_be_byte_for_byte_identical(self):
        entries = [extinf("Chan", "c.1", logo="logos/chan.png")]
        tree = Tree(iptv_entries=entries, intl_entries=[extinf("Intl", "i.1")],
                    registry={reg_key(IPTV, "c.1", "Chan", "logos/chan.png"): verified_record()},
                    assets=["logos/chan.png"])
        self.addCleanup(tree.close)
        baselines = tree.root / "baseline"
        baselines.mkdir()
        for name in (IPTV, INTL):
            (baselines / (name + ".nonlogo")).write_text(
                validator.strip_logo_attributes((tree.root / name).read_text(encoding="utf-8")), encoding="utf-8")

        _, error, _ = tree.run(argv=["--baseline-dir", str(baselines)])
        self.assertIsNone(error)

        # Changing only a logo attribute is allowed; changing a stream URL is not.
        text = (tree.root / IPTV).read_text(encoding="utf-8")
        (tree.root / IPTV).write_text(text.replace("logos/chan.png", "logos/chan2.png"), encoding="utf-8")
        write_png(tree.root / "logos/chan2.png")
        self.assertIsNone(tree.run(argv=["--baseline-dir", str(baselines)])[1])

        (tree.root / IPTV).write_text(text.replace("example.invalid/live.m3u8", "example.invalid/other.m3u8"),
                                      encoding="utf-8")
        _, error, _ = tree.run(argv=["--baseline-dir", str(baselines)])
        self.assertEqual(error, "Non-logo playlist content changed: " + IPTV)

    def test_strip_logo_attributes_changes_nothing_but_logos(self):
        original = playlist(extinf("Chan", "c.1", logo="logos/a.png"))
        stripped = validator.strip_logo_attributes(original)
        self.assertNotIn("tvg-logo", stripped)
        self.assertEqual(stripped, validator.strip_logo_attributes(stripped))
        self.assertIn("https://example.invalid/live.m3u8", stripped)


class RepositoryPlaylistInvariantTests(unittest.TestCase):
    """Run the real final validation against the committed playlists."""

    def test_committed_playlists_have_no_external_nvision_or_non_png_references(self):
        registry = validator.load_registry(ROOT / validator.REGISTRY_PATH)
        for name in validator.PLAYLISTS:
            with self.subTest(playlist=name):
                text = (ROOT / name).read_text(encoding="utf-8-sig")
                result = validator.validate_playlist(name, text, registry, root=ROOT)
                summary = result["summary"]
                self.assertEqual(summary["nonrepository_logo_refs"], 0)
                self.assertEqual(summary["nvision_refs"], 0)
                self.assertEqual(summary["non_png_refs"], 0)
                self.assertEqual(
                    summary["invalid_or_blocked_refs"], 0,
                    msg=json.dumps(result["invalid"], ensure_ascii=False, sort_keys=True),
                )


if __name__ == "__main__":
    unittest.main()
