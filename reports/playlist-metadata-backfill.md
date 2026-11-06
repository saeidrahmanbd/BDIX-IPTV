# Cross-Playlist Metadata Backfill

Generated: **2026-11-06T16:19:03+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **d8ac07ce135cde8d024e6a4945c377175132e290d02e275bcd0e376fdddc692e**
- International-Playlist.m3u SHA-256: **b078f1fd249dddda658c225e25359a2770bfd1a866888f57f0c1e3ff37ae2bb4**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 56 | unchanged (71794ee9b03b...) | d8ac07ce135cde8d024e6a4945c377175132e290d02e275bcd0e376fdddc692e |
| International-Playlist.m3u | 0 | 0 | 0 | 1876 | unchanged (03b084500b37...) | b078f1fd249dddda658c225e25359a2770bfd1a866888f57f0c1e3ff37ae2bb4 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

