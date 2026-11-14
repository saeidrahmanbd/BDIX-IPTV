"""Regression tests for official Bangladesh schedule-page discovery."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from official_epg_sources import _RtvArticleLinkParser


class RtvArticleLinkParserTests(unittest.TestCase):
    def parse_links(self, markup):
        parser = _RtvArticleLinkParser()
        parser.feed(markup)
        parser.close()
        return parser.links

    def test_rtv_daily_schedule_link_with_bengali_date_in_anchor_text(self):
        links = self.parse_links(
            '<a href="/entertainment/rtv/403544">'
            'আরটিভিতে আজ (১৪ নভেম্বর) যা দেখবেন</a>'
        )
        self.assertEqual(
            links,
            ["https://rtvonline.com/entertainment/rtv/403544"],
        )

    def test_rtv_daily_schedule_link_with_title_in_image_alt_text(self):
        links = self.parse_links(
            '<a href="/entertainment/rtv/403544">'
            '<img src="/media/schedule.jpg" '
            'alt="আরটিভিতে আজ (১৪ নভেম্বর) যা দেখবেন">'
            '</a>'
        )
        self.assertEqual(
            links,
            ["https://rtvonline.com/entertainment/rtv/403544"],
        )

    def test_unrelated_rtv_article_is_not_mistaken_for_a_schedule(self):
        links = self.parse_links(
            '<a href="/news/123">বাংলাদেশ-পাকিস্তানের ম্যাচসহ টিভিতে আজকের খেলা</a>'
        )
        self.assertEqual(links, [])


if __name__ == "__main__":
    unittest.main()
