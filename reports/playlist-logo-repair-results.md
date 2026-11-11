# Playlist Logo Repair Results — Fresh Live Inventory

Generated: 2026-11-11 (fresh read of current main branch)

## Current verified IPTV inventory

| Metric | Current |
|---|---:|
| IPTV-Playlist.m3u entries | 1,391 |
| Entries with missing tvg-logo | 10 |
| Active primary entries missing tvg-logo | 7 |
| Review queue entries missing tvg-logo | 3 |
| Broken/missing local assets referenced by playlist | 0 |
| Duplicate primary identities in current playlist | 0 |
| Active primary entries missing tvg-country | 0 |
| Active primary entries missing tvg-language | 0 |
| Category registry matches canonical order | Yes |

The earlier 46-entry and 12-entry missing-logo counts were stale snapshots. A fresh parse of the current playlist finds 10 blank logo attributes. The earlier duplicate-primary and category-registry warnings are also not present in this snapshot.

## Unresolved logo entries

### Active primary (7)
| Channel | tvg-id | Group | Playlist line |
|---|---|---|---:|
| Channel Fight | channel.fight.com | Sports | 1373 |
| Channel Fight | channel.fight.com@channel.fight | Sports | 1375 |
| FIGHT \| MVMT Culture | fight.mvmt.culture.com | Sports | 1383 |
| Homerun TV | homerun.tv.com | Sports | 1399 |
| MVMT of Culture | mvmt.of.culture.com | Sports | 1415 |
| Surfing+ 冲浪 | surfing.com | Sports | 1443 |
| WWE Superstar Central | wwe.superstar.central.com | Sports | 1453 |

### Review queue (3)
| Channel | tvg-id | Group | Playlist line |
|---|---|---|---:|
| Action Bollywood Movies | action.bollywood.movies.in | Review | 2397 |
| MOV \| Bollywood OLD | mov.bollywood.old.in | Review | 2581 |
| playlist.m3u8 | playlist.m3u8.bd | Review | 2603 |

## Remediation status

- Added a verified official Channel Fight image source to the logo-repair catalog. The source is the image asset linked from the broadcaster's own About page; the scheduled logo-localization workflow will download, validate, localize and apply it to both Channel Fight entries.
- The other eight identities still require exact channel-specific source assets. No unrelated or generated logos have been assigned.
- The two Review entries SOLOCALCIO ITALIA and TVS Sports Bureau already have local logo references in the live playlist and are not missing-logo cases.
- The current primary metadata audit finds no missing country/language values and no duplicate primary identities.

Playlist stream URLs, group assignments, row order, and channel IDs remain protected. Logo repair may change only tvg-logo attributes and add verified local assets.
