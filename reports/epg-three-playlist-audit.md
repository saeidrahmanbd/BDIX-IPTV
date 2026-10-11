# EPG Audit — Three Playlists

Generated: **2026-10-11**

This report compares the three published M3U files with the current EPG mapping registry (`reports/epg-india-channel-mapping.csv`) and Xtream worker map (`xtream/worker.js`). Coverage counts are based on exact `tvg-id` matches. It does not claim a stream is working, or that a mapped channel currently has listings, unless the existing mapping registry marks it `MAPPED`.

## Summary

| Playlist | Entries | Primary entries | Backup entries | Unique Indian IDs | Exact IDs mapped | Marked current/future | EPG header |
|---|---:|---:|---:|---:|---:|---|---|
### BDIX-Playlist.m3u
- Entries: **190**; primary: **190**; Backup: **0**.
- Missing `tvg-id`: **0**; missing `channel-id`: **0**; primary entries missing `tvg-chno`: **0**.
- Indian-group IDs: **17**; exact IDs with a non-empty EPG mapping: **11/17 (64.7%)**; mapping status `MAPPED` (current/future) **11/17**; present in Xtream worker map: **11/17**.
- Playlist EPG header: **OK** — `https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml`.
- Indian IDs without an exact mapping in the main registry: `custom.bdix.aakashaath` (AAKASH AATH), `custom.bdix.abpananda` (ABP ANANDA), `custom.bdix.banglajago` (BANGLA JAGO), `BanglaPlus.in` (Bangla Plus), `Enterr10 Bangla.in` (ENTER 10 BANGLA), `custom.bdix.9bangla` (TV 9 BANGLA).

### IPTV-Playlist.m3u
- Entries: **1145**; primary: **652**; Backup: **493**.
- Missing `tvg-id`: **0**; missing `channel-id`: **0**; primary entries missing `tvg-chno`: **0**.
- Indian-group IDs: **299**; exact IDs with a non-empty EPG mapping: **243/299 (81.3%)**; mapping status `MAPPED` (current/future) **233/299**; present in Xtream worker map: **243/299**.
- Playlist EPG header: **OK** — `https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml`.
- Indian IDs without an exact mapping in the main registry: `custom.amar.bangla.digital` (Amar Bangla Digital), `BanglaPlus.in` (Bangla Plus), `staging.channel.52` (Channel 52), `JhankarTV.ca` (Jhankar TV), `JTVBangla.in@SD` (JTV Bangla), `custom.jtv.classic` (Jtv Classic), `OrangeBanglaTV.in@SD` (Orange Bangla TV), `SanandaTV.in` (Sananda), `custom.snb.cinema` (SNB Cinema), `custom.starbangla` (Star Bangla), `new.and.pictures.hd` (&pictures 2), `B4UBhojpuri.in@Plus` (B4U Bhojpuri Plus), `BollywoodFilm.in` (Bollywood Film), `custom.colors.cineplex` (Colors Cineplex [UK]), `custom.epic.bhojpuri.digital` (Epic Bhojpuri Digital), `Goldmines2.in@SD` (Goldmines 2), `GoldminesAction.in` (Goldmines Action), `new.hindi.movie.classic.24` (Hindi Movie Classic 24), `custom.hindi.movies` (Hindi Movies), `Mango.in@SD` (Mango), `MBCBollywood.ae` (MBC Bollywood), `MHOneMovies.in` (MH One Movies), `NHTamilGold.in` (NH Tamil Gold), `custom.ntv.malayalam` (NTV (Malyalam)), `ShubhCinemaTV.in` (Shubh Cinema TV), `custom.sony.max.2` (Sony Max 2 [US]), `custom.south.movies` (South Movies), `SouthStation.in` (South Station), `TheMovieClub.in@HD` (The Movie Club), `TheMovieClub.in@Plus2` (The Movie Club +2), `custom.7x.punjabi` (7X Punjabi), `ATNMusic.bd` (ATN Music), `DeewanaHD.in` (Deewana), `HindiHits.in` (Hindi Hits), `KalikaTV.in@SD` (Kalika TV), `custom.rang.rangoli` (Rang Rangoli), `custom.zoommusic` (Zoom Music), `CMalayalamTV.ca@SD` (C Malayalam TV), `custom.colors.mena` (Colors MENA), `custom.flowers.us` (Flowers US), `KairaliArabia.in` (Kairali Arabia), `KeralaVision.in@SD` (Kerala Vision), `MeiAlaiTV.in` (Mei Alai TV), `Mh1Prime.in` (MH One Prime), `MarutamTV.in` (MNTV (Tamil)), `NKRTVKannada.in` (NKR TV Kannada), `OliTV.in@SD` (Oli TV), `PulariTV.in@SD` (Pulari TV), `QTV.in` (Q TV), `SADATV.in` (SADA TV), `SonyKALHindi.us` (Sony KAL), `SooriyanTV.ca@SD` (Sooriyan TV), `Starnet.in@SD` (Starnet), `Swantham.in@SD` (Swantham), `UTVPalakkad.in@SD` (UTV Palakkad), `VCV.in@SD` (VCV).

### NVisionBD-Playlist.m3u
- Entries: **561**; primary: **471**; Backup: **90**.
- Missing `tvg-id`: **0**; missing `channel-id`: **0**; primary entries missing `tvg-chno`: **0**.
- Indian-group IDs: **106**; exact IDs with a non-empty EPG mapping: **63/106 (59.4%)**; mapping status `MAPPED` (current/future) **62/106**; present in Xtream worker map: **63/106**.
- Playlist EPG header: **OK** — `https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml`.
- Indian IDs without an exact mapping in the main registry: `custom.abp.ananda` (ABP Ananda), `custom.bangla.big.boss.24x7` (Bangla Big Boss 24x7), `BanglaPlus.in` (Bangla Plus HD), `custom.ctvn.akd.plus` (CTVN AKD Plus), `custom.ktv.bangla` (Ktv Bangla), `custom.news.18.bangla` (News 18 Bangla), `custom.nick.bangla` (Nick Bangla), `custom.r.plus` (R Plus), `RepublicBangla.in` (Republic Bangla), `custom.sananda.tv` (Sananda TV), `SunBangla.in@SD` (Sun Bangla HD), `custom.zb.cinema` (ZB Cinema), `custom.afra.film` (Afra Film), `custom.anmol.cinema` (Anmol Cinema), `custom.anmol.cinema.2` (Anmol Cinema 2), `custom.biz.cinema` (Biz Cinema), `custom.bollywood.classic` (Bollywood Classic HD), `custom.cafe.film` (Cafe Film), `custom.filmax` (Filmax), `new.hindi.movie.classic.24` (Hindi Movie Classic 24), `MBCBollywood.ae` (MBC Bollywood HD), `custom.sine.plus` (Sine Plus), `StarGold2.in@HD` (Star Gold 2), `Star Gold Romance.in` (Star Gold Romance), `custom.the.q.india` (The Q India), `ZeeAnmolCinema.in` (Zee Anmol Cinema), `custom.afro.music.channel` (Afro Music Channel), `custom.euro.indie.music.chart.tv` (Euro Indie Music Chart TV), `custom.isai.aruvi.tv` (Isai Aruvi TV), `custom.zoommusic` (Zoom Music), `custom.10.tv` (10 TV), `custom.aaj.tak` (Aaj Tak HD), `custom.amar.ujala` (Amar Ujala), `custom.epic` (Epic), `custom.global.panjab` (Global Panjab), `custom.good.news.today` (Good News Today), `custom.hindi.big.boss.24x7.2026` (Hindi Big Boss 24x7 2026), `custom.hindi.khabar` (Hindi Khabar), `custom.india.today` (India Today), `custom.ndtv` (NDTV), `custom.news.18.assam` (News 18 Assam), `SETASHD` (Sony TV HD), `custom.the.q` (The Q).

## Cross-playlist mapping notes

- The current mapping registry is generated from `IPTV-Playlist.m3u` only. A matching channel in BDIX or NVisionBD is counted as mapped only when its `tvg-id` exactly matches the registry; visually similar names are not auto-merged.
- BDIX has 6 Indian Bangla IDs with no exact registry mapping: `custom.bdix.aakashaath`, `custom.bdix.abpananda`, `custom.bdix.banglajago`, `BanglaPlus.in`, `Enterr10 Bangla.in`, and `custom.bdix.9bangla`. Some are identity aliases that likely need review; no schedule was assigned without validating the provider/channel identity.
- NVisionBD has 43 Indian-group IDs without an exact mapping in the main registry, including `custom.abp.ananda`, `custom.isai.aruvi.tv`, `custom.zb.cinema`, `custom.afra.film`, `custom.anmol.cinema`, and `custom.the.q.india`. Backups retain their separate stream URL and do not count toward primary EPG mapping coverage.
- The last source coverage report recorded **243/299 mapped Indian channels** and **233/299 (77.9%)** with current/future programming. Its generated timestamp is **2026-10-11T12:49:31Z**, before the `IPTV-Playlist.m3u` EPG header repair, so that report's previous `MISMATCH` flag is stale. The exact current published XMLTV file is large (22.9 MB) and could not be parsed through the repository file reader in this audit; an automated workflow should regenerate its published-guide validation after these commits.

## Highest-priority actions

1. Preserve exact `tvg-id` identities; add a reviewed alias registry for alternate IDs in BDIX and NVisionBD so one verified provider schedule can be rendered for more than one playlist identity without reverse-map collisions.
2. Add per-playlist EPG coverage validation to the workflow instead of validating only the main IPTV playlist.
3. Add an approved source policy / programme-data rights review before widening feeds or publishing additional source-derived listings.
4. Re-run the EPG coverage/generation workflow and verify channel IDs plus current/future programmes in the published XMLTV before calling mapping improvements complete.
