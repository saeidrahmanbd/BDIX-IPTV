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
        for name in ("xtream-main",):
            with self.subTest(worker=name):
                source = self.read_worker(name)
                match = re.search(r'const INACTIVE\s*=\s*new Set\(\[([^\]]+)\]\)', source)
                self.assertIsNotNone(match, "worker must declare inactive/review-only groups")
                groups = set(re.findall(r'"([^"]+)"', match.group(1)))
                self.assertTrue({"Test", "Review", "Not Playing", "New Backups", "New Channels"} <= groups)
                self.assertRegex(source, r"if\(!INACTIVE\.has\((?:cur|current)\.group\)\)")

        workflow = (ROOT / ".github/workflows/check-xtream.yml").read_text(encoding="utf-8")
        self.assertIn('inactive = {"Test", "Review", "Not Playing", "New Backups", "New Channels"}', workflow)

    def test_both_workers_support_cors_preflight_and_comparison_helper(self):
        for name in ("xtream-main",):
            with self.subTest(worker=name):
                source = self.read_worker(name)
                self.assertIn('"access-control-allow-origin":"*"', source)
                self.assertIn('request.method==="OPTIONS"', source)
                self.assertIn("function constantTimeEqual(a,b)", source)

    def test_both_workers_use_order_independent_stream_ids(self):
        for name in ("xtream-main",):
            with self.subTest(worker=name):
                source = self.read_worker(name)
                self.assertIn("function stableId(s)", source)
                self.assertIn("s.id=stableId(s)", source)
                self.assertNotRegex(source, r"let current=null,id=100000000")


if __name__ == "__main__":
    unittest.main()


class XtreamWorkerSecurityTests(unittest.TestCase):
    def setUp(self):
        self.source = (ROOT / "xtream-main" / "worker.js").read_text(encoding="utf-8")

    def test_upstream_errors_never_echo_exception_text(self):
        # Exception text can include PLAYLIST_URL, which may carry a private token.
        self.assertNotIn("String(e)", self.source)
        self.assertGreaterEqual(self.source.count("Upstream playlist or guide unavailable"), 4)

    def test_worker_does_not_log_requests_or_credentials(self):
        self.assertNotRegex(self.source, r"console\.(log|error|warn|info)\s*\(")

    def test_credentials_are_compared_in_constant_time(self):
        self.assertIn("function constantTimeEqual(a,b)", self.source)
        self.assertIn("auth(u,env)", self.source)
        self.assertIn("constantTimeEqual(suppliedPass,expectedPass)", self.source)

    def test_unauthorized_responses_are_generic(self):
        self.assertIn('return text("Unauthorized",401);', self.source)

    def test_stream_redirects_suppress_referrer(self):
        self.assertIn('"Referrer-Policy":"no-referrer"', self.source)

    def test_client_compatible_paths_are_preserved(self):
        for path in ("/player_api.php", "/get.php", "/xmltv.php", "/live/"):
            with self.subTest(path=path):
                self.assertIn(path, self.source)


if __name__ == "__main__":
    unittest.main()

