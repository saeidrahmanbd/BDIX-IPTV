# Cross-Playlist Metadata Backfill

Generated: **2026-11-06T16:36:02+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **92a045f671165942d728082edaac08bdaa83c0320afde042d00ed9b6ea1da67a**
- International-Playlist.m3u SHA-256: **aae6f5ef820c5a79ff1c0b8851f20d920017bd234c0f33ac9762a9d69fe2bd6c**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 56 | unchanged (71794ee9b03b...) | 92a045f671165942d728082edaac08bdaa83c0320afde042d00ed9b6ea1da67a |
| International-Playlist.m3u | 0 | 0 | 0 | 1875 | unchanged (03b084500b37...) | aae6f5ef820c5a79ff1c0b8851f20d920017bd234c0f33ac9762a9d69fe2bd6c |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

