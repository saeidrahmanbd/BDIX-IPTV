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
        self.assertEqual(stats["not_streaming_to_review"], 1)
        self.assertIn("https://example.test/movies.m3u8", updated)

if __name__ == "__main__":
    unittest.main()
