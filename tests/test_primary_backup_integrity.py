"""Unit tests for exact primary/Backup integrity and Review quarantine."""
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from enforce_primary_backup_integrity import GROUP_ORDER, is_authorized_orphan_backup_removal, repair_playlist_text
from restore_protected_review import is_authorized_removal
from maintenance_helpers import _is_authorized_removal


LOGO = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/x.png"


def row(cid, name, group, url, *, language="ben", country="BD", number="1", logo=LOGO):
    attrs = (
        f'tvg-id="{cid}" tvg-name="{name}" tvg-logo="{logo}" '
        f'channel-id="{cid}" tvg-country="{country}" tvg-language="{language}" '
        f'group-title="{group}"'
    )
    if number:
        attrs += f' tvg-chno="{number}"'
    return f"#EXTINF:-1 {attrs},{name}\n{url}\n"


class PrimaryBackupIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.sample = (
            "#EXTM3U\n"
            + row("X.bd", "Example TV", "Bangladesh", "https://stream.example/x-primary.m3u8")
            + row("X.bd", "Example TV", "Indian Entertainment", "https://stream.example/x-alt.m3u8")
            + row("X.bd", "Example TV", "Backup", "https://stream.example/x-backup.m3u8", language="")
            + row("ORPHAN.bd", "Orphan Channel", "Backup", "https://stream.example/orphan.m3u8")
            + row("OLD.bd", "Legacy Review", "Not Playing", "https://stream.example/old.m3u8")
            + row("NEW.bd", "New Candidate", "New Channels", "https://stream.example/new.m3u8")
            + row("ALT.bd", "New Alternate", "New Backups", "https://stream.example/new-alt.m3u8")
            + row("UNKNOWN.bd", "Unknown Language", "Bangladesh", "https://stream.example/unknown.m3u8", language="")
        )

    def test_live_playlist_selected_audit_repairs_are_applied(self):
        playlist = (ROOT / "IPTV-Playlist.m3u").read_text(encoding="utf-8")
        entries = []
        current = None
        for line in playlist.splitlines():
            if line.startswith("#EXTINF:"):
                if current is not None:
                    entries.append(current)
                attrs = dict(re.findall(r'([A-Za-z0-9_-]+)="([^"]*)"', line))
                current = {"attrs": attrs, "url": ""}
            elif current is not None and line.strip().startswith(("http://", "https://")):
                current["url"] = line.strip()
        if current is not None:
            entries.append(current)

        primary_groups = {
            "Bangladesh", "Indian Bangla", "Indian Movies", "Indian Music",
            "Indian Entertainment", "Pakistani", "International",
            "Documentary & Wildlife", "Kids", "Religious", "Sports",
        }
        active_ids = [
            e["attrs"].get("tvg-id", "").casefold()
            for e in entries if e["attrs"].get("group-title") in primary_groups
            and e["attrs"].get("tvg-id")
        ]
        self.assertEqual(len(active_ids), len(set(active_ids)), "primary tvg-id values must be unique")

        islamic = [e for e in entries if e["attrs"].get("tvg-name") == "Islamic TV"]
        self.assertEqual(len(islamic), 2)
        active_islamic = [e for e in islamic if e["attrs"].get("group-title") == "Religious"]
        self.assertEqual(len(active_islamic), 1)
        self.assertEqual(active_islamic[0]["attrs"].get("tvg-id"), "IslamicTV.bd")
        self.assertEqual(active_islamic[0]["attrs"].get("channel-id"), "IslamicTV.bd")
        self.assertEqual(active_islamic[0]["attrs"].get("tvg-country"), "BD")
        self.assertEqual(active_islamic[0]["attrs"].get("tvg-language"), "ben")
        self.assertEqual(active_islamic[0]["attrs"].get("tvg-chno"), "537")

        expected_review_metadata = {
            "Shikor TV Canada": ("custom.shikortvcanada", "CA"),
            "Ten TV Prime": ("custom.tentvprime", "BD"),
            "TV One UK": ("TVOne.uk", "GB"),
        }
        for name, (channel_id, country) in expected_review_metadata.items():
            candidate = [e for e in entries if e["attrs"].get("tvg-name") == name]
            self.assertEqual(len(candidate), 1, name)
            self.assertEqual(candidate[0]["attrs"].get("group-title"), "Review", name)
            self.assertEqual(
                candidate[0]["attrs"].get("channel-id") or candidate[0]["attrs"].get("tvg-id"),
                channel_id,
                name,
            )
            self.assertEqual(candidate[0]["attrs"].get("tvg-country"), country, name)

        for e in entries:
            if e["attrs"].get("group-title") == "Bangladesh":
                self.assertEqual(e["attrs"].get("tvg-country"), "BD", e["attrs"].get("tvg-name"))

        raj_primary = [e for e in entries if e["attrs"].get("tvg-name") == "Rajdhani TV"
                       and e["attrs"].get("group-title") == "Bangladesh"]
        raj_backup = [e for e in entries if e["attrs"].get("tvg-name") == "Rajdhani TV"
                      and e["attrs"].get("group-title") == "Backup"]
        self.assertEqual(len(raj_primary), 1)
        self.assertEqual(raj_primary[0]["url"], "https://stream.shariarsuvo.com/hls5/rajdhanicable.m3u8")
        self.assertEqual(len(raj_backup), 2)
        self.assertEqual(
            {e["url"] for e in raj_backup},
            {
                "http://stream.shariarsuvo.com/hls5/rajdhanicable.m3u8",
                "https://drk6xq0vhn.gpcdn.net/live/rajdhani_tv/index.m3u8",
            },
        )

        placeholder_ids = {
            "Colors.in", "Colors.Bangla.in", "ColorsBanglaCinema.in@SD",
            "ColorsCineplex.uk", "StarGold.in@HD",
        }
        quarantined = [e for e in entries if e["attrs"].get("tvg-id") in placeholder_ids
                       and e["attrs"].get("group-title") == "Review"]
        self.assertGreaterEqual(len(quarantined), 6)

        https_mirrors = {
            "Bangla TV": (
                "https://tvsen6.aynaott.com/39ee93nUbCCmm5LsyD4t/index.m3u8",
                "http://116.204.149.16/banglatv/index.m3u8",
            ),
            "SA TV": (
                "https://j6nfugukcl.gpcdn.net/tile_5/master.m3u8",
                "http://116.204.149.16/satv/index.m3u8",
            ),
            "Hindi Hits": (
                "https://samitaorigin.tangotv.in/HINDIHITS/SAMITAORIGIN/index.m3u8",
                "http://146.59.253.52:8080/hindihitshd/index.m3u8",
            ),
            "Zee TV": (
                "https://d47ddb99.wurl.com/master/f36d25e7e52f1ba8d7e56eb859c636563214f541/U2Ftc3VuZy1kZV9aZWVUVkhEVUtHZXJtYW55X0hMUw/playlist.m3u8",
                "http://41.205.93.154/ZEE-TV/index.m3u8",
            ),
        }
        for name, (url, original_http) in https_mirrors.items():
            primary = [e for e in entries if e["attrs"].get("tvg-name") == name
                       and e["attrs"].get("group-title") in primary_groups]
            backup = [e for e in entries if e["attrs"].get("tvg-name") == name
                      and e["attrs"].get("group-title") == "Backup"
                      and e["url"] == original_http]
            self.assertEqual(len(primary), 1, name)
            self.assertEqual(primary[0]["url"], url, name)
            self.assertEqual(len(backup), 1, name)

    def test_primary_without_verified_local_logo_is_preserved_in_review(self):
        dtalk_url = "https://stream.example/d-talk.m3u8"
        prime_url = "https://stream.example/prime-tv.m3u8"
        sample = (
            "#EXTM3U\n"
            + '#EXTINF:-1 tvg-name="Shikor TV Canada" channel-id="custom.shikortvcanada" tvg-country="CA" tvg-language="ben" tvg-chno="17" group-title="International",Shikor TV Canada\n'
            + dtalk_url + "\n"
            + '#EXTINF:-1 tvg-name="Ten TV Prime" channel-id="custom.tentvprime" tvg-country="BD" tvg-language="ben" tvg-chno="76" group-title="Bangladesh",Ten TV Prime\n'
            + prime_url + "\n"
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertEqual(stats["missing_logos_quarantined"], 2)
        self.assertIn(dtalk_url, updated)
        self.assertIn(prime_url, updated)
        self.assertIn('tvg-id="custom.shikortvcanada"', updated)
        self.assertIn('tvg-id="custom.tentvprime"', updated)
        self.assertIn('group-title="Review"', updated)
        self.assertNotIn('tvg-chno="17"', updated)
        self.assertNotIn('tvg-chno="76"', updated)
        self.assertEqual(stats["missing_logos_deferred"].count("Shikor TV Canada"), 1)
        self.assertEqual(stats["missing_logos_deferred"].count("Ten TV Prime"), 1)
    def test_generic_logo_is_removed_when_primary_is_quarantined(self):
        url = "https://stream.example/nkr-tv-kannada.m3u8"
        fallback = "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/generated-fallback-channel.svg"
        sample = (
            "#EXTM3U\n"
            + row("NKRTVKannada.in@SD", "NKR TV Kannada", "Indian Entertainment", url,
                  language="kan", country="IN", logo=fallback)
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        entry = updated.split(url)[0].split("#EXTINF:")[-1]
        self.assertIn('group-title="Review"', entry)
        self.assertNotIn("tvg-logo=", entry)
        self.assertIn(url, updated)
        self.assertEqual(stats["missing_logos_quarantined"], 1)

    def test_duplicate_primary_demotes_alternate_and_backup_has_primary(self):
        updated, stats, errors = repair_playlist_text(self.sample)
        self.assertEqual(errors, [])
        self.assertEqual(stats["duplicate_primary_demoted"], 1)
        self.assertIn('group-title="Backup"', updated)
        self.assertEqual(updated.count("https://stream.example/x-alt.m3u8"), 1)
        self.assertEqual(updated.count('tvg-id="X.bd"'), 3)
        self.assertEqual(stats["orphan_backups_quarantined"], 1)
        self.assertIn('group-title="Review"', updated)
        orphan_info = updated.split('https://stream.example/orphan.m3u8')[0].split('#EXTINF:')[-1]
        self.assertIn('group-title="Review"', orphan_info)

    def test_orphan_and_legacy_not_playing_are_review_only(self):
        updated, stats, errors = repair_playlist_text(self.sample)
        self.assertEqual(errors, [])
        self.assertIn('group-title="Review"', updated)
        self.assertNotIn('group-title="Not Playing"', updated)
        self.assertEqual(stats["legacy_review_renamed"], 1)
        self.assertEqual(stats["orphan_backups_quarantined"], 1)

    def test_backup_metadata_is_backfilled_from_exact_primary_id(self):
        updated, _, errors = repair_playlist_text(self.sample)
        self.assertEqual(errors, [])
        backup_block = updated.split("https://stream.example/x-backup.m3u8")[0]
        backup_block = backup_block.split("#EXTINF:")[-1]
        self.assertIn('tvg-language="ben"', backup_block)

    def test_unknown_language_is_marked_und_not_guessed(self):
        updated, stats, errors = repair_playlist_text(self.sample)
        self.assertEqual(errors, [])
        unknown = updated.split("https://stream.example/unknown.m3u8")[0].split("#EXTINF:")[-1]
        self.assertIn('tvg-language="und"', unknown)
        self.assertIn("Unknown Language", stats["undetermined_languages"])

    def test_review_and_discovery_groups_are_unnumbered_and_ordered(self):
        updated, _, errors = repair_playlist_text(self.sample)
        self.assertEqual(errors, [])
        self.assertIn("#PLAYLIST-STUDIO-CATEGORIES:" + json.dumps(GROUP_ORDER), updated)
        for name in ("Review", "New Channels", "New Backups"):
            self.assertIn(f'group-title="{name}"', updated)
        self.assertNotIn('group-title="Review" tvg-chno=', updated)
        self.assertLess(updated.index('group-title="Review"'), updated.index('group-title="New Channels"'))
        self.assertLess(updated.index('group-title="New Channels"'), updated.index('group-title="New Backups"'))
        self.assertLess(updated.index('group-title="New Backups"'), updated.index('group-title="Backup"'))

    def test_only_two_exact_orphan_backup_endpoints_are_authorized_for_removal(self):
        bhi_url = "https://server.livelegitpro.in/bhichannel/bhichannel/tracks-v1a1/mono.m3u8"
        rplus_url = "https://vglivessai.akamaized.net/sg/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/e5dcc9dc-3a33-4b19-a361-5a5b3aa022f7/index.m3u8"
        bhi_info = row("BHI.Channel.in", "BHI Channel", "Backup", bhi_url, country="IN").splitlines()[0]
        rplus_info = row("RPlus.in@SD", "R Plus", "Backup", rplus_url, country="IN").splitlines()[0]

        for info, url in ((bhi_info, bhi_url), (rplus_info, rplus_url)):
            self.assertTrue(is_authorized_orphan_backup_removal(info, url))
            self.assertTrue(is_authorized_removal(info, url))
            self.assertTrue(_is_authorized_removal(info, url))

        # The exception is exact: it does not authorize another stream URL or a
        # row moved into Review, and it does not authorize the whole channel name.
        self.assertFalse(is_authorized_orphan_backup_removal(bhi_info, "https://different.example/bhi.m3u8"))
        review_info = bhi_info.replace('group-title="Backup"', 'group-title="Review"')
        self.assertFalse(is_authorized_removal(review_info, bhi_url))
        self.assertFalse(_is_authorized_removal(review_info, bhi_url))

    def test_exactly_authorized_orphan_backup_rows_are_removed_but_other_orphans_are_reviewed(self):
        bhi_url = "https://server.livelegitpro.in/bhichannel/bhichannel/tracks-v1a1/mono.m3u8"
        rplus_url = "https://vglivessai.akamaized.net/sg/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/e5dcc9dc-3a33-4b19-a361-5a5b3aa022f7/index.m3u8"
        alternate_bhi_url = "https://different.example/bhi-alternate.m3u8"
        sample = (
            "#EXTM3U" + chr(10)
            + row("BHI.Channel.in", "BHI Channel", "Backup", bhi_url, country="IN")
            + row("RPlus.in@SD", "R Plus", "Backup", rplus_url, country="IN")
            + row("BHI.Channel.in", "BHI Channel", "Backup", alternate_bhi_url, country="IN")
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertNotIn(bhi_url, updated)
        self.assertNotIn(rplus_url, updated)
        self.assertIn(alternate_bhi_url, updated)
        self.assertEqual(stats["user_authorized_orphan_backups_removed"], 2)
        alternate_info = updated.split(alternate_bhi_url)[0].split("#EXTINF:")[-1]
        self.assertIn('group-title="Review"', alternate_info)

    def test_stream_urls_are_preserved(self):
        updated, _, errors = repair_playlist_text(self.sample)
        self.assertEqual(errors, [])
        before = sorted(line for line in self.sample.splitlines() if line.startswith("https://"))
        after = sorted(line for line in updated.splitlines() if line.startswith("https://"))
        self.assertEqual(before, after)

    def test_duplicate_stream_url_blocks_without_silent_deletion(self):
        duplicated = self.sample + row("OTHER.bd", "Second Row", "Bangladesh", "https://stream.example/x-primary.m3u8")
        updated, _, errors = repair_playlist_text(duplicated)
        self.assertTrue(any("Duplicate stream URL" in error for error in errors))
        self.assertEqual(updated.splitlines().count("https://stream.example/x-primary.m3u8"), 2)


    def test_verified_orphan_candidates_promote_to_their_genre(self):
        sample = (
            "#EXTM3U\n"
            + row("GTCPunjabi.in@UK", "GTC Punjabi UK", "Backup", "https://stream.example/gtc.m3u8", language="pan", country="IN")
            + row("MHOne.in@SD", "MH One", "Backup", "https://stream.example/mhone.m3u8", language="pan", country="IN")
            + row("QTV.in", "Q TV", "Backup", "https://stream.example/qtv.m3u8", language="hin", country="IN")
            + row("Eurosport.in@SD", "Eurosport", "Backup", "https://stream.example/eurosport.m3u8", language="eng", country="IN")
            + row("HumTV.pk", "Hum TV", "Backup", "https://stream.example/humtv.m3u8", language="urd", country="PK")
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertIn('tvg-name="GTC Punjabi UK"', updated)
        self.assertIn('group-title="Indian Entertainment"', updated)
        self.assertIn('tvg-name="MH One"', updated)
        self.assertIn('group-title="Indian Music"', updated)
        self.assertIn('tvg-name="Q TV"', updated)
        self.assertIn('tvg-name="Eurosport"', updated)
        self.assertIn('group-title="Sports"', updated)
        self.assertIn('tvg-name="Hum TV"', updated)
        self.assertIn('group-title="Pakistani"', updated)
        self.assertEqual(stats["orphan_backups_promoted"], 5)

    def test_removed_non_kids_candidates_are_deleted_and_unknown_backup_stays_reviewed(self):
        sample = (
            "#EXTM3U\n"
            + row("ChannelWIN.in@SD", "Channel WIN", "Backup", "https://stream.example/win.m3u8", language="und", country="IN")
            + row("Pogo.in@SD", "Pogo", "Backup", "https://stream.example/pogo.m3u8", language="eng", country="IN")
            + row("UNLISTED.in", "Unlisted Candidate", "Backup", "https://stream.example/unlisted.m3u8", language="und", country="IN")
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertNotIn("Channel WIN", updated)
        self.assertIn('tvg-name="Pogo"', updated)
        self.assertIn('group-title="Kids"', updated)
        self.assertIn('tvg-name="Unlisted Candidate"', updated)
        self.assertIn('group-title="Review"', updated)
        self.assertEqual(stats["non_kids_review_removed"], 1)
        self.assertEqual(stats["orphan_backups_promoted"], 1)
        self.assertEqual(stats["orphan_backups_quarantined"], 1)

    def test_ntv_malayalam_promotion_adds_the_local_logo(self):
        sample = (
            "#EXTM3U\n"
            + row("NTV.in", "NTV Malayalam", "Backup", "https://stream.example/ntv.m3u8", language="mal", country="IN", logo="")
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertIn('tvg-logo="' + "https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/ntv-malayalam.svg" + '"', updated)
        self.assertIn('group-title="Indian Entertainment"', updated)
        self.assertEqual(stats["orphan_backups_promoted"], 1)

    def test_jalsha_movies_alias_links_to_the_existing_primary(self):
        sample = (
            "#EXTM3U\n"
            + row("Star.Jalsha.Movies.in", "Jalsha Movies", "Indian Bangla", "https://stream.example/jalsha-primary.m3u8", language="ben", country="IN")
            + row("JalshaMovies.in@HD", "Jalsha Movies", "Backup", "https://stream.example/jalsha-backup.m3u8", language="ben", country="IN")
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertEqual(updated.count('group-title="Indian Bangla"'), 1)
        self.assertIn('tvg-id="Star.Jalsha.Movies.in"', updated)
        self.assertEqual(stats["name_matched_backups_linked"], 1)
        self.assertEqual(stats["orphan_backups_quarantined"], 0)



    def test_only_kids_leave_review_and_other_listed_channels_are_removed(self):
        sample = (
            "#EXTM3U\n"
            + row("GreenGoldTV.in@India", "Green Gold TV", "Review", "https://stream.example/greengold.m3u8", language="hin", country="IN")
            + row("Pogo.in@SD", "Pogo", "Review", "https://stream.example/pogo-primary.m3u8", language="eng", country="IN")
            + row("Pogo.in@SD", "Pogo", "Review", "https://stream.example/pogo-alt.m3u8", language="eng", country="IN")
            + row("WOWKidz.in@Hindi", "WOW Kidz Hindi", "Review", "https://stream.example/wow-hindi.m3u8", language="hin", country="IN")
            + row("TV9Bangla.in", "TV9 Bangla", "Review", "https://stream.example/tv9.m3u8", language="ben", country="IN")
            + row("DarshanaTV.in@SD", "Darshana TV", "Review", "https://stream.example/darshana.m3u8", language="mal", country="IN")
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertEqual(stats["kids_promoted_from_review"], 4)
        self.assertEqual(stats["non_kids_review_removed"], 2)
        self.assertIn('tvg-name="Green Gold TV"', updated)
        self.assertIn('tvg-name="WOW Kidz Hindi"', updated)
        self.assertNotIn("TV9 Bangla", updated)
        self.assertNotIn("Darshana TV", updated)
        self.assertEqual(updated.count('tvg-name="Pogo"'), 2)
        self.assertIn('group-title="Kids"', updated)
        self.assertIn('group-title="Backup"', updated)
        self.assertNotIn('group-title="Review"', updated)
        self.assertIn("https://stream.example/pogo-primary.m3u8", updated)
        self.assertIn("https://stream.example/pogo-alt.m3u8", updated)


    def test_mh_one_dil_se_is_restored_to_indian_music(self):
        sample = (
            "#EXTM3U\\n"
            + row("MHOneDilSe.in@SD", "MH One Dil Se", "Backup", "https://stream.example/dilse-primary.m3u8", language="hin", country="IN")
            + row("MHOneDilSe.in@SD", "MH One Dil Se", "Backup", "https://stream.example/dilse-alt.m3u8", language="hin", country="IN")
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertIn('tvg-name="MH One Dil Se"', updated)
        self.assertEqual(updated.count('group-title="Indian Music"'), 1)
        self.assertEqual(updated.count('group-title="Backup"'), 1)
        self.assertEqual(stats["orphan_backups_promoted"], 1)
        self.assertEqual(stats["orphan_backups_quarantined"], 0)
        self.assertNotIn("MH One Dil Se", stats.get("removed_channels", []))

    def test_mh_one_movies_is_restored_to_indian_movies(self):
        sample = (
            "#EXTM3U\\n"
            + row("MHOneMovies.in@SD", "MH One Movies", "Backup", "https://stream.example/movies-primary.m3u8", language="hin", country="IN")
            + row("MHOneMovies.in@SD", "MH One Movies", "Backup", "https://stream.example/movies-alt.m3u8", language="hin", country="IN")
        )
        updated, stats, errors = repair_playlist_text(sample)
        self.assertEqual(errors, [])
        self.assertIn('tvg-name="MH One Movies"', updated)
        self.assertEqual(updated.count('group-title="Indian Movies"'), 1)
        self.assertEqual(updated.count('group-title="Backup"'), 1)
        self.assertEqual(stats["orphan_backups_promoted"], 1)
        self.assertEqual(stats["orphan_backups_quarantined"], 0)


if __name__ == "__main__":
    unittest.main()
