# Cross-Playlist Metadata Backfill

Generated: **2026-11-22T02:39:15+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **7535ac5bcd4eac4cc0fd8d5d4f13254a73b76d8c1b366adaca9a6c4571ad83b1**
- International-Playlist.m3u SHA-256: **c84753e5cb4a8012f7214b7d3ca307ed0f6c3609e61ca8a71ab4b4dcbf6c3979**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (a3a2f9e6329e...) | 7535ac5bcd4eac4cc0fd8d5d4f13254a73b76d8c1b366adaca9a6c4571ad83b1 |
| International-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (bf6245df4e4c...) | c84753e5cb4a8012f7214b7d3ca307ed0f6c3609e61ca8a71ab4b4dcbf6c3979 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

