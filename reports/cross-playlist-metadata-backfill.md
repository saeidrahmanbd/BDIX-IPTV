# Cross-Playlist Metadata Backfill

Generated: **2026-10-30T02:22:16+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **7f2fa0e3b0ff34ceb5823b465b75dc99e6fb3fc8f1fac5a8c5f88b0ed52663ab**
- BDIX-Playlist.m3u SHA-256: **6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d**
- International-Playlist.m3u SHA-256: **359731d46ab6910e71335940aacfdeb1321d84c824fea6e120575031d128eff3**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 39 | unchanged (77d745e8b02d...) | 7f2fa0e3b0ff34ceb5823b465b75dc99e6fb3fc8f1fac5a8c5f88b0ed52663ab |
| BDIX-Playlist.m3u | 4 | 2 | 2 | 47 | unchanged (59c715a48503...) | 6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d |
| International-Playlist.m3u | 0 | 0 | 0 | 2078 | unchanged (478e4695edb9...) | 359731d46ab6910e71335940aacfdeb1321d84c824fea6e120575031d128eff3 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

