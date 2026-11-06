# EPG Audit — Published Playlists

Generated: **2026-11-06T21:42:01+00:00**

This report measures the two maintained M3U playlists included in the automated EPG pipeline. This report covers only the two maintained playlists.

| Playlist | Stream entries | Active unique IDs | Mapped IDs | Current/future source schedules | IDs in published guide | IDs with published schedules | No mapping | EPG header |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1121 | 671 | 428 | 397 | 428 | 380 | 243 | OK |
| International-Playlist.m3u | 3098 | 2563 | 1031 | 985 | 1020 | 928 | 1532 | OK |

## Group coverage

| Group | Active unique IDs | Mapped IDs | Current/future source schedules | No mapping |
|---|---:|---:|---:|---:|
| Adult | 351 | 11 | 11 | 340 |
| Argentina | 18 | 1 | 1 | 17 |
| Aruba | 6 | 0 | 0 | 6 |
| Austria | 4 | 0 | 0 | 4 |
| Bangladesh | 77 | 5 | 3 | 72 |
| Brazil | 12 | 3 | 3 | 9 |
| Bulgaria | 20 | 6 | 6 | 14 |
| Canada | 34 | 25 | 25 | 9 |
| Chile | 24 | 1 | 1 | 23 |
| China | 13 | 3 | 3 | 10 |
| Colombia | 15 | 1 | 0 | 14 |
| Costa Rica | 13 | 0 | 0 | 13 |
| Czech Republic | 26 | 17 | 17 | 9 |
| Documentary & Wildlife | 202 | 148 | 140 | 54 |
| Dominican Republic | 11 | 1 | 0 | 10 |
| Ecuador | 8 | 0 | 0 | 8 |
| Estonia | 6 | 1 | 1 | 5 |
| France | 48 | 17 | 16 | 31 |
| Germany | 40 | 29 | 29 | 11 |
| Greece | 9 | 2 | 2 | 7 |
| Hungary | 18 | 8 | 8 | 10 |
| Indian Bangla | 41 | 33 | 30 | 8 |
| Indian Entertainment | 219 | 183 | 174 | 36 |
| Indian Movies | 83 | 62 | 59 | 21 |
| Indian Music | 73 | 59 | 56 | 14 |
| International | 200 | 61 | 56 | 139 |
| Iran | 18 | 3 | 3 | 15 |
| Italy | 32 | 13 | 13 | 19 |
| Kids | 204 | 106 | 100 | 98 |
| Lebanon | 6 | 1 | 1 | 5 |
| Mexico | 17 | 7 | 6 | 10 |
| Netherlands | 21 | 9 | 9 | 12 |
| New Backups | 9 | 8 | 8 | 1 |
| New Channels | 117 | 22 | 20 | 95 |
| Pakistani | 17 | 2 | 2 | 15 |
| Panama | 6 | 0 | 0 | 6 |
| Paraguay | 10 | 0 | 0 | 10 |
| Peru | 13 | 0 | 0 | 13 |
| Poland | 33 | 18 | 18 | 15 |
| Portugal | 5 | 1 | 1 | 4 |
| Religious | 35 | 10 | 9 | 25 |
| Romania | 33 | 10 | 10 | 23 |
| Russia | 86 | 35 | 32 | 51 |
| Saudi Arabia | 10 | 0 | 0 | 10 |
| Serbia | 6 | 1 | 1 | 5 |
| Singapore | 6 | 1 | 1 | 5 |
| Spain | 17 | 4 | 4 | 13 |
| Sports | 254 | 123 | 120 | 131 |
| Sweden | 12 | 6 | 6 | 6 |
| Turkey | 15 | 0 | 0 | 15 |
| Ukraine | 28 | 9 | 9 | 19 |
| United Kingdom | 14 | 3 | 3 | 11 |
| United States | 180 | 90 | 89 | 90 |
| Uzbekistan | 5 | 0 | 0 | 5 |
| Vietnam | 6 | 0 | 0 | 6 |

## Interpretation

- Mapped IDs means a playlist identity was connected to a source XMLTV ID.
- Current/future source schedules means source data contains eligible programmes with valid non-empty titles in any language inside the generator's -6-hour/+7-day window; overlapping title variants are selected English first, Bengali second, then other valid languages.
- IDs in published guide and IDs with published schedules are verified against XMLTV using the playlist's tvg-id identities; these counts are not source-provider IDs.
- Domestic Bangladesh channels are not fuzzy-matched to similarly named Indian or foreign services. They remain unmapped until a trustworthy listing source or an exact explicit mapping can be verified.


## Source Playlist Fingerprints

- IPTV-Playlist.m3u SHA-256: **92a045f671165942d728082edaac08bdaa83c0320afde042d00ed9b6ea1da67a**
- International-Playlist.m3u SHA-256: **aae6f5ef820c5a79ff1c0b8851f20d920017bd234c0f33ac9762a9d69fe2bd6c**
