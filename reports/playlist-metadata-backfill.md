# Cross-Playlist Metadata Backfill

Generated: **2026-11-15T02:21:26+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **7a602ff4a6fe777cc812dcedb118b638ab62913c0987dff0a6ac7d674a974d65**
- International-Playlist.m3u SHA-256: **8acb8898c683fa633d4a1a86dfef767a1fb68f0a516ff9055f06d9a2fac6c38d**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (4bb8b2eea254...) | 7a602ff4a6fe777cc812dcedb118b638ab62913c0987dff0a6ac7d674a974d65 |
| International-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (d8d4a1e25b19...) | 8acb8898c683fa633d4a1a86dfef767a1fb68f0a516ff9055f06d9a2fac6c38d |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

