import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_discovery_run import NEWS_RE, append_section, classify_response, consolidate_international_country_groups, ensure_local_logo, final_mode, parse_playlist
from discover_bd_in_new_queues import parse as parse_bd_playlist


class DiscoveryRunValidationTests(unittest.TestCase):
    def test_news_filter_does_not_misclassify_ndtv_good_times(self):
        self.assertFalse(NEWS_RE.search("NDTV Good Times"))
        self.assertTrue(NEWS_RE.search("NDTV 24x7"))

    def test_hls_manifest_is_verified(self):
        status, _ = classify_response(200, {"Content-Type": "application/vnd.apple.mpegurl"}, b"#EXTM3U\n#EXT-X-VERSION:3\n", "https://example.test/live.m3u8")
        self.assertEqual(status, "verified")

    def test_dash_manifest_is_verified(self):
        status, _ = classify_response(200, {"Content-Type": "application/dash+xml"}, b"<MPD></MPD>", "https://example.test/live.mpd")
        self.assertEqual(status, "verified")

    def test_not_found_is_dead(self):
        self.assertEqual(classify_response(404, {}, b"", "https://example.test/dead.m3u8")[0], "dead")

    def test_access_denied_is_unknown_not_dead(self):
        self.assertEqual(classify_response(403, {}, b"", "https://example.test/live.m3u8")[0], "unknown")

    def test_html_error_page_is_not_a_live_stream(self):
        self.assertEqual(classify_response(200, {"Content-Type": "text/html"}, b"<html>error</html>", "https://example.test/live.m3u8")[0], "dead")

    def test_final_validation_keeps_stream_verification_section(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "report.md"
            report.write_text("# Report\n\n## Stream verification\n\n- Verified streams: 2\n", encoding="utf-8")
            append_section(report, "Final validation", "- Validation status: PASS")
            content = report.read_text(encoding="utf-8")
            self.assertIn("## Stream verification", content)
            self.assertIn("Verified streams: 2", content)
            self.assertIn("## Final validation", content)

    def test_country_group_is_promoted_when_five_primary_identities_exist_after_probe(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "International-Playlist.m3u"
            rows = [
                f'#EXTINF:-1 tvg-id="MK{i}.mk" tvg-country="MK" group-title="North Macedonia",MK {i}\nhttps://example.org/mk{i}.m3u8'
                for i in range(4)
            ]
            rows.append('#EXTINF:-1 tvg-id="MK5.mk" tvg-country="MK" group-title="International",MK 5\nhttps://example.org/mk5.m3u8')
            playlist.write_text("#EXTM3U\n" + "\n".join(rows) + "\n", encoding="utf-8")
            moved = consolidate_international_country_groups(playlist)
            content = playlist.read_text(encoding="utf-8")
            self.assertEqual(len(moved), 1)
            self.assertEqual(content.count('group-title="North Macedonia"'), 5)
            self.assertNotIn('group-title="New Channels"', content)

    def test_country_group_below_five_is_consolidated_into_international_after_probe(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "International-Playlist.m3u"
            rows = [
                f'#EXTINF:-1 tvg-id="MK{i}.mk" tvg-country="MK" group-title="North Macedonia",MK {i}\nhttps://example.org/under{i}.m3u8'
                for i in range(4)
            ]
            playlist.write_text("#EXTM3U\n" + "\n".join(rows) + "\n", encoding="utf-8")
            moved = consolidate_international_country_groups(playlist)
            content = playlist.read_text(encoding="utf-8")
            self.assertEqual(len(moved), 4)
            self.assertNotIn('group-title="North Macedonia"', content)
            self.assertEqual(content.count('group-title="International"'), 4)

    def test_attribution_block_stays_after_extm3u_when_country_groups_are_reconciled(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "International-Playlist.m3u"
            attribution = [
                "#=================================",
                "# Developed by: SAEID RAHMAN",
                "# Facebook: https://www.facebook.com/saeid.rahman.sr",
                "# Email: saeidrahman.mkt@gmail.com",
                "#=================================",
            ]
            rows = [
                f'#EXTINF:-1 tvg-id="MK{i}.mk" tvg-country="MK" group-title="North Macedonia",MK {i}\nhttps://example.org/attr{i}.m3u8'
                for i in range(4)
            ]
            rows.append('#EXTINF:-1 tvg-id="MK5.mk" tvg-country="MK" group-title="International",MK 5\nhttps://example.org/attr5.m3u8')
            playlist.write_text("#EXTM3U\n" + "\n".join(attribution) + "\n#PLAYLIST-STUDIO-CATEGORIES:[]\n" + "\n".join(rows) + "\n", encoding="utf-8")
            consolidate_international_country_groups(playlist)
            lines = playlist.read_text(encoding="utf-8").splitlines()
            self.assertEqual(lines[1:6], attribution)
            self.assertTrue(lines[6].startswith("#PLAYLIST-STUDIO-CATEGORIES:"))

    def test_final_validation_accepts_empty_new_backup_group_when_registry_order_is_correct(self):
        import os
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "International-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            (root / "logos").mkdir()
            (root / "logos" / "world-music.svg").write_text("<svg/>", encoding="utf-8")
            content = (
                '#EXTM3U\n'
                '#PLAYLIST-STUDIO-CATEGORIES:["Bangladesh","Review","New Channels","New Backups","Backup"]\n'
                '#EXTINF:-1 tvg-name="Bangladesh One" group-title="Bangladesh",Bangladesh One\n'
                'https://example.org/bangladesh.m3u8\n'
                '#EXTINF:-1 tvg-id="WorldMusic.us" tvg-name="World Music" tvg-country="US" tvg-logo="logos/world-music.svg" tvg-content="Music" group-title="New Channels",World Music\n'
                'https://example.org/world-music.m3u8\n'
                '#EXTINF:-1 tvg-name="Backup One" group-title="Backup",Backup One\n'
                'https://example.org/backup.m3u8\n'
            )
            playlist.write_text(content, encoding="utf-8")
            baseline.write_text(content, encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
            previous = os.environ.get("OFFICIAL_VALIDATOR_OUTCOME")
            os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = "success"
            old_cwd = Path.cwd()
            os.chdir(root)
            try:
                final_mode(str(playlist), str(report), str(baseline), "international")
            finally:
                os.chdir(old_cwd)
                if previous is None:
                    os.environ.pop("OFFICIAL_VALIDATOR_OUTCOME", None)
                else:
                    os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = previous
            self.assertIn("- Validation status: PASS", report.read_text(encoding="utf-8"))
            self.assertIn("- Review/New Channels/New Backups/Backup ordering: passed", report.read_text(encoding="utf-8"))

    def test_final_validation_accepts_pakistani_channels_of_any_genre_without_movie_music_tag(self):
        import os
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "logos").mkdir()
            for name in ("atv", "bstv"):
                (root / "logos" / f"{name}.svg").write_text("<svg/>", encoding="utf-8")
            playlist = root / "International-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            registry = ["Pakistani", "Review", "New Channels", "New Backups", "Backup"]
            rows = [
                f'#EXTINF:-1 tvg-id="PK{i}.pk" tvg-name="Pakistani Primary {i}" tvg-country="PK" group-title="Pakistani",Pakistani Primary {i}\nhttps://example.org/pk{i}.m3u8'
                for i in range(1, 6)
            ]
            rows.extend([
                '#EXTINF:-1 tvg-id="ATV.pk" tvg-name="ATV (Pakistan)" tvg-country="PK" tvg-logo="logos/atv.svg" group-title="New Channels",ATV (Pakistan)\nhttps://example.org/atv.m3u8',
                '#EXTINF:-1 tvg-id="BSTV.pk" tvg-name="BSTV (Pakistan)" tvg-country="PK" tvg-logo="logos/bstv.svg" group-title="New Channels",BSTV (Pakistan)\nhttps://example.org/bstv.m3u8',
            ])
            content = (
                "#EXTM3U\n"
                "#PLAYLIST-STUDIO-CATEGORIES:" + __import__("json").dumps(registry) + "\n"
                + "\n".join(rows) + "\n"
            )
            playlist.write_text(content, encoding="utf-8")
            baseline.write_text(content, encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
            previous = os.environ.get("OFFICIAL_VALIDATOR_OUTCOME")
            os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = "success"
            old_cwd = Path.cwd()
            os.chdir(root)
            try:
                final_mode(str(playlist), str(report), str(baseline), "international")
            finally:
                os.chdir(old_cwd)
                if previous is None:
                    os.environ.pop("OFFICIAL_VALIDATOR_OUTCOME", None)
                else:
                    os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = previous
            final_report = report.read_text(encoding="utf-8")
            self.assertIn("- Validation status: PASS", final_report)
            self.assertIn("- Geography/content policy issues: 0", final_report)

    def test_empty_logo_attribute_is_removed_when_no_authentic_asset_exists(self):
        extinf = '#EXTINF:-1 tvg-name="Definitely Missing Channel" tvg-logo="",Definitely Missing Channel'
        entry = {"extinf": extinf, "logo": "", "name": "Definitely Missing Channel"}
        updated, localized, cleared = ensure_local_logo(entry)
        self.assertNotIn('tvg-logo=""', updated)
        self.assertTrue(cleared)

    def test_candidate_without_logo_is_marked_unavailable_but_not_rewritten(self):
        extinf = '#EXTINF:-1 tvg-name="No Authentic Asset Candidate",No Authentic Asset Candidate'
        entry = {"extinf": extinf, "logo": "", "name": "No Authentic Asset Candidate"}
        updated, localized, unavailable = ensure_local_logo(entry)
        self.assertEqual(updated, extinf)
        self.assertFalse(localized)
        self.assertTrue(unavailable)

    def test_iptv_discovery_keeps_new_manual_review_candidate_with_wrong_country_and_no_logo(self):
        import tempfile
        from unittest.mock import patch
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "IPTV-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            existing = (
                '#EXTINF:-1 tvg-id="Old.us" tvg-country="US" group-title="New Channels" tvg-name="Old Queue Row",Old Queue Row\n'
                'https://example.org/old-queue.m3u8\n'
            )
            fresh = (
                '#EXTINF:-1 tvg-id="Fresh.us" tvg-country="US" group-title="New Channels" tvg-name="Fresh Candidate",Fresh Candidate\n'
                'https://example.org/fresh-candidate.m3u8\n'
            )
            playlist.write_text("#EXTM3U\n" + existing + fresh, encoding="utf-8")
            baseline.write_text("#EXTM3U\n" + existing, encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
            with patch.object(validation, "probe_url", return_value=("unknown", "HTTP 403")) as probe:
                with patch.object(
                    validation,
                    "ensure_local_logo",
                    side_effect=lambda entry: (entry["extinf"], False, True),
                ):
                    validation.probe_mode(str(playlist), str(report), str(baseline), "iptv")
            output = playlist.read_text(encoding="utf-8")
            self.assertIn('group-title="New Channels"', output)
            self.assertIn('tvg-name="Fresh Candidate",Fresh Candidate', output)
            self.assertIn('group-title="New Channels",Old Queue Row', output)
            self.assertEqual(probe.call_count, 1)
            self.assertIn("manual review", report.read_text(encoding="utf-8").casefold())

    def test_final_iptv_validation_ignores_country_logo_and_preexisting_playlist_duplicates(self):
        import os
        import tempfile
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "IPTV-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            registry = ["Bangladesh", "Backup", "New Channels", "New Backups", "Review"]
            duplicate_existing = (
                '#EXTINF:-1 tvg-name="Old duplicate A" group-title="Bangladesh",Old duplicate A\n'
                'https://example.org/old-duplicate.m3u8\n'
                '#EXTINF:-1 tvg-name="Old duplicate B" group-title="Bangladesh",Old duplicate B\n'
                'https://example.org/old-duplicate.m3u8\n'
            )
            fresh = (
                '#EXTINF:-1 tvg-id="Fresh.us" tvg-country="US" group-title="New Channels" tvg-name="Fresh Candidate",Fresh Candidate\n'
                'https://example.org/fresh-candidate.m3u8\n'
            )
            prefix = "#EXTM3U\n#PLAYLIST-STUDIO-CATEGORIES:" + __import__("json").dumps(registry) + "\n"
            playlist.write_text(prefix + duplicate_existing + fresh, encoding="utf-8")
            baseline.write_text(prefix + duplicate_existing, encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
            previous = os.environ.get("OFFICIAL_VALIDATOR_OUTCOME")
            os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = "success"
            try:
                validation.final_mode(str(playlist), str(report), str(baseline), "iptv")
            finally:
                if previous is None:
                    os.environ.pop("OFFICIAL_VALIDATOR_OUTCOME", None)
                else:
                    os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = previous
            final_report = report.read_text(encoding="utf-8")
            self.assertIn("- Validation status: PASS", final_report)
            self.assertIn("missing an authentic local logo: 1", final_report)
            self.assertIn("New duplicate stream URL occurrences: 0", final_report)

    def test_parser_skips_vlc_and_kodi_directives_before_media_url(self):
        text = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-name="Example",Example\n'
            '#EXTVLCOPT:http-user-agent=Mozilla/5.0\n'
            '#KODIPROP:inputstream.adaptive.manifest_type=hls\n'
            'https://cdn.example.test/Path/CaseSensitive.m3u8\n'
        )
        _, entries, malformed = parse_playlist(text)
        self.assertEqual(malformed, [])
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["url"], "https://cdn.example.test/Path/CaseSensitive.m3u8")
        self.assertEqual(entries[0]["end"], 4)

    def test_bd_discovery_parser_skips_vlc_directive_before_media_url(self):
        text = (
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="Demo.bd" tvg-name="Demo",Demo\n'
            '#EXTVLCOPT:http-user-agent=Mozilla/5.0\n'
            'https://cdn.example.test/Demo/live.m3u8\n'
        )
        entries = parse_bd_playlist(text)
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0][2], "https://cdn.example.test/Demo/live.m3u8")

    def test_parser_detects_malformed_extinf_pair(self):
        _, entries, malformed = parse_playlist('#EXTM3U\n#EXTINF:-1 group-title="New Channels",Example\n')
        self.assertEqual(entries, [])
        self.assertEqual(len(malformed), 1)
    def test_duplicate_stream_ids_for_one_channel_do_not_reach_five_channel_threshold(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "International-Playlist.m3u"
            rows = [
                '#EXTINF:-1 tvg-id="MK1.mk" tvg-country="MK" group-title="North Macedonia",Movie One\nhttps://example.org/one.m3u8',
                '#EXTINF:-1 tvg-id="MK2.mk" tvg-country="MK" group-title="North Macedonia",Movie Two\nhttps://example.org/two.m3u8',
                '#EXTINF:-1 tvg-id="MK3.mk" tvg-country="MK" group-title="North Macedonia",Movie Three\nhttps://example.org/three.m3u8',
                '#EXTINF:-1 tvg-id="MK4HD.mk" tvg-country="MK" group-title="North Macedonia",Movie Four HD\nhttps://example.org/four-hd.m3u8',
                '#EXTINF:-1 tvg-id="MK4SD.mk" tvg-country="MK" group-title="International",Movie Four SD\nhttps://example.org/four-sd.m3u8',
            ]
            playlist.write_text("#EXTM3U\n" + "\n".join(rows) + "\n", encoding="utf-8")
            moved = consolidate_international_country_groups(playlist)
            content = playlist.read_text(encoding="utf-8")
            self.assertEqual(len(moved), 4)
            self.assertNotIn('group-title="North Macedonia"', content)
            self.assertEqual(content.count('group-title="International"'), 5)

    def test_five_unique_channels_left_in_international_fail_threshold_gate(self):
        import discover_international_channels as discovery
        rows = [
            [f'#EXTINF:-1 tvg-id="MK{i}.mk" tvg-country="MK" tvg-content="Movies" group-title="International",Movie {i}', f"https://example.org/movie{i}.m3u8"]
            for i in range(1, 6)
        ]
        self.assertTrue(discovery.country_group_threshold_issues(rows))
        for row in rows:
            row[0] = row[0].replace('group-title="International"', 'group-title="North Macedonia"')
        self.assertFalse(discovery.country_group_threshold_issues(rows))



    def test_verified_channels_auto_promote_alternates_go_to_backup_and_inconclusive_go_to_review(self):
        import tempfile
        import validate_discovery_run as validation
        from pathlib import Path

        rows = []
        for i in range(1, 5):
            rows.append(
                f'#EXTINF:-1 tvg-id="PK{i}.pk" tvg-name="Pakistan Primary {i}" tvg-country="PK" group-title="International",Pakistan Primary {i}\n'
                f'https://example.org/pk{i}.m3u8'
            )
        rows.extend([
            '#EXTINF:-1 tvg-id="PK5.pk" tvg-name="Pakistan Primary 5" tvg-country="PK" group-title="New Channels",Pakistan Primary 5\nhttps://example.org/pk5.m3u8',
            '#EXTINF:-1 tvg-id="PK1.pk" tvg-name="Pakistan Primary 1" tvg-country="PK" group-title="New Backups",Pakistan Primary 1 alternate\nhttps://example.org/pk1-alt.m3u8',
            '#EXTINF:-1 tvg-id="IN-Kids.in" tvg-name="Indian Kids Example" tvg-country="IN" tvg-content="Kids" group-title="New Channels",Indian Kids Example\nhttps://example.org/indian-kids.m3u8',
        ])
        _, entries, malformed = parse_playlist("\n".join(rows) + "\n")
        self.assertFalse(malformed)
        verified = {entries[4]["start"], entries[5]["start"]}
        inconclusive = {entries[6]["start"]}
        updates = {}
        decisions = validation.promote_verified_candidates(entries, verified, inconclusive, updates)
        targets = {name: target for name, _old, target, _reason in decisions}
        self.assertEqual(targets["Pakistan Primary 5"], "Pakistani")
        self.assertEqual(targets["Pakistan Primary 1"], "Backup")
        self.assertEqual(targets["Indian Kids Example"], "Review")

        with tempfile.TemporaryDirectory() as directory:
            playlist = Path(directory) / "International-Playlist.m3u"
            text = "#EXTM3U\n" + "\n".join(rows) + "\n"
            lines = text.splitlines()
            for index, updated in updates.items():
                lines[index] = updated
            playlist.write_text("\n".join(lines) + "\n", encoding="utf-8")
            validation.consolidate_international_country_groups(playlist)
            output = playlist.read_text(encoding="utf-8")
        self.assertEqual(output.count('group-title="Pakistani"'), 5)
        self.assertNotIn('group-title="International"', output)
        self.assertIn('group-title="Backup"', output)
        self.assertIn('group-title="Review"', output)

    def test_inconclusive_candidate_without_local_logo_is_preserved_in_review(self):
        import os
        import tempfile
        from unittest.mock import patch
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "International-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            content = (
                '#EXTM3U\n'
                '#PLAYLIST-STUDIO-CATEGORIES:["Bangladesh","Review","New Channels","New Backups","Backup"]\n'
                '#EXTINF:-1 tvg-id="NetworkOneBD.bd" tvg-name="Bangladesh Network One" tvg-country="BD" group-title="New Channels",Bangladesh Network One\n'
                'https://example.org/bd-test.m3u8\n'
            )
            playlist.write_text(content, encoding="utf-8")
            baseline.write_text('#EXTM3U\n', encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
            with patch.object(validation, "probe_url", return_value=("unknown", "HTTP 403")), \
                 patch.object(validation, "ensure_local_logo", side_effect=lambda entry: (entry["extinf"], False, True)):
                validation.probe_mode(str(playlist), str(report), str(baseline), "international")
            output = playlist.read_text(encoding="utf-8")
            self.assertIn('group-title="Review"', output)
            self.assertIn("https://example.org/bd-test.m3u8", output)
            previous = os.environ.get("OFFICIAL_VALIDATOR_OUTCOME")
            os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = "success"
            try:
                validation.final_mode(str(playlist), str(report), str(baseline), "international")
            finally:
                if previous is None:
                    os.environ.pop("OFFICIAL_VALIDATOR_OUTCOME", None)
                else:
                    os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = previous
            self.assertIn("- Validation status: PASS", report.read_text(encoding="utf-8"))


    def test_final_validation_accepts_promoted_foreign_country_group_rows(self):
        import json
        import os
        import tempfile
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "logos").mkdir()
            for i in range(1, 6):
                (root / "logos" / f"albania-movie-{i}.svg").write_text("<svg/>", encoding="utf-8")
            playlist = root / "International-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            registry = ["Albania", "Review", "New Channels", "New Backups", "Backup"]
            rows = []
            for i in range(1, 6):
                rows.append(
                    f'#EXTINF:-1 tvg-id="Movie{i}.al" tvg-name="Albania Movie {i}" tvg-country="AL" '
                    f'tvg-logo="logos/albania-movie-{i}.svg" tvg-content="Movies" group-title="Albania",Albania Movie {i}\n'
                    f'https://example.org/albania-movie-{i}.m3u8'
                )
            content = "#EXTM3U\n#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(registry) + "\n" + "\n".join(rows) + "\n"
            playlist.write_text(content, encoding="utf-8")
            baseline.write_text("#EXTM3U\n", encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
            previous = os.environ.get("OFFICIAL_VALIDATOR_OUTCOME")
            os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = "success"
            old_cwd = Path.cwd()
            os.chdir(root)
            try:
                validation.final_mode(str(playlist), str(report), str(baseline), "international")
            finally:
                os.chdir(old_cwd)
                if previous is None:
                    os.environ.pop("OFFICIAL_VALIDATOR_OUTCOME", None)
                else:
                    os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = previous
            final_report = report.read_text(encoding="utf-8")
            self.assertIn("- Validation status: PASS", final_report)
            self.assertIn("- Geography/content policy issues: 0", final_report)


if __name__ == "__main__":
    unittest.main()
