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
    values = [{"state": state, "status": status, "reason": reason} for _ in blocks]
    return health.apply_results(text, values, history, day)


class InternationalStreamHealthTests(unittest.TestCase):
    def playlist(self, entry):
        return (
            "#EXTM3U\n"
            '#PLAYLIST-STUDIO-CATEGORIES:["International Movies","Bangladesh","Indian Movies","Indian Music","Indian Bangla","Indian Entertainment","Pakistani","News","Fashion TV","Documentary & Wildlife","Kids","Religious","Sports","Adult","Review","New Channels","New Backups","Backup"]\n'
            + entry
        )

    def test_recovery_accounting_matches_successful_probe_playlist_and_report(self):
        source = self.playlist(row(name="Recovered Movie", group="Review"))
        info, url = health.parse(source)[1][0][0], "https://example.test/live/test.m3u8"
        key = health.stream_key(info, url)
        history = {"entries": {key: {
            "name": "Recovered Movie", "tvg_id": "testmovie.us", "country": "US",
            "original_group": "International Movies", "auto_review": True,
            "consecutive_failures": 1, "last_checked_date": "2026-11-07",
            "last_status": "fail", "removed": False,
        }}, "removed": []}
        updated, history, events = apply(source, "ok", history, "2026-11-08", status=200, reason="HLS media segment reachable")
        report = health.build_report(events, history, "2026-11-08", "2026-11-08T00:00:00+00:00", 1)
        accounting = health.validate_recovery_accounting(source, updated, events, report)
        self.assertEqual(accounting["recovered"], 1)
        self.assertIn("Restored from Review to primary/Backup/discovery queue: **1**", report)
        self.assertIn("**Recovered Movie** — restored to **International Movies**", report)

    def test_recovery_accounting_rejects_non_successful_probe(self):
        source = self.playlist(row(name="Not Verified", group="Review"))
        info, url = health.parse(source)[1][0][0], "https://example.test/live/test.m3u8"
        key = health.stream_key(info, url)
        _, history, events = apply(source, "fail", {}, "2026-11-08", status=404, reason="HTTP 404")
        event = dict(events[0], stream_key=key, action="restored-to-primary",
                     group_before="Review", group_after="International Movies")
        report = health.build_report([event], history, "2026-11-08", "2026-11-08T00:00:00+00:00", 1)
        with self.assertRaisesRegex(ValueError, "successful media probe"):
            health.validate_recovery_accounting(source, source, [event], report)

    def test_recovery_accounting_rejects_report_count_or_destination_drift(self):
        source = self.playlist(row(name="Counted Movie", group="Review"))
        info, url = health.parse(source)[1][0][0], "https://example.test/live/test.m3u8"
        key = health.stream_key(info, url)
        history = {"entries": {key: {
            "name": "Counted Movie", "tvg_id": "testmovie.us", "country": "US",
            "original_group": "International Movies", "auto_review": True,
            "consecutive_failures": 1, "last_checked_date": "2026-11-07",
            "last_status": "fail", "removed": False,
        }}, "removed": []}
        updated, history, events = apply(source, "ok", history, "2026-11-08", status=200, reason="Media bytes received")
        report = health.build_report(events, history, "2026-11-08", "2026-11-08T00:00:00+00:00", 1)
        with self.assertRaisesRegex(ValueError, "Published recovery total"):
            health.validate_recovery_accounting(source, updated, events, report.replace("Restored from Review to primary/Backup/discovery queue: **1**", "Restored from Review to primary/Backup/discovery queue: **0**"))
        wrong_destination = updated.replace('group-title="International Movies"', 'group-title="Review"')
        with self.assertRaisesRegex(ValueError, "destination"):
            health.validate_recovery_accounting(source, wrong_destination, events, report)

    def test_report_summarizes_inconclusive_reasons_and_http_statuses(self):
        events = [
            {"state": "inconclusive", "status": 403, "reason": "HTTP 403", "action": "none", "name": "Example 403"},
            {"state": "inconclusive", "status": 403, "reason": "HTTP 403", "action": "none", "name": "Example 403"},
            {"state": "inconclusive", "status": 0, "reason": "Timeout", "action": "none", "name": "Example timeout"},
            {"state": "ok", "status": 200, "reason": "Media bytes received", "action": "none", "name": "Example OK"},
        ]
        report = health.build_report(events, {"entries": {}}, "2026-11-14", "2026-11-14T00:00:00+00:00", 4)
        self.assertIn("## Inconclusive reason summary", report)
        self.assertIn("**HTTP 403** — 2", report)
        self.assertIn("**Timeout** — 1", report)
        self.assertIn("### HTTP status breakdown", report)

    def test_first_failure_moves_to_review_and_preserves_metadata(self):
        output, history, events = apply(self.playlist(row()), "fail", {}, "2026-11-07")
        self.assertIn('group-title="Review"', output)
        for field in ('tvg-id="testmovie.us"', 'tvg-language="eng"', 'tvg-logo="logos/test-movie.png"'):
            self.assertIn(field, output)
        self.assertIn("https://example.test/live/test.m3u8", output)
        self.assertEqual(events[0]["streak"], 1)
        self.assertEqual(next(iter(history["entries"].values()))["original_group"], "International Movies")

    def test_recovered_new_channel_returns_to_new_channels_queue(self):
        url = "https://example.test/world-movie.m3u8"
        info = (
            '#EXTINF:-1 tvg-id="worldmovie.us" tvg-name="World Movie" tvg-country="US" '
            'tvg-content="Movies" group-title="Review",World Movie'
        )
        source = self.playlist(info + "\n" + url + "\n")
        key = health.stream_key(info, url)
        history = {"entries": {key: {
            "name": "World Movie", "tvg_id": "worldmovie.us", "country": "US",
            "original_group": "New Channels", "auto_review": True,
            "consecutive_failures": 1, "last_checked_date": "2026-11-07",
            "last_status": "fail", "removed": False,
        }}, "removed": []}
        output, _, events = apply(source, "ok", history, "2026-11-08", status=200, reason="Media bytes received")
        self.assertIn('group-title="New Channels"', output)
        self.assertEqual(events[0]["action"], "restored-to-discovery-queue")

    def test_recovered_new_backup_returns_to_new_backups_queue(self):
        url = "https://example.test/world-movie-backup.m3u8"
        info = (
            '#EXTINF:-1 tvg-id="worldmovie.us" tvg-name="World Movie" tvg-country="US" '
            'tvg-content="Movies" group-title="Review",World Movie'
        )
        source = self.playlist(info + "\n" + url + "\n")
        key = health.stream_key(info, url)
        history = {"entries": {key: {
            "name": "World Movie", "tvg_id": "worldmovie.us", "country": "US",
            "original_group": "New Backups", "auto_review": True,
            "consecutive_failures": 1, "last_checked_date": "2026-11-07",
            "last_status": "fail", "removed": False,
        }}, "removed": []}
        output, _, events = apply(source, "ok", history, "2026-11-08", status=200, reason="Media bytes received")
        self.assertIn('group-title="New Backups"', output)
        self.assertEqual(events[0]["action"], "restored-to-discovery-queue")

    def test_requeued_channel_updates_old_health_history_recovery_destination(self):
        url = "https://example.test/requeued-world-movie.m3u8"
        source = self.playlist(row(
            name="World Movie",
            group="New Channels",
            url=url,
            extra='tvg-content="Movies" ',
        ))
        info = health.parse(source)[1][0][0]
        key = health.stream_key(info, url)
        history = {"entries": {key: {
            "name": "World Movie", "tvg_id": "testmovie.us", "country": "US",
            "original_group": "Indian Movies", "auto_review": True,
            "consecutive_failures": 1, "last_checked_date": "2026-11-06",
            "last_status": "fail", "removed": False,
        }}, "removed": []}
        output, history, events = apply(source, "fail", history, "2026-11-07")
        self.assertIn('group-title="Review"', output)
        self.assertEqual(history["entries"][key]["original_group"], "New Channels")
        output, history, events = apply(output, "ok", history, "2026-11-08", status=200, reason="Media bytes received")
        self.assertIn('group-title="New Channels"', output)
        self.assertEqual(events[0]["action"], "restored-to-discovery-queue")

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

    def test_three_consecutive_inconclusive_days_move_primary_to_review_without_deleting(self):
        source = self.playlist(row(name="Unverified Movie"))
        output, history, _ = apply(
            source, "inconclusive", {}, "2026-11-07",
            status=403, reason="HTTP 403",
        )
        output, history, _ = apply(
            output, "inconclusive", history, "2026-11-08",
            status=403, reason="HTTP 403",
        )
        self.assertIn('group-title="International Movies"', output)
        output, history, events = apply(
            output, "inconclusive", history, "2026-11-09",
            status=403, reason="HTTP 403",
        )
        self.assertIn('group-title="Review"', output)
        self.assertIn("https://example.test/live/test.m3u8", output)
        self.assertEqual(events[0]["action"], "moved-to-review-after-inconclusive-streak")
        record = next(iter(history["entries"].values()))
        self.assertEqual(record["consecutive_failures"], 0)
        self.assertEqual(record["consecutive_inconclusive"], 3)
        self.assertFalse(record["removed"])

    def test_working_stream_recovers_after_inconclusive_quarantine(self):
        source = self.playlist(row(name="Recoverable Movie"))
        output, history, _ = apply(
            source, "inconclusive", {}, "2026-11-07",
            status=403, reason="HTTP 403",
        )
        output, history, _ = apply(
            output, "inconclusive", history, "2026-11-08",
            status=403, reason="HTTP 403",
        )
        output, history, _ = apply(
            output, "inconclusive", history, "2026-11-09",
            status=403, reason="HTTP 403",
        )
        output, _, events = apply(
            output, "ok", history, "2026-11-10",
            status=200, reason="Media bytes received",
        )
        self.assertIn('group-title="International Movies"', output)
        self.assertEqual(events[0]["action"], "restored-to-primary")

    def test_missing_day_restarts_inconclusive_quarantine_streak(self):
        source = self.playlist(row(name="Intermittent Movie"))
        output, history, _ = apply(
            source, "inconclusive", {}, "2026-11-07",
            status=403, reason="HTTP 403",
        )
        output, history, events = apply(
            output, "inconclusive", history, "2026-11-09",
            status=403, reason="HTTP 403",
        )
        self.assertIn('group-title="International Movies"', output)
        self.assertEqual(events[0]["action"], "inconclusive-streak")
        record = next(iter(history["entries"].values()))
        self.assertEqual(record["consecutive_inconclusive"], 1)

    def test_inconclusive_day_breaks_streak_but_keeps_review(self):
        output, history, _ = apply(self.playlist(row()), "fail", {}, "2026-11-07")
        output, history, _ = apply(output, "inconclusive", history, "2026-11-08", status=403, reason="HTTP 403")
        output, history, events = apply(output, "fail", history, "2026-11-09")
        self.assertIn('group-title="Review"', output)
        self.assertEqual(events[0]["streak"], 1)

    def test_success_reclassifies_auto_review_to_correct_primary_group(self):
        output, history, _ = apply(self.playlist(row(name="Example Movie")), "fail", {}, "2026-11-07")
        output, history, events = apply(output, "ok", history, "2026-11-08", status=200, reason="Media bytes received")
        self.assertIn('group-title="International Movies"', output)
        self.assertEqual(events[0]["action"], "restored-to-primary")
        self.assertEqual(events[0]["streak"], 0)


    def test_same_day_success_rechecks_review_after_recovery_policy_fix(self):
        source = self.playlist(row(name="Example Movie", group="Review"))
        blocks = health.parse(source)[1]
        info = blocks[0][0]
        url = health.urls(blocks[0])[0]
        key = health.stream_key(info, url)
        history = {"entries": {key: {
            "name": "Example Movie", "tvg_id": "testmovie.us", "country": "US",
            "original_group": "International Movies", "auto_review": True,
            "consecutive_failures": 0, "consecutive_inconclusive": 0,
            "last_checked_date": "2026-11-08", "last_status": "ok",
            "removed": False,
        }}, "removed": []}
        output, _, events = apply(
            source, "ok", history, "2026-11-08",
            status=200, reason="Media bytes received",
        )
        self.assertIn('group-title="International Movies"', output)
        self.assertEqual(events[0]["action"], "restored-to-primary")

    def test_working_manual_review_channel_moves_to_primary(self):
        source = self.playlist(row(name="Manual Movie", group="Review"))
        output, _, events = apply(source, "ok", {}, "2026-11-08", status=200, reason="Media bytes received")
        self.assertIn('group-title="International"', output)
        self.assertEqual(events[0]["action"], "restored-to-primary")

    def test_working_review_special_genres_are_restored_to_primary_groups(self):
        cases = (
            ("CNN International", "News"),
            ("Cartoon Network", "Kids"),
            ("ESPN", "Sports"),
            ("National Geographic", "Documentary & Wildlife"),
            ("Peace TV", "Religious"),
            ("Fashion TV", "Fashion TV"),
        )
        for name, expected_group in cases:
            with self.subTest(name=name):
                source = self.playlist(row(name=name, group="Review"))
                blocks = health.parse(source)[1]
                info = blocks[0][0]
                url = health.urls(blocks[0])[0]
                key = health.stream_key(info, url)
                history = {"entries": {key: {
                    "name": name, "tvg_id": "testmovie.us", "country": "US",
                    "original_group": expected_group, "auto_review": True,
                    "consecutive_failures": 1, "last_checked_date": "2026-11-07",
                    "last_status": "fail", "removed": False,
                }}, "removed": []}
                output, _, events = apply(
                    source, "ok", history, "2026-11-08",
                    status=200, reason="Media bytes received",
                )
                self.assertIn(f'group-title="{expected_group}"', output)
                self.assertEqual(events[0]["action"], "restored-to-primary")

    def test_working_review_alternate_moves_to_backup_when_primary_exists(self):
        primary = row(name="Shared Movie", group="International Movies", url="https://example.test/primary.m3u8")
        review = row(name="Shared Movie", group="Review", url="https://example.test/alternate.m3u8")
        source = self.playlist(primary + review)
        output, _, events = apply(source, "ok", {}, "2026-11-08", status=200, reason="Media bytes received")
        self.assertIn('group-title="Backup"', output)
        self.assertEqual(events[1]["action"], "restored-to-backup")
        self.assertIn("https://example.test/alternate.m3u8", output)

    def test_working_review_channel_forms_country_group_on_fifth_primary_identity(self):
        header = (
            "#EXTM3U\n"
            '#PLAYLIST-STUDIO-CATEGORIES:["International","Review","New Channels","New Backups","Backup"]\n'
        )
        rows = []
        for number in range(1, 5):
            rows.append(row(
                name=f"Albania Movie {number}", group="International",
                url=f"https://al.example/{number}.m3u8",
            ).replace("testmovie.us", f"albania{number}.al").replace('tvg-country="US"', 'tvg-country="AL"').replace('tvg-language="eng"', 'tvg-language="sqi"').replace('tvg-logo="logos/test-movie.png"', 'tvg-logo="logos/albania.png"'))
        candidate = row(
            name="Albania Movie 5", group="Review",
            url="https://al.example/5.m3u8",
        ).replace("testmovie.us", "albania5.al").replace('tvg-country="US"', 'tvg-country="AL"').replace('tvg-language="eng"', 'tvg-language="sqi"').replace('tvg-logo="logos/test-movie.png"', 'tvg-logo="logos/albania.png"')
        source = header + "".join(rows) + candidate
        output, _, _ = health.apply_results(
            source,
            [{"state": "ok", "status": 200, "reason": "Media bytes received"}] * 5,
            {},
            "2026-11-08",
        )
        self.assertIn('group-title="Albania"', output)
        self.assertIn('"Albania"', next(x for x in output.splitlines() if x.startswith("#PLAYLIST-STUDIO-CATEGORIES:")))

    def test_working_but_policy_ineligible_indian_review_stays_in_review(self):
        source = self.playlist(
            row(name="Indian Quran Channel", group="Review")
            .replace("testmovie.us", "indianquranchannel.in")
            .replace('tvg-country="US"', 'tvg-country="IN"')
        )
        output, _, events = apply(source, "ok", {}, "2026-11-08", status=200, reason="Media bytes received")
        self.assertIn('group-title="Review"', output)
        self.assertEqual(events[0]["action"], "unchanged")


    def test_working_but_unclassified_foreign_review_stays_in_review(self):
        source = self.playlist(
            row(name="General Entertainment Channel", group="Review")
        )
        output, _, events = apply(source, "ok", {}, "2026-11-08", status=200, reason="Media bytes received")
        self.assertIn('group-title="Review"', output)
        self.assertEqual(events[0]["action"], "unchanged")

    def test_token_rotation_does_not_reset_history(self):
        one = row(url="https://example.test/live/user/pass/12.m3u8?token=old")
        two = row(url="https://example.test/live/user/pass/12.m3u8?token=new")
        _, a = health.parse(one)
        _, b = health.parse(two)
        self.assertEqual(
            health.stream_key(a[0][0], health.urls(a[0])[0]),
            health.stream_key(b[0][0], health.urls(b[0])[0]),
        )

    def test_network_probe_failures_are_inconclusive_not_dead_streams(self):
        from unittest.mock import patch
        with patch.object(health, "fetch", return_value={"kind": "network", "status": 0, "error": "Timeout"}):
            self.assertEqual(health.probe_resource("https://example.test/live.m3u8", {})["state"], "inconclusive")

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

    def test_auth_rate_limit_timeout_and_server_http_codes_are_inconclusive(self):
        for status in (401, 403, 407, 408, 425, 429, 451, 500, 502, 503, 504, 599):
            self.assertEqual(health.http_state(status), "inconclusive")
        self.assertEqual(health.http_state(404), "fail")

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

    def test_blank_lines_do_not_count_as_stream_directive_changes(self):
        info = row()
        source = self.playlist(info) + "\n"
        normalized = self.playlist(info)
        health.validate_metadata_preservation(source, normalized, set())

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

    def test_adult_entries_are_never_moved_to_review_or_removed(self):
        source = (
            "#EXTM3U\\n"
            '#PLAYLIST-STUDIO-CATEGORIES:["Adult","Review","New Channels","New Backups","Backup"]\\n'
            + row(name="Protected Adult", group="Adult", url="https://example.test/adult/live.m3u8")
        )
        output, history = source, {}
        for day in range(7, 11):
            output, history, events = apply(output, "fail", history, f"2026-11-{day:02d}")
            self.assertIn('group-title="Adult"', output)
            self.assertNotIn('group-title="Review"', output)
            self.assertIn("https://example.test/adult/live.m3u8", output)
            self.assertFalse(next(iter(history["entries"].values()))["removed"])
            self.assertEqual(events[0]["action"], "protected-adult-diagnostic")
            self.assertEqual(events[0]["streak"], 0)

    def test_adult_origin_already_in_review_is_restored_and_protected(self):
        source = (
            "#EXTM3U\\n"
            '#PLAYLIST-STUDIO-CATEGORIES:["Adult","Review","New Channels","New Backups","Backup"]\\n'
            + row(name="Legacy Adult", group="Review", url="https://example.test/adult/legacy.m3u8")
        )
        key = health.stream_key(
            health.parse(source)[1][0][0],
            "https://example.test/adult/legacy.m3u8",
        )
        history = {"entries": {key: {
            "name": "Legacy Adult", "tvg_id": "testmovie.us", "country": "US",
            "original_group": "Adult", "auto_review": True,
            "consecutive_failures": 2, "last_checked_date": "2026-11-06",
            "last_status": "fail", "removed": False,
        }}, "removed": []}
        output, history, events = apply(source, "fail", history, "2026-11-07")
        self.assertIn('group-title="Adult"', output)
        self.assertIn("https://example.test/adult/legacy.m3u8", output)
        self.assertEqual(events[0]["action"], "restored-protected-adult")
        self.assertFalse(history["entries"][key]["removed"])
