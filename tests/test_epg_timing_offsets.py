"""Accuracy tests for cross-source XMLTV timezone correction."""
from datetime import datetime, timedelta, timezone
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import generate_epg


class SourceOffsetAccuracyTests(unittest.TestCase):
    def records(self, feeds):
        """Build signatures from (feed index, channel ID, hour offset[, source URL])."""
        base = datetime(2026, 11, 8, 12, 0, tzinfo=timezone.utc)
        titles = (
            "Morning News Bulletin",
            "Daily Drama Episode",
            "Evening Sports Review",
            "Late Night Interview",
        )
        result = []
        for feed in feeds:
            source_index, source_id, hours = feed[:3]
            source_url = (
                feed[3] if len(feed) > 3
                else f"https://feed-{source_index}.example/epg.xml"
            )
            for title in titles:
                start = base + timedelta(hours=hours)
                result.append({
                    "title": title,
                    "start_dt": start,
                    "stop_dt": start + timedelta(minutes=30),
                    "source_index": source_index,
                    "source_id": source_id,
                    "source": source_url,
                })
        return result

    def test_six_hour_offset_requires_three_distinct_feed_inputs(self):
        records = self.records([
            (0, "feed-a-channel", 0),
            (1, "feed-b-channel", 0),
            (2, "feed-c-channel", 6),
        ])
        corrections = generate_epg.infer_source_offsets(records)
        self.assertEqual(corrections, {(2, "feed-c-channel"): timedelta(hours=-6)})

    def test_multiple_channel_ids_from_one_feed_are_not_independent_evidence(self):
        records = self.records([
            (0, "feed-one-channel-a", 0),
            (0, "feed-one-channel-b", 0),
            (0, "feed-one-channel-c", 6),
        ])
        self.assertEqual(generate_epg.infer_source_offsets(records), {})

    def test_multiple_country_files_from_one_provider_are_one_vote(self):
        records = self.records([
            (0, "feed-in1", 0, "https://epgshare.example/IN1.xml.gz"),
            (1, "feed-in4", 0, "https://epgshare.example/IN4.xml.gz"),
            (2, "feed-us2", 6, "https://epgshare.example/US2.xml.gz"),
        ])
        self.assertEqual(generate_epg.infer_source_offsets(records), {})

    def test_outlier_from_a_feed_already_in_the_consensus_is_not_corrected(self):
        records = self.records([
            (0, "feed-a-canonical", 0),
            (0, "feed-a-alternate", 6),
            (1, "feed-b-channel", 0),
            (2, "feed-c-channel", 0),
        ])
        self.assertEqual(generate_epg.infer_source_offsets(records), {})

    def test_24_hour_displacement_is_manual_review_only(self):
        records = self.records([
            (0, "feed-a-channel", 0),
            (1, "feed-b-channel", 0),
            (2, "feed-c-channel", 24),
        ])
        manual_review = []
        corrections = generate_epg.infer_source_offsets(records, manual_review)
        self.assertEqual(corrections, {})
        self.assertEqual(
            manual_review,
            [(2, "feed-c-channel", -24 * 60, 4, 4)],
        )

    def test_14_hour_timezone_boundary_remains_eligible_for_auto_correction(self):
        records = self.records([
            (0, "feed-a-channel", 0),
            (1, "feed-b-channel", 0),
            (2, "feed-c-channel", 14),
        ])
        corrections = generate_epg.infer_source_offsets(records)
        self.assertEqual(
            corrections,
            {(2, "feed-c-channel"): timedelta(hours=-14)},
        )


if __name__ == "__main__":
    unittest.main()
