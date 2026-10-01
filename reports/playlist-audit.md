# Playlist Audit

Generated: 2026-10-01 09:12 UTC

Recalculated directly from the current main-branch IPTV-Playlist.m3u.

## Summary

| Check | Current |
|---|---:|
| Playlist entries | **1,000** |
| Active primary entries | **587** |
| Backup entries | **413** |
| Unique channel IDs | **624** |
| Duplicate stream URLs | **0** |
| Duplicate primary identities | **5** |
| Primary channel-number collisions | **0** |
| Primary entries missing tvg-chno | **31** |
| Missing tvg-id | **0** |
| Missing channel-id | **0** |
| Missing tvg-name | **0** |
| Missing tvg-logo | **0** |
| Missing stream URL | **0** |
| External logo references | **0** |
| Signed/tokenized stream URLs | **15** |
| Suspicious credential/malformed URLs | **0** |
| Same-name / different-ID collisions | **6** |

## Important Findings

### Five duplicate primary identities

- custom.bengali.beats — Bangladesh + Indian Bangla
- ColorsBanglaCinema.in@SD — Indian Bangla + Indian Movies
- B4UMusic.in@India — Indian Movies + Indian Music
- ColorsCineplex.in@SD — two Indian Movies entries
- SonyEntertainmentTelevision.in@SD — Indian Movies + Indian Entertainment

### Thirty-one active entries have no channel number

Affected entries include ATN BANGLA UK, Bengali Beats, Green TV, Sony AATH, B4U Bhojpuri Plus (1080p), B4U Music, Colors Bangla Cinema, Colors Cineplex, Colors Cineplex Superhits, Colors Gujarati Cinema, Colors Kannada Cinema, Goldmines Movies, Kairali TV, Sidharth Gold, Sony Entertainment TV, Star Suvarna Plus, Star Utsav Movies, Vijay Super, Zee Cinemalu HD, Zee Talkies HD, 7X Music, Colors, Colors Rishtey, 30A Music, AMC, GREAT! movies, Sony Movies, Trace Urban, XITE Hits, Піксель TV, and Lego Channel.

### Duplicate stream URLs

**0 detected.**

### Logo integrity

**0 missing, 0 external, 0 broken-local references** were detected from playlist metadata. All 1,000 entries currently point to repository-hosted logo assets.

### Signed/tokenized URLs

**15 entries** contain token/signature/session-style URL parameters. These are warnings, not automatic failures.

### Stream health limitation

This is a structural/metadata audit. It does not prove that a stream is currently playable. A separate health check is required to classify HTTP failure, timeout, invalid HLS/TS, and successful responses. Backup entries should not be deleted from a single failed probe.

## Category Totals

| Category | Entries |
|---|---:|
| Bangladesh | 57 |
| Indian Bangla | 35 |
| Indian Movies | 81 |
| Indian Music | 49 |
| Indian Entertainment | 94 |
| International | 90 |
| Documentary & Wildlife | 62 |
| Kids | 57 |
| Religious | 18 |
| Sports | 44 |
| Backup | 413 |

## EPG Reconciliation

The existing EPG report covers 244 active Indian channels, with 158 mapped and 86 without a guide mapping. The current playlist now contains 259 Indian-category entries, so the EPG report is stale and its denominator must be regenerated.

## Audit Interpretation

**STRUCTURAL STATUS: NEEDS REPAIR.**

The playlist has no duplicate stream URLs and complete logo/ID/name fields, but it is not metadata-clean because of 5 duplicate primary identities and 31 missing primary channel numbers.

No stream was removed by this audit.
