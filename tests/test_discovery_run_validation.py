import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_discovery_run import NEWS_RE, append_section, classify_response, consolidate_international_country_groups, ensure_local_logo, final_mode, now, parse_playlist
from discover_bd_in_new_queues import parse as parse_bd_playlist


class DiscoveryRunValidationTests(unittest.TestCase):
    def test_fashion_tv_is_global_exception_but_not_generic_fashion_named_channels(self):
        import discover_international_channels as discovery

        target, reason, code = discovery.discovery_eligibility(
            {"tvg-id": "fashiontv.ru", "tvg-country": "RU"},
            "FashionTV Russia",
        )
        self.assertEqual((target, reason, code), ("Fashion TV", None, "RU"))

        target, reason, code = discovery.discovery_eligibility(
            {"tvg-id": "genericfashion.us", "tvg-country": "US"},
            "Generic Fashion Channel",
        )
        self.assertIsNone(target)
        self.assertTrue(reason)

    def test_discovery_report_timestamps_use_bangladesh_offset(self):
        self.assertTrue(now().endswith("+06:00"))

    def test_ensure_local_logo_converts_verified_repo_raw_url_to_relative_path(self):
        import os
        import tempfile
        from validate_discovery_run import RAW_BASE
        with tempfile.TemporaryDirectory() as directory:
            old_cwd = Path.cwd()
            os.chdir(directory)
            try:
                Path("logos").mkdir()
                (Path("logos") / "sample.png").write_bytes(b"authentic-local-logo")
                extinf = f'#EXTINF:-1 tvg-name="Sample" tvg-logo="{RAW_BASE}sample.png" group-title="New Channels",Sample'
                entry = {"name": "Sample", "logo": RAW_BASE + "sample.png", "extinf": extinf}
                updated, localized, unavailable = ensure_local_logo(entry)
                self.assertIn('tvg-logo="logos/sample.png"', updated)
                self.assertTrue(localized)
                self.assertFalse(unavailable)
            finally:
                os.chdir(old_cwd)

    def test_iptv_new_backup_requires_an_already_represented_channel(self):
        import os
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            old_cwd = Path.cwd()
            os.chdir(directory)
            try:
                playlist = Path("IPTV-Playlist.m3u")
                baseline = Path("before.m3u")
                report = Path("report.md")
                prefix = '#EXTM3U\n#PLAYLIST-STUDIO-CATEGORIES:["New Channels","New Backups","Backup","Review"]\n'
                backup = (
                    '#EXTINF:-1 tvg-id="Orphan.in" tvg-name="Orphan" tvg-country="IN" group-title="New Backups",Orphan\n'
                    "https://example.org/orphan.m3u8\n"
                )
                playlist.write_text(prefix + backup, encoding="utf-8")
                baseline.write_text(prefix, encoding="utf-8")
                report.write_text("# Report\n", encoding="utf-8")
                previous = os.environ.get("OFFICIAL_VALIDATOR_OUTCOME")
                os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = "success"
                try:
                    final_mode(str(playlist), str(report), str(baseline), "iptv")
                finally:
                    if previous is None:
                        os.environ.pop("OFFICIAL_VALIDATOR_OUTCOME", None)
                    else:
                        os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = previous
                self.assertIn("- Validation status: FAIL", report.read_text(encoding="utf-8"))
                self.assertIn("New Backups row has no already-represented channel identity: Orphan", report.read_text(encoding="utf-8"))
            finally:
                os.chdir(old_cwd)

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

    def test_final_validation_accepts_pakistani_movie_candidates_with_explicit_genre_tags(self):
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
                '#EXTINF:-1 tvg-id="ATV.pk" tvg-name="ATV (Pakistan)" tvg-country="PK" tvg-content="Movies" tvg-logo="logos/atv.svg" group-title="New Channels",ATV (Pakistan)\nhttps://example.org/atv.m3u8',
                '#EXTINF:-1 tvg-id="BSTV.pk" tvg-name="BSTV (Pakistan)" tvg-country="PK" tvg-content="Movies" tvg-logo="logos/bstv.svg" group-title="New Channels",BSTV (Pakistan)\nhttps://example.org/bstv.m3u8',
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

    def test_iptv_discovery_keeps_new_indian_candidate_with_missing_country_and_no_logo(self):
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
                '#EXTINF:-1 tvg-id="Fresh.in" x-discovery-source-country="BD" group-title="New Channels" tvg-name="Fresh Candidate",Fresh Candidate\n'
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
                ) as logo_repair:
                    validation.probe_mode(str(playlist), str(report), str(baseline), "iptv")
            output = playlist.read_text(encoding="utf-8")
            self.assertIn('group-title="New Channels"', output)
            self.assertIn('tvg-name="Fresh Candidate"', output)
            self.assertIn('tvg-name="Old Queue Row"', output)
            self.assertIn('tvg-id="Fresh.in"', output)
            self.assertIn('x-discovery-source-country="BD"', output)
            self.assertEqual(probe.call_count, 1)
            logo_repair.assert_called_once()
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
            registry = ["Bangladesh", "New Channels", "New Backups", "Backup", "Review"]
            duplicate_existing = (
                '#EXTINF:-1 tvg-name="Old duplicate A" group-title="Bangladesh",Old duplicate A\n'
                'https://example.org/old-duplicate.m3u8\n'
                '#EXTINF:-1 tvg-name="Old duplicate B" group-title="Bangladesh",Old duplicate B\n'
                'https://example.org/old-duplicate.m3u8\n'
            )
            fresh = (
                '#EXTINF:-1 tvg-id="Fresh.in" group-title="New Channels" tvg-name="Fresh Candidate",Fresh Candidate\n'
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

    def test_final_iptv_validation_blocks_prohibited_legacy_indian_queue_rows(self):
        import os
        import tempfile
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "IPTV-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            registry = ["Bangladesh", "New Channels", "New Backups", "Backup", "Review"]
            prefix = "#EXTM3U\n#PLAYLIST-STUDIO-CATEGORIES:" + __import__("json").dumps(registry) + "\n"
            legacy = (
                '#EXTINF:-1 tvg-id="SonyYay.in@SD" tvg-name="Sony Yay!" group-title="New Backups",Sony Yay!\n'
                "https://example.org/sony-yay.m3u8\n"
            )
            playlist.write_text(prefix + legacy, encoding="utf-8")
            baseline.write_text(prefix + legacy, encoding="utf-8")
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
            self.assertIn("- Validation status: FAIL", final_report)
            self.assertIn("Prohibited Indian queue row: Sony Yay!", final_report)
            self.assertIn("Out-of-scope/prohibited Indian rows remaining in New Channels/New Backups: 1", final_report)

    def test_final_iptv_validation_blocks_foreign_country_queue_rows(self):
        import os
        import tempfile
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "IPTV-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            registry = ["Bangladesh", "New Channels", "New Backups", "Backup", "Review"]
            prefix = "#EXTM3U\n#PLAYLIST-STUDIO-CATEGORIES:" + __import__("json").dumps(registry) + "\n"
            foreign = (
                '#EXTINF:-1 tvg-id="BTLTV.nl@SD" x-discovery-source-country="BD" '
                'group-title="New Channels" tvg-name="BTL TV",BTL TV\n'
                "https://example.org/btl.m3u8\n"
            )
            playlist.write_text(prefix + foreign, encoding="utf-8")
            baseline.write_text(prefix, encoding="utf-8")
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
            self.assertIn("- Validation status: FAIL", final_report)
            self.assertIn("Out-of-scope queue row: BTL TV", final_report)
            self.assertIn("explicit country NL is outside Bangladesh/India", final_report)

    def test_iptv_inconclusive_backup_moves_to_review_not_new_backups(self):
        import tempfile
        from unittest.mock import patch
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "IPTV-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            registry = ["Bangladesh", "New Channels", "New Backups", "Backup", "Review"]
            content = (
                "#EXTM3U\n"
                "#PLAYLIST-STUDIO-CATEGORIES:" + __import__("json").dumps(registry) + "\n"
                '#EXTINF:-1 tvg-id="Travelxp.in@4KHDR" tvg-country="IN" group-title="New Backups" tvg-name="Travelxp",Travelxp\n'
                "https://example.org/travelxp.m3u8\n"
            )
            playlist.write_text(content, encoding="utf-8")
            baseline.write_text("#EXTM3U\n", encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
            with patch.object(validation, "probe_url", return_value=("unknown", "HTTP 403")):
                validation.probe_mode(str(playlist), str(report), str(baseline), "iptv")
            output = playlist.read_text(encoding="utf-8")
            self.assertIn('group-title="Review"', output)
            self.assertIn('x-discovery-hold-reason="unverified-backup-stream"', output)
            self.assertNotIn('group-title="New Backups"', output)
            self.assertIn("Moved unverified alternate stream Travelxp from New Backups to Review", report.read_text(encoding="utf-8"))

    def test_final_iptv_validation_allows_explicitly_tagged_unverified_backup_review_hold(self):
        import os
        import tempfile
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "IPTV-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            registry = ["Bangladesh", "New Channels", "New Backups", "Backup", "Review"]
            content = (
                "#EXTM3U\n"
                "#PLAYLIST-STUDIO-CATEGORIES:" + __import__("json").dumps(registry) + "\n"
                '#EXTINF:-1 tvg-id="Travelxp.in@4KHDR" tvg-country="IN" x-discovery-hold-reason="unverified-backup-stream" group-title="Review" tvg-name="Travelxp",Travelxp\n'
                "https://example.org/travelxp.m3u8\n"
            )
            playlist.write_text(content, encoding="utf-8")
            baseline.write_text("#EXTM3U\n", encoding="utf-8")
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
            self.assertIn("New candidates outside New Channels/New Backups or approved Review holds: 0", final_report)

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



    def test_raw_repository_logo_url_resolves_to_local_asset(self):
        import tempfile
        import validate_discovery_run as validation
        from unittest.mock import patch

        with tempfile.TemporaryDirectory() as directory:
            logos = Path(directory) / "logos"
            logos.mkdir()
            asset = logos / "test-logo.png"
            asset.write_bytes(b"authentic local logo")
            with patch.object(validation, "LOGOS", logos):
                path = validation.local_logo_path(validation.RAW_BASE + "test-logo.png")
            self.assertEqual(path, asset)
            self.assertTrue(path.is_file())

    def test_international_probe_keeps_verified_candidates_in_discovery_queues(self):
        import tempfile
        from unittest.mock import patch
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "International-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            prefix = (
                "#EXTM3U\n"
                '#PLAYLIST-STUDIO-CATEGORIES:["International","Review","New Channels","New Backups","Backup"]\n'
            )
            rows = (
                '#EXTINF:-1 tvg-id="WorldMovie.us" tvg-name="World Movie" tvg-country="US" tvg-content="Movies" tvg-logo="logos/world-movie.svg" group-title="New Channels",World Movie\n'
                'https://example.org/world-movie.m3u8\n'
                '#EXTINF:-1 tvg-id="WorldMusic.us" tvg-name="World Music" tvg-country="US" tvg-content="Music" tvg-logo="logos/world-music.svg" group-title="New Backups",World Music\n'
                'https://example.org/world-music.m3u8\n'
            )
            playlist.write_text(prefix + rows, encoding="utf-8")
            baseline.write_text(prefix, encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
            with patch.object(validation, "probe_url", side_effect=[
                ("verified", "Media bytes received"),
                ("verified", "Media bytes received"),
            ]), patch.object(
                validation, "ensure_local_logo",
                side_effect=lambda entry: (entry["extinf"], False, False),
            ), patch.object(
                validation, "promote_verified_candidates",
                side_effect=AssertionError("automatic promotion must not run"),
            ):
                validation.probe_mode(str(playlist), str(report), str(baseline), "international")
            output = playlist.read_text(encoding="utf-8")
            self.assertIn('group-title="New Channels"', output)
            self.assertIn('group-title="New Backups"', output)
            self.assertNotIn('group-title="Backup"', output)
            result = report.read_text(encoding="utf-8")
            self.assertIn("Verified new primary channels retained in New Channels: 1", result)
            self.assertIn("Verified alternate streams retained in New Backups: 1", result)

    def test_international_probe_keeps_valid_candidate_without_logo_in_new_channels(self):
        import tempfile
        from unittest.mock import patch
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "International-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            prefix = (
                "#EXTM3U\n"
                '#PLAYLIST-STUDIO-CATEGORIES:["International","Review","New Channels","New Backups","Backup"]\n'
            )
            row = (
                '#EXTINF:-1 tvg-id="NoLogoMovie.us" tvg-name="No Logo Movie" tvg-country="US" tvg-content="Movies" group-title="New Channels",No Logo Movie\n'
                'https://example.org/no-logo-movie.m3u8\n'
            )
            playlist.write_text(prefix + row, encoding="utf-8")
            baseline.write_text(prefix, encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
            with patch.object(validation, "probe_url", return_value=("verified", "Media bytes received")), patch.object(
                validation, "ensure_local_logo",
                side_effect=lambda entry: (entry["extinf"], False, True),
            ):
                validation.probe_mode(str(playlist), str(report), str(baseline), "international")
            output = playlist.read_text(encoding="utf-8")
            self.assertIn('group-title="New Channels"', output)
            self.assertNotIn('tvg-logo=""', output)
            self.assertIn("without tvg-logo", report.read_text(encoding="utf-8"))

    def test_legacy_promotion_helper_is_disabled(self):
        import validate_discovery_run as validation

        row = (
            '#EXTINF:-1 tvg-id="PK1.pk" tvg-name="Pakistan Primary 1" tvg-country="PK" '
            'tvg-content="Movies" group-title="New Channels",Pakistan Primary 1\n'
            'https://example.org/pk1.m3u8'
        )
        _, entries, malformed = parse_playlist(row)
        self.assertFalse(malformed)
        updates = {}
        decisions = validation.promote_verified_candidates(
            entries, {entries[0]["start"]}, set(), updates
        )
        self.assertEqual(decisions, [])
        self.assertEqual(updates, {})

    def test_legacy_promotion_helper_does_not_change_missing_country_candidate(self):
        import validate_discovery_run as validation

        row = (
            '#EXTINF:-1 tvg-id="MysteryCinema" tvg-name="Mystery Cinema" '
            'tvg-logo="logos/mystery-cinema.svg" tvg-content="Movies" '
            'group-title="New Channels",Mystery Cinema\nhttps://example.org/mystery.m3u8'
        )
        _, entries, malformed = parse_playlist(row)
        self.assertFalse(malformed)
        updates = {}
        decisions = validation.promote_verified_candidates(
            entries, {entries[0]["start"]}, set(), updates
        )
        self.assertEqual(decisions, [])
        self.assertEqual(updates, {})

    def test_legacy_promotion_helper_does_not_change_candidate_without_local_logo(self):
        import validate_discovery_run as validation

        row = (
            '#EXTINF:-1 tvg-id="MCMPop.fr" tvg-name="MCM Pop" tvg-country="FR" '
            'group-title="New Channels",MCM Pop\nhttps://example.org/mcm-pop.m3u8'
        )
        _, entries, malformed = parse_playlist(row)
        self.assertFalse(malformed)
        updates = {}
        decisions = validation.promote_verified_candidates(
            entries, {entries[0]["start"]}, set(), updates
        )
        self.assertEqual(decisions, [])
        self.assertEqual(updates, {})

    def test_definitively_dead_candidate_is_not_reported_as_promoted_to_review(self):
        import validate_discovery_run as validation
        row = (
            '#EXTINF:-1 tvg-id="DeadMovie.us" tvg-name="Dead Movie" tvg-country="US" '
            'group-title="New Channels",Dead Movie\nhttps://example.org/dead.m3u8'
        )
        _, entries, malformed = parse_playlist(row)
        self.assertFalse(malformed)
        decisions = validation.promote_verified_candidates(
            entries, set(), set(), {}, {entries[0]["start"]}
        )
        self.assertEqual(decisions, [])

    def test_inconclusive_movie_candidate_without_local_logo_is_preserved_in_new_channels(self):
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
                '#EXTINF:-1 tvg-id="NetworkOneBD.bd" tvg-name="Bangladesh Network One" tvg-country="BD" tvg-content="Movies" group-title="New Channels",Bangladesh Network One\n'
                'https://example.org/bd-test.m3u8\n'
            )
            playlist.write_text(content, encoding="utf-8")
            baseline.write_text('#EXTM3U\n', encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
            with patch.object(validation, "probe_url", return_value=("unknown", "HTTP 403")), \
                 patch.object(validation, "ensure_local_logo", side_effect=lambda entry: (entry["extinf"], False, True)):
                validation.probe_mode(str(playlist), str(report), str(baseline), "international")
            output = playlist.read_text(encoding="utf-8")
            self.assertIn('group-title="New Channels"', output)
            self.assertNotIn('group-title="Review"', output)
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


    def test_final_validation_accepts_new_backup_for_channel_in_review(self):
        import json
        import os
        import tempfile
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "International-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            registry = ["International", "Review", "New Channels", "New Backups", "Backup"]
            prefix = "#EXTM3U\n#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(registry) + "\n"
            existing = (
                '#EXTINF:-1 tvg-id="stargold.in" tvg-name="Star Gold" tvg-country="IN" tvg-content="Movies" group-title="Review",Star Gold\n'
                "https://example.org/star-gold-old.m3u8\n"
            )
            backup = (
                '#EXTINF:-1 tvg-id="stargold.in" tvg-name="Star Gold" tvg-country="IN" tvg-content="Movies" group-title="New Backups",Star Gold\n'
                "https://example.org/star-gold-new.m3u8\n"
            )
            baseline.write_text(prefix + existing, encoding="utf-8")
            playlist.write_text(prefix + existing + backup, encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
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

    def test_final_validation_rejects_new_backup_without_existing_channel(self):
        import json
        import os
        import tempfile
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "International-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            registry = ["International", "Review", "New Channels", "New Backups", "Backup"]
            prefix = "#EXTM3U\n#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(registry) + "\n"
            backup = (
                '#EXTINF:-1 tvg-id="stargold.in" tvg-name="Star Gold" tvg-country="IN" tvg-content="Movies" group-title="New Backups",Star Gold\n'
                "https://example.org/star-gold-new.m3u8\n"
            )
            baseline.write_text(prefix, encoding="utf-8")
            playlist.write_text(prefix + backup, encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
            previous = os.environ.get("OFFICIAL_VALIDATOR_OUTCOME")
            os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = "success"
            try:
                validation.final_mode(str(playlist), str(report), str(baseline), "international")
            finally:
                if previous is None:
                    os.environ.pop("OFFICIAL_VALIDATOR_OUTCOME", None)
                else:
                    os.environ["OFFICIAL_VALIDATOR_OUTCOME"] = previous
            final_report = report.read_text(encoding="utf-8")
            self.assertIn("- Validation status: FAIL", final_report)
            self.assertIn("New Backups row has no already-represented channel identity: Star Gold", final_report)

    def test_final_validation_rejects_new_candidates_promoted_out_of_queues(self):
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
            self.assertIn("- Validation status: FAIL", final_report)
            self.assertIn("new International candidates must remain in New Channels/New Backups", final_report)
            self.assertIn("- Geography/content policy issues: 0", final_report)


    def test_international_final_validation_accepts_fashion_tv_exception(self):
        import json
        import os
        import tempfile
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "International-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            registry = ["Fashion TV", "Review", "New Channels", "New Backups", "Backup"]
            row = (
                '#EXTINF:-1 tvg-id="FashionTV.fr" tvg-name="Fashion TV" tvg-country="FR" '
                'group-title="Fashion TV",Fashion TV\n'
                'https://example.org/fashion-tv.m3u8\n'
            )
            playlist.write_text(
                "#EXTM3U\n#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(registry) + "\n" + row,
                encoding="utf-8",
            )
            baseline.write_text("#EXTM3U\n", encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
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

    def test_international_final_validation_accepts_adult_group_exception(self):
        import json
        import os
        import tempfile
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            playlist = root / "International-Playlist.m3u"
            baseline = root / "baseline.m3u"
            report = root / "report.md"
            registry = ["Adult", "Review", "New Channels", "New Backups", "Backup"]
            row = (
                '#EXTINF:-1 tvg-id="adult.us" tvg-name="Adult Channel" tvg-country="US" '
                'tvg-content="Adult" group-title="Adult",Adult Channel\n'
                'https://example.org/adult.m3u8\n'
            )
            playlist.write_text(
                "#EXTM3U\n#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(registry) + "\n" + row,
                encoding="utf-8",
            )
            baseline.write_text("#EXTM3U\n", encoding="utf-8")
            report.write_text("# Report\n", encoding="utf-8")
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

    def test_international_probe_keeps_fashion_tv_and_stably_reorders_review_holds(self):
        from validate_discovery_run import stable_group_order

        registry = ["Fashion TV", "Review", "New Channels", "New Backups", "Backup"]
        lines = [
            "#EXTM3U",
            "#PLAYLIST-STUDIO-CATEGORIES:" + __import__("json").dumps(registry),
            '#EXTINF:-1 group-title="New Backups" tvg-name="Fashion TV",Fashion TV',
            "https://example.org/fashion-backup.m3u8",
            '#EXTINF:-1 group-title="Fashion TV" tvg-name="FashionTV Europe",FashionTV Europe',
            "https://example.org/fashion-europe.m3u8",
            '#EXTINF:-1 group-title="Review" tvg-name="Existing Review",Existing Review',
            "https://example.org/review.m3u8",
        ]
        ordered = stable_group_order(lines)
        groups = [
            line.split('group-title="', 1)[1].split('"', 1)[0]
            for line in ordered if line.startswith("#EXTINF:")
        ]
        self.assertEqual(groups, ["Fashion TV", "Review", "New Backups"])
        self.assertLess(
            next(i for i, line in enumerate(ordered) if 'tvg-name="FashionTV Europe"' in line),
            next(i for i, line in enumerate(ordered) if 'tvg-name="Existing Review"' in line),
        )

    def test_logo_lookup_restores_only_one_exact_local_match(self):
        import os
        import tempfile
        import validate_discovery_run as validation

        with tempfile.TemporaryDirectory() as directory:
            old_cwd = Path.cwd()
            os.chdir(directory)
            try:
                logos = Path("logos")
                (logos / "one").mkdir(parents=True)
                (logos / "one" / "fashion-tv.svg").write_text("<svg/>", encoding="utf-8")
                self.assertEqual(validation.find_logo("Fashion TV"), "logos/one/fashion-tv.svg")
                (logos / "two").mkdir()
                (logos / "two" / "fashion-tv.png").write_bytes(b"duplicate exact-name asset")
                self.assertIsNone(validation.find_logo("Fashion TV"))
            finally:
                os.chdir(old_cwd)

if __name__ == "__main__":
    unittest.main()
