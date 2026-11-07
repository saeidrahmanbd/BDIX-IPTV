import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import international_stream_health as health


def row(name="Test Movie", group="International Movies", url="https://example.test/live/test.m3u8", extra=""):
    return (
        f'#EXTINF:-1 tvg-id="testmovie.us" tvg-name="{name}" tvg-country="US" '
        f'tvg-language="eng" tvg-logo="logos/test-movie.png" {extra}group-title="{group}",{name}\n'
        f"{url}\n"
    )


def apply(text, state, history, day, status=404, reason="HTTP 404"):
    _, blocks = health.parse(text)
    monitored = [block for block in blocks if health.group_of(block[0]).casefold() != "adult"]
    values = [{"state": state, "status": status, "reason": reason} for _ in monitored]
    return health.apply_results(text, values, history, day)


class InternationalStreamHealthTests(unittest.TestCase):
    def playlist(self, entry):
        return (
            "#EXTM3U\n"
            '#PLAYLIST-STUDIO-CATEGORIES:["International Movies","New Channels","New Backups","Backup"]\n'
            + entry
        )

    def test_first_failure_moves_to_review_and_preserves_metadata(self):
        output, history, events = apply(self.playlist(row()), "fail", {}, "2026-11-07")
        self.assertIn('group-title="Review"', output)
        for field in ('tvg-id="testmovie.us"', 'tvg-language="eng"', 'tvg-logo="logos/test-movie.png"'):
            self.assertIn(field, output)
        self.assertIn("https://example.test/live/test.m3u8", output)
        self.assertEqual(events[0]["streak"], 1)
        self.assertEqual(next(iter(history["entries"].values()))["original_group"], "International Movies")

    def test_third_consecutive_daily_failure_removes_row(self):
        output, history = self.playlist(row()), {}
        for day in range(7, 10):
            output, history, events = apply(output, "fail", history, f"2026-11-{day:02d}")
        self.assertNotIn("https://example.test/live/test.m3u8", output)
        self.assertEqual(events[0]["action"], "removed-after-three-failed-days")
        self.assertEqual(history["removed"][-1]["removed_date"], "2026-11-09")

    def test_same_day_rerun_does_not_increment_streak(self):
        output, history, _ = apply(self.playlist(row()), "fail", {}, "2026-11-07")
        output, history, events = apply(output, "fail", history, "2026-11-07")
        self.assertEqual(events[0]["streak"], 1)
        self.assertEqual(events[0]["action"], "already-checked-today")

    def test_missing_day_restarts_streak(self):
        output, history, _ = apply(self.playlist(row()), "fail", {}, "2026-11-07")
        output, history, events = apply(output, "fail", history, "2026-11-09")
        self.assertEqual(events[0]["streak"], 1)

    def test_inconclusive_day_breaks_streak_but_keeps_review(self):
        output, history, _ = apply(self.playlist(row()), "fail", {}, "2026-11-07")
        output, history, _ = apply(output, "inconclusive", history, "2026-11-08", status=403, reason="HTTP 403")
        output, history, events = apply(output, "fail", history, "2026-11-09")
        self.assertIn('group-title="Review"', output)
        self.assertEqual(events[0]["streak"], 1)

    def test_success_restores_original_group(self):
        output, history, _ = apply(self.playlist(row()), "fail", {}, "2026-11-07")
        output, history, events = apply(output, "ok", history, "2026-11-08", status=200, reason="Media bytes received")
        self.assertIn('group-title="International Movies"', output)
        self.assertEqual(events[0]["action"], "restored")
        self.assertEqual(events[0]["streak"], 0)

    def test_adult_rows_are_not_probed_or_rewritten(self):
        adult = (
            '#EXTINF:-1 tvg-name="Adult Feed" group-title="Adult",Adult Feed\n'
            '# a protected comment\n'
            'https://adult.example.test/live.m3u8\n'
        )
        source = (
            "#EXTM3U\n"
            '#PLAYLIST-STUDIO-CATEGORIES:["International Movies","Adult","Review","New Channels","New Backups","Backup"]\n'
            + adult + row()
        )
        output, history, events = apply(source, "ok", {}, "2026-11-07", status=200)
        _, output_blocks = health.parse(output)
        output_adult = next(block for block in output_blocks if health.group_of(block[0]) == "Adult")
        self.assertEqual("\n".join(output_adult) + "\\n", adult)
        self.assertEqual(len(events), 1)
        self.assertEqual(len(history["entries"]), 1)
        self.assertNotIn("Adult Feed", "\n".join(record.get("name", "") for record in history["entries"].values()))

    def test_adult_rows_do_not_block_structural_validation_or_duplicate_url_audit(self):
        adult = (
            '#EXTINF:-1 tvg-name="Adult Feed" group-title="Adult",Adult Feed\n'
            'https://adult.example.test/duplicate.m3u8\n'
        )
        source = (
            "#EXTM3U\n"
            '#PLAYLIST-STUDIO-CATEGORIES:["Adult","International Movies","Review","New Channels","New Backups","Backup"]\n'
            + adult
            + row(url="https://adult.example.test/duplicate.m3u8")
        )
        self.assertTrue(health.validate_rendered_playlist(source))

    def test_token_rotation_does_not_reset_history(self):
        one = row(url="https://example.test/live/user/pass/12.m3u8?token=old")
        two = row(url="https://example.test/live/user/pass/12.m3u8?token=new")
        _, a = health.parse(one)
        _, b = health.parse(two)
        self.assertEqual(
            health.stream_key(a[0][0], health.urls(a[0])[0]),
            health.stream_key(b[0][0], health.urls(b[0])[0]),
        )

    def test_batch_safety_stop_prevents_mass_false_review_when_runner_reaches_nothing(self):
        results = [{"state": "fail", "reason": "Timeout"} for _ in range(3098)]
        with self.assertRaisesRegex(SystemExit, "zero media streams"):
            health.validate_probe_batch(results)

    def test_batch_safety_stop_catches_global_reachability_anomaly(self):
        results = ([{"state": "fail"}] * 3000) + ([{"state": "ok"}] * 10) + ([{"state": "inconclusive"}] * 88)
        with self.assertRaisesRegex(SystemExit, "repository-wide reachability anomaly"):
            health.validate_probe_batch(results)

    def test_batch_guard_allows_normal_mix_of_stream_results(self):
        results = ([{"state": "ok"}] * 2200) + ([{"state": "fail"}] * 700) + ([{"state": "inconclusive"}] * 198)
        health.validate_probe_batch(results)

    def test_auth_and_rate_limit_http_codes_are_inconclusive(self):
        for status in (401, 403, 407, 429, 451):
            self.assertEqual(health.http_state(status), "inconclusive")
        self.assertEqual(health.http_state(404), "fail")
        self.assertEqual(health.http_state(500), "fail")

    def test_health_rewrite_preserves_every_metadata_field_and_logo(self):
        source = self.playlist(row(extra='tvg-network="Example" '))
        output, _, _ = apply(source, "fail", {}, "2026-11-07")
        self.assertTrue(health.validate_rendered_playlist(output))
        _, old_blocks = health.parse(source)
        _, new_blocks = health.parse(output)
        old = health.attrs(old_blocks[0][0])
        new = health.attrs(new_blocks[0][0])
        old.pop("group-title")
        new.pop("group-title")
        self.assertEqual(old, new)

    def test_metadata_loss_is_rejected(self):
        source = self.playlist(row())
        output, _, _ = apply(source, "ok", {}, "2026-11-07", status=200, reason="Media bytes received")
        damaged = output.replace('tvg-logo="logos/test-movie.png"', 'tvg-logo=""')
        with self.assertRaisesRegex(ValueError, "metadata/logo"):
            health.validate_metadata_preservation(source, damaged, set())

    def test_structural_validator_rejects_duplicate_stream_urls(self):
        source = (
            "#EXTM3U\n"
            '#PLAYLIST-STUDIO-CATEGORIES:["International Movies","Review","New Channels","New Backups","Backup"]\n'
            + row(name="A", url="https://example.test/same.m3u8")
            + row(name="B", url="https://example.test/same.m3u8")
        )
        with self.assertRaisesRegex(ValueError, "Duplicate stream URL"):
            health.validate_rendered_playlist(source)

    def test_review_category_added_and_rows_sorted(self):
        source = (
            "#EXTM3U\n"
            '#PLAYLIST-STUDIO-CATEGORIES:["International Movies","New Channels","New Backups","Backup"]\n'
            + row(name="Zed Movie", url="https://example.test/z.m3u8")
            + row(name="Alpha Movie", url="https://example.test/a.m3u8")
        )
        output, _, _ = apply(source, "ok", {}, "2026-11-07", status=200, reason="Media bytes received")
        reg = next(x for x in output.splitlines() if x.startswith("#PLAYLIST-STUDIO-CATEGORIES:"))
        self.assertIn('"Review"', reg)
        self.assertLess(output.index("Alpha Movie"), output.index("Zed Movie"))


if __name__ == "__main__":
    unittest.main()
