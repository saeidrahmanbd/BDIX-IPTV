# EPG Audit — Published Playlists

Generated: **2026-11-04T01:49:16+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1090 | 741 | 488 | 455 | 488 | 439 | 253 | OK |
| International-Playlist.m3u | 2808 | 2387 | 831 | 774 | 819 | 726 | 1556 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 351 | 12 | 12 | 339 |
| Argentina | 18 | 1 | 1 | 17 |
| Aruba | 6 | 0 | 0 | 6 |
| Austria | 4 | 0 | 0 | 4 |
| Bangladesh | 74 | 3 | 2 | 71 |
| Brazil | 12 | 2 | 2 | 10 |
| Bulgaria | 19 | 6 | 5 | 13 |
| Canada | 31 | 23 | 21 | 8 |
| Chile | 24 | 1 | 1 | 23 |
| China | 13 | 3 | 3 | 10 |
| Colombia | 15 | 1 | 1 | 14 |
| Costa Rica | 13 | 0 | 0 | 13 |
| Czech Republic | 26 | 9 | 9 | 17 |
| Documentary & Wildlife | 204 | 135 | 125 | 69 |
| Dominican Republic | 11 | 1 | 0 | 10 |
| Ecuador | 8 | 0 | 0 | 8 |
| Estonia | 6 | 1 | 1 | 5 |
| France | 47 | 10 | 9 | 37 |
| Germany | 31 | 10 | 10 | 21 |
| Greece | 9 | 2 | 2 | 7 |
| Hungary | 18 | 8 | 8 | 10 |
| Indian Bangla | 42 | 33 | 30 | 9 |
| Indian Entertainment | 219 | 181 | 171 | 38 |
| Indian Movies | 82 | 61 | 59 | 21 |
| Indian Music | 73 | 59 | 56 | 14 |
| International | 189 | 59 | 52 | 130 |
| Iran | 18 | 3 | 3 | 15 |
| Italy | 27 | 9 | 9 | 18 |
| Kids | 209 | 93 | 86 | 116 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 17 | 5 | 4 | 12 |
| Netherlands | 21 | 9 | 9 | 12 |
| New Backup | 6 | 4 | 4 | 2 |
| New Channels | 55 | 43 | 41 | 12 |
| Pakistani | 18 | 3 | 3 | 15 |
| Panama | 6 | 0 | 0 | 6 |
| Paraguay | 10 | 0 | 0 | 10 |
| Peru | 13 | 0 | 0 | 13 |
| Poland | 33 | 18 | 18 | 15 |
| Portugal | 5 | 1 | 1 | 4 |
| Religious | 35 | 10 | 9 | 25 |
| Romania | 33 | 10 | 10 | 23 |
| Russia | 83 | 15 | 11 | 68 |
| Saudi Arabia | 10 | 0 | 0 | 10 |
| Serbia | 6 | 1 | 1 | 5 |
| Singapore | 6 | 1 | 1 | 5 |
| Spain | 16 | 3 | 3 | 13 |
| Sports | 252 | 108 | 100 | 144 |
| Sweden | 5 | 0 | 0 | 5 |
| Turkey | 15 | 0 | 0 | 15 |
| Ukraine | 24 | 2 | 2 | 22 |
| United Kingdom | 13 | 2 | 2 | 11 |
| United States | 155 | 45 | 44 | 110 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **f9899be34933deceb7b8eb79fc830c4bfbe7e6d1f902e499f09ddc54c9c0d315**
- International-Playlist.m3u SHA-256: **e1e064ef07f3952a9d9e379779159ced08680810a83be4727fcf572c59b6f5a0**
