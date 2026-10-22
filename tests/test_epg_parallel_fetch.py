import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import epg_coverage
import generate_epg
import threading
import time


class ParallelSourceFetchTests(unittest.TestCase):
    def test_results_keep_configured_order_and_isolate_failures(self):
        def fake_fetch(url):
            if url == "slow-or-bad":
                raise TimeoutError("simulated slow source")
            return ({url}, {url}, defaultdict(int, {url: 2}), defaultdict(set, {url: {url}}))

        urls = ["first", "slow-or-bad", "last"]
        with patch.object(epg_coverage, "fetch_source", side_effect=fake_fetch):
            data, statuses = epg_coverage.fetch_all_sources(urls, max_workers=2)

        self.assertEqual([sorted(item[0]) for item in data], [["first"], [], ["last"]])
        self.assertEqual([status[0] for status in statuses], urls)
        self.assertEqual([status[1] for status in statuses], ["OK", "FAILED", "OK"])
        self.assertEqual([status[2] for status in statuses], [1, 0, 1])

    def test_empty_source_list_is_supported(self):
        data, statuses = epg_coverage.fetch_all_sources([])
        self.assertEqual(data, [])
        self.assertEqual(statuses, [])


class GeneratorParallelFetchTests(unittest.TestCase):
    def test_fetch_failures_are_isolated_and_successes_are_kept(self):
        def fake_fetch(url):
            if url == "broken-feed":
                raise TimeoutError("simulated timeout")
            return url.encode("utf-8")

        urls = ["feed-a", "broken-feed", "feed-c"]
        with patch.object(generate_epg, "fetch", side_effect=fake_fetch):
            payloads, errors = generate_epg.fetch_xmltv_sources_concurrently(urls, max_workers=2)

        self.assertEqual(payloads, {"feed-a": b"feed-a", "feed-c": b"feed-c"})
        self.assertIn("broken-feed", errors)
        self.assertIsInstance(errors["broken-feed"], TimeoutError)

    def test_fetch_pool_is_bounded_and_downloads_overlap(self):
        lock = threading.Lock()
        active = 0
        peak = 0

        def fake_fetch(url):
            nonlocal active, peak
            with lock:
                active += 1
                peak = max(peak, active)
            time.sleep(0.03)
            with lock:
                active -= 1
            return url.encode("utf-8")

        urls = [f"feed-{i}" for i in range(6)]
        with patch.object(generate_epg, "fetch", side_effect=fake_fetch):
            payloads, errors = generate_epg.fetch_xmltv_sources_concurrently(urls, max_workers=3)

        self.assertEqual(set(payloads), set(urls))
        self.assertEqual(errors, {})
        self.assertGreater(peak, 1)
        self.assertLessEqual(peak, 3)

    def test_dedicated_html_schedule_sources_are_not_generic_xmltv_fetches(self):
        urls = [generate_epg.HUM_TV_SOURCE, generate_epg.RTV_SOURCE, "ordinary-feed"]
        with patch.object(generate_epg, "fetch", return_value=b"ok") as mocked_fetch:
            payloads, errors = generate_epg.fetch_xmltv_sources_concurrently(urls, max_workers=2)

        mocked_fetch.assert_called_once_with("ordinary-feed")
        self.assertEqual(payloads, {"ordinary-feed": b"ok"})
        self.assertEqual(errors, {})


if __name__ == "__main__":
    unittest.main()
