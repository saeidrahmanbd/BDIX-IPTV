# Cross-Playlist Metadata Backfill

Generated: **2026-11-14T11:03:29+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **7fd0e715791c7916376cb3c6b854255968394936eb0c4def468bfa8ce4fb0bc0**
- International-Playlist.m3u SHA-256: **7a4bc7da2f2131dbc25986094a3e30fe02503241772fe4730afa8947aec02a7a**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (5a0a6e938d19...) | 7fd0e715791c7916376cb3c6b854255968394936eb0c4def468bfa8ce4fb0bc0 |
| International-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (f2275dd504fd...) | 7a4bc7da2f2131dbc25986094a3e30fe02503241772fe4730afa8947aec02a7a |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

