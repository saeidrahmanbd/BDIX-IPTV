# Playlist Logo Repair Results — Fresh Live Inventory

Generated: 2026-11-11 (fresh read of current main branch)

## Current verified inventory

| Metric | Current |
|---|---:|
| IPTV-Playlist.m3u entries | 1,391 |
| Entries with missing tvg-logo | 12 |
| Active primary entries missing tvg-logo | 7 |
| Review queue entries missing tvg-logo | 5 |
| Broken/missing local assets referenced by playlist | 0 |
| Duplicate primary identities in current playlist | 0 |
| Active primary entries missing tvg-country | 0 |
| Active primary entries missing tvg-language | 0 |
| Category registry matches canonical order | Yes |

The previous 46-missing-logo figure was stale: it came from an older audit snapshot. The current playlist contains 12 blank logo attributes, not 46. The old audit's duplicate-primary and category-registry warnings are also stale; a fresh read finds zero duplicate primary IDs and a canonical category registry.

## Unresolved logo entries

### Active primary (7)
| Channel | tvg-id | Group | Playlist line |
|---|---|---|---:|
| Channel Fight | channel.fight.com | Sports | 1389 |
| Channel Fight | channel.fight.com@channel.fight | Sports | 1391 |
| FIGHT \| MVMT Culture | fight.mvmt.culture.com | Sports | 1399 |
| Homerun TV | homerun.tv.com | Sports | 1415 |
| MVMT of Culture | mvmt.of.culture.com | Sports | 1431 |
| Surfing+ 冲浪 | surfing.com | Sports | 1459 |
| WWE Superstar Central | wwe.superstar.central.com | Sports | 1469 |

### Review queue (5)
| Channel | tvg-id | Group | Playlist line |
|---|---|---|---:|
| Action Bollywood Movies | action.bollywood.movies.in | Review | 2423 |
| MOV \| Bollywood OLD | mov.bollywood.old.in | Review | 2609 |
| playlist.m3u8 | playlist.m3u8.bd | Review | 2631 |
| SOLOCALCIO ITALIA | Si Solo Calcio.it | Review | 2663 |
| TVS Sports Bureau | TVSSportsBureau.us@SD | Review | 2737 |

## Remediation status

No logo has been fabricated or assigned from an unrelated broadcaster. The current curated logo source catalog has no exact channel-specific match for these 12 identities. The seven active primary logo gaps remain unresolved pending verified source assets; the five Review entries remain manual-review items.

Playlist stream URLs, group assignments, row order, and channel IDs were not changed by this inventory refresh. Logo repair must update only tvg-logo attributes and add verified local files.