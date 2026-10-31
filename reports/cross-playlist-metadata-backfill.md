# Cross-Playlist Metadata Backfill

Generated: **2026-10-31T08:28:13+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **3602101f00a9ad15e65a0892743076a3c8fb52f5c135f1b288b318691497b8e4**
- BDIX-Playlist.m3u SHA-256: **6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d**
- International-Playlist.m3u SHA-256: **ff55ab74a403066cf3713a188d4867b65b1179db7fcfa6c0645955a0449081b3**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 39 | unchanged (be37b44a2ab7...) | 3602101f00a9ad15e65a0892743076a3c8fb52f5c135f1b288b318691497b8e4 |
| BDIX-Playlist.m3u | 0 | 0 | 0 | 47 | unchanged (59c715a48503...) | 6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d |
| International-Playlist.m3u | 0 | 0 | 0 | 2139 | unchanged (7407cdbb0008...) | ff55ab74a403066cf3713a188d4867b65b1179db7fcfa6c0645955a0449081b3 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

