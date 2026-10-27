# EPG Audit — Published Playlists

Generated: **2026-10-27T15:35:13+00:00**

This report measures the three maintained M3U playlists included in the automated EPG pipeline. The historic filename epg-three-playlist-audit.md is retained for link compatibility.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1169 | 701 | 472 | 450 | 472 | 431 | 229 | OK |
| BDIX-Playlist.m3u | 131 | 131 | 75 | 73 | 75 | 71 | 56 | OK |
| International-Playlist.m3u | 3167 | 2622 | 868 | 826 | 855 | 773 | 1754 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 359 | 13 | 11 | 346 |
| Argentina | 17 | 1 | 1 | 16 |
| Aruba | 6 | 0 | 0 | 6 |
| Bangladesh | 87 | 1 | 0 | 86 |
| Brazil | 12 | 2 | 2 | 10 |
| Bulgaria | 15 | 7 | 6 | 8 |
| Canada | 26 | 20 | 20 | 6 |
| Chile | 27 | 1 | 1 | 26 |
| China | 13 | 0 | 0 | 13 |
| Colombia | 13 | 1 | 0 | 12 |
| Czech Republic | 26 | 9 | 9 | 17 |
| Documentary & Wildlife | 217 | 136 | 131 | 81 |
| Dominican Republic | 7 | 0 | 0 | 7 |
| Egypt | 5 | 2 | 2 | 3 |
| Estonia | 6 | 1 | 1 | 5 |
| France | 45 | 9 | 9 | 36 |
| Germany | 72 | 11 | 11 | 61 |
| Greece | 9 | 2 | 2 | 7 |
| Hungary | 16 | 8 | 8 | 8 |
| Indian Bangla | 50 | 40 | 36 | 10 |
| Indian Entertainment | 227 | 190 | 180 | 37 |
| Indian Movies | 93 | 70 | 69 | 23 |
| Indian Music | 72 | 59 | 56 | 13 |
| International | 98 | 56 | 53 | 42 |
| Iran | 15 | 3 | 3 | 12 |
| Italy | 26 | 6 | 6 | 20 |
| Kids | 226 | 96 | 90 | 130 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 19 | 6 | 5 | 13 |
| Netherlands | 21 | 8 | 8 | 13 |
| New Backup | 15 | 14 | 14 | 1 |
| New Channels | 173 | 28 | 28 | 145 |
| Pakistani | 21 | 3 | 3 | 18 |
| Paraguay | 6 | 0 | 0 | 6 |
| Peru | 14 | 0 | 0 | 14 |
| Poland | 33 | 17 | 17 | 16 |
| Portugal | 6 | 2 | 2 | 4 |
| Religious | 37 | 11 | 10 | 26 |
| Romania | 40 | 12 | 12 | 28 |
| Russia | 84 | 15 | 12 | 69 |
| Saudi Arabia | 15 | 3 | 3 | 12 |
| Serbia | 5 | 1 | 1 | 4 |
| Spain | 17 | 4 | 4 | 13 |
| Sports | 258 | 113 | 108 | 145 |
| Sweden | 40 | 0 | 0 | 40 |
| Turkey | 20 | 1 | 0 | 19 |
| Ukraine | 29 | 3 | 3 | 26 |
| United Arab Emirates | 4 | 2 | 2 | 2 |
| United Kingdom | 12 | 2 | 2 | 10 |
| United States | 199 | 41 | 40 | 158 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 5 | 0 | 0 | 5 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **faee9d0d61b69ea2136a0baffe887415e579273713dc58d4fcc1e62184161c1d**
- BDIX-Playlist.m3u SHA-256: **596c7c069bed399dc8e5029090b788b7421ac82a315c5ac55b8caf1b82ff529d**
- International-Playlist.m3u SHA-256: **612b81a96e063fd29be693cde5d32c4bbcd463ba05db94c81591140f2377041c**
