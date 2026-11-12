import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import migrate_owner_requested_main_queues as migration

class OwnerRequestedMigrationTests(unittest.TestCase):
    def test_identity_key_ignores_quality_suffix(self):
        self.assertEqual(migration.id_key("ZeeTV.in@HD"), migration.id_key("ZeeTV.in@SD"))

    def test_name_key_ignores_resolution_and_quality(self):
        self.assertEqual(migration.name_key("Movies Now HD (576p)"), migration.name_key("Movies Now"))

    def test_display_normalization_removes_quality_prefixes_and_suffixes(self):
        self.assertEqual(migration.normalized_label("IN | Movies Now HD (576p)"), "Movies Now")
        self.assertEqual(migration.normalized_label("TamilVision-TV (1080p)"), "TamilVision TV")

    def test_indian_movie_music_kids_and_sports_groups(self):
        self.assertEqual(migration.target_group({"tvg-country":"IN","tvg-language":"hin"}, "Movies Now", 18), "Indian Movies")
        self.assertEqual(migration.target_group({"tvg-country":"IN","tvg-language":"ben"}, "KTV Bangla", 18), "Indian Bangla")
        self.assertEqual(migration.target_group({"tvg-country":"IN"}, "ZB Cartoon", 18), "Kids")
        self.assertEqual(migration.target_group({"tvg-country":"IN"}, "DD Sports", 18), "Sports")

    def test_nonstreaming_candidate_moves_only_to_review(self):
        text = "\n".join([
            '#EXTM3U',
            '#PLAYLIST-STUDIO-CATEGORIES:["Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani","International","Documentary & Wildlife","Kids","Religious","Sports","Backup","New Channels","New Backups","Review"]',
            '#EXTINF:-1 tvg-id="MoviesNow.in@HD" tvg-name="Movies Now HD (576p)" tvg-logo="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/movies-now.png" tvg-country="IN" tvg-language="hin" group-title="New Channels",Movies Now HD (576p)',
            'https://example.test/movies.m3u8',
            ''
        ])
        probe_data = {"results":[{"url":"https://example.test/movies.m3u8","ok":False,"status":404,"error":"HTTP 404"}]}
        updated, stats, changes, approvals = migration.migrate(text, probe_data)
        self.assertIn('group-title="Review"', updated)
        self.assertEqual(stats["definitive_offline_to_review"], 1)
        self.assertIn("https://example.test/movies.m3u8", updated)


    def test_reachable_unclassified_orphan_stays_in_new_channels_not_review(self):
        text = "\n".join([
            '#EXTM3U',
            '#PLAYLIST-STUDIO-CATEGORIES:["Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani","International","Documentary & Wildlife","Kids","Religious","Sports","Backup","New Channels","New Backups","Review"]',
            '#EXTINF:-1 tvg-id="custom.unknownservice" channel-id="custom.unknownservice" tvg-name="Unknown Service" tvg-logo="https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/unknown-service.png" tvg-country="" tvg-language="und" group-title="Backup",Unknown Service',
            'https://example.test/unknown.m3u8',
            ''
        ])
        probe_data = {"results":[{"url":"https://example.test/unknown.m3u8","ok":True,"status":200,"bytes":512,"error":""}]}
        updated, stats, changes, approvals = migration.migrate(text, probe_data)
        self.assertIn('group-title="New Channels"', updated)
        self.assertNotIn('group-title="Review"', updated)
        self.assertEqual(stats["unverified_orphans_staged_for_manual_review"], 1)


    def test_wrong_country_queue_candidate_is_not_promoted(self):
        text = "\n".join([
            '#EXTM3U',
            '#PLAYLIST-STUDIO-CATEGORIES:["Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani","International","Documentary & Wildlife","Kids","Religious","Sports","Backup","New Channels","New Backups","Review"]',
            '#EXTINF:-1 tvg-id="MoviesNow.in@HD" channel-id="MoviesNow.in@HD" tvg-name="Movies Now" tvg-country="US" tvg-language="hin" group-title="New Channels",Movies Now',
            'https://example.test/movies.m3u8',
            ''
        ])
        probe_data = {"results":[{"url":"https://example.test/movies.m3u8","ok":True,"status":200,"bytes":512,"error":""}]}
        updated, stats, changes, approvals = migration.migrate(text, probe_data)
        self.assertIn('group-title="New Channels"', updated)
        self.assertNotIn('group-title="Indian Movies"', updated)
        self.assertEqual(stats["unverified_queue_candidates_deferred"], 1)


    def test_access_restricted_candidate_is_deferred_not_quarantined(self):
        text = "\n".join([
            '#EXTM3U',
            '#PLAYLIST-STUDIO-CATEGORIES:["Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani","International","Documentary & Wildlife","Kids","Religious","Sports","Backup","New Channels","New Backups","Review"]',
            '#EXTINF:-1 tvg-id="MoviesNow.in@HD" channel-id="MoviesNow.in@HD" tvg-name="Movies Now" tvg-country="IN" tvg-language="hin" group-title="New Channels",Movies Now',
            'https://example.test/movies.m3u8',
            ''
        ])
        probe_data = {"results":[{"url":"https://example.test/movies.m3u8","ok":False,"status":403,"error":"HTTP 403"}]}
        updated, stats, changes, approvals = migration.migrate(text, probe_data)
        self.assertIn('group-title="New Channels"', updated)
        self.assertNotIn('group-title="Review"', updated)
        self.assertEqual(stats["inconclusive_probe_deferred"], 1)


    def test_existing_review_entry_metadata_and_stream_url_are_preserved(self):
        review_info = '#EXTINF:-1 tvg-id="custom.review" tvg-name="Review Channel HD (720p)" tvg-chno="777" channel-id="custom.review" group-title="Review",Review Channel HD (720p)'
        text = "\n".join([
            '#EXTM3U',
            '#PLAYLIST-STUDIO-CATEGORIES:["Bangladesh","Indian Bangla","Indian Movies","Indian Music","Indian Entertainment","Pakistani","International","Documentary & Wildlife","Kids","Religious","Sports","Backup","New Channels","New Backups","Review"]',
            review_info,
            'https://example.test/review.m3u8',
            ''
        ])
        updated, stats, changes, approvals = migration.migrate(text, {"results":[]})
        self.assertIn(review_info, updated)
        self.assertIn('https://example.test/review.m3u8', updated)

if __name__ == "__main__":
    unittest.main()
