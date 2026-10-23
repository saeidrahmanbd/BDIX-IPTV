# Cross-Playlist Metadata Backfill

Generated: **2026-10-23T08:43:58+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **0ce6e1a9799733fae3febaa075d00c8c19a71f5ec225525a6559bbdcdc7ad3d5**
- BDIX-Playlist.m3u SHA-256: **9cc2eaa4f9209e4d1a2576f9953f47240c176f15a929c41c94b9394f62323d81**
- International-Playlist.m3u SHA-256: **dedc725ba5eccdb5619232a12750cd1b3397122ca4627d5c7a1da58c18c3537c**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 203 | unchanged (c7b22678f256...) | 0ce6e1a9799733fae3febaa075d00c8c19a71f5ec225525a6559bbdcdc7ad3d5 |
| BDIX-Playlist.m3u | 96 | 96 | 90 | 49 | unchanged (4b0e1b0e7504...) | 9cc2eaa4f9209e4d1a2576f9953f47240c176f15a929c41c94b9394f62323d81 |
| International-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (1070f6ed34ae...) | dedc725ba5eccdb5619232a12750cd1b3397122ca4627d5c7a1da58c18c3537c |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

