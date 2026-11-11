# Cross-Playlist Metadata Backfill

Generated: **2026-11-11T07:41:11+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **de1b7f58ac232ec72d734c2aca3bb35070d31536fda83b52f4e4ac1cc39dde5a**
- International-Playlist.m3u SHA-256: **04d00a92994d4ed13aa2f78ce3d2c0ecf3dc2467eac328f4327fe4d78c36840a**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (7581ebd540e0...) | de1b7f58ac232ec72d734c2aca3bb35070d31536fda83b52f4e4ac1cc39dde5a |
| International-Playlist.m3u | 0 | 0 | 0 | 896 | unchanged (fc8f60cd00a1...) | 04d00a92994d4ed13aa2f78ce3d2c0ecf3dc2467eac328f4327fe4d78c36840a |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

