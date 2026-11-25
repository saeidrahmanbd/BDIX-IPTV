# IPTV Playlist Audit
Generated: **2026-11-25T00:19:59.374877+00:00**
Source playlist SHA-256: **a2ef9bb3e7d03dbfffd4f78e796027e4f5e46374fe9717d89785190c04f23e6a**

Non-destructive audit of channel identity, metadata consistency, duplicate identities, and logo integrity.
Scope note: Metadata conflicts and same-name/different-ID counts below cover canonical primary entries; cross-queue variants are shown separately as review diagnostics.

## Summary

- Playlist entries: **1354**
- Unique channel IDs: **814**
- IDs with multiple streams: **265**
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **0**
- Cross-queue same-ID name variants (review): **0**
- Cross-queue normalized-name/different-ID groups (review): **17**
- Cross-country backup collisions: **0**
- IDs with multiple logo references: **6**
- Protected primary-entry changes: **0**
- Logo exceptions requiring repair: **0**
- Missing logos in review queues (review only): **0**
- External logo references (review only): **0**
- Logo references checked: **1354**
- Duplicate primary identities: **4**
- Potential near-duplicate primary name groups (review only): **0**
- Primary channel-number collisions: **1**
- Primary channel-number sequence issues (review only): **1**
- Primary entries missing channel numbers: **9**
- Primary entries missing tvg-country: **0**
- Primary entries missing tvg-language: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Category registry issues: **0**
- Alphabetical ordering issues: **5**
- Suspicious URL credentials/syntax: **0**
- Unverified provider playback routes (review only): **0**
- Signed/tokenized stream URLs: **14**
- Embedded Xtream-style credential paths (redacted): **3**


## Primary Metadata Completeness

Missing country/language values are informational, not a reason to delete, reclassify, or block otherwise valid channel entries. Only trusted exact-ID source metadata should be used to fill these fields.
- Active primary entries missing tvg-country: **0**
- Active primary entries missing tvg-language: **0**

| Group | Missing tvg-country | Missing tvg-language |
|---|---:|---:|

## Review Queue Country Verification

New Channels/New Backups contain only entries verified as BD/IN.

## Category Registry

Canonical registry matches the permanent IPTV category order.

## Cross-Queue Identity Variants

These diagnostics include canonical and review groups. Name/ID differences can be legitimate; this section does not merge identities, remove entries, or print stream URLs.

No same-ID label variants found across groups.

- Same normalized name: Apna Punjab TV [apnapunjabtv.ca@sd] (Indian Entertainment); Apna Punjab TV [apnapunjabtv.in@sd] (Indian Entertainment)
- Same normalized name: Colors [colors.in] (Review); Colors [colors.in@hd] (Indian Entertainment); Colors [colors.in@hd] (Review)
- Same normalized name: Colors Bangla [colors.bangla.in] (Review); Colors Bangla [colorsbangla.in@hd] (Review)
- Same normalized name: Duronto TV [durontotv.bd] (Kids); Duronto TV [durontotv.bd] (Review); Duronto TV (720p) [durontotv.bd@sd] (New Backups)
- Same normalized name: ETV Cinema [etvcinema.in] (Indian Movies); ETV Cinema [etvcinema.in] (Review); ETV Cinema [etvcinema.in@hd] (Indian Movies)
- Same normalized name: ETV Comedy [etvcomedy.in] (Indian Entertainment); ETV Comedy [etvcomedy.in@hd] (Indian Entertainment)
- Same normalized name: ETV Music [etvmusic.in] (Indian Music); ETV Music [etvmusic.in@sd] (Indian Music)
- Same normalized name: Eurosport [eurosport.fr@asia] (Review); Eurosport [eurosport.in@hd] (Review); Eurosport [eurosport.in@sd] (Review)
- Same normalized name: InWild [inwild.nl] (Documentary & Wildlife); INWILD (1080p) [inwild.nl@sd] (New Backups)
- Same normalized name: Jalsha Movies [jalshamovies.in@sd] (Indian Bangla); Jalsha Movies [star.jalsha.movies.in] (Review)
- Same normalized name: MTV India [mtv.in@hd] (Review); MTV (India) [mtv.in@sd] (Review); MTV India [mtv.in@sd] (Indian Music); MTV India [mtv.in@sd] (Review)
- Same normalized name: Peace TV Bangla [peacetvbangla.ae] (Backup); Peace TV Bangla [peacetvbangla.ae] (Religious); Peace TV Bangla [peacetvbangla.ae@sd] (Review)
- Same normalized name: &pictures HD [andpictures.in@hd] (Review); &pictures HD [andpictures.in@sd] (Review)
- Same normalized name: Star Movies (India) HD [starmovies.in] (Review); Star Movies (India) HD [starmovies.in@hd] (Review)
- Same normalized name: Star Sports 2 [starsports2.in] (Sports); Star Sports 2 [starsports2.in@hd] (Review)
- Same normalized name: Travelxp 4K HDR [travelxp.in@4khdr] (Review); Travelxp 4K HDR [travelxp.in@hd] (Review)
- Same normalized name: &TV [andtv.in@hd] (Review); &TV [andtv.in@sd] (Indian Entertainment); &TV [andtv.in@sd] (Review)

## Duplicate IDs

### 7smusic.in@sd (3 streams)
- 7S Music — Indian Music — https://cdn.pishow.tv/ott/live/1257/master.m3u8
- 7S Music — Backup — https://fta.ektv.in/live/771/master.m3u8
- 7S Music — Backup — https://mumt03.tangotv.in/Dsly5z3H7SMUSIC/index.m3u8
### 7xpunjabi.in (2 streams)
- 7X Punjabi — Indian Music — https://cdn2.in/7xPunjabihls/live.m3u8
- 7X Punjabi — Backup — https://7xshreeshyam.akamaized.net/7XPunjabi/index.m3u8
### 8xm.pk@sd (2 streams)
- 8XM — Pakistani — https://vodzong.mjunoon.tv:8087/streamtest/8XM-131/playlist.m3u8
- 8XM — Review — https://cdn4.mjunoon.tv:8087/streamtest/131M/chunks.m3u8
### 9xjalwa.in (5 streams)
- 9X Jalwa — Indian Music — https://wiselp.wiseplayout.com/9X_Jalwa/master.m3u8
- 9X Jalwa — Backup — https://d3kdywbtdfbp9z.cloudfront.net/v1/manifest/93ce20f0f52760bf38be911ff4c91ed02aa2fd92/dff423e0-3c82-46d6-9ecb-3baa96b5694a/70fca4d1-156e-4c03-baa4-9a4b602e33d5/0.m3u8
- 9X Jalwa — Backup — https://fta.ektv.in/live/161/master.m3u8
- 9X Jalwa — Backup — https://mumt03.tangotv.in/Dsly5z3H9XJALWA/index.m3u8
- 9X Jalwa — Backup — https://tvsen6.aynaott.com/CiPT1VTG8bVekeAZiibd/index.m3u8
### 9xjhakaas.in@sd (3 streams)
- 9X Jhakaas — Indian Music — https://wiselp.wiseplayout.com/9X_Jhakaas/master.m3u8
- 9X Jhakaas — Review — https://amg01281-9xmediapvtltd-9xjhakaas-samsungin-ci2cs.amagi.tv/playlist/amg01281-9xmediapvtltd-9xjhakaas-samsungin/playlist.m3u8
- 9X Jhakaas — Review — https://cdn.pishow.tv/ott/live/6/master.m3u8
### 9xm.in@sd (6 streams)
- 9XM — Indian Music — https://cc-706183qeo55ez.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-706183qeo55ez/DIYC/PMSL/9X/9XMusic_IN/9XMusic_IN.m3u8
- 9XM — Backup — https://fta.ektv.in/live/155/master.m3u8
- 9XM — Backup — https://streams.tangotv.in/9XM/ORIGIN/index.m3u8
- 9XM — Backup — https://wiselp.wiseplayout.com/9XM/HD1080/HD1080.m3u8
- 9XM — Backup — https://wiselp.wiseplayout.com/9XM/master.m3u8
- 9XM — Review — https://9xjio.wiseplayout.com/9XM/master.m3u8
### 9xtashan.in@sd (6 streams)
- 9X Tashan — Indian Music — https://wiselp.wiseplayout.com/9X_Tashan/master.m3u8
- 9X Tashan — Backup — https://fta.ektv.in/live/178/master.m3u8
- 9X Tashan — Backup — https://mumt01.tangotv.in/O5aw8Zn39XTASHAN/index.m3u8
- 9X Tashan — Backup — https://streams.tangotv.in/9XTASHAN/ORIGIN/index.m3u8
- 9X Tashan — Review — https://amg01281-9xmediapvtltd-9xtashan-samsungin-xz1sd.amagi.tv/playlist/amg01281-9xmediapvtltd-9xtashan-samsungin/playlist.m3u8
- 9X Tashan — Review — https://cdn.pishow.tv/ott/live/1613/master.m3u8
### aakaashaath.in@sd (4 streams)
- Aakaash Aath — Indian Bangla — https://tvsen5.aynaott.com/Wm9Lv2RjZGT6/index.m3u8
- Aakaash Aath — Backup — https://cdn.pishow.tv/ott/live/969/master.m3u8
- Aakaash Aath — Backup — https://mumt03.tangotv.in/Dsly5z3HAAKASHAATH/index.m3u8
- Aakaash Aath — Review — http://tvsen5.aynascope.net/Wm9Lv2RjZGT6/index.m3u8
### aamarbangla.in (3 streams)
- Amar Bangla — Indian Bangla — http://115.187.41.216:8080/hls/amarbangla/index.m3u8
- Amar Bangla — Review — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI/amarbanglatv.stream/playlist.m3u8
- Amar Bangla — Review — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFseWRtaW51ajPhnPTI/amarbanglatv.stream/playlist.m3u8
### alltimemovies.in@sd (3 streams)
- All Time Movies — Indian Movies — https://samitaorigin.tangotv.in/ALLTIMEMOVIES/SAMITAORIGIN/index.m3u8
- All Time Movies — Backup — https://fta.ektv.in/live/54/54_0.m3u8
- All Time Movies — Review — https://tvsen6.aynaott.com/a2cKGQtB/index.m3u8
### alquranalkareemtv.sa (2 streams)
- Al Quran Al Kareem TV — Religious — https://cdn-globecast.akamaized.net/live/eds/saudi_quran/hls_roku/index.m3u8
- Al Quran Al Kareem TV — Backup — http://m.live.net.sa:1935/live/quran/playlist.m3u8
### amarbangladigital.in (3 streams)
- Amar Bangla Digital — Indian Bangla — http://115.187.41.216:8080/hls/amardigital/index.m3u8
- Amar Bangla Digital — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/amardigital.stream/playlist.m3u8
- Amar Bangla Digital — Review — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI/amarbanglatv.stream/live-orgin/amarbanglatv.stream/chunks.m3u8
### amritatv.in@sd (3 streams)
- Amrita TV — Indian Entertainment — https://ddash74r36xqp.cloudfront.net/master.m3u8
- Amrita TV — Backup — https://ddash74r36xqp.cloudfront.net/master_2000.m3u8
- Amrita TV — Backup — https://mumt07.tangotv.in/zHjX9OFlAMRITATV/index.m3u8
### anandatv.bd (6 streams)
- Ananda TV — Bangladesh — https://tvsen6.aynaott.com/LeUAm4F1iixYns3s3Non/index.m3u8
- Ananda TV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/anandatv.stream/index.m3u8
- Ananda TV — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/anandatv.stream/live-orgin/anandatv.stream/playlist.m3u8
- Ananda TV — Backup — https://playztv-apps.pages.dev/ananda-tv/index.m3u8
- Ananda TV — Backup — http://live-stream.amarbanglatv.in:8080/hls/sanandatv/index.m3u8
- Ananda TV — Review — http://103.135.253.32:8080/Anando-TV/index.m3u8
### andtv.in@sd (2 streams)
- &TV — Indian Entertainment — https://3f56f997.wurl.com/master/f36d25e7e52f1ba8d7e56eb859c636563214f541/U2Ftc3VuZy1nYl9BbmRUVl9ITFM/playlist.m3u8
- &TV — Review — https://drk6xq0vhn.gpcdn.net/live/and_tv_hd_abr/index.m3u8
### animalplanet.in@sd (4 streams)
- Animal Planet — Documentary & Wildlife — https://tvsen3.aynaott.com/wpa56Uk3/index.m3u8
- Animal Planet — Backup — https://vodzong.mjunoon.tv:8087/streamtest/Animal-Planet-158-3/playlist.m3u8
- Animal Planet — Backup — http://27.124.71.27/Animal_Planet/index.m3u8
- Animal Planet — Review — https://drk6xq0vhn.gpcdn.net/live/animal_planet_hd/index.m3u8
### anjantv.in@sd (3 streams)
- Anjan TV — Indian Entertainment — https://cdn.pishow.tv/ott/live/993/master.m3u8
- Anjan TV — Backup — https://anjan.vstream.online/anjanorg/ngrp:anjan_hdall/playlist.m3u8
- Anjan TV — Backup — https://mumt06.tangotv.in/qYyB8fXVANJANTV/index.m3u8
### asianet.in (2 streams)
- Asianet — Indian Entertainment — https://da86m1sqpm3o0.cloudfront.net/28072023/smil:starasianet.smil/chunklist_b1928000.m3u8
- Asianet — Backup — https://listas-m3u8.github.io/iptv/128.19.173.10:8888/ASIANETHD.m3u8
### asianetmiddleeast.in@sd (2 streams)
- Asianet Middle East — Indian Entertainment — https://mumt03.tangotv.in/Dsly5z3HASIANETMIDDLEEAST/index.m3u8
- Asianet Middle East — Backup — https://fta.ektv.in/live/697/master.m3u8
### asiantv.bd (2 streams)
- Asian TV — Bangladesh — https://tvsen6.aynaott.com/pKb5k6NnzxsKpWUs6E8M/tracks-v1a1/mono.ts.m3u8
- Asian TV — Review — https://stream.ottplus.live/live/asian_tv_abr/index.m3u8
### asports.pk (2 streams)
- A Sports — Sports — https://playztv-apps.pages.dev/a-sports/index.m3u8
- A Sports — Backup — https://tvsen6.aynaott.com/zv68oqPDu7MZZwmHhRxt/index.m3u8
### atnbangla.bd (5 streams)
- ATN Bangla — Bangladesh — https://tvsen5.aynaott.com/atnbangla/index.m3u8
- ATN Bangla — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/atnbd-8-org.stream/tracks-v1a1/mono.m3u8
- ATN Bangla — Backup — https://iptvlive.ahmed-bd-org.workers.dev/atn-bangla-1/index.m3u8
- ATN Bangla — Backup — https://tvsen5.aynaott.com/P3y2URgG7LDe/index.m3u8
- ATN Bangla — Review — http://tvsen5.aynascope.net/atnbangla/index.m3u8
### atnbanglauk.uk (3 streams)
- ATN Bangla UK — Bangladesh — https://app.ncare.live/live-orgin/atnbanglauk-off.stream/playlist.m3u8
- ATN Bangla UK — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/atnbanglauk-off.stream/playlist.m3u8
- ATN Bangla UK — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/atnbanglauk-off.stream/playlist.m3u8
### atnnews.bd (3 streams)
- ATN News — Bangladesh — https://tvsen6.aynaott.com/da6WMXAk/index.m3u8
- ATN News — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/atnws-sg.stream/tracks-v1a1/mono.m3u8
- ATN News — Backup — https://iptv-proxy.ahmed-bd-org.workers.dev/atn-news/index.m3u8
### b4ubhojpuri.in@sd (2 streams)
- B4U Bhojpuri — Indian Movies — https://mumt05.tangotv.in/87NeALx2B4UBHOJPURI/index.m3u8
- B4U Bhojpuri — Review — https://cdnb4u.wiseplayout.com/B4U_Bhojpuri/master.m3u8
### b4ukadak.in@sd (7 streams)
- B4U Kadak — Indian Movies — https://cdn.pishow.tv/ott/live/227/master.m3u8
- B4U Kadak — Backup — http://163.61.226.31:9981/stream/channelid/282021969?profile=pass
- B4U Kadak — Backup — https://fta.ektv.in/live/44/44_0.m3u8
- B4U Kadak — Backup — https://mumt06.tangotv.in/qYyB8fXVB4UKADAK/index.m3u8
- B4U Kadak — Backup — https://streams.tangotv.in/B4UKADAK/ORIGIN/index.m3u8
- B4U Kadak — Review — https://tvsen3.aynaott.com/X9E6bxg3/index.m3u8
- B4U Kadak — Review — https://amg00877-b4unew-amg00877c4-xiaomi-in-5473.playouts.now.amagi.tv/playlist.m3u8
### b4umovies.in@india (8 streams)
- B4U Movies — Indian Movies — https://cdn.pishow.tv/ott/live/419/master.m3u8
- B4U Movies — Backup — http://163.61.226.31:9981/stream/channelid/1547127176?profile=pass
- B4U Movies — Backup — https://fta.ektv.in/live/43/43_0.m3u8
- B4U Movies — Backup — https://mumt06.tangotv.in/qYyB8fXVB4UMOVIES/index.m3u8
- B4U Movies — Backup — https://streams.tangotv.in/B4UMOVIES/ORIGIN/index.m3u8
- B4U Movies — Review — http://103.135.253.32:8080/B4U-MOVIES/index.m3u8
- B4U Movies — Review — https://drk6xq0vhn.gpcdn.net/live/b4u_movies_abr/index.m3u8
- B4U Movies — Review — https://amg00877-b4unew-amg00877c2-xiaomi-in-5489.playouts.now.amagi.tv/playlist.m3u8
### b4umusic.in@india (10 streams)
- B4U Music — Indian Music — https://streams.tangotv.in/B4UMUSIC/ORIGIN/index.m3u8
- B4U Music (1080p) — New Backups — https://amg00877-b4unew-amg00877c3-xiaomi-in-5474.playouts.now.amagi.tv/playlist.m3u8
- B4U Music — Backup — http://103.175.73.12:8080/live/157/master.m3u8
- B4U Music — Backup — http://163.61.226.31:9981/stream/channelid/494430938?profile=pass
- B4U Music — Backup — https://amg01408-amg01408c5-amgplt0747.playout.now3.amagi.tv/b4um001/playlist.m3u8
- B4U Music — Backup — https://cdn.pishow.tv/ott/live/415/master.m3u8
- B4U Music — Backup — https://fta.ektv.in/live/157/master.m3u8
- B4U Music — Review — https://drk6xq0vhn.gpcdn.net/live/b4u_music_abr/index.m3u8
- B4U Music — Review — https://mumt04.tangotv.in/m18aqlK4B4UMUSIC/index.m3u8
- B4U Music — Review — https://amg00877-b4unew-amg00877c3-xiaomi-in-5474.playouts.now.amagi.tv/720p/index.m3u8
### bahrainsports2.bh@sd (2 streams)
- Bahrain Sports 2 — Sports — https://5c7b683162943.streamlock.net/live/ngrp:bahrainsportstwo_all/playlist.m3u8
- Bahrain Sports 2 — Backup — https://tvsen6.aynaott.com/BahrainSports2/index.m3u8
### balleballe.in@sd (6 streams)
- Balle Balle — Indian Music — https://mcncdndigital.com/balleballetv/index.m3u8
- Balle Balle — Backup — https://cdn.pishow.tv/ott/live/987/master.m3u8
- Balle Balle — Backup — https://fta.ektv.in/live/365/master.m3u8
- Balle Balle — Backup — https://mcncdndigital.com/worldpunjabitv/index.m3u8
- Balle Balle — Backup — https://mumt04.tangotv.in/m18aqlK4BALLEBALLE/index.m3u8
- Balle Balle — Backup — https://streams.tangotv.in/BALLEBALLE/ORIGIN/index.m3u8
### banglatv.bd (5 streams)
- Bangla TV — Bangladesh — https://tvsen6.aynaott.com/39ee93nUbCCmm5LsyD4t/index.m3u8
- Bangla TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/bangla-tv-2/index.m3u8
- Bangla TV — Review — http://116.204.149.16/banglatv/index.m3u8
- Bangla TV — Review — http://116.204.149.16/banglatv/tracks-v1a1/mono.m3u8
- Bangla TV — Review — https://cdn.ghuddi.live/tvapp/Bangla_TV_BD_New/playlist.m3u8
### banglavision.bd (4 streams)
- Bangla Vision — Bangladesh — https://tvsen5.aynaott.com/banglavision/index.m3u8
- Bangla Vision — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/banglav000.stream/tracks-v1a1/mono.m3u8
- Bangla Vision — Backup — https://iptvlive.ahmed-bd-org.workers.dev/banglavision-1/index.m3u8
- Bangla Vision — Backup — https://tvsen5.aynaott.com/tgUzpPc9r6xw/index.m3u8
### beinsportsxtra.us (5 streams)
- beIN SPORTS XTRA — Sports — https://bein-esp-xumo.amagi.tv/playlistR1080p.m3u8
- beIN SPORTS XTRA — Backup — https://bein-beinxtrasports-firetv.amagi.tv/playlist.m3u8
- beIN SPORTS XTRA — Backup — https://bein-esp-xumo.amagi.tv/playlistR720P.m3u8
- beIN SPORTS XTRA — Backup — https://bein-xtra-bein.amagi.tv/playlist.m3u8
- beIN SPORTS XTRA — Backup — https://d9ssxzmclhfo4.cloudfront.net/bein_sports.m3u8
### bhojpuricinema.in@sd (7 streams)
- Bhojpuri Cinema — Indian Movies — https://live-bhojpuri.akamaized.net/liveabr/playlist.m3u8
- Bhojpuri Cinema — Backup — https://cdn.pishow.tv/ott/live/1033/master.m3u8
- Bhojpuri Cinema — Backup — https://fta.ektv.in/live/646/master.m3u8
- Bhojpuri Cinema — Backup — https://iptvlive.ahmed-bd-org.workers.dev/bhojpuri-cinema-1/index.m3u8
- Bhojpuri Cinema — Backup — https://live-bhojpuri.akamaized.net/liveabr/pub-iobhojpuqbu6yj/live_720p/chunks.m3u8
- Bhojpuri Cinema — Backup — https://mumt05.tangotv.in/87NeALx2BHOJPURICINEMA/index.m3u8
- Bhojpuri Cinema — Backup — https://streams.tangotv.in/BHOJPURICINEMA/ORIGIN/index.m3u8
### bijoytv.bd (3 streams)
- Bijoy TV — Bangladesh — https://tvsen6.aynaott.com/N8Xbo5vdwVU6sF43RsW0/index.m3u8
- Bijoy TV — Review — https://drk6xq0vhn.gpcdn.net/live/bijoy_tv_abr/index.m3u8
- Bijoy TV — Review — https://stream.ottplus.live/live/bijoy_tv_abr/index.m3u8
### boishakhitv.bd (4 streams)
- Boishakhi TV — Bangladesh — https://tvsen6.aynaott.com/1d3uG9VCgrR9DRtWZM57/index.m3u8
- Boishakhi TV — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/boishakhitv-org.stream/tracks-v1a1/mono.m3u8
- Boishakhi TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/boishakhi-tv-1/index.m3u8
- Boishakhi TV — Backup — https://boishakhi.sonarbanglatv.com/boishakhi/boishakhitv/index.m3u8
### btvnational.bd (2 streams)
- BTV National — Bangladesh — https://nkafmbewiff.gpcdn.net/tile_2/master.m3u8
- BTV National — Review — https://btv.hridoytv-channel.workers.dev/btv.m3u8
### channel1.bd (3 streams)
- Channel 1 — Bangladesh — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/channel1bd.stream/playlist.m3u8
- Channel 1 — Review — https://drk6xq0vhn.gpcdn.net/live/channel_1_hd_abr/index.m3u8
- Channel 1 — Review — https://stream.ottplus.live/live/channel_1_hd_abr/index.m3u8
### channel16.bd (2 streams)
- Channel 16 — Bangladesh — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/channel16bd.stream/tracks-v1a1/mono.m3u8
- Channel 16 — Backup — https://iptvlive.ahmed-bd-org.workers.dev/channel-16-1/index.m3u8
### channel24.bd (5 streams)
- Channel 24 — Bangladesh — https://tvsen6.aynaott.com/YrVDF8gujkdh/index.m3u8
- Channel 24 — Review — http://103.135.253.32:8080/Channel-24/index.m3u8
- Channel 24 — Review — https://drk6xq0vhn.gpcdn.net/live/channel_24_abr/index.m3u8
- Channel 24 — Review — https://iptvlive.ahmed-bd-org.workers.dev/channel-24-hd-1/index.m3u8
- Channel 24 — Review — https://stream.ottplus.live/live/channel_24_abr/index.m3u8
### channel52.bd (3 streams)
- Channel 52 — Bangladesh — http://str24.l9574.com/503.stream/tracks-v1a1/mono.m3u8
- Channel 52 — Backup — https://tvsen6.aynaott.com/channel52/index.m3u8
- Channel 52 — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/channel25usa.stream/tracks-v1a1/mono.m3u8
### channel9.bd (4 streams)
- Channel 9 — Bangladesh — https://nkafmbewiff.gpcdn.net/tile_7/1080p.m3u8
- Channel 9 — Backup — https://nkafmbewiff.gpcdn.net/tile_7/master.m3u8
- Channel 9 — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/channel9hd.stream/tracks-v1a1/mono.m3u8
- Channel 9 — Backup — https://tvsen6.aynaott.com/kajlsd57jnzxyo/index.m3u8
### channeli.bd (4 streams)
- Channel I — Bangladesh — https://tvsen6.aynaott.com/FNHpYvGZ7FkCE10PwTHm/index.m3u8
- Channel I — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/channeli-8-org.stream/tracks-v1a1/mono.m3u8
- Channel I — Backup — https://iptvlive.ahmed-bd-org.workers.dev/channel-i-1/index.m3u8
- Channel I — Backup — https://tvsen3.b-cdn.net/qUud8Nxs/index.m3u8
### channels.bd (5 streams)
- Channel S — Bangladesh — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/channels.stream/live-orgin/channels.stream/playlist.m3u8
- Channel S — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/channels.stream/index.m3u8
- Channel S — Backup — https://app.ncare.live/live-orgin/channels.stream/live-orgin/channels.stream/chunks.m3u8
- Channel S — Backup — https://app.ncare.live/live-orgin/channels.stream/playlist.m3u8
- Channel S — Backup — https://iptvlive.ahmed-bd-org.workers.dev/channel-s-1/index.m3u8
### channels.uk@679aa9 (2 streams)
- Channel S UK — Bangladesh — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI/chsukoff.stream/playlist.m3u8
- Channel S UK — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/chsukoff.stream/live-orgin/chsukoff.stream/chunks.m3u8
### colors.in@hd (2 streams)
- Colors — Indian Entertainment — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/sg/YuppTV/ColorsAPAC.m3u8
- Colors — Review — https://livetv.shamon-cable.net:8443/Colors-HD/index.m3u8
### colorsbangla.in@hd (2 streams)
- Colors Bangla — Review — https://livetv.shamon-cable.net:8443/Colors-bangla/index.m3u8
- Colors Bangla — Review — http://103.135.253.32:8080/COLORS-BANGLA-HD/index.m3u8
### colorsbanglacinema.in@sd (3 streams)
- Colors Bangla Cinema — Indian Bangla — http://103.114.11.37:8081/Colors-bangla-cinema/tracks-v1a1/mono.m3u8?token=[REDACTED]
- Colors Bangla Cinema — Indian Bangla — http://103.135.253.32:8080/COLORS-BANGLA-CINEMA/index.m3u8
- Colors Bangla Cinema — Indian Bangla — https://livetv.shamon-cable.net:8443/Colors-bangla-cinema/index.m3u8
### colorscineplex.uk (3 streams)
- Colors Cineplex — Indian Movies — https://d1rc86nwwc9fag.cloudfront.net/260723/smil:rishteycineplexukdev.smil/chunklist_b1928000.m3u8
- Colors Cineplex — Backup — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/gb/YuppTV/ColorsCineplexUK.m3u8
- Colors Cineplex — Review — http://103.135.253.32:8080/COLOR-CINEPLEX/index.m3u8
### colorsrishteyamericas.in (2 streams)
- Colors Rishtey — Indian Entertainment — https://manatv.akamaized.net/090823/smil:ristheyamerica.smil/playlist.m3u8
- Colors Rishtey — Backup — http://163.61.226.31:9981/stream/channelid/297962113?profile=pass
### colorstamil.in@sd (2 streams)
- Colors Tamil — Indian Entertainment — https://da86m1sqpm3o0.cloudfront.net/28072023/smil:colorstamilhd11.smil/playlist.m3u8
- Colors Tamil — Backup — https://da86m1sqpm3o0.cloudfront.net/28072023/smil:colorstamilhd11.smil/chunklist_b2628000.m3u8
### cricketgold.au@sd (4 streams)
- Cricket Gold — Sports — https://d1nj4u39ja4cn0.cloudfront.net/v1/master/9d062541f2ff39b5c0f48b743c6411d25f62fc25/FLS-MuxIP-CricketGold/418.m3u8
- Cricket Gold — Backup — https://d382r3rgbxdixq.cloudfront.net/scheduler/scheduleMaster/418.m3u8
- Cricket Gold — Backup — https://streams2.sofast.tv/scheduler/scheduleMaster/418.m3u8
- Cricket Gold — Backup — https://tvsen6.aynaott.com/M2W2UR49dmeKbZnmdRzN/index.m3u8
### custom.azantv (2 streams)
- Azan TV — Religious — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/azantv.stream/tracks-v1a1/mono.m3u8
- Azan TV — Backup — https://dbcanada.sonarbanglatv.com/azantv/atv/index.m3u8
### custom.islamchannelbangla (2 streams)
- Islam Channel Bangla — Religious — https://live-islamtv-bangla.simplestreamcdn.com/out/v1/islamchannel/islamtv-bangla/hls-ts/index.m3u8
- Islam Channel Bangla — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/islamchbangla.stream/tracks-v1a1/mono.m3u8
### custom.sportsgrid (2 streams)
- Sports Grid — Sports — https://tvsen6.aynaott.com/SportsGrid/index.m3u8
- Sports Grid — Backup — https://sportsgrid-tribal.amagi.tv/playlist1080p.m3u8
### dangal2.in@sd (5 streams)
- Dangal 2 — Indian Entertainment — https://live-dangal2.akamaized.net/liveabr/playlist.m3u8
- Dangal 2 — Backup — http://163.61.226.31:9981/stream/channelid/568470441?profile=pass
- Dangal 2 — Backup — https://fta.ektv.in/live/18/master.m3u8
- Dangal 2 — Backup — https://mumt03.tangotv.in/Dsly5z3HDANGAL2/index.m3u8
- Dangal 2 — Backup — https://streams.tangotv.in/DANGAL2/ORIGIN/index.m3u8
### dangaltv.in@sd (8 streams)
- Dangal — Indian Entertainment — https://live-dangal.akamaized.net/liveabr/playlist.m3u8
- Dangal — Backup — https://cdn.pishow.tv/ott/live/1141/master.m3u8
- Dangal — Backup — https://live-dangal.akamaized.net/liveabr/pub-iodang10p4al/live_720p/chunks.m3u8
- Dangal — Backup — https://streams.tangotv.in/DANGAL/ORIGIN/index.m3u8
- Dangal — Backup — http://163.61.226.31:9981/stream/channelid/359795895?profile=pass
- Dangal — Backup — https://fta.ektv.in/live/17/master.m3u8
- Dangal — Backup — https://mumt04.tangotv.in/m18aqlK4DANGAL/index.m3u8
- Dangal — Review — https://tvsen3.aynaott.com/qPNg4LJK/index.m3u8
### dbcnews.bd (4 streams)
- DBC News — Bangladesh — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/dbcnews.stream/tracks-v1a1/mono.m3u8
- DBC News — Backup — https://tvsen6.aynaott.com/pF66Tkz0qFwP2aMMqHyt/index.m3u8
- DBC News — Backup — https://iptvlive.ahmed-bd-org.workers.dev/dbc-news-1/index.m3u8
- DBC News — Review — http://tvn3.chowdhury-shaheb.com/dbc/index.m3u8
### ddarunprabha.in@sd (2 streams)
- DD Arun Prabha — Indian Entertainment — https://d2lk5u59tns74c.cloudfront.net/out/v1/308556d9fd1246adb479ef012a39bbfe/index.m3u8
- DD Arun Prabha — Backup — https://cdn.pishow.tv/ott/live/32/master.m3u8
### ddbangla.in@sd (4 streams)
- DD Bangla — Indian Bangla — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/7ff57cc9046b4c188b51a0d506f36e7f/index.m3u8
- DD Bangla — Backup — https://cdn.pishow.tv/ott/live/37/master.m3u8
- DD Bangla — Backup — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/7ff57cc9046b4c188b51a0d506f36e7f/index_3.m3u8
- DD Bangla — Review — https://fta.ektv.in/live/197/master.m3u8
### ddbihar.in@sd (2 streams)
- DD Bihar — Indian Entertainment — https://cdn.pishow.tv/ott/live/35/master.m3u8
- DD Bihar — Backup — https://d2lk5u59tns74c.cloudfront.net/out/v1/380b0765f87741a4812bc952ec6fbf21/index.m3u8
### ddchandana.in@sd (2 streams)
- DD Chandana — Indian Entertainment — https://cdn.pishow.tv/ott/live/28/master.m3u8
- DD Chandana — Backup — https://d2lk5u59tns74c.cloudfront.net/out/v1/0c980455d2fb4b69bcc6235745ee6039/index.m3u8
### ddchhattisgarh.in@sd (2 streams)
- DD Chhattisgarh — Indian Entertainment — https://cdn.pishow.tv/ott/live/15/master.m3u8
- DD Chhattisgarh — Backup — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/5078083881bc489ea14f4c85e7abe4d6/index.m3u8
### ddgirnar.in@sd (2 streams)
- DD Girnar — Indian Entertainment — https://d2lk5u59tns74c.cloudfront.net/out/v1/558fdb9aebb54bb5bbbf0ced03686148/index.m3u8
- DD Girnar — Review — https://fta.ektv.in/live/368/master.m3u8
### ddgoa.in@sd (2 streams)
- DD Goa — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/e5b9db1cc184406bb97159da2f120f91/index.m3u8
- DD Goa — Review — https://fta.ektv.in/live/367/master.m3u8
### ddharyana.in@sd (2 streams)
- DD Haryana — Indian Entertainment — https://d2lk5u59tns74c.cloudfront.net/out/v1/950fc69666474351bde0a32b9600c804/index.m3u8
- DD Haryana — Backup — https://fta.ektv.in/live/580/master.m3u8
### ddhimachalpradesh.in@sd (2 streams)
- DD Himachal Pradesh — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/afd2e335b0ba40eb9bdf1096118c6ede/index.m3u8
- DD Himachal Pradesh — Review — https://fta.ektv.in/live/575/master.m3u8
### ddjharkhand.in@sd (2 streams)
- DD Jharkhand — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/e8c3741f8c154d3185831f4e31777fb2/index.m3u8
- DD Jharkhand — Backup — https://cdn.pishow.tv/ott/live/1617/master.m3u8
### ddkashir.in@sd (2 streams)
- DD Kashir — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/8a59a828e80c49d0958925950cec0204/index.m3u8
- DD Kashir — Backup — https://cdn.pishow.tv/ott/live/16/master.m3u8
### ddmadhyapradesh.in@sd (3 streams)
- DD Madhya Pradesh — Indian Entertainment — https://mumbai-edge.smartplaytv.in/ddmadhyapradesh/index.m3u8
- DD Madhya Pradesh — Backup — https://cdn.pishow.tv/ott/live/31/master.m3u8
- DD Madhya Pradesh — Backup — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/b5256b391a7c4ae6977535b73fd6f591/index.m3u8
### ddmalayalam.in@sd (2 streams)
- DD Malayalam — Indian Entertainment — https://d2lk5u59tns74c.cloudfront.net/out/v1/c313674ffced4c9a90f1bba436df2b9b/index.m3u8
- DD Malayalam — Review — https://fta.ektv.in/live/680/master.m3u8
### ddnational.in@sd (3 streams)
- DD National — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/40492a64c1db4a1385ba1a397d357d3a/index.m3u8
- DD National — Backup — https://fta.ektv.in/live/15/master.m3u8
- DD National — Review — http://107.167.16.138/ddnational/index.m3u8
### ddodia.in@sd (3 streams)
- DD Odia — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/ef4ea632b77a480ebd77106968aa99a9/index.m3u8
- DD Odia — Backup — https://mumbai-edge.smartplaytv.in/ddodiya/index.m3u8
- DD Odia — Review — https://fta.ektv.in/live/384/master.m3u8
### ddpunjabi.in@sd (2 streams)
- DD Punjabi — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/da821c24a59d4e57960497aeaca8fb33/index.m3u8
- DD Punjabi — Backup — http://163.61.226.31:9981/stream/channelid/2094424586?profile=pass
### ddrajasthan.in@sd (2 streams)
- DD Rajasthan — Indian Entertainment — https://d2lk5u59tns74c.cloudfront.net/out/v1/5b6bbbf682b741ecbe279f75a4a9a3e6/index.m3u8
- DD Rajasthan — Backup — https://cdn.pishow.tv/ott/live/34/master.m3u8
### ddsahyadri.in@sd (2 streams)
- DD Sahyadri — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/66dcc3ebe182447ba42837e746cf0c7c/index.m3u8
- DD Sahyadri — Review — https://fta.ektv.in/live/187/master.m3u8
### ddsaptagiri.in@sd (2 streams)
- DD Saptagiri — Indian Entertainment — https://d2lk5u59tns74c.cloudfront.net/out/v1/26e915d6d12b4a06822c5e33c088ed56/index.m3u8
- DD Saptagiri — Backup — https://cdn.pishow.tv/ott/live/22/master.m3u8
### ddsports.in@sd (6 streams)
- DD Sports — Sports — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/b17adfe543354fdd8d189b110617cddd/index.m3u8
- DD Sports — Backup — https://cdn.pishow.tv/ott/live/1161/master.m3u8
- DD Sports — Backup — https://fta.ektv.in/live/280/master.m3u8
- DD Sports — Backup — https://fta.ektv.in/live/64/64_0.m3u8
- DD Sports — Backup — https://mumbai-edge.smartplaytv.in/DDSports/index.m3u8
- DD Sports — Backup — https://mumbai-edge.smartplaytv.in/DDSportsHD/index.m3u8
### ddtamil.in@sd (3 streams)
- DD Tamil — Indian Entertainment — https://d2lk5u59tns74c.cloudfront.net/out/v1/abf46b14847e45499f4a47f3a9afe93d/index.m3u8
- DD Tamil — Backup — https://cdn.pishow.tv/ott/live/1737/master.m3u8
- DD Tamil — Review — https://fta.ektv.in/live/679/master.m3u8
### ddurdu.in@sd (2 streams)
- DD Urdu — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/9b91e9007e754db39a8b32c6bfc5b24a/index.m3u8
- DD Urdu — Backup — https://cdn.pishow.tv/ott/live/8/master.m3u8
### dduttarakhand.in@sd (2 streams)
- DD Uttarakhand — Indian Entertainment — https://cdn.pishow.tv/ott/live/17/master.m3u8
- DD Uttarakhand — Backup — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/a70323c56ac647c2a8c8fc34e4c73912/index.m3u8
### dduttarpradesh.in@sd (2 streams)
- DD Uttar Pradesh — Indian Entertainment — https://cdn.pishow.tv/ott/live/36/master.m3u8
- DD Uttar Pradesh — Backup — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/70d4f6874fa64032a685e3123520f07d/index.m3u8
### ddyadagiri.in@sd (3 streams)
- DD Yadagiri — Indian Entertainment — https://cdn.pishow.tv/ott/live/21/master.m3u8
- DD Yadagiri — Backup — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/c89fa6d6f5864ac29670d6f91cb7e32a/index.m3u8
- DD Yadagiri — Review — https://fta.ektv.in/live/678/master.m3u8
### deentv.uk (3 streams)
- Deen TV — Religious — https://cd198.anystream.uk:9092/iqapp/d33ntv/playlist.m3u8
- Deen TV — Backup — https://app.ncare.live/live-orgin/deentv.stream/playlist.m3u8
- Deen TV — Backup — https://tvsen3.aynaott.com/TJcnZW3U/index.m3u8
### deeptotv.bd (3 streams)
- Deepto TV — Bangladesh — https://byphdgllyk.gpcdn.net/hls/deeptotv/index.m3u8
- Deepto TV — Backup — https://tvsen5.aynaott.com/tK2BNdfsdfsdf/index.m3u8
- Deepto TV — Review — http://103.135.253.32:8080/Deepto-TV/index.m3u8
### deshebideshe.ca (2 streams)
- Deshe Bideshe — Bangladesh — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/deshebideshe.stream/tracks-v1a1/mono.m3u8
- Deshe Bideshe — Backup — https://dbcanada.sonarbanglatv.com/deshebideshe/dbtv/index.m3u8
### deshtv.bd (3 streams)
- Desh TV — Bangladesh — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/deshtv.stream/index.m3u8
- Desh TV — Backup — https://tvsen6.aynaott.com/ryFkXfd1a4CQ7mMdc820/index.m3u8
- Desh TV — Review — https://stream.ottplus.live/live/desh_tv_abr/index.m3u8
### desichannel.in (2 streams)
- Desi Channel — Indian Entertainment — https://livestream.unlimitedcdn.com/agm-dc/desi-channel/index.m3u8
- Desi Channel — Backup — https://desichannel.kableone.com/desichannel/master.m3u8
### dhoommusic.in@sd (3 streams)
- Dhoom Music — Indian Bangla — https://fta.ektv.in/live/378/master.m3u8
- Dhoom Music — Indian Bangla — https://cdn.pishow.tv/ott/live/1456/master.m3u8
- Dhoom Music — Indian Bangla — https://mumt06.tangotv.in/qYyB8fXVDHOOMMUSIC/index.m3u8
### discoverpakistan.pk@sd (2 streams)
- Discover Pakistan — Pakistani — https://livecdn.live247stream.com/discoverpakistan/web/playlist.m3u8
- Discover Pakistan — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/discoverpakistan.stream/playlist.m3u8
### disneychannel.in@hd (2 streams)
- Disney Channel — Kids — http://212.5.144.156:8080/disney/index.m3u8
- Disney Channel — Backup — http://rgkkw.live/live/[REDACTED]/[REDACTED]/19741.ts
### durontotv.bd (3 streams)
- Duronto TV — Kids — https://tvsen5.aynaott.com/6xyZ3N4oHv2KBJdB6W4p/index.fmp4.m3u8
- Duronto TV — Review — http://103.135.253.32:8080/DORONTU-TV/index.m3u8
- Duronto TV — Review — https://livetv.shamon-cable.net:8443/Duronto/index.m3u8
### e24.in (3 streams)
- E24 — Indian Entertainment — https://amg13643-amg13643c2-amgplt0016.playout.now3.amagi.tv/ts-eu-w1-n2/playlist/amg13643-amg13643c2-amgplt0016/playlist.m3u8
- E24 — Backup — https://mumt04.tangotv.in/m18aqlK4E24/index.m3u8
- E24 — Backup — https://fta.ektv.in/live/159/master.m3u8
### ekattortv.bd (2 streams)
- Ekattor TV — Bangladesh — https://tvsen6.aynaott.com/EWDrV5QskgarZEUBb3pU/index.m3u8
- Ekattor TV — Review — https://stream.ottplus.live/live/ekattor_tv_abr/index.m3u8
### ekhontv.bd (5 streams)
- Ekhon TV — Bangladesh — https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8
- Ekhon TV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/globaltv.stream/index.m3u8
- Ekhon TV — Review — https://tplay.live/out/bangladesh/ekhontv.index.m3u8
- Ekhon TV — Review — https://drk6xq0vhn.gpcdn.net/live/ekhon_tv_abr/index.m3u8
- Ekhon TV — Review — https://stream.ottplus.live/live/ekhon_tv_abr/index.m3u8
### ekusheytv.bd (5 streams)
- Ekushey TV — Bangladesh — https://tvsen5.aynaott.com/SyQuXz8sC3TB/index.m3u8
- Ekushey TV — Backup — http://210.4.72.204/hls-live/livepkgr/_definst_/liveevent/livestream3.m3u8
- Ekushey TV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/ekusheytv-8-org.stream/index.m3u8
- Ekushey TV — Backup — https://ekusheyserver.com/etvlivesn.m3u8
- Ekushey TV — Backup — https://tvsen6.aynaott.com/y4mEVZNAbeNWTbd6Z2Pw/index.m3u8
### enter10bangla.in (4 streams)
- Enterr10 Bangla — Indian Bangla — https://live-bangla.akamaized.net/liveabr/playlist.m3u8
- Enterr10 Bangla — Backup — https://amg01448-samsungin-enterr10bangla-samsungin-ad-gg.amagi.tv/playlist/amg01448-samsungin-enterr10bangla-samsungin/playlist.m3u8
- Enterr10 Bangla — Backup — https://mumt07.tangotv.in/zHjX9OFlENTERR10BANGLA/index.m3u8
- Enterr10 Bangla — Backup — https://iptvlive.ahmed-bd-org.workers.dev/enter-10-bangla-1/index.m3u8
### entertv.bd (2 streams)
- Enter TV — Bangladesh — https://live1.entertv.com.bd/entertv/tracks-v1a1/mono.m3u8
- Enter TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/enter-tv-1/index.m3u8
### epicbharat.in@digital (2 streams)
- Epic Bharat Digital (1080p) — New Backups — https://dt4psgz92awc5.cloudfront.net/v1/master/071c0467fcd02420cdf0d8a1ca3524b96c27a151/naazara_tv/master.m3u8
- Epic Bharat Digital — Review — https://cc-p1izg43bk7sj5.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-p1izg43bk7sj5/DIYC/PMSL/IN10/Nazara_IN_B/Nazara_IN_B.m3u8
### epicbharat.in@sd (3 streams)
- Epic Bharat — Indian Entertainment — https://mumt06.tangotv.in/qYyB8fXVEPICTV/index.m3u8
- Epic Bharat — Backup — https://epiconvh.akamaized.net/live/nazara/master.m3u8
- Epic Bharat — Backup — https://fta.ektv.in/live/471/master.m3u8
### epicbhojpuri.in@sd (2 streams)
- Epic Bhojpuri — Indian Movies — https://mumt01.tangotv.in/O5aw8Zn3EPICBHOJPURI/index.m3u8
- Epic Bhojpuri — Backup — https://fta.ektv.in/live/467/master.m3u8
### epicbhojpuridigital.in (2 streams)
- Epic Bhojpuri Digital — Indian Movies — https://cc-8hy4a26pz2uos.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-8hy4a26pz2uos/playlist.m3u8
- Epic Bhojpuri Digital — Backup — https://cc-8hy4a26pz2uos.akamaized.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-8hy4a26pz2uos/45b71b91-51a1-4cfd-a422-c7f32efbf377/3.m3u8
### epicmusic.in@sd (8 streams)
- Epic Music — Indian Music — https://mumt04.tangotv.in/m18aqlK4EPICMUSIC/index.m3u8
- Epic Music — Backup — https://cc-3cyxq80qusspd.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-3cyxq80qusspd/playlist.m3u8
- Epic Music — Backup — https://fta.ektv.in/live/469/master.m3u8
- Epic Music — Backup — https://iptvlive.ahmed-bd-org.workers.dev/epic-music-1/index.m3u8
- Epic Music — Backup — https://jmp2.uk/stvp-IN8000196E
- Epic Music — Backup — https://streams.tangotv.in/EPICMUSIC/ORIGIN/index.m3u8
- Epic Music — Backup — https://cc-3cyxq80qusspd.akamaized.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-3cyxq80qusspd/d68f6612-3a4e-4ed4-9853-fc41801678d1/2.m3u8
- Epic Music — Review — http://66.102.126.10:8000/play/a01i/index.m3u8
### espn.us (5 streams)
- ESPN — Sports — http://181.78.197.59:8000/play/a07z/index.m3u8
- ESPN — Backup — http://212.5.144.156:8080/espn/index.m3u8
- ESPN — Backup — http://85.237.89.160:9590/usa-s/ESPN-HD/index.m3u8
- ESPN — Backup — https://tvsen5.aynaott.com/espn/index.m3u8
- ESPN — Backup — https://tvsen7.aynaott.com/espn/index.m3u8
### etvbeats.in@hd (2 streams)
- ETV Beats — Indian Music — https://jmp2.uk/stvp-IN4900002RV
- ETV Beats — Backup — https://cc-szivnms4rlah6.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-szivnms4rlah6/WWBI/Amagi/ETV_Music_IN/playlist.m3u8
### etvcinema.in (2 streams)
- ETV Cinema — Indian Movies — https://yupplivegcpusa.yuppcdn.net/100823/smil:etvcinema.smil/playlist.m3u8?hdnts=[REDACTED]
- ETV Cinema — Review — https://d27zlkxhgwrfgo.cloudfront.net/v1/master/9d43eacaed199f8d5883927e7aef514a8a08e108/ETV_CINEMA_H264_cloud_in/index.m3u8
### etvjosh.in (2 streams)
- ETV Josh — Indian Entertainment — https://cc-uyh1ow5zouoio.akamaized.net/WWBI/Amagi/ETV_Josh_IN/playlist.m3u8
- ETV Josh — Backup — https://cc-uyh1ow5zouoio.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-uyh1ow5zouoio/WWBI/Amagi/ETV_Josh_IN/playlist.m3u8
### etvplus.in@hd (2 streams)
- ETV Plus HD — Indian Entertainment — https://d1qqzrxc7kpb0u.cloudfront.net/v1/50e3ae620bd6496cb3ac4294c877c36a/airtTA6RA.m3u8
- ETV Plus HD — Review — https://d12ee3o8yfkkhd.cloudfront.net/c6a4b411295f47f48c908d2ac0605bad/index.m3u8
### faktmarathi.in@sd (3 streams)
- Fakt Marathi — Indian Entertainment — https://mumt07.tangotv.in/zHjX9OFlFAKTMARATHI/index.m3u8
- Fakt Marathi — Backup — https://cdn.pishow.tv/ott/live/10002/master.m3u8
- Fakt Marathi — Backup — https://fta.ektv.in/live/188/master.m3u8
### fox.sports.com (2 streams)
- FOX Sports — Sports — https://d1jzu95oc8fgt3.cloudfront.net/FOX_Sports.m3u8
- FOX Sports — Backup — https://d1jzu95oc8fgt3.cloudfront.net/FOX_Sports720p.m3u8
### gangaurtv.in@sd (3 streams)
- Gangaur TV — Indian Entertainment — https://pbgangaur.wiseplayout.com/Gangaur/master.m3u8
- Gangaur TV — Backup — https://cdn.pishow.tv/ott/live/1221/master.m3u8
- Gangaur TV — Backup — https://mumt04.tangotv.in/m18aqlK4GANGAURTV/index.m3u8
### gazitv.bd (6 streams)
- G TV — Bangladesh — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/gazibdz.stream/live-orgin/gazibdz.stream/playlist.m3u8
- G TV — Backup — https://app.ncare.live/live-orgin/gazibdz.stream/live-orgin/gazibdz.stream/chunks.m3u8
- G TV — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/gazibdz.stream/playlist.m3u8
- G TV — Backup — https://app.ncare.live/live-orgin/gazibdz.stream/playlist.m3u8
- G TV — Review — http://103.135.253.32:8080/Gazi-TV/index.m3u8
- G TV — Review — http://tvn1.chowdhury-shaheb.com/gazitv/index.m3u8
### globaltv.bd (4 streams)
- Global TV — Bangladesh — https://tvsen6.aynaott.com/y0q9eFAuquAtvTxRzUHq/index.m3u8
- Global TV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/Global-tv.stream/playlist.m3u8
- Global TV — Review — http://116.204.149.16/globaltv/index.m3u8
- Global TV — Review — https://stream.ottplus.live/live/global_tv_abr/index.m3u8
### goldmines.in@sd (4 streams)
- Goldmines — Indian Movies — https://streams.tangotv.in/GOLDMINES/ORIGIN/index.m3u8
- Goldmines — Backup — http://163.61.226.31:9981/stream/channelid/863672695?profile=pass
- Goldmines — Backup — https://cdn.pishow.tv/ott/live/1459/master.m3u8
- Goldmines — Backup — https://mumt04.tangotv.in/m18aqlK4GOLDMINES/index.m3u8
### goldminesaction.in (2 streams)
- Goldmines Action — Indian Movies — https://mumt03.tangotv.in/Dsly5z3HGOLDMINESACTION/index.m3u8
- Goldmines Action — Backup — https://fta.ektv.in/live/584/master.m3u8
### goldminesbollywood.in@sd (3 streams)
- Goldmines Bollywood — Indian Movies — https://streams.tangotv.in/GOLDMINESBOLLYWOOD/ORIGIN/index.m3u8
- Goldmines Bollywood — Backup — http://163.61.226.31:9981/stream/channelid/1436412639?profile=pass
- Goldmines Bollywood — Backup — https://mumt03.tangotv.in/Dsly5z3HGOLDMINESBOLLYWOOD/index.m3u8
### goldminesmovies.in@sd (5 streams)
- Goldmines Movies — Indian Movies — https://streams.tangotv.in/GOLDMINEMOVIES/ORIGIN/index.m3u8
- Goldmines Movies — Backup — http://163.61.226.31:9981/stream/channelid/1393052638?profile=pass
- Goldmines Movies — Backup — https://cdn.pishow.tv/ott/live/1461/master.m3u8
- Goldmines Movies — Backup — https://mumt04.tangotv.in/m18aqlK4GOLDMINEMOVIES/index.m3u8
- Goldmines Movies — Review — https://tvsen3.aynaott.com/5CGfPvGp/index.m3u8
### gtcpunjabi.in@sd (2 streams)
- GTC Punjabi — Indian Entertainment — https://gtc-yupp.vgcdn.net/vglive-sk-254807/index.m3u8
- GTC Punjabi — Backup — https://cdn.ottlive.co.in/gtcpunjabi/index.m3u8
### hindihits.in (2 streams)
- Hindi Hits — Indian Music — https://samitaorigin.tangotv.in/HINDIHITS/SAMITAORIGIN/index.m3u8
- Hindi Hits — Backup — http://146.59.253.52:8080/hindihitshd/index.m3u8
### hummasala.pk (2 streams)
- HUM Masala — Pakistani — https://j6nfugukcl.gpcdn.net/tile_1/master.m3u8
- HUM Masala — Backup — http://38.101.217.46/HumMasala/index.m3u8
### humtv.pk (5 streams)
- Hum TV — Pakistani — https://g4wlkwx8l23a-hls-live.5centscdn.com/HUM/271ddf829afeece44d8732757fba1a66.sdp/playlist_dvr.m3u8
- Hum TV — Backup — https://g4wlkwx8l23a-hls-live.5centscdn.com/HUM/271ddf829afeece44d8732757fba1a66.sdp/HUM/TV1/chunks_dvr.m3u8
- Hum TV — Backup — https://cdn4.mjunoon.tv:8087/streamtest/82M/chunks.m3u8
- Hum TV — Review — https://drk6xq0vhn.gpcdn.net/live/hum_tv_abr/index.m3u8
- Hum TV — Review — https://stream.ottplus.live/live/hum_tv_abr/index.m3u8
### insync.in (3 streams)
- Insync — Indian Music — https://mumt04.tangotv.in/m18aqlK4INSYNC/index.m3u8
- Insync — Backup — https://d1msejlow1t3l4.cloudfront.net/fta/insync/playlist.m3u8
- Insync — Backup — https://fta.ektv.in/live/160/master.m3u8
### iqrabangla.uk (4 streams)
- Iqra Bangla — Religious — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/iqrabanglatvoffice.stream/live-orgin/iqrabanglatvoffice.stream/chunks.m3u8
- Iqra Bangla — Backup — https://tvsen5.aynaott.com/iqrabangla/index.m3u8
- Iqra Bangla — Backup — https://tvsen3.aynaott.com/EuEy5mBW/index.m3u8
- Iqra Bangla — Backup — https://cd198.anystream.uk:9092/iqapp/iq53la/chunks.m3u8
### islamictv.bd (2 streams)
- Islamic TV — Religious — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/islamictvbd.stream/tracks-v1a1/mono.m3u8
- Islamic TV — Review — https://drk6xq0vhn.gpcdn.net/live/islamic_tv/index.m3u8
### jagonews24.bd (3 streams)
- Jago News 24 — Bangladesh — https://app.ncare.live/live-orgin/jagonews24.stream/playlist.m3u8
- Jago News 24 — Backup — https://app.ncare.live/live-orgin/jagonews24.stream/live-orgin/jagonews24.stream/chunks.m3u8
- Jago News 24 — Backup — https://iptvlive.ahmed-bd-org.workers.dev/jago-news-24-1/index.m3u8
### jalshamovies.in@sd (2 streams)
- Jalsha Movies — Indian Bangla — https://box.bbaria.net:8083/Jalsha_Movie/tracks-v1a1/mono.m3u8
- Jalsha Movies — Indian Bangla — https://livetv.shamon-cable.net:8443/Jalsha-Movies/index.m3u8
### jalwatv.pk@sd (2 streams)
- Jalwa TV — Indian Music — https://cdn4.mjunoon.tv:8087/streamtest/135M/chunks.m3u8
- Jalwa TV — Backup — https://vodzong.mjunoon.tv:8087/streamtest/JalwaTV-135/live/135M/chunks.m3u8
### jamunatv.bd (4 streams)
- Jamuna TV — Bangladesh — https://tvsen6.aynaott.com/KGdZEdA7qQ43dmPkgk1j/index.m3u8
- Jamuna TV — Backup — https://iptv-proxy.ahmed-bd-org.workers.dev/jamuna-tv/index.m3u8
- Jamuna TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/jamuna-tv-1/index.m3u8
- Jamuna TV — Review — https://stream.ottplus.live/live/jamuna_tv_abr/index.m3u8
### jatv.bd (2 streams)
- JA TV — Review — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/jtvbd12.stream/tracks-v1a1/mono.m3u8
- JA TV — Review — https://dish.porosh.com.bd/hls/jtvnews.m3u8
### jonack.in@sd (2 streams)
- Jonack — Indian Entertainment — https://cdn.pishow.tv/ott/live/10006/master.m3u8
- Jonack — Backup — https://cdn.smartstream.video/smartstream-us/jonakk/jonakk/playlist.m3u8
### kairalitv.in@sd (2 streams)
- Kairali TV — Indian Entertainment — https://streams.tangotv.in/KAIRALI/ORIGIN/index.m3u8
- Kairali TV — Backup — https://mumt01.tangotv.in/O5aw8Zn3KAIRALI/index.m3u8
### kairaliwe.in@sd (3 streams)
- Kairali We — Indian Movies — https://streams.tangotv.in/WETV/ORIGIN/index.m3u8
- Kairali We — Backup — https://cdn.pishow.tv/ott/live/1530/master.m3u8
- Kairali We — Backup — https://mumt01.tangotv.in/O5aw8Zn3WETV/index.m3u8
### kalaignarmurasu.in (2 streams)
- Kalaignar Murasu — Indian Movies — https://yuppmedtaorire.akamaized.net/v1/master/a0d007312bfd99c47f76b77ae26b1ccdaae76cb1/murasu_nim_https/050522/murasu/playlist.m3u8
- Kalaignar Murasu — Backup — https://segment.yuppcdn.net/050522/murasu/playlist.m3u8
### kappatv.in@alt1 (3 streams)
- Kappa TV (Music) — Indian Music — https://cdn.pishow.tv/ott/live/1123/master.m3u8
- Kappa TV (Music) — Backup — https://d1msejlow1t3l4.cloudfront.net/fta/kappatv/playlist.m3u8
- Kappa TV (Music) — Backup — https://mumt03.tangotv.in/Dsly5z3HKAPPATV/index.m3u8
### keralavision.in@sd (2 streams)
- Kerala Vision — Indian Entertainment — https://cdn.pishow.tv/ott/live/243/master.m3u8
- Kerala Vision — Backup — https://mumt03.tangotv.in/Dsly5z3HKERALAVISION/index.m3u8
### khushboobangla.in@sd (3 streams)
- Khushboo Bangla — Indian Bangla — https://mumt01.tangotv.in/O5aw8Zn3KHUSHBOOTVBANGLA/index.m3u8
- Khushboo Bangla — Backup — https://cdn.pishow.tv/ott/live/1473/master.m3u8
- Khushboo Bangla — Review — https://tvsen6.aynaott.com/mzwbzfZ4/index.m3u8
### ktvbangla.in@sd (2 streams)
- KTV Bangla — Indian Bangla — https://server.livelegitpro.in:9899/tribetv/tribetv/index.m3u8
- KTV Bangla — Backup — https://stream.ottlive.co.in/ktvbangla/index.m3u8
### maasrangatv.bd (6 streams)
- Maasranga TV — Bangladesh — https://mtv.sunplex.live/MAASRANGA/index.m3u8
- Maasranga TV — Backup — https://tvsen5.aynaott.com/maasrangatv/index.m3u8
- Maasranga TV — Backup — https://tvsen6.aynaott.com/maasrangatv/index.m3u8
- Maasranga TV — Backup — https://nkafmbewiff.gpcdn.net/tile_4/master.m3u8
- Maasranga TV — Review — http://116.204.149.16/maasranga/index.m3u8
- Maasranga TV — Review — http://tvsen5.aynascope.net/maasrangatv/index.m3u8
### mahaamax.in (3 streams)
- Mahaa Max — Indian Entertainment — https://mumbai-edge.smartplaytv.in/MahaMax/index.m3u8
- Mahaa Max — Backup — https://cdn.pishow.tv/ott/live/1147/master.m3u8
- Mahaa Max — Backup — https://mumt03.tangotv.in/Dsly5z3HMAHAAMAX/index.m3u8
### mahamovie.in@sd (2 streams)
- Maha Movie — Indian Movies — https://cdn.pishow.tv/ott/live/10007/master.m3u8
- Maha Movie — Backup — https://fta.ektv.in/live/48/48_0.m3u8
### makkahtv.sa (3 streams)
- Makkah TV — Religious — https://media2.streambrothers.com:1936/8122/8122/playlist.m3u8
- Makkah TV — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/makkahtv.stream/tracks-v1a1/mono.m3u8
- Makkah TV — Backup — https://media2.streambrothers.com:1936/8122/8122/chunklist_w1247854077.m3u8
### manoranjangrand.in (3 streams)
- Manoranjan Grand — Indian Entertainment — https://mumt06.tangotv.in/qYyB8fXVMANORANJANGRAND/index.m3u8
- Manoranjan Grand — Backup — https://streams.tangotv.in/MANORANJANGRAND/ORIGIN/index.m3u8
- Manoranjan Grand — Backup — https://cdn.pishow.tv/ott/live/1011/master.m3u8
### manoranjanmovies.in@sd (3 streams)
- Manoranjan Movies — Indian Movies — https://mumt04.tangotv.in/m18aqlK4MANORANJANMOVIES/index.m3u8
- Manoranjan Movies — Backup — http://163.61.226.31:9981/stream/channelid/509213855?profile=pass
- Manoranjan Movies — Backup — https://fta.ektv.in/live/47/47_0.m3u8
### manoranjanprime.in@sd (2 streams)
- Manoranjan Prime — Indian Movies — https://cdn.pishow.tv/ott/live/1474/master.m3u8
- Manoranjan Prime — Review — https://mumt06.tangotv.in/qYyB8fXVMANORANJANPRIME/index.m3u8
### manoranjantv.in@sd (5 streams)
- Manoranjan TV — Indian Entertainment — https://streams.tangotv.in/MANORANJANTV/ORIGIN/index.m3u8
- Manoranjan TV — Backup — http://163.61.226.31:9981/stream/channelid/889274687?profile=pass
- Manoranjan TV — Backup — https://fta.ektv.in/live/23/master.m3u8
- Manoranjan TV — Backup — https://mumt04.tangotv.in/m18aqlK4MANORANJANTV/index.m3u8
- Manoranjan TV — Review — https://cdn.pishow.tv/ott/live/1013/master.m3u8
### marutamtv.in (2 streams)
- MNTV (Tamil) — Indian Entertainment — https://mntv.livebox.co.in/mntvhls/live.m3u8
- MNTV (Tamil) — Backup — https://www.khuwemultimedia.com/hls/mntv/mntv.m3u8
### matribhumitv.bd (2 streams)
- Matribhumi TV — Bangladesh — https://live.playmax.live/matribhumi/index.m3u8
- Matribhumi TV — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/matribhumitv.stream/playlist.m3u8
### mazhavilmanorama.in@sd (8 streams)
- Mazhavil Manorama — Indian Entertainment — https://yuppmedtaorire.akamaized.net/v1/master/a0d007312bfd99c47f76b77ae26b1ccdaae76cb1/mazhavilmanorama_nim_https/050522/mazhavilmanorama/playlist.m3u8
- Mazhavil Manorama (576p) — New Backups — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/ad6c59acd03b4b5a9928e32d7fee66db/index.m3u8
- Mazhavil Manorama — Backup — https://cdn.pishow.tv/ott/live/1479/master.m3u8
- Mazhavil Manorama — Backup — https://mmtv-vglivessai.akamaized.net/v1/master/673630b269b766886555eebfddd4f27f3de3ab50/f8a0827f-030f-4a0d-b7e5-338996c09a5b/index.m3u8
- Mazhavil Manorama — Backup — https://mumt03.tangotv.in/Dsly5z3HMAZHAVILMANORAMAINT/index.m3u8
- Mazhavil Manorama — Backup — https://mumt07.tangotv.in/zHjX9OFlMAZHAVILMANORAMAHD/index.m3u8
- Mazhavil Manorama — Backup — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/in/YuppTV/MazhavilManoramaInternational.m3u8
- Mazhavil Manorama — Backup — https://fta.ektv.in/live/245/master.m3u8
### mbcbollywood.ae (2 streams)
- MBC Bollywood — Indian Movies — https://shd-gcp-live.edgenextcdn.net/live/bitmovin-mbc-bollywood/546eb40d7dcf9a209255dd2496903764/index.m3u8
- MBC Bollywood — Review — http://93.184.10.248/MBCBollywood/index.m3u8
### medinalive.bd (3 streams)
- Medina Live — Religious — https://cdn-globecast.akamaized.net/live/eds/saudi_sunnah/hls_roku/index.m3u8
- Medina Live — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/madina.stream/playlist.m3u8
- Medina Live — Backup — http://m.live.net.sa:1935/live/sunnah/playlist.m3u8
### metv.bd (2 streams)
- ME TV — Bangladesh — https://iptvbd.live/metv1080/1080.m3u8
- ME TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/me-tv-1/index.m3u8
### mhone.in@sd (2 streams)
- MH One — Indian Music — https://samitaorigin.tangotv.in/MHONE/SAMITAORIGIN/index.m3u8
- MH One — Backup — https://fta.ektv.in/live/353/master.m3u8
### mhonedilse.in@sd (3 streams)
- MH One Dil Se — Indian Music — https://mumt01.tangotv.in/O5aw8Zn3MHONEDILSE/index.m3u8
- MH One Dil Se — Backup — https://fta.ektv.in/live/351/master.m3u8
- MH One Dil Se — Backup — https://streams.tangotv.in/MHONEDILSE/ORIGIN/index.m3u8
### mhonemovies.in@sd (2 streams)
- MH One Movies — Indian Movies — https://mumt03.tangotv.in/Dsly5z3HMHONEMOVIE/index.m3u8
- MH One Movies — Backup — https://fta.ektv.in/live/639/master.m3u8
### mksix.in (2 streams)
- MK Six — Indian Entertainment — https://mumt06.tangotv.in/qYyB8fXVMKSIX/index.m3u8
- MK Six — Backup — https://cdn.pishow.tv/ott/live/1253/master.m3u8
### mohonatv.bd (3 streams)
- Mohona TV — Bangladesh — https://tvsen6.aynaott.com/AkyX5dunzju4cpo26dr7/tracks-v1a1/mono.ts.m3u8
- Mohona TV — Backup — https://playztv-apps.pages.dev/mohona-tv/index.m3u8
- Mohona TV — Review — https://stream.ottplus.live/live/mohona_tv_abr/index.m3u8
### montvbangla.in (2 streams)
- Mon Bangla — Indian Bangla — http://115.187.41.216:8080/hls/montvbangla/index.m3u8
- Mon Bangla — Backup — http://115.187.41.216:8080/hls/montvbangla/2_1/index.m3u8
### moviebangla.bd (4 streams)
- Movie Bangla — Bangladesh — http://alvetv.com/moviebanglatv/8080/index.m3u8
- Movie Bangla — Backup — https://iptvlive.ahmed-bd-org.workers.dev/movie-bangla-1/index.m3u8
- Movie Bangla — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/moviebanglalink2.stream/tracks-v1a1/mono.m3u8
- Movie Bangla — Review — https://stream.ottplus.live/live/movie_bangla_abr/index.m3u8
### moviepunjab.in@sd (2 streams)
- Movie Punjab — Indian Movies — https://samitaorigin.tangotv.in/MOVIEPUNJAB/SAMITAORIGIN/index.m3u8
- Movie Punjab — Backup — https://mumt01.tangotv.in/O5aw8Zn3MOVIEPUNJAB/index.m3u8
### moviesnow.in@hd (2 streams)
- Movies Now — Review — http://27.124.71.27/Movies_Now/index.m3u8
- Movies Now — Review — http://116.90.120.149:8000/play/a11f/index.m3u8
### mtv.in@sd (3 streams)
- MTV India — Indian Music — https://tvsen6.aynaott.com/mtv/index.m3u8
- MTV (India) — Review — https://da86m1sqpm3o0.cloudfront.net/28072023/smil:mtvindia.smil/playlist.m3u8
- MTV India — Review — https://yupp-music.keralive.workers.dev/out/v1/a797c00cba954265ba781f92a57e2cf5/index.m3u8
### musicindia.in@sd (4 streams)
- Music India — Indian Music — https://streams.tangotv.in/MUSICINDIA/ORIGIN/index.m3u8
- Music India — Backup — https://cdn.pishow.tv/ott/live/226/master.m3u8
- Music India — Backup — https://fta.ektv.in/live/158/master.m3u8
- Music India — Backup — https://mumt05.tangotv.in/87NeALx2MUSICINDIA/index.m3u8
### mytv.bd (4 streams)
- My TV — Bangladesh — https://tvsen6.aynaott.com/XMpHaEf0ANBhv8w6NWR7/index.m3u8
- My TV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/mytv-up-off.stream/index.m3u8
- My TV — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/mytv-up-off.stream/live-orgin/mytv-up-off.stream/playlist.m3u8
- My TV — Review — http://116.204.149.16/mytv/index.m3u8
### nagoriktv.bd (2 streams)
- Nagorik TV — Bangladesh — https://box.bbaria.net:8083/Nagorik_TV/video.m3u8
- Nagorik TV — Backup — https://box.bbaria.net/Nagorik_TV/tracks-v1a1/mono.m3u8
### natgeotv.us (3 streams)
- Nat Geo TV — Documentary & Wildlife — http://iptv.prosto.tv:7000/ch83/video.m3u8
- Nat Geo TV — Review — http://103.135.253.32:8080/NATGEO-HD/index.m3u8
- Nat Geo TV — Review — https://tvsen3.aynaott.com/7mm4pwCy/index.m3u8
### nepal1.in@sd (2 streams)
- Nepal 1 — Indian Entertainment — https://mumt05.tangotv.in/87NeALx2NEPAL1/index.m3u8
- Nepal 1 — Backup — https://cdn.pishow.tv/ott/live/1490/master.m3u8
### news24.bd (3 streams)
- News 24 — Bangladesh — https://tvsen6.aynaott.com/cdgr3tw6WoG7JyRnLbi0/index.m3u8
- News 24 — Backup — https://amg13643-amg13643c1-amgplt0016.playout.now3.amagi.tv/ts-eu-w1-n2/playlist/amg13643-amg13643c1-amgplt0016/playlist.m3u8
- News 24 — Backup — https://iptvlive.ahmed-bd-org.workers.dev/news-24-hd-1/index.m3u8
### nexustv.bd (2 streams)
- Nexus TV — Bangladesh — https://tvsen6.aynaott.com/Epm7WrFa/index.m3u8
- Nexus TV — Review — https://stream.ottplus.live/live/nexus_tv_abr/index.m3u8
### nhbollyflix.in (4 streams)
- NH BollyFlix — Indian Movies — https://cc-r5hupcym5oehh.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-r5hupcym5oehh/SBUM/RunnTV/BollyFlix_IN/BollyFlix_IN.m3u8
- NH BollyFlix — Backup — https://cc-r5hupcym5oehh.akamaized.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-r5hupcym5oehh/d47d1910-8862-4b83-a8a6-00ac11307859/0.m3u8
- NH BollyFlix — Backup — https://cc-r5hupcym5oehh.akamaized.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-r5hupcym5oehh/ece6e311-8eb0-4fdf-8378-d337cba07ec2/0.m3u8
- NH BollyFlix — Backup — https://jmp2.uk/stvp-IN46000140Q
### nhbollyraga.in (3 streams)
- NH BollyRaga — Indian Music — https://cc-up9j649x4thrj.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-up9j649x4thrj/SBUM/RunnTV/BollyRaga_IN/BollyRaga_IN.m3u8
- NH BollyRaga — Backup — https://cc-up9j649x4thrj.akamaized.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-up9j649x4thrj/f935ee75-bf1b-4bf6-a30c-1f096a0083c5/0.m3u8
- NH BollyRaga — Backup — https://jmp2.uk/stvp-IN460001373
### nrbtv.ca (2 streams)
- NRB TV — Bangladesh — https://app.ncare.live/live-orgin/nrb-eu.stream/playlist.m3u8
- NRB TV — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/nrb-eu.stream/playlist.m3u8
### ntv.bd (3 streams)
- NTV — Bangladesh — https://tvsen5.aynaott.com/xV4jEKf3D9zc/index.m3u8
- NTV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/ntv-1/index.m3u8
- NTV — Backup — https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8
### ntveurope.bd (2 streams)
- NTV Europe — Bangladesh — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/ntvuk00332211.stream/playlist.m3u8
- NTV Europe — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/ntvuk00332211.stream/live-orgin/ntvuk00332211.stream/chunks.m3u8
### olitv.in@sd (2 streams)
- Oli TV — Indian Music — https://live.olidigital.in/olitv/olitv/index.m3u8
- Oli TV — Backup — https://hlslive.olidigital.in/olitv/olitv/index.m3u8
### oscarmoviesbhojpuri.in@sd (3 streams)
- Oscar Movies Bhojpuri — Indian Movies — https://mumt05.tangotv.in/87NeALx2OSCARMOVIESBHOJPURI/index.m3u8
- Oscar Movies Bhojpuri — Backup — https://fta.ektv.in/live/348/master.m3u8
- Oscar Movies Bhojpuri — Backup — https://cdn.pishow.tv/ott/live/233/master.m3u8
### pasandtv.in@sd (2 streams)
- Pasand TV — Indian Entertainment — https://d1msejlow1t3l4.cloudfront.net/fta/pasand/playlist.m3u8
- Pasand TV — Backup — https://mumt01.tangotv.in/O5aw8Zn3PASANDTV/index.m3u8
### peacetvbangla.ae (2 streams)
- Peace TV Bangla — Religious — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/peacetvban.stream/index.m3u8
- Peace TV Bangla — Backup — https://dzkyvlfyge.erbvr.com/PeaceTvBangla/index.m3u8
### peartv.in@sd (2 streams)
- Pear TV — Indian Entertainment — https://mumt01.tangotv.in/O5aw8Zn3PEARTV/index.m3u8
- Pear TV — Backup — https://fta.ektv.in/live/695/master.m3u8
### pitaara.in@sd (8 streams)
- Pitaara — Indian Movies — https://d2lk5u59tns74c.cloudfront.net/out/v1/500a6b45f5ae41dda445d912b59eaa09/index.m3u8
- Pitaara — Backup — https://d3i5c1nmken8bh.cloudfront.net/Live/Pitaara_TV_SCTE/playlist.m3u8
- Pitaara — Backup — https://fta.ektv.in/live/352/master.m3u8
- Pitaara — Backup — https://mumt04.tangotv.in/m18aqlK4PITAARA/index.m3u8
- Pitaara — Backup — https://pitaara-lg.vgcdn.net/v1/vglive-sk-326599/playlist.m3u8
- Pitaara — Backup — https://d2lk5u59tns74c.cloudfront.net/out/v1/500a6b45f5ae41dda445d912b59eaa09/index_5.m3u8
- Pitaara — Backup — https://streams.tangotv.in/PITAARA/ORIGIN/index.m3u8
- Pitaara — Backup — https://vg-pitaaratvlive.akamaized.net/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/vglive-sk-583798/playlist.m3u8
### pitaaracomedy.in@sd (4 streams)
- Pitaara Comedy — Indian Entertainment — https://vglivessai.akamaized.net/ptnr-lgtv/title-Pitaara_Comedy_LG/sg/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/5a5410c0-1b79-4adc-9243-0139b249798b/playlist.m3u8
- Pitaara Comedy — Backup — https://janya-pitaaralive.akamaized.net/ptnr-monitoring/v1/vglive-sk-217489/live/PitaaraComedy_15/chunks.m3u8
- Pitaara Comedy — Backup — https://pitaara-lg.vgcdn.net/v1/vglive-sk-217489/playlist.m3u8
- Pitaara Comedy — Backup — https://vg-pitaaratvyupp.akamaized.net/ptnr-yupptv/title-Pitaara_Comedy/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/vglive-sk-343626/playlist.m3u8
### pocketfilms.in (2 streams)
- Pocket Films — Indian Movies — https://vglivessai.akamaized.net/sg/v1/manifest/611d79b11b77e2f571934fd80ca1413453772ac7/b8ada260-bb81-472b-b7c1-3a79213a84b8/e02a0ce5-6c42-4cca-bb53-e5cfecff74a9/0.m3u8
- Pocket Films — Backup — https://vglivessai.akamaized.net/sg/v1/manifest/611d79b11b77e2f571934fd80ca1413453772ac7/b8ada260-bb81-472b-b7c1-3a79213a84b8/6408f97591ee7861ab0d4839eefdbbee/0.m3u8
### polimertv.in@sd (3 streams)
- Polimer TV — Indian Entertainment — https://cdn.pishow.tv/ott/live/1241/master.m3u8
- Polimer TV — Backup — https://mumt04.tangotv.in/m18aqlK4POLIMERTV/index.m3u8
- Polimer TV — Backup — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/in/YuppTV/PolimerTV.m3u8
### ptcchakde.in@sd (2 streams)
- PTC Chakde — Indian Music — https://cdn.pishow.tv/ott/live/449/master.m3u8
- PTC Chakde — Backup — https://mumt06.tangotv.in/qYyB8fXVPTCCHAKDE/index.m3u8
### ptcmusic.in@sd (5 streams)
- PTC Music — Indian Music — https://d2lk5u59tns74c.cloudfront.net/out/v1/f913cf893c594f73b114216e74a2efbc/index.m3u8
- PTC Music — Backup — https://fta.ektv.in/live/181/master.m3u8
- PTC Music — Backup — https://iptvlive.ahmed-bd-org.workers.dev/ptc-music-1/index.m3u8
- PTC Music — Backup — https://mumt04.tangotv.in/m18aqlK4PTCMUSIC/index.m3u8
- PTC Music — Review — https://cdn.pishow.tv/ott/live/1501/master.m3u8
### ptcpunjabi.in@sd (4 streams)
- PTC Punjabi — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/3e22a9c278db4e3eb779afd42e41b0a6/index.m3u8
- PTC Punjabi — Backup — https://cdn.pishow.tv/ott/live/1604/master.m3u8
- PTC Punjabi — Backup — https://mumt04.tangotv.in/m18aqlK4PTCPUNJABI/index.m3u8
- PTC Punjabi — Backup — https://streams.tangotv.in/PTCPUNJABI/ORIGIN/index.m3u8
### ptcpunjabigold.in@sd (3 streams)
- PTC Punjabi Gold — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/6e14bac6d0384e129521a4d005188bfb/index.m3u8
- PTC Punjabi Gold — Backup — https://mumt04.tangotv.in/m18aqlK4PTCPUNJABIGOLD/index.m3u8
- PTC Punjabi Gold — Backup — https://streams.tangotv.in/PTCPUNJABIGOLD/ORIGIN/index.m3u8
### ptvsports.pk (2 streams)
- PTV Sports — Sports — https://tvsen5.aynaott.com/kP9vX2mZ7qL5wN3t/index.m3u8
- PTV Sports — Review — http://103.135.253.32:8080/PTV-SPORTS/tracks-v1a1/mono.m3u8
### publicmovies.in@sd (2 streams)
- Public Movies — Indian Movies — https://mumt04.tangotv.in/m18aqlK4PUBLICMOVIES/index.m3u8
- Public Movies — Backup — https://fta.ektv.in/live/239/master.m3u8
### publicmusic.in@sd (3 streams)
- Public Music — Indian Music — https://mumt04.tangotv.in/m18aqlK4PUBLICMUSIC/index.m3u8
- Public Music — Backup — https://cdn.pishow.tv/ott/live/441/master.m3u8
- Public Music — Backup — https://fta.ektv.in/live/240/master.m3u8
### pularitv.in@sd (2 streams)
- Pulari TV — Indian Entertainment — https://mumbai-edge.smartplaytv.in/PulariTV/index.m3u8
- Pulari TV — Backup — https://royalstarindia.co.in/pularitv_hls/pularitv.m3u8
### punjabihits.in (3 streams)
- Punjabi Hits — Indian Music — https://stream.ottlive.co.in/punjabihits/index.m3u8
- Punjabi Hits — Backup — https://legitpro.co.in/punjabihits/punjabihits/index.m3u8
- Punjabi Hits — Backup — https://livingindiaottlive.akamaized.net/punjabihits/index.m3u8
### punjabishorts.in (2 streams)
- Punjabi Shorts — Indian Entertainment — https://vglivessai.akamaized.net/ptnr-yupptv/title-Punjabi_Shorts/in/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/27c3fd7a-b01f-4b00-ac03-557ac77acd47/index.m3u8
- Punjabi Shorts — Backup — https://gtc.ottlive.co.in/punjabshort/index.m3u8
### punjabitv.in@sd (2 streams)
- Punjabi TV — Indian Music — https://samitaorigin.tangotv.in/PUNJABITV/SAMITAORIGIN/index.m3u8
- Punjabi TV — Backup — https://mumt07.tangotv.in/zHjX9OFlPUNJABITV/index.m3u8
### qtv.in (4 streams)
- Q TV — Indian Entertainment — https://fta.ektv.in/live/25/master.m3u8
- Q TV — Backup — http://163.61.226.31:9981/stream/channelid/359164420?profile=pass
- Q TV — Backup — https://mumt05.tangotv.in/87NeALx2THEQ/index.m3u8
- Q TV — Backup — https://samitaorigin.tangotv.in/THEQ/SAMITAORIGIN/index.m3u8
### qurantv.iq (2 streams)
- Quran TV — Religious — https://live.kwikmotion.com/sharjahtvquranlive/shqurantv.smil/sharjahtvquranpublish/shqurantv_source/chunks.m3u8
- Quran TV — Backup — https://live.kwikmotion.com/sharjahtvquranlive/shqurantv.smil/playlist.m3u8
### rajdhanitv.bd (3 streams)
- Rajdhani TV — Bangladesh — https://stream.shariarsuvo.com/hls5/rajdhanicable.m3u8
- Rajdhani TV — Backup — https://stream.shariarsuvo.com/hls6/rajdhaniweb.m3u8
- Rajdhani TV — Review — https://drk6xq0vhn.gpcdn.net/live/rajdhani_tv/index.m3u8
### rajmusixkannada.in@sd (2 streams)
- Raj Musix Kannada — Indian Music — https://mumt01.tangotv.in/O5aw8Zn3RAJMUSIXKANDA/index.m3u8
- Raj Musix Kannada — Backup — https://samitaorigin.tangotv.in/RAJMUSIXKANDA/SAMITAORIGIN/index.m3u8
### rajmusixmalayalam.in@sd (2 streams)
- Raj Musix Malayalam — Indian Music — https://cdn.pishow.tv/ott/live/1073/master.m3u8
- Raj Musix Malayalam — Backup — https://mumt04.tangotv.in/m18aqlK4RAJMUSIXMALAYALAM/index.m3u8
### rajmusixtelugu.in@sd (2 streams)
- Raj Musix Telugu — Indian Music — https://cdn.pishow.tv/ott/live/1213/master.m3u8
- Raj Musix Telugu — Backup — https://mumt07.tangotv.in/zHjX9OFlRAJMUSIXTELUGU/index.m3u8
### rajtv.in@sd (2 streams)
- Raj TV — Indian Entertainment — https://livestream.rajtv.tv/hlslive/Admin/px08241087/live/RAJTV/master_1.m3u8
- Raj TV — Review — https://d3kdywbtdfbp9z.cloudfront.net/v1/manifest/93ce20f0f52760bf38be911ff4c91ed02aa2fd92/dff423e0-3c82-46d6-9ecb-3baa96b5694a/b8640d6b-d131-4401-9451-944e1e65fe79/0.m3u8
### ramdhenu.in@sd (2 streams)
- Ramdhenu — Indian Music — https://mumt01.tangotv.in/O5aw8Zn3RAMDHENU/mpegts
- Ramdhenu — Backup — https://mumt01.tangotv.in/O5aw8Zn3RAMDHENU/index.m3u8
### rengoni.in@sd (4 streams)
- Rengoni — Indian Entertainment — https://d1msejlow1t3l4.cloudfront.net/fta/rengonitv/playlist.m3u8
- Rengoni — Backup — https://mumt05.tangotv.in/87NeALx2RENGONI/index.m3u8
- Rengoni — Backup — https://streams.tangotv.in/RENGONI/ORIGIN/index.m3u8
- Rengoni — Backup — https://fta.ektv.in/live/709/master.m3u8
### rongeentv.in@sd (6 streams)
- Rongeen TV — Indian Bangla — https://server.thelegitpro.in/rongeentv/rongeentv/index.m3u8
- Rongeen TV — Backup — https://fta.ektv.in/live/202/master.m3u8
- Rongeen TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/rongeen-tv-1/index.m3u8
- Rongeen TV — Backup — https://mumbai-edge.smartplaytv.in/RongeenTV/index.m3u8
- Rongeen TV — Backup — https://mumt05.tangotv.in/87NeALx2RONGEENTV/index.m3u8
- Rongeen TV — Backup — https://stream.ottlive.co.in/rongeentv/index.m3u8
### rplusgold.in@sd (5 streams)
- R Plus Gold — Indian Bangla — https://vglivessai.akamaized.net/sg/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/cf883da3-f9f5-4c70-b0ef-b3ac2e2ad1e3/index.m3u8
- R Plus Gold — Backup — https://cdn.pishow.tv/ott/live/1231/master.m3u8
- R Plus Gold — Backup — https://stream.ottlive.co.in/rplusgold/index.m3u8
- R Plus Gold — Backup — https://thelegitpro.in/pntv/rplusnews24x7/tracks-v1a1/mono.m3u8
- R Plus Gold — Backup — https://vglivessai.akamaized.net/sg/v1/manifest/611d79b11b77e2f571934fd80ca1413453772ac7/cf883da3-f9f5-4c70-b0ef-b3ac2e2ad1e3/5552ef1c-ee8a-4743-8321-08b260d3b1f3/0.m3u8
### rtv.bd (8 streams)
- RTV — Bangladesh — https://tvsen5.aynaott.com/RtvHD/index.m3u8
- RTV — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/rtv-sg.stream/index.m3u8
- RTV — Backup — https://j6nfugukcl.gpcdn.net/tile_6/master.m3u8
- RTV — Backup — https://tvsen5.aynaott.com/ba47dHpDk3Se/index.m3u8
- RTV — Backup — https://tvsen6.aynaott.com/rtv/tracks-v1a1/mono.ts.m3u8
- RTV — Review — http://tvsen5.aynascope.net/RtvHD/index.m3u8
- RTV — Review — http://tvsen5.aynascope.net/RtvHD/tracks-v1a1/mono.ts.m3u8
- RTV — Review — http://116.204.149.16/rtvhd/index.m3u8
### rupasibangla.in@sd (4 streams)
- Ruposhi Bangla — Indian Bangla — https://mumt05.tangotv.in/87NeALx2RUPASIBANGLA/index.m3u8
- Ruposhi Bangla — Backup — http://103.175.73.12:8080/live/664/664_0.m3u8
- Ruposhi Bangla — Backup — https://cdn.pishow.tv/ott/live/1039/master.m3u8
- Ruposhi Bangla — Backup — https://da86m1sqpm3o0.cloudfront.net/28072023/smil:rupashibangla.smil/playlist.m3u8
### safaritv.in@sd (2 streams)
- Safari TV — Documentary & Wildlife — https://mumt04.tangotv.in/m18aqlK4SAFARITV/index.m3u8
- Safari TV — Backup — https://fta.ektv.in/live/410/master.m3u8
### sanandatv.in (4 streams)
- Sananda — Indian Bangla — http://27.124.71.27/Sun_Bangla/index.m3u8
- Sananda — Backup — https://iptvlive.ahmed-bd-org.workers.dev/sananda-tv-1/index.m3u8
- Sananda — Backup — http://115.187.41.216:8080/hls/sanandatv/index.m3u8
- Sananda — Review — https://live.sanandatelevision.in/sananda/index.m3u8
### sanaplus.in@sd (2 streams)
- Sana Plus — Indian Music — https://mumbai-edge.smartplaytv.in/SanaPlusHD/index.m3u8
- Sana Plus — Backup — https://galaxyott.live/hls/sanaplus.m3u8
### sangeetbangla.in@sd (5 streams)
- Sangeet Bangla — Indian Bangla — https://mumt05.tangotv.in/87NeALx2SANGEETBANGLA/index.m3u8
- Sangeet Bangla — Indian Bangla — http://103.175.73.12:8080/live/379/379_0.m3u8
- Sangeet Bangla — Indian Bangla — https://cdn.pishow.tv/ott/live/1143/master.m3u8
- Sangeet Bangla — Indian Bangla — https://fta.ektv.in/live/379/master.m3u8
- Sangeet Bangla — Indian Bangla — https://tvsen6.aynaott.com/hT5jHczt/index.m3u8
### sangeetbhojpuri.in@sd (3 streams)
- Sangeet Bhojpuri — Indian Music — https://cdn.pishow.tv/ott/live/1293/master.m3u8
- Sangeet Bhojpuri — Backup — https://mumt01.tangotv.in/O5aw8Zn3SANGEETBHOJPURI/index.m3u8
- Sangeet Bhojpuri — Backup — https://fta.ektv.in/live/349/master.m3u8
### sangeetmarathi.in@sd (3 streams)
- Sangeet Marathi — Indian Music — https://cdn.pishow.tv/ott/live/1229/master.m3u8
- Sangeet Marathi — Backup — https://fta.ektv.in/live/712/master.m3u8
- Sangeet Marathi — Backup — https://mumt07.tangotv.in/zHjX9OFlSANGEETMARATHI/index.m3u8
### satv.bd (5 streams)
- SA TV — Bangladesh — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/satvoff5666.stream/playlist.m3u8
- SA TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/sa-tv-1/index.m3u8
- SA TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/sa-tv-2/index.m3u8
- SA TV — Backup — https://tvsen6.aynaott.com/rELXiuUXqbgzPb06Npom/index.m3u8
- SA TV — Review — http://116.204.149.16/satv/index.m3u8
### shansontv.ru (2 streams)
- Shanson TV — International — https://streaming.thestream.cyou/live/7009.m3u8
- Shanson TV — Backup — http://hls-shansontv.cdnvideo.ru/shansontv/shansontv-sd.smil/playlist.m3u8
### shemaroobollywood.us (2 streams)
- Shemaroo Bollywood — Review — https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg00864-shemarooenterta-shemabollywood-ono/playlist.m3u8
- Shemaroo Bollywood — Review — https://amg00864-shemarooenterta-shemabollywood-ono-nlwbw.amagi.tv/playlist/amg00864-shemarooenterta-shemabollywood-ono/playlist.m3u8
### shemaroojosh.in@sd (4 streams)
- Shemaroo Josh — Indian Movies — https://airtelapp.shemaroo.com/shemarooChumbakTV/smil:shemarooChumbakTVadp.smil/playlist.m3u8
- Shemaroo Josh — Backup — https://cdn.pishow.tv/ott/live/337/master.m3u8
- Shemaroo Josh — Backup — https://fta.ektv.in/live/21/master.m3u8
- Shemaroo Josh — Backup — https://mumt04.tangotv.in/m18aqlK4SHEMAROOJOSH/index.m3u8
### shemarootv.in@sd (5 streams)
- Shemaroo TV — Indian Entertainment — https://cdn.pishow.tv/ott/live/230/master.m3u8
- Shemaroo TV — Backup — https://fta.ektv.in/live/274/master.m3u8
- Shemaroo TV — Backup — https://mumt06.tangotv.in/qYyB8fXVSHEMAROOTV/index.m3u8
- Shemaroo TV — Backup — https://streams.tangotv.in/SHEMAROOTV/ORIGIN/index.m3u8
- Shemaroo TV — Backup — https://airtelapp.shemaroo.com/shemarootv/smil:shemarootvadp.smil/playlist.m3u8
### shemarooumang.in@sd (4 streams)
- Shemaroo Umang — Indian Entertainment — https://airtelapp.shemaroo.com/shemarooumang/smil:shemarooumangadp.smil/playlist.m3u8
- Shemaroo Umang — Backup — https://fta.ektv.in/live/258/master.m3u8
- Shemaroo Umang — Backup — https://mumt04.tangotv.in/m18aqlK4SHEMAROOUMANG/index.m3u8
- Shemaroo Umang — Backup — https://streams.tangotv.in/SHEMAROOUMANG/ORIGIN/index.m3u8
### shubhcinematv.in (4 streams)
- Shubh Cinema TV — Indian Movies — https://d393sxaxig6bax.cloudfront.net/out/v1/589cf2cf44bf42bb941e817a2240d62e/index.m3u8
- Shubh Cinema TV — Backup — https://d393sxaxig6bax.cloudfront.net/out/v1/589cf2cf44bf42bb941e817a2240d62e/index_8.m3u8
- Shubh Cinema TV — Backup — https://fta.ektv.in/live/49/49_0.m3u8
- Shubh Cinema TV — Backup — https://mumt03.tangotv.in/Dsly5z3HSHUBHCINEMA/index.m3u8
### somoynewstv.bd (5 streams)
- Somoy TV — Bangladesh — https://tvsen6.aynaott.com/4XcqdovJzbbC9WdJA9gk/index.m3u8
- Somoy TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/somoy-tv-2/index.m3u8
- Somoy TV — Backup — https://tvsen5.aynaott.com/somoytv/tracks-v1a1/mono.m3u8
- Somoy TV — Review — http://116.204.149.16/somoytv/index.m3u8
- Somoy TV — Review — https://drk6xq0vhn.gpcdn.net/live/somoy_tv_abr/index.m3u8
### sonyaath.in@sd (4 streams)
- Sony Aath — Indian Bangla — http://27.124.71.27/Sony_Aath/index.m3u8
- Sony Aath — Review — http://103.165.93.31:8095/sonyAath/index.m3u8
- Sony Aath — Review — https://drk6xq0vhn.gpcdn.net/live/sony_aath_abr/index.m3u8
- Sony Aath — Review — https://stream.ottplus.live/live/sony_aath_abr/index.m3u8
### sonyentertainmenttelevision.in@hd (2 streams)
- Sony Entertainment TV — Indian Entertainment — http://38.96.178.205/SONYHD/index.m3u8
- Sony Entertainment TV — Review — http://103.135.253.32:8080/SONY-ENTARTANMEN/index.m3u8
### sonykalhindi.us (2 streams)
- Sony KAL — Indian Entertainment — https://wurlsonypicturestv.global.transmit.live/hls/68deeb1c0238cda82df543dd/v1/spt_sonykal_1/lg_us/latest/main/hls/playlist.m3u8
- Sony KAL — Backup — https://e77bef9b.wurl.com/master/f36d25e7e52f1ba8d7e56eb859c636563214f541/TEctY2FfU29ueUtBTF9ITFM/playlist.m3u8
### sonymax.in@sd (2 streams)
- Sony Max — Indian Movies — https://drk6xq0vhn.gpcdn.net/hls/set_max_m4fb8dz2wp6kr9s_720/index.m3u8
- Sony Max — Review — http://103.135.253.32:8080/Sony-Max-HD/index.m3u8
### sonypal.in@sd (2 streams)
- Sony Pal — Indian Entertainment — http://163.61.226.31:9981/stream/channelid/1571254341?profile=pass
- Sony Pal — Review — http://59.103.38.46:8000/play/a0ac/index.m3u8
### sonysab.in@hd (2 streams)
- Sony SAB HD — Review — https://drk6xq0vhn.gpcdn.net/live/sub_hd_abr/index.m3u8
- Sony SAB HD — Review — http://116.90.120.149:8000/play/a128/index.m3u8
### southstation.in (2 streams)
- South Station — Indian Movies — https://cc-yw7ztecy8do3q.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-yw7ztecy8do3q/SS_IN.m3u8
- South Station — Backup — https://jmp2.uk/stvp-IN3800008CX
### spondon.in@sd (3 streams)
- Spondon — Indian Entertainment — https://mumt05.tangotv.in/87NeALx2SPONDON/index.m3u8
- Spondon — Backup — https://indianews-yupptv.vgcdn.net/vglive-sk-926943/index.m3u8
- Spondon — Review — https://nktv.smartstream.video/smartstream-us/spondon/spondon/playlist.m3u8
### srk.bd (2 streams)
- SRK — Bangladesh — https://srknowapp.ncare.live/srktvhlswodrm/srktv.stream/playlist.m3u8
- SRK — Backup — https://srktv.net/srktvhls/cdnlive_srktv.m3u8
### stargold.in@hd (3 streams)
- Star Gold HD — Review — http://103.135.253.32:8080/STAR-GOLD-HD/index.m3u8
- Star Gold HD — Review — http://103.185.24.134:3001/Star-Gold/index.m3u8
- Star Gold HD — Review — http://116.90.120.149:8000/play/a12a/index.m3u8
### stargoldselect.in@hd (2 streams)
- Star Gold Select HD — Review — https://livetv.shamon-cable.net:8443/StarGoldSelect/index.m3u8
- Star Gold Select HD — Review — http://116.90.120.149:8000/play/a131/index.m3u8
### starjalsha.in@hd (4 streams)
- Star Jalsha — Indian Bangla — https://da86m1sqpm3o0.cloudfront.net/28072023/smil:starjalsha.smil/chunklist_b1928000.m3u8
- Star Jalsha — Backup — http://cdn98.com/play/live.php?extension=ts&mac=00:1A:79:99:54:11&play_token=o1cczsG9wV&stream=225805
- Star Jalsha — Review — http://103.135.253.32:8080/STAR-JALSHA-HD/index.m3u8
- Star Jalsha — Review — https://livetv.shamon-cable.net:8443/Star-Jalsha/index.m3u8
### starmoviesselect.in@hd (2 streams)
- Star Movies Select HD — Review — http://103.135.253.32:8080/STAR-MOVIES-SEL/index.m3u8
- Star Movies Select HD — Review — http://116.90.120.149:8000/play/a139/index.m3u8
### starnews.bd (2 streams)
- Star News — Bangladesh — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/starnewsbd.stream/playlist.m3u8
- Star News — Review — http://103.135.253.32:8080/Star-News/index.m3u8
### starplus.in@hd (3 streams)
- Star Plus — Indian Entertainment — http://38.96.178.205/STARPLUS/index.m3u8
- Star Plus — Review — http://103.135.253.32:8080/STAR-PLUS/index.m3u8
- Star Plus — Review — http://66.102.126.10:8000/play/a008/index.m3u8
### starsports1.in@hd (2 streams)
- Star Sports 1 HD — Sports — http://103.114.11.37:8081/Star-sports-1/index.m3u8?token=[REDACTED]
- Star Sports 1 HD — Review — http://116.90.120.149:8000/play/a11x/index.m3u8
### starsports1hindi.in@hd (2 streams)
- Star Sports 1 Hindi — Sports — https://starsportshindiii.pages.dev/index.m3u8
- Star Sports 1 Hindi — Review — http://116.90.120.149:8000/play/a122/index.m3u8
### starsportsselect1.in@sd (2 streams)
- Star Sports Select 1 — Sports — http://103.114.11.37:8081/Star-select-1/index.m3u8?token=[REDACTED]
- Star Sports Select 1 — Review — http://103.135.253.32:8080/STAR-SPORTS-SELECT-1/index.m3u8
### starsportsselect2.in@sd (2 streams)
- Star Sports Select 2 — Sports — http://103.114.11.37:8081/Star-select-2/index.m3u8?token=[REDACTED]
- Star Sports Select 2 — Review — http://tvsen7.aynascope.net/ssport2hd/index.m3u8
### studiooneplus.in@sd (2 streams)
- Studio One+ — Indian Movies — https://cdn.pishow.tv/ott/live/276/master.m3u8
- Studio One+ — Backup — https://mumt04.tangotv.in/m18aqlK4STUDIOONEPLUS/index.m3u8
### studioyuva.in (2 streams)
- Studio Yuva — Indian Entertainment — https://mumt01.tangotv.in/O5aw8Zn3STUDIOYUVA/index.m3u8
- Studio Yuva — Backup — https://d2gvyg6lvauoko.cloudfront.net/230226/studioyuva/playlist.m3u8?hdnts=[REDACTED]
### suriyantv.in@sd (2 streams)
- Suriyan TV — Indian Entertainment — https://stream.ottlive.co.in/suriyantvtamil/index.m3u8
- Suriyan TV — Backup — https://hlslive.olidigital.in/suriyantv/suriyantv/index.m3u8
### tabbarhits.in (3 streams)
- Tabbar Hits — Indian Movies — https://vglivessai.akamaized.net/sg/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/e11b0319-52e8-4190-ab03-3931cc68eac9/index.m3u8
- Tabbar Hits — Backup — https://livingindiaottlive.akamaized.net/tabbarhits/index.m3u8
- Tabbar Hits — Backup — https://server.thelegitpro.in/tabbarhits/tabbarhits/index.m3u8
### thalaatv.in@hd (2 streams)
- Thalaa TV — Indian Movies — https://streams2.sofast.tv/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/2069c593-3c07-4d62-9d44-746be5c3a5d6/manifest.m3u8
- Thalaa TV — Backup — https://streams2.sofast.tv/ptnr-khabriya/title-THALAA-TV-TAM_Khabriya/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/c9d5c8a0-8c52-47bc-954d-e64a11314de2/manifest.m3u8
### thanthione.in (2 streams)
- Thanthi One — Indian Entertainment — https://mumt07.tangotv.in/zHjX9OFlTHANTHIONE/index.m3u8
- Thanthi One — Review — https://mumbai-edge.smartplaytv.in/thanthione/index.m3u8
### themovieclub.in@hd (2 streams)
- The Movie Club — Indian Movies — https://sis-global.prod.samsungtv.plus/v1/tvpprd/sc-mp2ar4ca425xo.m3u8
- The Movie Club — Backup — https://mumbai-edge.smartplaytv.in/TheMovieClub/index.m3u8
### thikanatv.us (2 streams)
- Thikana TV — Bangladesh — https://5dd3981940faa.streamlock.net/thikanatv/thikanatv/playlist.m3u8
- Thikana TV — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/thikanatv.stream/tracks-v1a1/mono.m3u8
### tollytv.in (2 streams)
- Tolly TV — Indian Movies — https://streams2.sofast.tv/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/13b5735d-52c3-4be0-853d-e0ec0127e708/manifest.m3u8
- Tolly TV — Backup — https://streams2.sofast.tv/ptnr-khabriya/title-TOLLY-TV-TEL_Khabriya/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/9bb55dff-7a74-43aa-bcf7-ea537e8b9e92/manifest.m3u8
### tsports.bd (2 streams)
- T Sports — Review — http://103.135.253.32:8080/T-SPORTS-FULL-HD/tracks-v1a1/mono.m3u8
- T Sports — Review — https://tvsen5.aynaott.com/TnMn5kZz8aLmjklkk/index.m3u8
### tunes6.in (2 streams)
- Tunes 6 — Indian Music — https://stream.d6-pro.com/tunes6music/live/video.m3u8
- Tunes 6 — Backup — https://stream.d6-pro.com/Tunes6music/live/video.m3u8
### turkmenistansport.tm@sd (2 streams)
- Türkmenistan Sport — Sports — https://alpha.tv.online.tm/hls/ch004.m3u8
- Türkmenistan Sport — Backup — http://217.174.225.146/hls/ch004_720/index.m3u8
### ultimatetv.in@sd (2 streams)
- Ultimate TV — Indian Music — https://stream.ottlive.co.in/utvtamil/index.m3u8
- Ultimate TV — Backup — https://mumbai-edge.smartplaytv.in/utv/index.m3u8
### utvpalakkad.in@sd (2 streams)
- UTV Palakkad — Indian Entertainment — https://em4qj6nedyvg-hls-live.wmncdn.net/utv/ab2de115318ae40bdd434e193a2f2e7f.sdp/playlist.m3u8
- UTV Palakkad — Backup — https://em4qj6nedyvg-hls-live.wmncdn.net/liveunit/89b1e919eed04e59383cf820d644c20e.sdp/playlist.m3u8
### vaanaviltv.in@sd (2 streams)
- Vaanavil TV — Indian Entertainment — https://6n3yope4d9ok-hls-live.5centscdn.com/vaanavil/TV.stream/playlist.m3u8
- Vaanavil TV — Backup — https://mumt01.tangotv.in/O5aw8Zn3VAANAVILTV/index.m3u8
### vanithatv.in@sd (2 streams)
- Vanitha TV — Indian Entertainment — https://cdn.pishow.tv/ott/live/393/master.m3u8
- Vanitha TV — Backup — https://mumt01.tangotv.in/O5aw8Zn3VANITHA/index.m3u8
### vasanthtv.in@sd (2 streams)
- Vasanth TV — Indian Entertainment — https://mumt04.tangotv.in/m18aqlK4VASANTHTV/index.m3u8
- Vasanth TV — Backup — https://fta.ektv.in/live/228/master.m3u8
### vendhartv.in@sd (4 streams)
- Vendhar TV — Indian Entertainment — https://mumt04.tangotv.in/m18aqlK4VENDHARTV/index.m3u8
- Vendhar TV — Backup — https://cdn.pishow.tv/ott/live/1271/master.m3u8
- Vendhar TV — Backup — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/in/YuppTV/VendharTV.m3u8
- Vendhar TV — Backup — https://fta.ektv.in/live/223/master.m3u8
### yrfmusic.in (3 streams)
- YRF Music — Indian Music — https://amg01412-xiaomiasia-yrfmusic-xiaomi-1rmk2.amagi.tv/playlist/amg01412-xiaomiasia-yrfmusic-xiaomi/playlist.m3u8
- YRF Music — Backup — https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg01412-xiaomiasia-yrfmusic-xiaomi/playlist.m3u8
- YRF Music — Backup — https://vidaa.kableone.com/hls/live/2111218/YrfMusic/1.m3u8
### zeebangla.in@hd (8 streams)
- Zee Bangla — Indian Bangla — https://tvsen6.aynaott.com/ZeeBangla/index.m3u8
- Zee Bangla — Backup — https://d1rc86nwwc9fag.cloudfront.net/260723/smil:zeebangla.smil/chunklist_b896000.m3u8
- Zee Bangla — Backup — https://iptvlive.ahmed-bd-org.workers.dev/zee-bangla-hd-2/index.m3u8
- Zee Bangla — Backup — https://raw.githubusercontent.com/ahan443/vibe-tv/refs/heads/main/ZeeBanglaHD.m3u8
- Zee Bangla — Backup — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/in/YuppTV/ZeeBanglaHD.m3u8
- Zee Bangla — Backup — http://rgkkw.live:80/live/[REDACTED]/[REDACTED]/98881.ts
- Zee Bangla — Review — https://livetv.shamon-cable.net:8443/ZEE-Bangla/index.m3u8
- Zee Bangla — Review — https://drk6xq0vhn.gpcdn.net/live/zee_bangla_720/index.m3u8
### zeebanglasonar.in@sd (2 streams)
- Zee Bangla Sonar — Review — http://103.135.253.32:8080/ZEE-BANGLA-CINEMA/index.m3u8
- Zee Bangla Sonar — Review — http://103.185.24.134:3001/ZEE-BANGLA-CINEMA/index.m3u8
### zeecinema.in@hd (4 streams)
- Zee Cinema — Indian Movies — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/sg/YuppTV/ZeeCinemaAPAC.m3u8
- Zee Cinema — Backup — https://j6nfugukcl.gpcdn.net/tile_5/master.m3u8
- Zee Cinema — Review — http://103.135.253.32:8080/ZEE-CINEMA/index.m3u8
- Zee Cinema — Review — https://drk6xq0vhn.gpcdn.net/live/zee_cinema_hd_abr/index.m3u8
### zeetamil.in@sd (2 streams)
- Zee Tamil — Indian Entertainment — https://da86m1sqpm3o0.cloudfront.net/28072023/smil:zeetamil1.smil/playlist.m3u8
- Zee Tamil — Review — https://d2o8pibksxtln6.cloudfront.net/live/media/Zee_Tamil_HD/hls/Zee_Tamil_HD.m3u8
### zeetelugu.in@hd (2 streams)
- Zee Telugu — Indian Entertainment — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/in/YuppTV/ZeeTeluguHD.m3u8
- Zee Telugu — Backup — https://listas-m3u8.github.io/iptv/128.19.173.10:8888/ZEETELUGUHD.m3u8
### zeetv.in@sd (4 streams)
- Zee TV — Indian Entertainment — https://d47ddb99.wurl.com/master/f36d25e7e52f1ba8d7e56eb859c636563214f541/U2Ftc3VuZy1kZV9aZWVUVkhEVUtHZXJtYW55X0hMUw/playlist.m3u8
- Zee TV — Backup — http://41.205.93.154/ZEE-TV/index.m3u8
- Zee TV — Review — http://103.135.253.32:8080/ZEE-TV/index.m3u8
- Zee TV — Review — https://drk6xq0vhn.gpcdn.net/live/zee_tv_hd_abr/index.m3u8
### zoom.in (5 streams)
- Zoom — Indian Music — https://d2esfk1pb9cdob.cloudfront.net/master.m3u8
- Zoom — Backup — https://dai.google.com/linear/hls/event/JCAm25qkRXiKcK1AJMlvKQ/master.m3u8
- Zoom — Backup — https://mumbai-edge.smartplaytv.in/Zoom/index.m3u8
- Zoom — Backup — https://d2esfk1pb9cdob.cloudfront.net/chunklist_1.m3u8
- Zoom — Review — http://stream.mcquack.net/377/index.m3u8

## Duplicate Primary Identities

- **colorsbanglacinema.in@sd** — Colors Bangla Cinema [Indian Bangla] — http://103.114.11.37:8081/Colors-bangla-cinema/tracks-v1a1/mono.m3u8?token=[REDACTED]; Colors Bangla Cinema [Indian Bangla] — http://103.135.253.32:8080/COLORS-BANGLA-CINEMA/index.m3u8; Colors Bangla Cinema [Indian Bangla] — https://livetv.shamon-cable.net:8443/Colors-bangla-cinema/index.m3u8
- **dhoommusic.in@sd** — Dhoom Music [Indian Bangla] — https://fta.ektv.in/live/378/master.m3u8; Dhoom Music [Indian Bangla] — https://cdn.pishow.tv/ott/live/1456/master.m3u8; Dhoom Music [Indian Bangla] — https://mumt06.tangotv.in/qYyB8fXVDHOOMMUSIC/index.m3u8
- **jalshamovies.in@sd** — Jalsha Movies [Indian Bangla] — https://box.bbaria.net:8083/Jalsha_Movie/tracks-v1a1/mono.m3u8; Jalsha Movies [Indian Bangla] — https://livetv.shamon-cable.net:8443/Jalsha-Movies/index.m3u8
- **sangeetbangla.in@sd** — Sangeet Bangla [Indian Bangla] — https://mumt05.tangotv.in/87NeALx2SANGEETBANGLA/index.m3u8; Sangeet Bangla [Indian Bangla] — http://103.175.73.12:8080/live/379/379_0.m3u8; Sangeet Bangla [Indian Bangla] — https://cdn.pishow.tv/ott/live/1143/master.m3u8; Sangeet Bangla [Indian Bangla] — https://fta.ektv.in/live/379/master.m3u8; Sangeet Bangla [Indian Bangla] — https://tvsen6.aynaott.com/hT5jHczt/index.m3u8

## Potential Near-Duplicate Primary Names (Review Only)

None.

## Primary Channel-Number Collisions

- **426** — FON Music, Fashion&LifeStyle

## Primary Channel-Number Sequence (Review Only)

- **Fashion&LifeStyle** — expected channel number a number above 480, found 426

## Malformed EXTINF Entries

None.

## Ordering

Category block order: OK.
- **Indian Bangla** — **Dhoom Music** appears after **Zee Bangla**
- **Indian Bangla** — **Colors Bangla Cinema** appears after **Sangeet Bangla**
- **Indian Movies** — **Kalaignar Murasu** appears after **Zee Cinema**
- **Indian Music** — **Peppers TV** appears after **Zoom**
- **International** — **Fashion&LifeStyle** appears after **XITE Summer**
Backup/Review/New Channels/New Backups internal order is preserved for manual review and is intentionally not auto-enforced.

## Suspicious URLs

None.

## Unverified Provider Playback Routes (Review Only)

Opaque provider-specific playback paths remain unchanged and require manual source verification.

None.

## Signed / Tokenized Stream URLs

- **Colors Bangla Cinema** — Indian Bangla — http://103.114.11.37:8081/Colors-bangla-cinema/tracks-v1a1/mono.m3u8?token=[REDACTED]
- **ETV Cinema** — Indian Movies — https://yupplivegcpusa.yuppcdn.net/100823/smil:etvcinema.smil/playlist.m3u8?hdnts=[REDACTED]
- **Boogle Bollywood** — Indian Music — https://yuppnimrestreammum.akamaized.net/181224/smil:bogglebollywood.smil/playlist.m3u8?hdnts=[REDACTED]
- **Songdew TV** — Indian Music — https://yuppnimrestreammum.akamaized.net/181224/smil:songdewtv.smil/playlist.m3u8?hdnts=[REDACTED]
- **Wah Punjabi** — Indian Music — https://yuppnimrestreammum.akamaized.net/181224/smil:wahpunjabi.smil/playlist.m3u8?hdnts=[REDACTED]
- **Colors Super** — Indian Entertainment — https://d1rc86nwwc9fag.cloudfront.net/260723/smil:colorssuper1.smil/playlist.m3u8?hdnts=[REDACTED]
- **Zee Kannada** — Indian Entertainment — https://yuppnimresmum.akamaized.net/28072023/smil:zeekannadahd.smil/playlist.m3u8?hdnts=[REDACTED]
- **WOW Kidz Hindi** — Kids — https://yuppparoriglin.akamaized.net/181224/smil:wowkidzhindi.smil/playlist.m3u8?hdnts=[REDACTED]
- **WOW Kidz Tamil** — Kids — https://yuppparoriglin.akamaized.net/181224/smil:wowkidztam.smil/playlist.m3u8?hdnts=[REDACTED]
- **WOW Kidz Telugu** — Kids — https://yuppparoriglin.akamaized.net/181224/smil:wowkidztelgu.smil/playlist.m3u8?hdnts=[REDACTED]
- **Star Sports 1 HD** — Sports — http://103.114.11.37:8081/Star-sports-1/index.m3u8?token=[REDACTED]
- **Star Sports Select 1** — Sports — http://103.114.11.37:8081/Star-select-1/index.m3u8?token=[REDACTED]
- **Star Sports Select 2** — Sports — http://103.114.11.37:8081/Star-select-2/index.m3u8?token=[REDACTED]
- **Studio Yuva** — Backup — https://d2gvyg6lvauoko.cloudfront.net/230226/studioyuva/playlist.m3u8?hdnts=[REDACTED]

## Embedded Xtream-Style Credential Paths (redacted)

- **Independent TV** — Bangladesh — http://premiumtvs.space/live/[REDACTED]/[REDACTED]/423.ts
- **Disney Channel** — Backup — http://rgkkw.live/live/[REDACTED]/[REDACTED]/19741.ts
- **Zee Bangla** — Backup — http://rgkkw.live:80/live/[REDACTED]/[REDACTED]/98881.ts

## Logo Integrity

- Healthy/local references: **1354**
- External references (review only): **0**

## Logo Exceptions Requiring Repair

Active playlist entries with missing or invalid logo references. These rows are listed for diagnosis; the audit never invents or substitutes artwork.

None.

## Missing Logos in Discovery Queues

These candidates have no verified local logo available yet; no external or placeholder logo has been assigned.

None.
- missing: **0**
- broken-local: **0**
- unsupported-format: **0**
- invalid-dimensions: **0**
- corrupt-image: **0**
- unvalidated-image: **0**
- other: **0**

## External Logo Review

None.

## Protected Primary Entries

No protected primary-entry changes detected.
