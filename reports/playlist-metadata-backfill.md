# Cross-Playlist Metadata Backfill

Generated: **2026-11-16T02:45:41+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **910e85f0a79f101b8afe550c781126fb156b183e4c678472f2fe3f1699777d73**
- International-Playlist.m3u SHA-256: **38d1fd58e55765408fb8599d7bad532fc9711e27611fa1345dfd9e76775fe11c**

Only missing tvg-country and tvg-language values were filled. Sources: exact playlist tvg-id/channel-id, unique exact channel names, and iptv-org channel/feed metadata. Unresolved broadcast languages are marked und (ISO 639-2 undetermined), never guessed. iptv-org catalogue status: loaded.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Review/Adult/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Language marked undetermined | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | 0 | unchanged (18e0425c59f2...) | 910e85f0a79f101b8afe550c781126fb156b183e4c678472f2fe3f1699777d73 |
| International-Playlist.m3u | 8 | 0 | 8 | 2 | 0 | unchanged (00810fab5b7a...) | 38d1fd58e55765408fb8599d7bad532fc9711e27611fa1345dfd9e76775fe11c |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

