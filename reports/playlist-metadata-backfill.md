# Cross-Playlist Metadata Backfill

Generated: **2026-11-06T01:37:58+00:00**

## Source playlist fingerprints

- IPTV-Playlist.m3u SHA-256: **c1e170f5553fb67bfd7966dc803db253fd14b6e20a94375f13cf7f6b50710bc0**
- International-Playlist.m3u SHA-256: **e814b18119f4b61d43e5847f0873e7149ccd419b95fffee10ec79d21af75b0da**

Only missing tvg-country and tvg-language values were filled. Source evidence was an exact tvg-id match or an unambiguous exact tvg-name match. Unknown or ambiguous values remain blank.
The script does not modify tvg-id, tvg-name, tvg-logo, tvg-chno, group-title, stream URLs, or Backup/Not Playing entries.

## Playlist results

| Playlist | Entries changed | Country fields filled | Language fields filled | Active entries still missing either field | Stream URL inventory | SHA-256 |
|---|---:|---:|---:|---:|---|---|
| IPTV-Playlist.m3u | 0 | 0 | 0 | 0 | unchanged (c3d3966c20ca...) | c1e170f5553fb67bfd7966dc803db253fd14b6e20a94375f13cf7f6b50710bc0 |
| International-Playlist.m3u | 3 | 0 | 3 | 1783 | unchanged (c2ac5a45bbf2...) | e814b18119f4b61d43e5847f0873e7149ccd419b95fffee10ec79d21af75b0da |

## Policy

- Channel numbers and group placement are playlist-specific and are intentionally not synchronized.
- Country/language values are not inferred from group names alone.
- Complete metadata does not guarantee EPG schedule coverage.

