# Cross-Playlist Metadata Backfill

Generated: **2026-11-17T04:58:44+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **037d30711009a5d40bb284fd4e55a73f8669cc19e5fb36f8d85f86181f377561**
- International-Playlist.m3u SHA-256: **02fa0e014d1b14e61df1acc8684e5b925123a2ae7fac1b6152c3264b384f7faf**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (d14fbec69f2d...) | 037d30711009a5d40bb284fd4e55a73f8669cc19e5fb36f8d85f86181f377561 |
| International-Playlist.m3u | 8 | 0 | 8 | 1 | 0 | unchanged (6296b39ded93...) | 02fa0e014d1b14e61df1acc8684e5b925123a2ae7fac1b6152c3264b384f7faf |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

