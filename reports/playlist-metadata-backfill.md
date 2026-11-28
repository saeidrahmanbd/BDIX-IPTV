# Cross-Playlist Metadata Backfill

Generated: **2026-11-28T17:17:14+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **83aaad779aa5e264863fe62a7f14406ee21c34e2c8dc7b46bccf60f8918b563b**
- International-Playlist.m3u SHA-256: **3f5544e59667a5d364259a8597706c9c58b7a4c1712ed1a990487f259da730b0**

Only missing country/language fields and blank channel-id fields were filled. Country may also come from dedicated country-group labels; generic genre groups are never used as country evidence. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries. Existing channel-id values are preserved.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Channel IDs filled | Country-group fills | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | 0 | 91 | unchanged (af797a878a42...) | 83aaad779aa5e264863fe62a7f14406ee21c34e2c8dc7b46bccf60f8918b563b |
| International-Playlist.m3u | 995 | 0 | 0 | 995 | 0 | 0 | 7 | unchanged (8e34d53a6e7c...) | 3f5544e59667a5d364259a8597706c9c58b7a4c1712ed1a990487f259da730b0 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country is inferred only from dedicated country groups; generic genre groups are never treated as country evidence.
- Complete metadata does not guarantee EPG schedule coverage.

