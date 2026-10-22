"""Source regression tests for exact active-channel logo repairs."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_playlist_logos as logo_repair


class LogoRepairSourceTests(unittest.TestCase):
    def test_alone_uses_a_direct_validated_commons_asset_url(self):
        hint = logo_repair.EXTRA_DIRECT_HINTS["Alone"]
        self.assertTrue(hint["url"].startswith("https://upload.wikimedia.org/wikipedia/commons/"))
        self.assertIn("Alone_%28Leftfield_Pictures_TV_series%29_logo.svg", hint["url"])
        self.assertIn("commons.wikimedia.org/wiki/File:Alone_", hint["page"])
        self.assertIn("history.com/shows/alone", hint["license_url"])

    def test_zainabia_logo_source_is_identity_attributed(self):
        hint = logo_repair.EXTRA_DIRECT_HINTS["Zainabia Channel"]
        self.assertIn("ZAINABIA", hint["license"].upper())
        self.assertIn("zainabiachannel.co.in", hint["license_url"])
        self.assertIn("shialivetv.com", hint["url"])


if __name__ == "__main__":
    unittest.main()
