import sys
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from automation.engines.epg.source_provider import build_epg_source_candidate


class EpgSourceProviderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "scripts").mkdir()
        (self.root / "reports").mkdir()
        (self.root / "epg").mkdir()
        for path in (
            "scripts/generate_epg.py",
            "scripts/epg_source_cache.py",
            "scripts/epg_mapping_policy.py",
            "scripts/official_epg_sources.py",
            "reports/epg-channel-mapping.csv",
            "IPTV-Playlist.m3u",
            "International-Playlist.m3u",
            "epg/epg.xml",
        ):
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("baseline:" + path, encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_candidate_is_generated_in_temp_workspace_only(self):
        production_before = (self.root / "epg/epg.xml").read_text()
        def generate(*args, **kwargs):
            cwd = Path(kwargs["cwd"])
            (cwd / "epg/epg.xml").write_text("<tv><channel id='x'/></tv>", encoding="utf-8")
            return subprocess.CompletedProcess(args[0], 0, stdout="", stderr="")
        with patch("automation.engines.epg.source_provider.subprocess.run", side_effect=generate) as run:
            candidate = build_epg_source_candidate(self.root, timeout_seconds=60, max_workers=2)
        self.assertIn("<tv>", candidate)
        self.assertEqual((self.root / "epg/epg.xml").read_text(), production_before)
        self.assertEqual(run.call_args.kwargs["timeout"], 60)
        self.assertEqual(run.call_args.kwargs["env"]["EPG_SOURCE_CACHE_TTL_SECONDS"], "0")

    def test_failed_generator_aborts_without_touching_production_guide(self):
        production_before = (self.root / "epg/epg.xml").read_text()
        def fail(*args, **kwargs):
            raise subprocess.CalledProcessError(1, args[0])
        with patch("automation.engines.epg.source_provider.subprocess.run", side_effect=fail):
            with self.assertRaisesRegex(RuntimeError, "production guide was not changed"):
                build_epg_source_candidate(self.root, timeout_seconds=60)
        self.assertEqual((self.root / "epg/epg.xml").read_text(), production_before)

    def test_timeout_aborts_candidate_generation(self):
        def timeout(*args, **kwargs):
            raise subprocess.TimeoutExpired(args[0], kwargs["timeout"])
        with patch("automation.engines.epg.source_provider.subprocess.run", side_effect=timeout):
            with self.assertRaisesRegex(RuntimeError, "timed out"):
                build_epg_source_candidate(self.root, timeout_seconds=60)

    def test_missing_required_input_is_rejected_before_network(self):
        (self.root / "reports/epg-channel-mapping.csv").unlink()
        with patch("automation.engines.epg.source_provider.subprocess.run") as run:
            with self.assertRaisesRegex(FileNotFoundError, "epg-channel-mapping.csv"):
                build_epg_source_candidate(self.root)
        run.assert_not_called()

    def test_timeout_and_worker_bounds_are_enforced(self):
        with self.assertRaisesRegex(ValueError, "timeout"):
            build_epg_source_candidate(self.root, timeout_seconds=30)
        with self.assertRaisesRegex(ValueError, "workers"):
            build_epg_source_candidate(self.root, max_workers=17)


if __name__ == "__main__":
    unittest.main()
