# Cross-Playlist Metadata Backfill

Generated: **2026-10-30T07:14:55+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **2f00cd81215b375e4776d6dd458f71acc5734daf86990b5c85061a1bec922a77**
- BDIX-Playlist.m3u SHA-256: **6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d**
- International-Playlist.m3u SHA-256: **359731d46ab6910e71335940aacfdeb1321d84c824fea6e120575031d128eff3**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 40 | unchanged (5a6888004d1f...) | 2f00cd81215b375e4776d6dd458f71acc5734daf86990b5c85061a1bec922a77 |
| BDIX-Playlist.m3u | 0 | 0 | 0 | 47 | unchanged (59c715a48503...) | 6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d |
| International-Playlist.m3u | 0 | 0 | 0 | 2078 | unchanged (478e4695edb9...) | 359731d46ab6910e71335940aacfdeb1321d84c824fea6e120575031d128eff3 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

