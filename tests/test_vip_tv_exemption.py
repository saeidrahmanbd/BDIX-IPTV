#!/usr/bin/env python3
"""Regression tests: no VIP TV exemption from the foreign Movies/Music-only rule."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import discover_international_channels as discovery  # noqa: E402
import validate_international_playlist as intl_validator  # noqa: E402

VIP_ID = "custom.vip-tv-aw-music"


def attrs(tvg_id, group="Music", country="AW"):
    return {
        "group-title": group,
        "tvg-id": tvg_id,
        "channel-id": tvg_id,
        "tvg-country": country,
    }


class VipTvExemptionTests(unittest.TestCase):
    def test_exact_vip_identity_is_not_automatically_exempted(self):
        target, reason, _code = discovery.policy(attrs(VIP_ID), "VIP TV", allow_legacy_group=True)
        self.assertIsNone(target, f"VIP TV must be rejected, got {target!r} ({reason!r})")
        self.assertNotEqual(intl_validator.foreign_movie_music_error(attrs(VIP_ID), "VIP TV", "AW"), "")

    def test_similar_name_cannot_bypass_movies_music_rule(self):
        # The foreign rule is group-based: a similar name or the VIP identity in a
        # non-Movies/Music group must still fail. Music is allowed by the general rule,
        # so only non-Movies/Music groups are used as bypass attempts here.
        for name in ("VIP TV", "VIP Music TV", "vip tv"):
            for group in ("Sports", "News", "Religious"):
                with self.subTest(name=name, group=group):
                    self.assertNotEqual(
                        intl_validator.foreign_movie_music_error(attrs(VIP_ID, group=group), name, "AW"), ""
                    )

    def test_no_generic_vip_exception_for_other_identities(self):
        for tvg_id in ("custom.vip-tv-aw", "VIPTV.aw", "custom.vip-tv-zz-music"):
            with self.subTest(tvg_id=tvg_id):
                target, _reason, _code = discovery.policy(attrs(tvg_id), "VIP TV", allow_legacy_group=True)
                self.assertIsNone(target)

    def test_no_identity_music_exception_table_remains(self):
        self.assertFalse(hasattr(discovery, "IDENTITY_MUSIC_EXCEPTIONS"))


if __name__ == "__main__":
    unittest.main()
