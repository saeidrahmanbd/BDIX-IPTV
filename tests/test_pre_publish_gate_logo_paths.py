import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from pre_publish_gate import referenced_logo_file, referenced_logo_relative_path, review_state, logo_audit, LOCAL_BASE, EXCLUDE, REVIEW_QUEUES, identity_key, parse


class PrePublishLogoPathTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "logos"
        self.root.mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def test_plural_new_backups_is_a_protected_review_queue_not_a_primary_group(self):
        self.assertIn("New Backups", EXCLUDE)
        self.assertIn("New Backups", REVIEW_QUEUES)
        self.assertIn("New Backup", REVIEW_QUEUES)

    def test_indian_discovery_genre_policy_does_not_block_existing_playlist_rows(self):
        entries = [
            ("", {"tvg-name": "BHI Channel", "tvg-id": "BHI.Channel.in", "tvg-country": "IN", "group-title": "Indian Bangla"}, "https://example.invalid/bhi.m3u8"),
            ("", {"tvg-name": "Disney Channel", "tvg-id": "DisneyChannel.in@HD", "tvg-country": "IN", "group-title": "Backup"}, "https://example.invalid/disney.m3u8"),
            ("", {"tvg-name": "Shekinah TV", "tvg-id": "ShekinahTV.in@SD", "tvg-country": "IN", "group-title": "Review"}, "https://example.invalid/shekinah.m3u8"),
        ]
        state = review_state(entries)
        self.assertEqual(len(state), 2)
        self.assertIn("https://example.invalid/disney.m3u8", state)
        self.assertIn("https://example.invalid/shekinah.m3u8", state)

    def test_current_indian_kids_and_news_rows_are_not_gate_policy_errors(self):
        playlist = Path(__file__).resolve().parents[1] / "IPTV-Playlist.m3u"
        entries = parse(playlist.read_text(encoding="utf-8-sig"))
        # The pre-publish gate validates integrity, not the discovery-only genre policy.
        self.assertTrue(any(a.get("group-title") == "Kids" for _, a, _ in entries))
    def test_missing_logo_in_not_playing_is_advisory_but_active_group_is_blocking(self):
        not_playing = [(
            '#EXTINF:-1 tvg-name="Vyas Channel" group-title="Not Playing",Vyas Channel',
            {"tvg-name": "Vyas Channel", "group-title": "Not Playing"},
            "https://example.invalid/vyas.m3u8",
        )]
        missing, review_missing, external, bad = logo_audit(not_playing)
        self.assertEqual(missing, [])
        self.assertEqual(review_missing, ["Vyas Channel"])
        active = [(
            '#EXTINF:-1 tvg-name="Active Channel" group-title="Indian Movies",Active Channel',
            {"tvg-name": "Active Channel", "group-title": "Indian Movies"},
            "https://example.invalid/active.m3u8",
        )]
        missing, review_missing, external, bad = logo_audit(active)
        self.assertEqual(missing, ["Active Channel"])
        self.assertEqual(review_missing, [])

    def test_authorized_permanent_removal_is_not_reported_as_review_queue_deletion(self):
        info = '#EXTINF:-1 tvg-name="Aaj Tak" group-title="Not Playing",Aaj Tak'
        entries = [(info, {"tvg-name": "Aaj Tak", "group-title": "Not Playing"}, "https://example.invalid/aajtak.m3u8")]
        self.assertEqual(review_state(entries), {})

    def test_indian_discovery_policy_does_not_unprotect_existing_queue_rows(self):
        info = '#EXTINF:-1 tvg-id="DishaTV.in@SD" tvg-name="Disha TV" group-title="New Backups",Disha TV'
        entries = [(info, {"tvg-id": "DishaTV.in@SD", "tvg-name": "Disha TV", "group-title": "New Backups"}, "https://example.invalid/disha.m3u8")]
        self.assertIn("https://example.invalid/disha.m3u8", review_state(entries))

    def test_explicit_bangladesh_queue_country_is_not_overridden_by_indian_alias(self):
        info = '#EXTINF:-1 tvg-country="BD" tvg-id="DishaTV.in@SD" tvg-name="Disha TV" group-title="New Backups",Disha TV'
        attrs = {"tvg-country": "BD", "tvg-id": "DishaTV.in@SD", "tvg-name": "Disha TV", "group-title": "New Backups"}
        entries = [(info, attrs, "https://example.invalid/disha-bd.m3u8")]
        self.assertIn("https://example.invalid/disha-bd.m3u8", review_state(entries))

    def test_unapproved_review_entry_remains_in_protected_review_state(self):
        info = '#EXTINF:-1 tvg-name="Sample Channel" group-title="Backup",Sample Channel'
        entries = [(info, {"tvg-name": "Sample Channel", "group-title": "Backup"}, "https://example.invalid/sample.m3u8")]
        state = review_state(entries)
        self.assertIn("https://example.invalid/sample.m3u8", state)

    def test_nested_logo_asset_preserves_subdirectory_and_query_is_ignored(self):
        path = self.root / "international" / "music" / "channel.png"
        path.parent.mkdir(parents=True)
        path.write_bytes(b"png")
        url = LOCAL_BASE + "international/music/channel.png?raw=1"
        self.assertEqual(referenced_logo_relative_path(url), Path("international/music/channel.png"))
        self.assertEqual(referenced_logo_file(url, self.root), path.resolve())

    def test_canonical_github_raw_url_resolves_to_local_logo(self):
        path = self.root / "channel.png"
        path.write_bytes(b"png")
        url = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/channel.png"
        self.assertEqual(referenced_logo_relative_path(url), Path("channel.png"))
        self.assertEqual(referenced_logo_file(url, self.root), path.resolve())
        self.assertEqual(logo_audit([("", {"tvg-name": "Channel", "group-title": "Bangladesh", "tvg-logo": url}, "")])[2], [])

    def test_identity_key_ignores_hd_sd_quality_suffix(self):
        self.assertEqual(identity_key("AnandaTV.bd@HD"), identity_key("AnandaTV.bd@SD"))
        self.assertEqual(identity_key("DangalTV.in@SD@dangal.tv"), identity_key("DangalTV.in@HD"))

    def test_root_level_logo_still_resolves(self):
        path = self.root / "channel.png"
        path.write_bytes(b"png")
        url = LOCAL_BASE + "channel.png"
        self.assertEqual(referenced_logo_file(url, self.root), path.resolve())

    def test_encoded_filename_is_decoded(self):
        path = self.root / "channel logo.png"
        path.write_bytes(b"png")
        url = LOCAL_BASE + "channel%20logo.png"
        self.assertEqual(referenced_logo_file(url, self.root), path.resolve())

    def test_path_traversal_is_rejected(self):
        self.assertIsNone(referenced_logo_relative_path(LOCAL_BASE + "../secrets.txt"))
        self.assertIsNone(referenced_logo_file(LOCAL_BASE + "../secrets.txt", self.root))

    def test_non_repository_logo_is_not_resolved_as_local(self):
        self.assertIsNone(referenced_logo_file("https://example.invalid/logos/channel.png", self.root))


if __name__ == "__main__":
    unittest.main()
