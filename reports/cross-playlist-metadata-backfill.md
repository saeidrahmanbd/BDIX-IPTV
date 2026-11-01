# Cross-Playlist Metadata Backfill

Generated: **2026-11-01T01:11:01+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **d9faa0bd18a7e337a947e992e486b256c8fc0eca1c451f59668ea256e0a0d5fd**
- BDIX-Playlist.m3u SHA-256: **6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d**
- International-Playlist.m3u SHA-256: **52ad5362536bcde90b14021af92b76cc1496ab5f084fcf0b0645e7ead017630a**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 40 | unchanged (9b699eda426e...) | d9faa0bd18a7e337a947e992e486b256c8fc0eca1c451f59668ea256e0a0d5fd |
| BDIX-Playlist.m3u | 0 | 0 | 0 | 47 | unchanged (59c715a48503...) | 6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d |
| International-Playlist.m3u | 0 | 0 | 0 | 2160 | unchanged (ddfe5bf9b041...) | 52ad5362536bcde90b14021af92b76cc1496ab5f084fcf0b0645e7ead017630a |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

