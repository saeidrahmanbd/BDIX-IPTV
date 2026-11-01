# Cross-Playlist Metadata Backfill

Generated: **2026-11-01T01:04:55+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **f0cb6668da556a3fb1ade5b33d0d5bcda66a9f5485eee0f181b201837a0602a3**
- BDIX-Playlist.m3u SHA-256: **6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d**
- International-Playlist.m3u SHA-256: **cee4b739eaa039a5f617b2fdcfca785b2fb2fe18484bb850778a4f212f302267**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 40 | unchanged (de8ed0ee83f4...) | f0cb6668da556a3fb1ade5b33d0d5bcda66a9f5485eee0f181b201837a0602a3 |
| BDIX-Playlist.m3u | 0 | 0 | 0 | 47 | unchanged (59c715a48503...) | 6e98537a07d9bb5f5ee818f86defff1357302adeaca270e0786a7185bcd33b2d |
| International-Playlist.m3u | 0 | 0 | 0 | 2177 | unchanged (48c5bafb7fa8...) | cee4b739eaa039a5f617b2fdcfca785b2fb2fe18484bb850778a4f212f302267 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

