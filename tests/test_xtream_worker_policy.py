"""Regression checks for the Xtream worker playlist policy.

These source-level checks complement live integration tests, which require
Cloudflare Worker runtime bindings and deployed secrets.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class XtreamWorkerPolicyTests(unittest.TestCase):
    def read_worker(self, name: str) -> str:
        return (ROOT / name / "worker.js").read_text(encoding="utf-8")

    def test_both_workers_exclude_review_only_groups(self):
        for name in ("xtream-main", "xtream-bdix"):
            with self.subTest(worker=name):
                source = self.read_worker(name)
                match = re.search(r'const INACTIVE\s*=\s*new Set\(\[([^\]]+)\]\)', source)
                self.assertIsNotNone(match, "worker must declare inactive/review-only groups")
                groups = set(re.findall(r'"([^"]+)"', match.group(1)))
                self.assertTrue({"Test", "Not Playing", "New Backup", "New Channels"} <= groups)
                self.assertIn("if(!INACTIVE.has(cur.group))", source)

    def test_both_workers_support_cors_preflight_and_comparison_helper(self):
        for name in ("xtream-main", "xtream-bdix"):
            with self.subTest(worker=name):
                source = self.read_worker(name)
                self.assertIn('"access-control-allow-origin":"*"', source)
                self.assertIn('request.method==="OPTIONS"', source)
                self.assertIn("function constantTimeEqual(a,b)", source)

    def test_both_workers_use_order_independent_stream_ids(self):
        for name in ("xtream-main", "xtream-bdix"):
            with self.subTest(worker=name):
                source = self.read_worker(name)
                self.assertIn("function stableId(s)", source)
                self.assertIn("s.id=stableId(s)", source)
                self.assertNotRegex(source, r"let current=null,id=100000000")


if __name__ == "__main__":
    unittest.main()
