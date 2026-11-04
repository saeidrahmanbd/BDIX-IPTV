# Cross-Playlist Metadata Backfill

Generated: **2026-11-04T06:59:31+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **f5525b8591cc8d59e6d66f26bb068d63e51cf4ae91b6e0f369dc8bf54c0a9ef7**
- International-Playlist.m3u SHA-256: **aeb8d4a01127431800f3d41cd7e5934b47898a40cbdbecf0961070f51a3b6a59**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (fb4e00d52aff...) | f5525b8591cc8d59e6d66f26bb068d63e51cf4ae91b6e0f369dc8bf54c0a9ef7 |
| International-Playlist.m3u | 0 | 0 | 0 | 1723 | unchanged (b3c3aa61eb59...) | aeb8d4a01127431800f3d41cd7e5934b47898a40cbdbecf0961070f51a3b6a59 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

