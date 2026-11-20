# Cross-Playlist Metadata Backfill

Generated: **2026-11-20T05:26:40+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **10dc5d953b8fa919ba140bcf0d52bec4b3bdcf891a095bd114c71c57796b4afe**
- International-Playlist.m3u SHA-256: **0731d79d35f8d9e3565f4f05f4e8512bdc8658b9b14d674cdb34d170cb5c0262**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (120951c54a47...) | 10dc5d953b8fa919ba140bcf0d52bec4b3bdcf891a095bd114c71c57796b4afe |
| International-Playlist.m3u | 11 | 0 | 11 | 4 | 0 | unchanged (6c09c2a29d7a...) | 0731d79d35f8d9e3565f4f05f4e8512bdc8658b9b14d674cdb34d170cb5c0262 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

