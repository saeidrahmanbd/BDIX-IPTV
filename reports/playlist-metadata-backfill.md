# Cross-Playlist Metadata Backfill

Generated: **2026-11-14T15:38:45+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **d47607e2306ca0561e6181336ea25952f4f93a6f56d47b33abbb2b7d221b6c6b**
- International-Playlist.m3u SHA-256: **225d5cf541242d32ce489e1dccd3c1fb234fc78fc60e918ae449ff129b48a5dd**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (5a0a6e938d19...) | d47607e2306ca0561e6181336ea25952f4f93a6f56d47b33abbb2b7d221b6c6b |
| International-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (f2275dd504fd...) | 225d5cf541242d32ce489e1dccd3c1fb234fc78fc60e918ae449ff129b48a5dd |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

