# Two-Playlist Maintenance Audit — Live Inventory

Generated: 2026-11-11 from current main-branch playlist files.

## IPTV-Playlist.m3u

| Metric | Verified result |
|---|---:|
| Entries | 1,331 |
| Missing tvg-logo attributes | 7 (4 active primary, 3 Review) |
| Active primary missing tvg-country | 0 |
| Active primary missing tvg-language | 0 |
| Broken local logo references | 0 |
| Duplicate primary identities | 0 |
| Duplicate alternatives retained in Backup | Yes |

### Remaining missing logo attributes
| Channel | tvg-id | Group | Playlist line |
|---|---|---|---:|
| Channel Fight | channel.fight.com | Sports | 1319 |
| FIGHT \| MVMT Culture | fight.mvmt.culture.com | Sports | 1323 |
| Homerun TV | homerun.tv.com | Sports | 1337 |
| WWE Superstar Central | wwe.superstar.central.com | Sports | 1371 |
| Action Bollywood Movies | action.bollywood.movies.in | Review | 2341 |
| MOV \| Bollywood OLD | mov.bollywood.old.in | Review | 2525 |
| playlist.m3u8 | playlist.m3u8.bd | Review | 2547 |

### Duplicate identity repair
The three repeated primary identities identified in the prior audit—Zee Bangla, 9X Tashan and Dangal 2—now have no duplicate primary rows. The extra stream rows were retained in Backup; stream URLs were not deleted. The latest completed Test Suite run at commit `c61bf147` passed.

## International-Playlist.m3u

| Metric | Verified result |
|---|---:|
| Entries | 3,094 |
| Active entries (excluding Adult, Backup and Review queues) | 1,362 |
| Missing tvg-logo attributes, all groups | 374 |
| Active entries missing tvg-logo | 19 |
| Active entries missing tvg-country | 0 |
| Active entries with blank tvg-language | 905 |
| Duplicate active tvg-id identities | 0 |

## Remediation commits and pending execution

- Official Channel Fight logo source added from the broadcaster's own About page.
- Exact FIGHT | MVMT Culture logo source added from a public playlist carrying the same channel identity and matching stream.
- Exact WWE SUPERSTAR CENTRAL trademark image source added; trademark filing identifies World Wrestling Entertainment, LLC as owner.
- The logo localization workflow will download, validate, localize and commit these assets only if the source bytes pass image validation.
- International metadata backfill now reads exact channel/feed language records from the public iptv-org API. If no reliable source resolves a language, it will use `und` (ISO 639-2: undetermined) rather than guess a language. This preserves metadata completeness without inventing broadcast languages.

## Outstanding source limitations

- Homerun TV and the active Surfing+/MVMT of Culture identities still need exact, channel-specific static logo assets. No unrelated or generated logo is assigned.
- The remaining 19 active International logo gaps still require exact source validation; 355 other missing-logo attributes are in Adult/Backup/Review or other non-primary queues.
- EPG refresh is currently occupying the repository's writer slot. The playlist-maintenance and logo-localization runs are queued behind it, so the latest source-backed metadata/logo changes have not yet been applied to the published playlist.

## Protection

No stream URL was deleted during the duplicate repair. The IPTV playlist's existing row order and channel positions were preserved. Review, Adult and Backup queues remain intact.
