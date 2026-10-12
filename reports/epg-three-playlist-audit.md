# EPG Audit — Three Playlists

Generated: **2026-10-12**

Coverage uses exact playlist `tvg-id` matches against the shared mapping registry. Current/future counts use mapping status and do not assert stream health.

| Playlist | Entries | Unique primary IDs | Unique Indian IDs | Mapped | Current/future | Xtream map | EPG header |
|---|---:|---:|---:|---:|---:|---:|---|
| IPTV-Playlist.m3u | 1018 | 624 | 282 | 234/282 (83.0%) | 225/282 (79.8%) | 0/282 | OK |
| BDIX-Playlist.m3u | 139 | 131 | 17 | 16/17 (94.1%) | 16/17 (94.1%) | 0/17 | OK |

## Published XMLTV verification — all active channels

This section measures the guide actually present at report-generation time, not merely upstream source matches.
If the publish gate retains an older guide, the workflow must refresh this report against the retained guide.

| Playlist | Active unique IDs | Mapped IDs | Published IDs with programmes | Current/future IDs |
|---|---:|---:|---:|---:|
| IPTV-Playlist.m3u | 624 | 352 | 322 | 321 |
| IPTV-Playlist.m3u — Bangladesh | 57 | 0 | 0 | 0 |
| BDIX-Playlist.m3u | 131 | 72 | 60 | 60 |
| BDIX-Playlist.m3u — Bangladesh | 41 | 1 | 1 | 1 |

- Non-English programme text fields detected: **0**
- Missing or blank programme titles: **0**
- Active-channel programme overlap rows: **0 across 0 channels**
- Channels with overlaps (top 30): none
- XMLTV read error: **none**
- Latin-script text is not proof of English: untagged transliterations need human/source verification.
- Never invent programme titles or map Bangladesh broadcasters to similarly named Indian channels.

## Channels without mappings

### IPTV-Playlist.m3u

- Indian-group IDs without an exact mapping: **48/282**

`custom.amar.bangla.digital` (Amar Bangla Digital), `BanglaPlus.in` (Bangla Plus), `staging.channel.52` (Channel 52), `custom.jalsha.bangla.bd` (Jalsha Bangla BD), `JhankarTV.ca` (Jhankar TV), `JTVBangla.in@SD` (JTV Bangla), `custom.jtv.classic` (Jtv Classic), `OrangeBanglaTV.in@SD` (Orange Bangla TV), `SanandaTV.in` (Sananda), `custom.snb.cinema` (SNB Cinema), `custom.starbangla` (Star Bangla), `BollywoodFilm.in` (Bollywood Film), `custom.epic.bhojpuri.digital` (Epic Bhojpuri Digital), `Goldmines2.in@SD` (Goldmines 2), `GoldminesAction.in` (Goldmines Action), `new.hindi.movie.classic.24` (Hindi Movie Classic 24), `custom.hindi.movies` (Hindi Movies), `Mango.in@SD` (Mango), `MBCBollywood.ae` (MBC Bollywood), `MHOneMovies.in` (MH One Movies), `custom.ntv.malayalam` (NTV (Malyalam)), `ShubhCinemaTV.in` (Shubh Cinema TV), `custom.sony.max.2` (Sony Max 2 [US]), `custom.south.movies` (South Movies), `custom.7x.punjabi` (7X Punjabi), `ATNMusic.bd` (ATN Music), `DeewanaHD.in` (Deewana), `HindiHits.in` (Hindi Hits), `KalikaTV.in@SD` (Kalika TV), `custom.rang.rangoli` (Rang Rangoli), `custom.zoommusic` (Zoom Music), `CMalayalamTV.ca@SD` (C Malayalam TV), `custom.colors.mena` (Colors MENA), `custom.flowers.us` (Flowers US), `KairaliArabia.in` (Kairali Arabia), `KeralaVision.in@SD` (Kerala Vision), `MeiAlaiTV.in` (Mei Alai TV), `Mh1Prime.in` (MH One Prime), `MarutamTV.in` (MNTV (Tamil)), `NKRTVKannada.in` (NKR TV Kannada), `OliTV.in@SD` (Oli TV), `PulariTV.in@SD` (Pulari TV), `QTV.in` (Q TV), `SADATV.in` (SADA TV), `SooriyanTV.ca@SD` (Sooriyan TV), `Starnet.in@SD` (Starnet), `Swantham.in@SD` (Swantham), `UTVPalakkad.in@SD` (UTV Palakkad)

### BDIX-Playlist.m3u

- Indian-group IDs without an exact mapping: **1/17**

`BanglaPlus.in` (Bangla Plus)
