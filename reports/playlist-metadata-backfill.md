# Cross-Playlist Metadata Backfill

Generated: **2026-11-07T03:57:55+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **b95fe4f2b49f5681cd74d8b38165f16c748156de54b083c92d5d53e581752040**
- International-Playlist.m3u SHA-256: **9f8e42770e48101f22b5d788c9ca4df55778699ca1ea4d33ebff70289038edf0**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (f94da253b876...) | b95fe4f2b49f5681cd74d8b38165f16c748156de54b083c92d5d53e581752040 |
| International-Playlist.m3u | 0 | 0 | 0 | 1872 | unchanged (03b084500b37...) | 9f8e42770e48101f22b5d788c9ca4df55778699ca1ea4d33ebff70289038edf0 |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

