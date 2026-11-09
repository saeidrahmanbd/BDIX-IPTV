# Cross-Playlist Metadata Backfill

Generated: **2026-11-09T04:16:32+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **e55dc8cf1536db3e5db4794947ea664c267179f08882d87e89517b0eacd5e286**
- International-Playlist.m3u SHA-256: **2f73d5e7ee3cde3ea44fe9a60438d57aa0ea6ddcdcddf39dbe53ca5be0132b4f**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (b01e30fba1ab...) | e55dc8cf1536db3e5db4794947ea664c267179f08882d87e89517b0eacd5e286 |
| International-Playlist.m3u | 0 | 0 | 0 | 738 | unchanged (3ef6b105080d...) | 2f73d5e7ee3cde3ea44fe9a60438d57aa0ea6ddcdcddf39dbe53ca5be0132b4f |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

