# Cross-Playlist Metadata Backfill

Generated: **2026-11-14T18:26:29+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **7a602ff4a6fe777cc812dcedb118b638ab62913c0987dff0a6ac7d674a974d65**
- International-Playlist.m3u SHA-256: **225d5cf541242d32ce489e1dccd3c1fb234fc78fc60e918ae449ff129b48a5dd**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (4bb8b2eea254...) | 7a602ff4a6fe777cc812dcedb118b638ab62913c0987dff0a6ac7d674a974d65 |
| International-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (f2275dd504fd...) | 225d5cf541242d32ce489e1dccd3c1fb234fc78fc60e918ae449ff129b48a5dd |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

