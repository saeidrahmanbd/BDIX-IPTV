import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.international.candidate_engine import GroupChange, build_candidate, assert_international_existing_rows_preserved

BASE = '#EXTM3U\n#EXTINF:-1 tvg-id="x" tvg-chno="1" group-title="Nepal",A\nhttps://a.example/a.m3u8\n#EXTINF:-1 tvg-id="y" tvg-chno="2" group-title="Nepal",B\nhttps://b.example/b.m3u8\n'

class InternationalCandidateEngineTests(unittest.TestCase):
    def test_group_change_preserves_stream_and_metadata(self):
        result=build_candidate(BASE,[GroupChange(0,"Review","first failed probe")])
        self.assertIn('group-title="Review"',result)
        self.assertIn('https://a.example/a.m3u8',result)
        self.assertIn('tvg-id="x"',result)

    def test_three_day_review_decision_does_not_delete(self):
        result=build_candidate(BASE,[GroupChange(1,"Review","removal review only")])
        self.assertEqual(result.count("#EXTINF:"),2)
        self.assertEqual(result.count("https://"),2)

    def test_duplicate_row_change_rejected(self):
        with self.assertRaisesRegex(ValueError,"duplicate group change"):
            build_candidate(BASE,[GroupChange(0,"Review","x"),GroupChange(0,"Backup","y")])

    def test_out_of_range_row_rejected(self):
        with self.assertRaisesRegex(ValueError,"out of range"):
            build_candidate(BASE,[GroupChange(5,"Review","x")])

    def test_missing_header_rejected(self):
        with self.assertRaisesRegex(ValueError,"#EXTM3U"):
            build_candidate("not a playlist",[GroupChange(0,"Review","x")])

    def test_unsafe_group_value_rejected(self):
        with self.assertRaisesRegex(ValueError,"single line"):
            build_candidate(BASE,[GroupChange(0,'Bad"Group',"unsafe")])

    def test_unchanged_input_returns_identical_text(self):
        self.assertEqual(build_candidate(BASE,[]),BASE)


    def test_preservation_guard_allows_group_only_change_to_existing_row(self):
        changed=build_candidate(BASE,[GroupChange(0,"Bangladesh","verified Review recovery")])
        assert_international_existing_rows_preserved(BASE,changed)

    def test_preservation_guard_allows_new_rows_only_in_manual_review_queues(self):
        candidate=(
            '#EXTM3U\n'
            '#EXTINF:-1 tvg-id="x" tvg-chno="1" group-title="Bangladesh",A\nhttps://a.example/a.m3u8\n'
            '#EXTINF:-1 tvg-id="new" group-title="New Channels",New\nhttps://new.example/live\n'
            '#EXTINF:-1 tvg-id="y" tvg-chno="2" group-title="Nepal",B\nhttps://b.example/b.m3u8\n'
        )
        assert_international_existing_rows_preserved(BASE,candidate)

    def test_preservation_guard_rejects_new_primary_row(self):
        candidate=BASE+'#EXTINF:-1 tvg-id="new" group-title="Nepal",New\nhttps://new.example/live\n'
        with self.assertRaisesRegex(ValueError,"outside manual-review queues"):
            assert_international_existing_rows_preserved(BASE,candidate)


    def test_preservation_guard_rejects_duplicate_existing_url_in_review_queue(self):
        candidate=BASE+'#EXTINF:-1 tvg-id="x" group-title="New Channels",Duplicate\nhttps://a.example/a.m3u8\n'
        with self.assertRaisesRegex(ValueError,"duplicated or displaced"):
            assert_international_existing_rows_preserved(BASE,candidate)


    def test_policy_authorized_removal_removes_only_the_failed_identity(self):
        candidate=build_candidate(BASE,[],{"x"})
        self.assertEqual(candidate.count("#EXTINF:"),1)
        self.assertNotIn('tvg-id="x"',candidate)
        self.assertIn('tvg-id="y"',candidate)

    def test_backup_rows_are_protected_from_automatic_removal(self):
        backup=BASE.replace('group-title="Nepal"','group-title="Backup"')
        with self.assertRaisesRegex(ValueError,"protected"):
            build_candidate(backup,[],{"x"})

    def test_removal_identity_must_exist_exactly_once(self):
        with self.assertRaisesRegex(ValueError,"exactly one"):
            build_candidate(BASE,[],{"missing"})

if __name__=="__main__":
    unittest.main()
