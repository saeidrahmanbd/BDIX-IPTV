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

    def test_bangladesh_and_india_are_fixed_groups(self):
        self.assertTrue(should_create_country_group("Bangladesh",[]))
        self.assertTrue(should_create_country_group("India",[]))

if __name__=="__main__":
    unittest.main()
