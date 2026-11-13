import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "automation/engines/international"))
from country_groups import ChannelIdentity, eligible_country_groups, should_create_country_group

class CountryGroupPolicyTests(unittest.TestCase):
    def test_five_unique_primary_identities_create_group(self):
        rows=[ChannelIdentity(f"id-{i}","Nepal") for i in range(5)]
        self.assertIn("Nepal",eligible_country_groups(rows))

    def test_four_identities_do_not_create_group(self):
        rows=[ChannelIdentity(f"id-{i}","Nepal") for i in range(4)]
        self.assertNotIn("Nepal",eligible_country_groups(rows))

    def test_duplicate_streams_for_same_identity_count_once(self):
        rows=[ChannelIdentity("same","Nepal") for _ in range(5)]
        self.assertNotIn("Nepal",eligible_country_groups(rows))

    def test_backup_review_and_discovery_do_not_count(self):
        rows=[ChannelIdentity(f"id-{i}","Nepal",is_primary=False) for i in range(5)]
        rows += [ChannelIdentity(f"queue-{i}",group) for i,group in enumerate(["Backup","Review","New Channels","New Backups","Backup"])]
        self.assertEqual(eligible_country_groups(rows),set())

    def test_group_names_are_case_insensitive(self):
        rows=[ChannelIdentity(f"id-{i}", "Nepal" if i<3 else "nepal") for i in range(5)]
        self.assertTrue(should_create_country_group("NEPAL", rows))

    def test_bangladesh_and_india_are_fixed_groups(self):
        self.assertTrue(should_create_country_group("Bangladesh",[]))
        self.assertTrue(should_create_country_group("India",[]))


    def test_genre_and_catch_all_groups_never_count_as_countries(self):
        rows = [
            ChannelIdentity(f"id-{i}", group)
            for i, group in enumerate([
                "International", "Sports", "Kids", "Documentary & Wildlife",
                "Indian Movies", "Indian Music", "Religious", "Fashion TV",
            ])
        ]
        self.assertEqual(eligible_country_groups(rows), set())

if __name__=="__main__":
    unittest.main()
