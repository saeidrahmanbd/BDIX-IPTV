# EPG Audit — Three Playlists

Generated: **2026-10-14**

Coverage uses exact playlist `tvg-id` matches against the shared mapping registry. Current/future counts use mapping status and do not assert stream health.

| Playlist | Entries | Unique primary IDs | Unique Indian IDs | Mapped | Current/future | Xtream map | EPG header |
|---|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 940 | 575 | 273 | 224/273 (82.1%) | 215/273 (78.8%) | 0/273 | OK |
| BDIX-Playlist.m3u | 139 | 131 | 43 | 41/43 (95.3%) | 41/43 (95.3%) | 0/43 | OK |

## Published XMLTV verification — all active channels

This section measures the guide actually present at report-generation time, not merely upstream source matches.
If the publish gate retains an older guide, the workflow must refresh this report against the retained guide.

| Playlist | Active unique IDs | Mapped IDs | Published IDs with programmes | Current/future IDs |
|---|---:|---:|---:|---:|
| IPTV-Playlist.m3u | 575 | 313 | 284 | 284 |
| IPTV-Playlist.m3u — Bangladesh | 54 | 0 | 0 | 0 |
| BDIX-Playlist.m3u | 131 | 71 | 59 | 59 |
| BDIX-Playlist.m3u — Bangladesh | 41 | 0 | 0 | 0 |

- Non-English programme text fields detected: **0**
- Missing or blank programme titles: **0**
- Active-channel programme overlap rows: **0 across 0 channels**
- Channels with overlaps (top 30): none
- XMLTV read error: **none**
- Latin-script text is not proof of English: untagged transliterations need human/source verification.
- Never invent programme titles or map Bangladesh broadcasters to similarly named Indian channels.

## Channels without mappings

### IPTV-Playlist.m3u

- Indian-group IDs without an exact mapping: **49/273**

`custom.amar.bangla.digital` (Amar Bangla Digital), `custom.banglacinema` (Bangla Cinema), `BanglaPlus.in` (Bangla Plus), `staging.channel.52` (Channel 52), `custom.jalsha.bangla.bd` (Jalsha Bangla BD), `JhankarTV.ca` (Jhankar TV), `JTVBangla.in@SD` (JTV Bangla), `custom.jtv.classic` (Jtv Classic), `OrangeBanglaTV.in@SD` (Orange Bangla TV), `SanandaTV.in` (Sananda), `custom.snb.cinema` (SNB Cinema), `custom.starbangla` (Star Bangla), `BollywoodFilm.in` (Bollywood Film), `custom.epic.bhojpuri.digital` (Epic Bhojpuri Digital), `Goldmines2.in@SD` (Goldmines 2), `GoldminesAction.in` (Goldmines Action), `new.hindi.movie.classic.24` (Hindi Movie Classic 24), `custom.hindi.movies` (Hindi Movies), `Mango.in@SD` (Mango), `MBCBollywood.ae` (MBC Bollywood), `MHOneMovies.in` (MH One Movies), `ShubhCinemaTV.in` (Shubh Cinema TV), `custom.sony.max.2` (Sony Max 2 [US]), `custom.south.movies` (South Movies), `custom.7x.punjabi` (7X Punjabi), `DeewanaHD.in` (Deewana), `HindiHits.in` (Hindi Hits), `custom.rang.rangoli` (Rang Rangoli), `custom.zoommusic` (Zoom Music), `custom.baiscope.tv` (Baiscope TV), `CMalayalamTV.ca@SD` (C Malayalam TV), `custom.colors.mena` (Colors MENA), `custom.flowers.us` (Flowers US), `KairaliArabia.in` (Kairali Arabia), `KalikaTV.in@SD` (Kalika TV), `KeralaVision.in@SD` (Kerala Vision), `MeiAlaiTV.in` (Mei Alai TV), `Mh1Prime.in` (MH One Prime), `MarutamTV.in` (MNTV (Tamil)), `NKRTVKannada.in` (NKR TV Kannada), `custom.ntv.malayalam` (NTV (Malyalam)), `OliTV.in@SD` (Oli TV), `PulariTV.in@SD` (Pulari TV), `QTV.in` (Q TV), `SADATV.in` (SADA TV), `SooriyanTV.ca@SD` (Sooriyan TV), `Starnet.in@SD` (Starnet), `Swantham.in@SD` (Swantham), `UTVPalakkad.in@SD` (UTV Palakkad)

### BDIX-Playlist.m3u

- Indian-group IDs without an exact mapping: **2/43**

`BanglaPlus.in` (Bangla Plus), `MBCBollywood.ae` (MBC Bollywood)
