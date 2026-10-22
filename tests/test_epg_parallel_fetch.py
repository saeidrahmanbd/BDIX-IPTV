import sys
import unittest
from pathlib import Path
from unittest.mock import patch
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import epg_coverage


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


if __name__ == "__main__":
    unittest.main()
