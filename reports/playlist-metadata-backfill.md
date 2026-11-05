# Cross-Playlist Metadata Backfill

Generated: **2026-11-05T09:32:26+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **f5795953ab6e9474334bc1dc17149eaf70528a4602c0084f59ecbe44665f78ef**
- International-Playlist.m3u SHA-256: **6d2eff069479f56cae583e9f3abda2e8e9bd1721794e53ba34ae55220a8fc4d7**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (1ad7dec94e0d...) | f5795953ab6e9474334bc1dc17149eaf70528a4602c0084f59ecbe44665f78ef |
| International-Playlist.m3u | 12 | 0 | 12 | 1786 | unchanged (c2ac5a45bbf2...) | 6d2eff069479f56cae583e9f3abda2e8e9bd1721794e53ba34ae55220a8fc4d7 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

