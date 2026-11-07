# Cross-Playlist Metadata Backfill

Generated: **2026-11-07T04:31:06+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **b21a4dad6ee749428f415bb044c876dc88c6e8cada2c5e50c155b3c9397a16ff**
- International-Playlist.m3u SHA-256: **9f8e42770e48101f22b5d788c9ca4df55778699ca1ea4d33ebff70289038edf0**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (2f05c80d4e56...) | b21a4dad6ee749428f415bb044c876dc88c6e8cada2c5e50c155b3c9397a16ff |
| International-Playlist.m3u | 0 | 0 | 0 | 1872 | unchanged (03b084500b37...) | 9f8e42770e48101f22b5d788c9ca4df55778699ca1ea4d33ebff70289038edf0 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

