import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from logo_asset_naming import is_blocked_logo_basename, safe_logo_filename


class LogoAssetNamingTests(unittest.TestCase):
    def test_blocklist_is_shared_and_case_insensitive(self):
        self.assertTrue(is_blocked_logo_basename("logos/ATN-News.png"))
        self.assertTrue(is_blocked_logo_basename("https://example.invalid/logos/placeholder-bangla-tv.svg"))
        self.assertFalse(is_blocked_logo_basename("ananda-tv.png"))

    def test_sanitized_filename_avoids_blocked_assets_and_prefixes(self):
        for title in ("ATN News", "Placeholder Channel", "Unknown TV", "Colors"):
            filename = safe_logo_filename(title)
            self.assertFalse(is_blocked_logo_basename(filename), (title, filename))
            self.assertTrue(filename.endswith(".png"))

    def test_ordinary_name_stays_stable(self):
        self.assertEqual(safe_logo_filename("Ananda TV"), "ananda-tv.png")


if __name__ == "__main__":
    unittest.main()
