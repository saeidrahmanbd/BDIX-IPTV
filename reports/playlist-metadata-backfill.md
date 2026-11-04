# Cross-Playlist Metadata Backfill

Generated: **2026-11-04T03:59:25+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **f5525b8591cc8d59e6d66f26bb068d63e51cf4ae91b6e0f369dc8bf54c0a9ef7**
- International-Playlist.m3u SHA-256: **8323569d467e288ca7fa7cda014698d9182009da45345456ffb252bf4aa54b6c**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (fb4e00d52aff...) | f5525b8591cc8d59e6d66f26bb068d63e51cf4ae91b6e0f369dc8bf54c0a9ef7 |
| International-Playlist.m3u | 1 | 0 | 1 | 1685 | unchanged (b6ab7a4c8fab...) | 8323569d467e288ca7fa7cda014698d9182009da45345456ffb252bf4aa54b6c |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

