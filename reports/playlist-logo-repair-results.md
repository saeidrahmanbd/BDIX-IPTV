# Two-Playlist Maintenance Audit — Live Inventory

Generated: 2026-11-11 from current main-branch playlist files.

## IPTV-Playlist.m3u

| Metric | Verified result |
|---|---:|
| Entries | 1,373 |
| Missing tvg-logo | 10 (7 active primary, 3 Review) |
| Active primary missing tvg-country | 0 |
| Active primary missing tvg-language | 0 |
| Broken local logo references | 0 |
| Duplicate primary identities | 3 |
| Category registry | Matches canonical order |

### Missing logo attributes
| Channel | tvg-id | Group | Playlist line |
|---|---|---|---:|
| Channel Fight | channel.fight.com | Sports | 1373 |
| Channel Fight | channel.fight.com@channel.fight | Sports | 1375 |
| FIGHT \| MVMT Culture | fight.mvmt.culture.com | Sports | 1383 |
| Homerun TV | homerun.tv.com | Sports | 1399 |
| MVMT of Culture | mvmt.of.culture.com | Sports | 1415 |
| Surfing+ 冲浪 | surfing.com | Sports | 1443 |
| WWE Superstar Central | wwe.superstar.central.com | Sports | 1453 |
| Action Bollywood Movies | action.bollywood.movies.in | Review | 2397 |
| MOV \| Bollywood OLD | mov.bollywood.old.in | Review | 2581 |
| playlist.m3u8 | playlist.m3u8.bd | Review | 2603 |

### Duplicate primary identities requiring owner-safe review
| Channel | tvg-id | Rows | Distinct stream URLs |
|---|---|---:|---:|
| Zee Bangla | ZeeBangla.in@HD | 171, 2359 | 2 |
| 9X Tashan | 9XTashan.in@SD | 313, 1487 | 2 |
| Dangal 2 | Dangal2.in@SD | 479, 1707 | 2 |

These are real repeated identities with different stream URLs, not duplicate URL rows. They have been left untouched: the owner's protection policy prohibits deleting, moving, reordering, or changing existing primary rows without explicit channel-specific authorization.

## International-Playlist.m3u

| Metric | Verified result |
|---|---:|
| Entries | 3,094 |
| Active entries (excluding Adult, Backup and Review queues) | 1,362 |
| Active entries missing tvg-logo | 19 |
| Active entries missing tvg-country | 0 |
| Active entries with blank tvg-language | 905 |
| Duplicate active tvg-id identities | 0 |

The 19 missing-logo rows and 905 blank language fields need source-backed correction. Adult entries are intentionally excluded from this metadata summary; Adult and Review/Backup rows remain protected.

## Source-backed logo work started

A verified official Channel Fight image asset was added to `scripts/repair_playlist_logos.py`, sourced from the broadcaster's own About page. Both Channel Fight identities can use this exact brand asset. The logo-localization workflow was automatically queued by the code commit and must complete validation before the image can be counted as committed/localized.

The other eight IPTV logo gaps and the 19 International logo gaps remain open until exact broadcaster/channel assets are verified. No unrelated or generated logo has been assigned.

## Protection and next actions

- No playlist stream URL, row position, group assignment, channel ID, or primary identity was modified by this audit.
- Metadata gaps are not filled with guessed language values.
- The three IPTV repeated identities are documented for an explicit owner decision; each pair has two distinct stream URLs.
- The International blank-language backlog needs channel-by-channel source verification.
- The logo workflow must finish and its resulting playlist and asset changes must be re-audited before claiming completion.
