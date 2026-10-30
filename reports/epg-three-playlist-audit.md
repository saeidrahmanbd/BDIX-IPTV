# EPG Audit — Published Playlists

Generated: **2026-10-30T01:10:43+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1161 | 694 | 466 | 412 | 466 | 399 | 228 | OK |
| BDIX-Playlist.m3u | 131 | 131 | 78 | 71 | 78 | 71 | 53 | OK |
| International-Playlist.m3u | 3257 | 2707 | 869 | 705 | 863 | 670 | 1838 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 359 | 6 | 6 | 353 |
| Argentina | 17 | 1 | 1 | 16 |
| Aruba | 6 | 0 | 0 | 6 |
| Bangladesh | 87 | 3 | 1 | 84 |
| Brazil | 12 | 2 | 2 | 10 |
| Bulgaria | 15 | 7 | 6 | 8 |
| Canada | 26 | 20 | 16 | 6 |
| Chile | 27 | 1 | 0 | 26 |
| China | 14 | 0 | 0 | 14 |
| Colombia | 13 | 1 | 1 | 12 |
| Czech Republic | 26 | 9 | 3 | 17 |
| Documentary & Wildlife | 217 | 137 | 102 | 80 |
| Dominican Republic | 7 | 0 | 0 | 7 |
| Egypt | 5 | 2 | 0 | 3 |
| Estonia | 6 | 1 | 0 | 5 |
| France | 45 | 9 | 7 | 36 |
| Germany | 78 | 11 | 9 | 67 |
| Greece | 9 | 2 | 2 | 7 |
| Hungary | 16 | 8 | 6 | 8 |
| Indian Bangla | 51 | 41 | 35 | 10 |
| Indian Entertainment | 228 | 191 | 176 | 37 |
| Indian Movies | 93 | 70 | 67 | 23 |
| Indian Music | 72 | 59 | 56 | 13 |
| International | 98 | 56 | 46 | 42 |
| Iran | 16 | 3 | 2 | 13 |
| Italy | 27 | 6 | 6 | 21 |
| Kids | 226 | 96 | 75 | 130 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 19 | 6 | 4 | 13 |
| Netherlands | 21 | 8 | 8 | 13 |
| New Backup | 8 | 6 | 6 | 2 |
| New Channels | 163 | 28 | 25 | 135 |
| Pakistani | 21 | 3 | 3 | 18 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 14 | 0 | 0 | 14 |
| Poland | 34 | 18 | 14 | 16 |
| Portugal | 7 | 3 | 3 | 4 |
| Religious | 36 | 11 | 6 | 25 |
| Romania | 40 | 12 | 12 | 28 |
| Russia | 100 | 16 | 13 | 84 |
| Saudi Arabia | 15 | 3 | 1 | 12 |
| Serbia | 5 | 1 | 0 | 4 |
| Spain | 42 | 4 | 1 | 38 |
| Sports | 262 | 117 | 94 | 145 |
| Sweden | 55 | 0 | 0 | 55 |
| Turkey | 20 | 1 | 0 | 19 |
| Ukraine | 33 | 3 | 0 | 30 |
| United Arab Emirates | 4 | 2 | 0 | 2 |
| United Kingdom | 12 | 2 | 1 | 10 |
| United States | 223 | 43 | 31 | 180 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 5 | 0 | 0 | 5 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **0b18acde8c29cd30467257abef66790d59bbd07417e3e4e86c1426d2a63f96be**
- BDIX-Playlist.m3u SHA-256: **596c7c069bed399dc8e5029090b788b7421ac82a315c5ac55b8caf1b82ff529d**
- International-Playlist.m3u SHA-256: **11eb0263be906c63e29b807bc79c2d767384de46ef2e28f2b9660dbe833358c3**
