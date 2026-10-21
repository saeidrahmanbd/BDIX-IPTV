# EPG Audit — Published Playlists

Generated: **2026-10-21T00:38:55+00:00**

This report measures the two M3U files currently published at the repository root. The historic filename epg-three-playlist-audit.md is retained for link compatibility; it does not mean a third playlist file exists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1088 | 639 | 422 | 401 | 422 | 392 | 217 | OK |
| BDIX-Playlist.m3u | 139 | 131 | 78 | 74 | 78 | 73 | 53 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Bangladesh | 66 | 3 | 1 | 63 |
| Documentary & Wildlife | 84 | 66 | 64 | 18 |
| Indian Bangla | 44 | 34 | 33 | 10 |
| Indian Entertainment | 142 | 123 | 116 | 19 |
| Indian Movies | 63 | 51 | 49 | 12 |
| Indian Music | 53 | 47 | 44 | 6 |
| International | 107 | 62 | 60 | 45 |
| Kids | 48 | 32 | 32 | 16 |
| Pakistani | 18 | 3 | 3 | 15 |
| Religious | 26 | 10 | 9 | 16 |
| Sports | 41 | 29 | 26 | 12 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with allowed-language titles inside the generator's -6-hour/+7-day window.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **ee851e7cc4586db6af2ed6053089b2b6847adfba5ccf91fd7f69e56f36d0b819**
- BDIX-Playlist.m3u SHA-256: **b119c1b2cb35778f42345430829ffcd4787b2dc77210c99ba8d6bdefeb7ef531**
