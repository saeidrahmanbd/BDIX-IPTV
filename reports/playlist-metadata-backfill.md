# Cross-Playlist Metadata Backfill

Generated: **2026-11-02T11:00:34+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **0effbae25904525535b8b1cccb3c1c4a955b5785b5476d006857db7be5f26a1f**
- International-Playlist.m3u SHA-256: **40a24be4246311287b2dd8832fae710f90d84e662ce01d9917bceda503cca03a**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 64 | unchanged (c06dc482981e...) | 0effbae25904525535b8b1cccb3c1c4a955b5785b5476d006857db7be5f26a1f |
| International-Playlist.m3u | 0 | 0 | 0 | 1546 | unchanged (60d744521834...) | 40a24be4246311287b2dd8832fae710f90d84e662ce01d9917bceda503cca03a |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

