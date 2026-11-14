"""Regression tests for official Bangladesh schedule-page discovery."""
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from official_epg_sources import (
    RTV_LIVE_SOURCE,
    _RtvArticleLinkParser,
    _parse_rtv_daily_programmes,
    _parse_rtv_live_programmes,
)


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



class RtvLiveScheduleParsingTests(unittest.TestCase):
    def test_official_live_page_parses_explicit_english_times(self):
        html = """
        <h2>Today's show on Rtv</h2>
        <div>09:04 AM - Aj Potrikay -> Live</div>
        <div>05:00 PM - R-Syudio</div>
        <div>06:04 PM - ASIA-WEEKLY</div>
        <div>07:35 PM - Dawater Ranna SC</div>
        <div>09:20 PM - Boka Poribar -> Drama</div>
        <div>10:00 PM - Cheater And Gentleman -> Drama</div>
        <div>11:23 PM - Road to Democracy -> Talk Show</div>
        """
        now = datetime(2026, 11, 14, 3, 0, tzinfo=timezone.utc)
        programmes = _parse_rtv_live_programmes(html, now)
        self.assertEqual(RTV_LIVE_SOURCE, "https://www.rtvbd.tv/live.php")
        self.assertEqual(len(programmes), 5)
        self.assertEqual(programmes[0]["title"], "R-Syudio")
        self.assertEqual(
            programmes[0]["start_dt"],
            datetime(2026, 11, 14, 11, 0, tzinfo=timezone.utc),
        )
        self.assertEqual(
            programmes[0]["stop_dt"],
            datetime(2026, 11, 14, 12, 4, tzinfo=timezone.utc),
        )
        self.assertTrue(all(item["channel_id"] == "RTV.bd" for item in programmes))

    def test_live_page_requires_the_official_today_schedule_heading(self):
        html = "<h2>Sports news</h2><div>05:00 PM - Unrelated show</div>"
        self.assertEqual(
            _parse_rtv_live_programmes(
                html, datetime(2026, 11, 14, 3, 0, tzinfo=timezone.utc)
            ),
            [],
        )


class RtvDailyScheduleParsingTests(unittest.TestCase):
    def test_bengali_minute_suffix_is_consumed_without_polluting_programme_title(self):
        schedule = """
        শনিবার, ১৪ নভেম্বর ২০২৬, ৩০ কার্তিক ১৪৩৩।
        সকাল ৯টায় লাইভ টকশো ‘আজ পত্রিকায়’।
        সকাল ৯টা ৪৫ মিনিটে ‘সকালের সংবাদ’।
        সকাল ১০টা ১০ মিনিটে বাংলা ছায়াছবি ‘স্বপ্নের পৃথিবী’।
        দুপুর ২টা ১০ মিনিটে বাংলা ছায়াছবি ‘কিলহিম’।
        বিকেল ৫টায় কৃষি বিষয়ক অনুষ্ঠান ‘কৃষি ও কৃষ্টি’।
        সন্ধ্যা ৬টা ৫মিনিটে শিশু-কিশোরদের বাংলা গানের প্রতিযোগিতামূলক আয়োজন ‘লিটল স্টার সিজন-২’।
        সন্ধ্যা ৭টা ৩০ মিনিটে ‘স্টেপ গ্ল্যামার শো’।
        রাত ৮টায় নির্বাচিত নাটক ‘খাল কেটে কুমির’।
        রাত ৯টা ২০ মিনিটে ধারাবাহিক নাটক ‘মোস্তফা’।
        রাত ১০টায় ধারাবাহিক নাটক ‘ম্যানেজ মাস্টার’।
        রাত ১০টা ৪৫ মিনিটে ‘রাতের সংবাদ’।
        রাত ১১টা ২৫ মিনিটে ‘রোড টু ডেমোক্রেসি’।
        রাত ১২টা ১৫ মিনিটে টকশো ‘মনের কথা’।
        রাত ১টায় ‘মধ্যরাতের সংবাদ’।
        """
        programmes = _parse_rtv_daily_programmes(
            schedule, datetime(2026, 11, 14, 0, 0, tzinfo=timezone.utc)
        )
        titles = [programme["title"] for programme in programmes]
        self.assertGreaterEqual(len(programmes), 8)
        self.assertIn("‘সকালের সংবাদ’", titles)
        self.assertIn("‘রাতের সংবাদ’", titles)
        self.assertTrue(all(not title.startswith("ে") for title in titles))


if __name__ == "__main__":
    unittest.main()
