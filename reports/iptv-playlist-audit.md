# IPTV Playlist Audit
Generated: **2026-11-07T14:23:33.396123+00:00**
Source playlist SHA-256: **84c02ef014377e5b6ba95a227f9783389650950895cfd82aece9c12b369a6a98**

Non-destructive audit of channel identity, metadata consistency, duplicate identities, and logo integrity.
Scope note: Metadata conflicts and same-name/different-ID counts below cover canonical primary entries; cross-queue variants are shown separately as review diagnostics.

## Summary

- Playlist entries: **1005**
- Unique channel IDs: **674**
- IDs with multiple streams: **185**
- Duplicate stream URLs: **0**
- Metadata conflicts: **0**
- Same-name / different-ID collisions: **0**
- Cross-queue same-ID name variants (review): **0**
- Cross-queue normalized-name/different-ID groups (review): **0**
- Cross-country backup collisions: **0**
- IDs with multiple logo references: **0**
- Protected primary-entry changes: **0**
- Logo exceptions requiring repair: **0**
- Missing logos in review queues (review only): **0**
- External logo references (review only): **0**
- Logo references checked: **1005**
- Duplicate primary identities: **0**
- Potential near-duplicate primary name groups (review only): **1**
- Primary channel-number collisions: **0**
- Primary channel-number sequence issues: **0**
- Primary entries missing channel numbers: **0**
- Primary entries missing tvg-country: **0**
- Primary entries missing tvg-language: **0**
- Malformed EXTINF entries: **0**
- Category block-order issues: **0**
- Category registry issues: **0**
- Alphabetical ordering issues: **0**
- Suspicious URL credentials/syntax: **0**
- Signed/tokenized stream URLs: **8**
- Embedded Xtream-style credential paths (redacted): **0**


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

No normalized same-name/different-ID groups found across groups.

## Duplicate IDs

### 7smusic.in@sd (2 streams)
- 7S Music — Indian Music — https://mumt03.tangotv.in/Dsly5z3H7SMUSIC/index.m3u8
- 7S Music — Backup — https://cdn.pishow.tv/ott/live/1257/master.m3u8
### 8xm.pk@sd (2 streams)
- 8XM — Pakistani — https://cdn4.mjunoon.tv:8087/streamtest/131M/chunks.m3u8
- 8XM — Backup — https://vodzong.mjunoon.tv:8087/streamtest/8XM-131/playlist.m3u8
### 9xjalwa.in (3 streams)
- 9X Jalwa — Indian Music — https://wiselp.wiseplayout.com/9X_Jalwa/master.m3u8
- 9X Jalwa — Backup — https://d3kdywbtdfbp9z.cloudfront.net/v1/manifest/93ce20f0f52760bf38be911ff4c91ed02aa2fd92/dff423e0-3c82-46d6-9ecb-3baa96b5694a/70fca4d1-156e-4c03-baa4-9a4b602e33d5/0.m3u8
- 9X Jalwa — Backup — https://mumt03.tangotv.in/Dsly5z3H9XJALWA/index.m3u8
### 9xm.in@sd (3 streams)
- 9XM — Indian Music — https://cc-706183qeo55ez.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-706183qeo55ez/DIYC/PMSL/9X/9XMusic_IN/9XMusic_IN.m3u8
- 9XM — Backup — https://wiselp.wiseplayout.com/9XM/HD1080/HD1080.m3u8
- 9XM — Backup — https://wiselp.wiseplayout.com/9XM/master.m3u8
### aakaashaath.in@sd (3 streams)
- Aakaash Aath — Indian Bangla — https://mumt03.tangotv.in/Dsly5z3HAAKASHAATH/index.m3u8
- Aakaash Aath — Backup — https://mumt03.tangotv.in/Dsly5z3HAAKASHAATH/tracks-v1a1/mono.m3u8
- Aakaash Aath — Backup — https://tvsen5.aynaott.com/Wm9Lv2RjZGT6/index.m3u8
### aamarbangla.in (2 streams)
- Amar Bangla — Indian Bangla — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI/amarbanglatv.stream/playlist.m3u8
- Amar Bangla — Backup — http://115.187.41.216:8080/hls/amarbangla/index.m3u8
### alquranalkareemtv.sa (2 streams)
- Al Quran Al Kareem TV — Religious — https://cdn-globecast.akamaized.net/live/eds/saudi_quran/hls_roku/index.m3u8
- Al Quran Al Kareem TV — Backup — http://m.live.net.sa:1935/live/quran/playlist.m3u8
### amarbangladigital.in (2 streams)
- Amar Bangla Digital — Indian Bangla — http://115.187.41.216:8080/hls/amardigital/index.m3u8
- Amar Bangla Digital — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/amardigital.stream/playlist.m3u8
### amritatv.in@sd (2 streams)
- Amrita TV — Indian Entertainment — https://ddash74r36xqp.cloudfront.net/master.m3u8
- Amrita TV — Backup — https://ddash74r36xqp.cloudfront.net/master_2000.m3u8
### anandatv.bd (5 streams)
- Ananda TV — Bangladesh — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/anandatv.stream/index.m3u8
- Ananda TV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/anandatv.stream/tracks-v1a1/mono.m3u8
- Ananda TV — Backup — http://live-stream.amarbanglatv.in:8080/hls/sanandatv/index.m3u8
- Ananda TV — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/anandatv.stream/live-orgin/anandatv.stream/playlist.m3u8
- Ananda TV — Backup — https://tvsen6.aynaott.com/LeUAm4F1iixYns3s3Non/index.m3u8
### animalplanet.in@sd (4 streams)
- Animal Planet — Documentary & Wildlife — https://drk6xq0vhn.gpcdn.net/live/animal_planet_hd_abr/index.m3u8
- Animal Planet — Backup — https://drk6xq0vhn.gpcdn.net/live/animal_planet_hd/index.m3u8
- Animal Planet — Backup — https://drk6xq0vhn.gpcdn.net/live/animal_planet_sd_abr/index.m3u8
- Animal Planet — Backup — https://vodzong.mjunoon.tv:8087/streamtest/Animal-Planet-158-3/playlist.m3u8
### anjantv.in@sd (2 streams)
- Anjan TV — Indian Entertainment — https://cdn.pishow.tv/ott/live/993/master.m3u8
- Anjan TV — Backup — https://anjan.vstream.online/anjanorg/ngrp:anjan_hdall/playlist.m3u8
### aryqtv.pk (2 streams)
- ARY Q TV — Religious — https://aryqtvm.aryzap.com/v1/0183ea2a0eec0b8ed5941a38bc76/0183ea2a4e470b8ed5aa4d793457/ARYQTVH264_1080p.m3u8
- ARY Q TV — Backup — https://aryqtvm.aryzap.com/v1/0183ea2a0eec0b8ed5941a38bc76/0183ea2a4e470b8ed5aa4d793457/ARYQTVH264_720p.m3u8
### asiantv.bd (3 streams)
- Asian TV — Bangladesh — https://tvsen6.aynaott.com/pKb5k6NnzxsKpWUs6E8M/tracks-v1a1/mono.ts.m3u8
- Asian TV — Backup — https://stream.ottplus.live/live/asian_tv_abr/index.m3u8
- Asian TV — Backup — https://tvsen6.aynaott.com/pKb5k6NnzxsKpWUs6E8M/index.m3u8
### atnbangla.bd (3 streams)
- ATN Bangla — Bangladesh — https://tvsen5.aynaott.com/atnbangla/index.m3u8
- ATN Bangla — Backup — https://iptvlive.ahmed-bd-org.workers.dev/atn-bangla-1/index.m3u8
- ATN Bangla — Backup — https://tvsen5.aynaott.com/P3y2URgG7LDe/index.m3u8
### atnbanglauk.uk (2 streams)
- ATN Bangla UK — Bangladesh — https://app.ncare.live/live-orgin/atnbanglauk-off.stream/playlist.m3u8
- ATN Bangla UK — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/atnbanglauk-off.stream/playlist.m3u8
### atnnews.bd (5 streams)
- ATN News — Bangladesh — https://tvsen6.aynaott.com/da6WMXAk/index.m3u8
- ATN News — Backup — https://iptv-proxy.ahmed-bd-org.workers.dev/atn-news/index.m3u8
- ATN News — Backup — https://iptvlive.ahmed-bd-org.workers.dev/atn-news-1/index.m3u8
- ATN News — Backup — https://iptvlive.ahmed-bd-org.workers.dev/atn-news-2/index.m3u8
- ATN News — Backup — https://tvsen6.aynaott.com/da6WMXAk/tracks-v1a1/mono.ts.m3u8
### b4ukadak.in@sd (3 streams)
- B4U Kadak — Indian Movies — https://amg00877-b4unew-amg00877c4-xiaomi-in-5473.playouts.now.amagi.tv/playlist.m3u8
- B4U Kadak — Backup — https://cdn.pishow.tv/ott/live/227/master.m3u8
- B4U Kadak — Backup — https://streams.tangotv.in/B4UKADAK/ORIGIN/index.m3u8
### b4umovies.in@india (5 streams)
- B4U Movies — Indian Movies — https://amg00877-b4unew-amg00877c2-xiaomi-in-5489.playouts.now.amagi.tv/playlist.m3u8
- B4U Movies — Backup — http://103.135.253.32:8080/B4U-MOVIES/index.m3u8
- B4U Movies — Backup — https://cdn.pishow.tv/ott/live/419/master.m3u8
- B4U Movies — Backup — https://drk6xq0vhn.gpcdn.net/live/b4u_movies_abr/index.m3u8
- B4U Movies — Backup — https://streams.tangotv.in/B4UMOVIES/ORIGIN/index.m3u8
### b4umusic.in@india (6 streams)
- B4U Music — Indian Music — https://streams.tangotv.in/B4UMUSIC/ORIGIN/index.m3u8
- B4U Music — Backup — http://103.175.73.12:8080/live/157/master.m3u8
- B4U Music — Backup — https://amg00877-b4unew-amg00877c3-xiaomi-in-5474.playouts.now.amagi.tv/720p/index.m3u8
- B4U Music — Backup — https://amg01408-amg01408c5-amgplt0747.playout.now3.amagi.tv/b4um001/playlist.m3u8
- B4U Music — Backup — https://cdn.pishow.tv/ott/live/415/master.m3u8
- B4U Music — Backup — https://drk6xq0vhn.gpcdn.net/live/b4u_music_abr/index.m3u8
### balleballe.in@sd (4 streams)
- Balle Balle — Indian Music — https://mcncdndigital.com/balleballetv/index.m3u8
- Balle Balle — Backup — https://mcncdndigital.com/balleballetv/tracks-v1a1/mono.m3u8
- Balle Balle — Backup — https://mcncdndigital.com/worldpunjabitv/index.m3u8
- Balle Balle — Backup — https://streams.tangotv.in/BALLEBALLE/ORIGIN/index.m3u8
### banglatv.bd (4 streams)
- Bangla TV — Bangladesh — http://116.204.149.16/banglatv/index.m3u8
- Bangla TV — Backup — https://cdn.ghuddi.live/Bangla_TV/Bangla_TV_BD/playlist.m3u8
- Bangla TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/bangla-tv-2/index.m3u8
- Bangla TV — Backup — https://tvsen6.aynaott.com/39ee93nUbCCmm5LsyD4t/index.m3u8
### banglavision.bd (4 streams)
- Bangla Vision — Bangladesh — https://tvsen5.aynaott.com/banglavision/index.m3u8
- Bangla Vision — Backup — https://iptvlive.ahmed-bd-org.workers.dev/banglavision-1/index.m3u8
- Bangla Vision — Backup — https://tvsen5.aynaott.com/banglavision/tracks-v1a1/mono.ts.m3u8
- Bangla Vision — Backup — https://tvsen5.aynaott.com/tgUzpPc9r6xw/index.m3u8
### bhi.channel.in (2 streams)
- BHI Channel — Indian Bangla — https://server.livelegitpro.in/bhichannel/bhichannel/index.m3u8
- BHI Channel — Backup — https://server.livelegitpro.in/bhichannel/bhichannel/tracks-v1a1/mono.m3u8
### bhojpuricinema.in@sd (4 streams)
- Bhojpuri Cinema — Indian Movies — https://live-bhojpuri.akamaized.net/liveabr/playlist.m3u8
- Bhojpuri Cinema — Backup — https://cdn.pishow.tv/ott/live/1033/master.m3u8
- Bhojpuri Cinema — Backup — https://iptvlive.ahmed-bd-org.workers.dev/bhojpuri-cinema-1/index.m3u8
- Bhojpuri Cinema — Backup — https://live-bhojpuri.akamaized.net/liveabr/pub-iobhojpuqbu6yj/live_720p/chunks.m3u8
### bijoytv.bd (3 streams)
- Bijoy TV — Bangladesh — https://tvsen6.aynaott.com/N8Xbo5vdwVU6sF43RsW0/index.m3u8
- Bijoy TV — Backup — https://drk6xq0vhn.gpcdn.net/live/bijoy_tv_abr/index.m3u8
- Bijoy TV — Backup — https://stream.ottplus.live/live/bijoy_tv_abr/index.m3u8
### boishakhitv.bd (3 streams)
- Boishakhi TV — Bangladesh — https://tvsen6.aynaott.com/1d3uG9VCgrR9DRtWZM57/index.m3u8
- Boishakhi TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/boishakhi-tv-1/index.m3u8
- Boishakhi TV — Backup — https://tvsen6.aynaott.com/1d3uG9VCgrR9DRtWZM57/tracks-v1a1/mono.ts.m3u8
### btvchattogram.bd (2 streams)
- BTV Chattogram — Bangladesh — https://tvsen6.aynaott.com/TjGR1GcxKetHNVcMVxbq/index.m3u8
- BTV Chattogram — Backup — https://tvsen6.aynaott.com/TjGR1GcxKetHNVcMVxbq/tracks-v1a1/mono.ts.m3u8
### cartoonnetwork.us (2 streams)
- Cartoon Network — Kids — https://drk6xq0vhn.gpcdn.net/live/cn_hd_abr/index.m3u8
- Cartoon Network — Backup — https://vodzong.mjunoon.tv:8087/streamtest/cartoon-network-87/playlist.m3u8
### channel1.bd (4 streams)
- Channel 1 — Bangladesh — https://stream.ottplus.live/live/channel_1_hd_abr/index.m3u8
- Channel 1 — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/channel1bd.stream/playlist.m3u8
- Channel 1 — Backup — https://drk6xq0vhn.gpcdn.net/live/channel_1_hd_abr/index.m3u8
- Channel 1 — Backup — https://stream.ottplus.live/live/channel_1_hd_abr/live/channel_1_hd_720/chunks.m3u8
### channel16.bd (2 streams)
- Channel 16 — Bangladesh — https://iptvlive.ahmed-bd-org.workers.dev/channel-16-1/index.m3u8
- Channel 16 — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/channel16bd.stream/tracks-v1a1/mono.m3u8
### channel24.bd (4 streams)
- Channel 24 — Bangladesh — https://tvsen6.aynaott.com/YrVDF8gujkdh/index.m3u8
- Channel 24 — Backup — https://drk6xq0vhn.gpcdn.net/live/channel_24_abr/index.m3u8
- Channel 24 — Backup — https://iptvlive.ahmed-bd-org.workers.dev/channel-24-hd-1/index.m3u8
- Channel 24 — Backup — https://stream.ottplus.live/live/channel_24_abr/index.m3u8
### channel52.bd (2 streams)
- Channel 52 — Bangladesh — http://str24.l9574.com/503.stream/tracks-v1a1/mono.m3u8
- Channel 52 — Backup — https://tvsen6.aynaott.com/channel52/index.m3u8
### channeli.bd (6 streams)
- Channel I — Bangladesh — https://tvsen6.aynaott.com/FNHpYvGZ7FkCE10PwTHm/index.m3u8
- Channel I — Backup — https://iptv-proxy.ahmed-bd-org.workers.dev/channel-i/index.m3u8
- Channel I — Backup — https://iptvlive.ahmed-bd-org.workers.dev/channel-i-1/index.m3u8
- Channel I — Backup — https://iptvlive.ahmed-bd-org.workers.dev/channel-i-hd-1/index.m3u8
- Channel I — Backup — https://tvsen3.b-cdn.net/qUud8Nxs/index.m3u8
- Channel I — Backup — https://tvsen6.aynaott.com/FNHpYvGZ7FkCE10PwTHm/tracks-v1a1/mono.ts.m3u8
### channels.uk (4 streams)
- Channel S — Bangladesh — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/channels.stream/live-orgin/channels.stream/playlist.m3u8
- Channel S — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/channels.stream/index.m3u8
- Channel S — Backup — https://app.ncare.live/live-orgin/channels.stream/live-orgin/channels.stream/chunks.m3u8
- Channel S — Backup — https://iptvlive.ahmed-bd-org.workers.dev/channel-s-1/index.m3u8
### channels.uk@679aa9 (2 streams)
- Channel S UK — Bangladesh — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI/chsukoff.stream/playlist.m3u8
- Channel S UK — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/chsukoff.stream/live-orgin/chsukoff.stream/chunks.m3u8
### cnn.us (2 streams)
- CNN — International — https://tvsen6.aynaott.com/cnn/index.m3u8
- CNN — Backup — https://amg01448-samsungin-cnnnow-samsungin-4npqg.amagi.tv/playlist/amg01448-samsungin-cnnnow-samsungin/playlist.m3u8
### colors.bangla.in (3 streams)
- Colors Bangla — Indian Bangla — https://yupptvcatchupire.yuppcdn.net/preview/colorsbanglahd/2500.m3u8
- Colors Bangla — Backup — https://catchup.yuppcdn.net/amazonv2/36/preview/colorsbanglahd/master/chunklist.m3u8
- Colors Bangla — Backup — https://yupptvcatchupire.yuppcdn.net/preview/colorsbanglahd/800.m3u8
### colors.in (2 streams)
- Colors — Indian Entertainment — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/sg/YuppTV/ColorsAPAC.m3u8
- Colors — Backup — http://103.135.253.32:8080/Color-HD/index.m3u8
### colorscineplex.uk (2 streams)
- Colors Cineplex [UK] — Indian Movies — https://d1rc86nwwc9fag.cloudfront.net/260723/smil:rishteycineplexukdev.smil/chunklist_b1928000.m3u8
- Colors Cineplex [UK] — Backup — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/gb/YuppTV/ColorsCineplexUK.m3u8
### colorstamil.in@sd (2 streams)
- Colors Tamil — Indian Entertainment — https://da86m1sqpm3o0.cloudfront.net/28072023/smil:colorstamilhd11.smil/playlist.m3u8
- Colors Tamil — Backup — https://da86m1sqpm3o0.cloudfront.net/28072023/smil:colorstamilhd11.smil/chunklist_b2628000.m3u8
### cricketgold.au@sd (2 streams)
- Cricket Gold — Sports — https://d1nj4u39ja4cn0.cloudfront.net/v1/master/9d062541f2ff39b5c0f48b743c6411d25f62fc25/FLS-MuxIP-CricketGold/418.m3u8
- Cricket Gold — Backup — https://tvsen6.aynaott.com/M2W2UR49dmeKbZnmdRzN/index.m3u8
### dangal2.in@sd (3 streams)
- Dangal 2 — Indian Entertainment — https://live-dangal2.akamaized.net/liveabr/playlist.m3u8
- Dangal 2 — Backup — https://mumt03.tangotv.in/Dsly5z3HDANGAL2/index.m3u8
- Dangal 2 — Backup — https://streams.tangotv.in/DANGAL2/ORIGIN/index.m3u8
### dangaltv.in@sd (3 streams)
- Dangal — Indian Entertainment — https://live-dangal.akamaized.net/liveabr/playlist.m3u8
- Dangal — Backup — https://live-dangal.akamaized.net/liveabr/pub-iodang10p4al/live_720p/chunks.m3u8
- Dangal — Backup — https://streams.tangotv.in/DANGAL/ORIGIN/index.m3u8
### dbcnews.bd (5 streams)
- DBC News — Bangladesh — https://tvsen6.aynaott.com/pF66Tkz0qFwP2aMMqHyt/index.m3u8
- DBC News — Backup — https://iptv-proxy.ahmed-bd-org.workers.dev/dbc-news/index.m3u8
- DBC News — Backup — https://iptvlive.ahmed-bd-org.workers.dev/dbc-news-1/index.m3u8
- DBC News — Backup — https://iptvlive.ahmed-bd-org.workers.dev/dbc-news-hd-1/index.m3u8
- DBC News — Backup — https://tvsen6.aynaott.com/pF66Tkz0qFwP2aMMqHyt/tracks-v1a1/mono.ts.m3u8
### ddarunprabha.in@sd (2 streams)
- DD Arun Prabha — Indian Entertainment — https://d2lk5u59tns74c.cloudfront.net/out/v1/308556d9fd1246adb479ef012a39bbfe/index.m3u8
- DD Arun Prabha — Backup — https://cdn.pishow.tv/ott/live/32/master.m3u8
### ddbangla.in@sd (4 streams)
- DD Bangla — Indian Bangla — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/7ff57cc9046b4c188b51a0d506f36e7f/index.m3u8
- DD Bangla — Backup — https://cdn.pishow.tv/ott/live/37/master.m3u8
- DD Bangla — Backup — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/7ff57cc9046b4c188b51a0d506f36e7f/index_3.m3u8
- DD Bangla — Backup — https://iptvlive.ahmed-bd-org.workers.dev/dd-bangla-1/index.m3u8
### ddbharati.in@sd (2 streams)
- DD Bharati — Indian Entertainment — https://d2lk5u59tns74c.cloudfront.net/out/v1/67cec794d8b14f9ba21f73924ac65797/index.m3u8
- DD Bharati — Backup — https://cdn.pishow.tv/ott/live/10/master.m3u8
### ddchandana.in@sd (2 streams)
- DD Chandana — Indian Entertainment — https://cdn.pishow.tv/ott/live/28/master.m3u8
- DD Chandana — Backup — https://d2lk5u59tns74c.cloudfront.net/out/v1/0c980455d2fb4b69bcc6235745ee6039/index.m3u8
### ddindia.in@sd (2 streams)
- DD India — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/ceda14583477426aa162a65392d8ea07/index.m3u8
- DD India — Backup — https://mumbai-edge.smartplaytv.in/DDIndia/index.m3u8
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
### ddnational.in@sd (4 streams)
- DD National — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/40492a64c1db4a1385ba1a397d357d3a/index.m3u8
- DD National — Backup — http://107.167.16.138/ddnational/index.m3u8
- DD National — Backup — https://cdn.pishow.tv/ott/live/11/master.m3u8
- DD National — Backup — https://mumbai-edge.smartplaytv.in/DDNational/index.m3u8
### ddodia.in@sd (2 streams)
- DD Odia — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/ef4ea632b77a480ebd77106968aa99a9/index.m3u8
- DD Odia — Backup — https://mumbai-edge.smartplaytv.in/ddodiya/index.m3u8
### ddrajasthan.in@sd (2 streams)
- DD Rajasthan — Indian Entertainment — https://cdn.pishow.tv/ott/live/34/master.m3u8
- DD Rajasthan — Backup — https://d2lk5u59tns74c.cloudfront.net/out/v1/5b6bbbf682b741ecbe279f75a4a9a3e6/index.m3u8
### ddsaptagiri.in@sd (2 streams)
- DD Saptagiri — Indian Entertainment — https://d2lk5u59tns74c.cloudfront.net/out/v1/26e915d6d12b4a06822c5e33c088ed56/index.m3u8
- DD Saptagiri — Backup — https://cdn.pishow.tv/ott/live/22/master.m3u8
### ddtamil.in@sd (2 streams)
- DD Tamil — Indian Entertainment — https://d2lk5u59tns74c.cloudfront.net/out/v1/abf46b14847e45499f4a47f3a9afe93d/index.m3u8
- DD Tamil — Backup — https://cdn.pishow.tv/ott/live/1737/master.m3u8
### ddurdu.in@sd (2 streams)
- DD Urdu — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/9b91e9007e754db39a8b32c6bfc5b24a/index.m3u8
- DD Urdu — Backup — https://cdn.pishow.tv/ott/live/8/master.m3u8
### deentv.uk (3 streams)
- Deen TV — Religious — https://cd198.anystream.uk:9092/iqapp/d33ntv/playlist.m3u8
- Deen TV — Backup — https://app.ncare.live/live-orgin/deentv.stream/playlist.m3u8
- Deen TV — Backup — https://tvsen3.aynaott.com/TJcnZW3U/index.m3u8
### deewanahd.in (2 streams)
- Deewana — Indian Music — https://live20.bozztv.com/giatvplayout7/giatv-209592/index.m3u8
- Deewana — Backup — https://live20.bozztv.com/giatvplayout7/giatv-209592/tracks-v1a1/mono.ts.m3u8
### deshtv.bd (3 streams)
- Desh TV — Bangladesh — https://stream.ottplus.live/live/desh_tv_abr/index.m3u8
- Desh TV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/deshtv.stream/index.m3u8
- Desh TV — Backup — https://tvsen6.aynaott.com/ryFkXfd1a4CQ7mMdc820/index.m3u8
### desichannel.in (2 streams)
- Desi Channel — Indian Entertainment — https://livestream.unlimitedcdn.com/agm-dc/desi-channel/index.m3u8
- Desi Channel — Backup — https://livestream.unlimitedcdn.com/agm-dc/desi-channel/tracks-v1a1/mono.m3u8
### dhoommusic.in@sd (2 streams)
- Dhoom Music Bangla — Indian Bangla — https://mumt06.tangotv.in/qYyB8fXVDHOOMMUSIC/index.m3u8
- Dhoom Music Bangla — Backup — https://cdn.pishow.tv/ott/live/1456/master.m3u8
### discoverpakistan.pk@sd (2 streams)
- Discover Pakistan — Pakistani — https://livecdn.live247stream.com/discoverpakistan/web/playlist.m3u8
- Discover Pakistan — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/discoverpakistan.stream/playlist.m3u8
### discoverykids.au (2 streams)
- Discovery Kids — Kids — https://stream.ottplus.live/live/discovery_kids_abr/index.m3u8
- Discovery Kids — Backup — https://drk6xq0vhn.gpcdn.net/live/discovery_kids_abr/index.m3u8
### durontotv.bd (4 streams)
- Duronto TV — Bangladesh — http://103.135.253.32:8080/DORONTU-TV/index.m3u8
- Duronto TV — Backup — https://livetv.shamon-cable.net:8443/Duronto/index.m3u8
- Duronto TV — Backup — https://tvsen5.aynaott.com/6xyZ3N4oHv2KBJdB6W4p/index.fmp4.m3u8
- Duronto TV — Backup — https://tvsen6.aynaott.com/6xyZ3N4oHv2KBJdB6W4p/index.m3u8
### e24.in (2 streams)
- E24 — Indian Music — https://amg13643-amg13643c2-amgplt0016.playout.now3.amagi.tv/ts-eu-w1-n2/playlist/amg13643-amg13643c2-amgplt0016/playlist.m3u8
- E24 — Backup — https://mumt04.tangotv.in/m18aqlK4E24/index.m3u8
### ekattortv.bd (3 streams)
- Ekattor TV — Bangladesh — https://tvsen6.aynaott.com/EWDrV5QskgarZEUBb3pU/index.m3u8
- Ekattor TV — Backup — https://stream.ottplus.live/live/ekattor_tv_abr/index.m3u8
- Ekattor TV — Backup — https://tvsen6.aynaott.com/EWDrV5QskgarZEUBb3pU/tracks-v1a1/mono.ts.m3u8
### ekhontv.bd (4 streams)
- Ekhon TV — Bangladesh — https://drk6xq0vhn.gpcdn.net/live/ekhon_tv_abr/index.m3u8
- Ekhon TV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/globaltv.stream/index.m3u8
- Ekhon TV — Backup — https://stream.ottplus.live/live/ekhon_tv_abr/index.m3u8
- Ekhon TV — Backup — https://tvsen6.aynaott.com/fbgZV3X17hwWcyfZ4pdb/index.m3u8
### ekusheytv.bd (6 streams)
- Ekushey TV — Bangladesh — https://tvsen5.aynaott.com/SyQuXz8sC3TB/index.m3u8
- Ekushey TV — Backup — http://210.4.72.204/hls-live/livepkgr/_definst_/liveevent/livestream3.m3u8
- Ekushey TV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/ekusheytv-8-org.stream/index.m3u8
- Ekushey TV — Backup — https://ekusheyserver.com/etvlivesn.m3u8
- Ekushey TV — Backup — https://ekusheyserver.com/hls-live/livepkgr/_definst_/liveevent/livestream2.m3u8
- Ekushey TV — Backup — https://tvsen6.aynaott.com/y4mEVZNAbeNWTbd6Z2Pw/index.m3u8
### enter10bangla.in (6 streams)
- Enter10 Bangla — Indian Bangla — https://live-bangla.akamaized.net/liveabr/pub-iobanglakp3sff/live_360p/chunks.m3u8
- Enter10 Bangla — Backup — https://amg01448-samsungin-enterr10bangla-samsungin-ad-gg.amagi.tv/playlist/amg01448-samsungin-enterr10bangla-samsungin/playlist.m3u8
- Enter10 Bangla — Backup — https://iptvlive.ahmed-bd-org.workers.dev/enter-10-bangla-1/index.m3u8
- Enter10 Bangla — Backup — https://live-bangla.akamaized.net/liveabr/playlist.m3u8
- Enter10 Bangla — Backup — https://live-bangla.akamaized.net/liveabr/pub-iobanglakp3sff/live_720p/chunks.m3u8
- Enter10 Bangla — Backup — https://mumt07.tangotv.in/zHjX9OFlENTERR10BANGLA/index.m3u8
### entertv.bd (3 streams)
- Enter TV — Bangladesh — https://live1.entertv.com.bd/entertv/tracks-v1a1/mono.m3u8
- Enter TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/enter-tv-1/index.m3u8
- Enter TV — Backup — https://live1.entertv.com.bd/entertv/index.fmp4.m3u8
### epicbharat.in@sd (2 streams)
- Epic Bharat — Indian Entertainment — https://mumt06.tangotv.in/qYyB8fXVEPICTV/index.m3u8
- Epic Bharat — Backup — https://epiconvh.akamaized.net/live/nazara/master.m3u8
### epicbhojpuri.in@sd (2 streams)
- Epic Bhojpuri — Indian Movies — https://mumt01.tangotv.in/O5aw8Zn3EPICBHOJPURI/index.m3u8
- Epic Bhojpuri — Backup — https://mumt01.tangotv.in/O5aw8Zn3EPICBHOJPURI/tracks-v1a1/mono.m3u8
### epicbhojpuridigital.in (2 streams)
- Epic Bhojpuri Digital — Indian Movies — https://cc-8hy4a26pz2uos.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-8hy4a26pz2uos/playlist.m3u8
- Epic Bhojpuri Digital — Backup — https://cc-8hy4a26pz2uos.akamaized.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-8hy4a26pz2uos/45b71b91-51a1-4cfd-a422-c7f32efbf377/3.m3u8
### epicmusic.in@sd (4 streams)
- Epic Music — Indian Music — https://mumt04.tangotv.in/m18aqlK4EPICMUSIC/index.m3u8
- Epic Music — Backup — https://cc-3cyxq80qusspd.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-3cyxq80qusspd/playlist.m3u8
- Epic Music — Backup — https://iptvlive.ahmed-bd-org.workers.dev/epic-music-1/index.m3u8
- Epic Music — Backup — https://jmp2.uk/stvp-IN8000196E
### faktmarathi.in@sd (2 streams)
- Fakt Marathi — Indian Entertainment — https://mumt07.tangotv.in/zHjX9OFlFAKTMARATHI/index.m3u8
- Fakt Marathi — Backup — https://cdn.pishow.tv/ott/live/10002/master.m3u8
### gazitv.bd (5 streams)
- G TV — Bangladesh — http://103.135.253.32:8080/Gazi-TV/index.m3u8
- G TV — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/gazibdz.stream/live-orgin/gazibdz.stream/playlist.m3u8
- G TV — Backup — https://app.ncare.live/live-orgin/gazibdz.stream/live-orgin/gazibdz.stream/chunks.m3u8
- G TV — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/gazibdz.stream/playlist.m3u8
- G TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/g-tv-1/index.m3u8
### globaltv.bd (4 streams)
- Global TV — Bangladesh — https://stream.ottplus.live/live/global_tv_abr/index.m3u8
- Global TV — Backup — http://116.204.149.16/globaltv/tracks-v1a1/mono.m3u8
- Global TV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/Global-tv.stream/playlist.m3u8
- Global TV — Backup — https://tvsen6.aynaott.com/y0q9eFAuquAtvTxRzUHq/index.m3u8
### goldmines.in@sd (4 streams)
- Goldmines — Indian Movies — https://streams.tangotv.in/GOLDMINES/ORIGIN/index.m3u8
- Goldmines — Backup — https://cdn.pishow.tv/ott/live/1459/master.m3u8
- Goldmines — Backup — https://mumt04.tangotv.in/m18aqlK4GOLDMINES/index.m3u8
- Goldmines — Backup — https://streams.tangotv.in/GOLDMINES/ORIGIN/tracks-v1a1/mono.m3u8
### goldmines2.in@sd (2 streams)
- Goldmines 2 — Indian Movies — https://mumt03.tangotv.in/Dsly5z3HGOLDMINES2/index.m3u8
- Goldmines 2 — Backup — https://mumt03.tangotv.in/Dsly5z3HGOLDMINES2/tracks-v1a1/mono.m3u8
### goldminesaction.in (2 streams)
- Goldmines Action — Indian Movies — https://mumt03.tangotv.in/Dsly5z3HGOLDMINESACTION/index.m3u8
- Goldmines Action — Backup — https://mumt03.tangotv.in/Dsly5z3HGOLDMINESACTION/tracks-v1a1/mono.m3u8
### goldminesbollywood.in@sd (3 streams)
- Goldmines Bollywood — Indian Movies — https://streams.tangotv.in/GOLDMINESBOLLYWOOD/ORIGIN/index.m3u8
- Goldmines Bollywood — Backup — https://mumt03.tangotv.in/Dsly5z3HGOLDMINESBOLLYWOOD/index.m3u8
- Goldmines Bollywood — Backup — https://streams.tangotv.in/GOLDMINESBOLLYWOOD/ORIGIN/tracks-v1a1/mono.m3u8
### goldminesmovies.in@sd (3 streams)
- Goldmines Movies — Indian Movies — https://streams.tangotv.in/GOLDMINEMOVIES/ORIGIN/index.m3u8
- Goldmines Movies — Backup — https://cdn.pishow.tv/ott/live/1461/master.m3u8
- Goldmines Movies — Backup — https://streams.tangotv.in/GOLDMINEMOVIES/ORIGIN/tracks-v1a1/mono.m3u8
### greentv.bd@sd (2 streams)
- Green TV — Bangladesh — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/greentv.stream/live-orgin/greentv.stream/playlist.m3u8
- Green TV — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/greentv.stream/playlist.m3u8
### gseriesdrama.bd (2 streams)
- G Series Drama — Bangladesh — https://vods2.aynaott.com/gseriesDrama/tracks-v1a1/mono.ts.m3u8
- G Series Drama — Backup — https://vods2.aynaott.com/gseriesDrama/index.m3u8
### gtcpunjabi.in@sd (2 streams)
- GTC Punjabi — Indian Entertainment — https://gtc-yupp.vgcdn.net/vglive-sk-254807/index.m3u8
- GTC Punjabi — Backup — https://cdn.ottlive.co.in/gtcpunjabi/index.m3u8
### hindihits.in (2 streams)
- Hindi Hits — Indian Music — http://146.59.253.52:8080/hindihitshd/index.m3u8
- Hindi Hits — Backup — https://samitaorigin.tangotv.in/HINDIHITS/SAMITAORIGIN/index.m3u8
### humtv.pk (5 streams)
- Hum TV — Pakistani — https://drk6xq0vhn.gpcdn.net/live/hum_tv_abr/index.m3u8
- Hum TV — Backup — https://cdn4.mjunoon.tv:8087/streamtest/82M/chunks.m3u8
- Hum TV — Backup — https://drk6xq0vhn.gpcdn.net/live/hum_tv_abr/live/hum_tv_720/chunks.m3u8
- Hum TV — Backup — https://g4wlkwx8l23a-hls-live.5centscdn.com/HUM/271ddf829afeece44d8732757fba1a66.sdp/playlist_dvr.m3u8
- Hum TV — Backup — https://stream.ottplus.live/live/hum_tv_abr/index.m3u8
### independenttv.bd (2 streams)
- Independent TV — Bangladesh — https://drk6xq0vhn.gpcdn.net/live/independent_tv_abr/index.m3u8
- Independent TV — Backup — https://drk6xq0vhn.gpcdn.net/live/independent_tv_abr/live/independent_tv_720/chunks.m3u8
### insync.in (2 streams)
- Insync — Indian Music — https://mumt04.tangotv.in/m18aqlK4INSYNC/index.m3u8
- Insync — Backup — https://d1msejlow1t3l4.cloudfront.net/fta/insync/playlist.m3u8
### iqrabangla.uk (3 streams)
- Iqra Bangla — Religious — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/iqrabanglatvoffice.stream/live-orgin/iqrabanglatvoffice.stream/chunks.m3u8
- Iqra Bangla — Backup — https://tvsen3.aynaott.com/EuEy5mBW/index.m3u8
- Iqra Bangla — Backup — https://tvsen5.aynaott.com/iqrabangla/index.m3u8
### jagonews24.bd (3 streams)
- Jago News 24 — Bangladesh — https://app.ncare.live/live-orgin/jagonews24.stream/playlist.m3u8
- Jago News 24 — Backup — https://app.ncare.live/live-orgin/jagonews24.stream/live-orgin/jagonews24.stream/chunks.m3u8
- Jago News 24 — Backup — https://iptvlive.ahmed-bd-org.workers.dev/jago-news-24-1/index.m3u8
### jalwatv.pk@sd (2 streams)
- Jalwa TV — Pakistani — https://cdn4.mjunoon.tv:8087/streamtest/135M/chunks.m3u8
- Jalwa TV — Backup — https://vodzong.mjunoon.tv:8087/streamtest/JalwaTV-135/live/135M/chunks.m3u8
### jamunatv.bd (4 streams)
- Jamuna TV — Bangladesh — https://tvsen6.aynaott.com/KGdZEdA7qQ43dmPkgk1j/index.m3u8
- Jamuna TV — Backup — https://iptv-proxy.ahmed-bd-org.workers.dev/jamuna-tv/index.m3u8
- Jamuna TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/jamuna-tv-1/index.m3u8
- Jamuna TV — Backup — https://stream.ottplus.live/live/jamuna_tv_abr/index.m3u8
### jeevantv.in@sd (2 streams)
- Jeevan TV — Indian Entertainment — https://cdn.pishow.tv/ott/live/1467/master.m3u8
- Jeevan TV — Backup — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/in/YuppTV/JeevanTV.m3u8
### kairalitv.in@sd (2 streams)
- Kairali TV — Indian Entertainment — https://streams.tangotv.in/KAIRALI/ORIGIN/index.m3u8
- Kairali TV — Backup — https://mumt01.tangotv.in/O5aw8Zn3KAIRALI/index.m3u8
### kairaliwe.in@sd (2 streams)
- Kairali We — Indian Movies — https://streams.tangotv.in/WETV/ORIGIN/index.m3u8
- Kairali We — Backup — https://mumt01.tangotv.in/O5aw8Zn3WETV/index.m3u8
### kalaignarmurasu.in (2 streams)
- Kalaignar Murasu — Indian Entertainment — https://yuppmedtaorire.akamaized.net/v1/master/a0d007312bfd99c47f76b77ae26b1ccdaae76cb1/murasu_nim_https/050522/murasu/playlist.m3u8
- Kalaignar Murasu — Backup — https://segment.yuppcdn.net/050522/murasu/playlist.m3u8
### kappatv.in@alt1 (3 streams)
- Kappa TV (Music) — Indian Music — https://mumt03.tangotv.in/Dsly5z3HKAPPATV/index.m3u8
- Kappa TV (Music) — Backup — https://cdn.pishow.tv/ott/live/1123/master.m3u8
- Kappa TV (Music) — Backup — https://d1msejlow1t3l4.cloudfront.net/fta/kappatv/playlist.m3u8
### keralavision.in@sd (2 streams)
- Kerala Vision — Indian Entertainment — https://mumt03.tangotv.in/Dsly5z3HKERALAVISION/index.m3u8
- Kerala Vision — Backup — https://cdn.pishow.tv/ott/live/243/master.m3u8
### khushboobangla.in@sd (3 streams)
- Khushboo Bangla — Indian Bangla — https://mumt01.tangotv.in/O5aw8Zn3KHUSHBOOTVBANGLA/index.m3u8
- Khushboo Bangla — Backup — https://cdn.pishow.tv/ott/live/1473/master.m3u8
- Khushboo Bangla — Backup — https://mumt01.tangotv.in/O5aw8Zn3KHUSHBOOTVBANGLA/tracks-v1a1/mono.m3u8
### maasrangatv.bd (5 streams)
- Maasranga TV — Bangladesh — https://mtv.sunplex.live/MAASRANGA/index.m3u8
- Maasranga TV — Backup — http://116.204.149.16/maasranga/index.m3u8
- Maasranga TV — Backup — https://mtv.sunplex.live/MAASRANGA/tracks-v1a1/mono.m3u8
- Maasranga TV — Backup — https://tvsen5.aynaott.com/maasrangatv/index.m3u8
- Maasranga TV — Backup — https://tvsen6.aynaott.com/maasrangatv/index.m3u8
### madhimugamtv.in (2 streams)
- Madhimugam TV — Indian Entertainment — https://cdn.pishow.tv/ott/live/1476/master.m3u8
- Madhimugam TV — Backup — https://mumt01.tangotv.in/O5aw8Zn3MATHIMUGAMTV/index.m3u8
### mahaamax.in (2 streams)
- Mahaa Max — Indian Entertainment — https://mumt03.tangotv.in/Dsly5z3HMAHAAMAX/index.m3u8
- Mahaa Max — Backup — https://mumbai-edge.smartplaytv.in/MahaMax/index.m3u8
### makkahtv.sa (2 streams)
- Makkah TV — Religious — https://media2.streambrothers.com:1936/8122/8122/playlist.m3u8
- Makkah TV — Backup — https://media2.streambrothers.com:1936/8122/8122/chunklist_w1247854077.m3u8
### manoranjanmovies.in@sd (2 streams)
- Manoranjan Movies — Indian Movies — https://mumt04.tangotv.in/m18aqlK4MANORANJANMOVIES/index.m3u8
- Manoranjan Movies — Backup — https://mumt04.tangotv.in/m18aqlK4MANORANJANMOVIES/tracks-v1a1/mono.m3u8
### manoranjanprime.in@sd (2 streams)
- Manoranjan Prime — Indian Entertainment — https://cdn.pishow.tv/ott/live/1474/master.m3u8
- Manoranjan Prime — Backup — https://mumt06.tangotv.in/qYyB8fXVMANORANJANPRIME/index.m3u8
### marutamtv.in (2 streams)
- MNTV (Tamil) — Indian Entertainment — https://mntv.livebox.co.in/mntvhls/live.m3u8
- MNTV (Tamil) — Backup — https://www.khuwemultimedia.com/hls/mntv/mntv.m3u8
### matribhumitv.bd (2 streams)
- Matribhumi TV — Bangladesh — http://live.playmax.live/matribhumi/index.m3u8
- Matribhumi TV — Backup — https://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/matribhumitv.stream/playlist.m3u8
### mazhavilmanorama.in@sd (5 streams)
- Mazhavil Manorama — Indian Entertainment — https://yuppmedtaorire.akamaized.net/v1/master/a0d007312bfd99c47f76b77ae26b1ccdaae76cb1/mazhavilmanorama_nim_https/050522/mazhavilmanorama/playlist.m3u8
- Mazhavil Manorama — Backup — https://cdn.pishow.tv/ott/live/1479/master.m3u8
- Mazhavil Manorama — Backup — https://mmtv-vglivessai.akamaized.net/v1/master/673630b269b766886555eebfddd4f27f3de3ab50/f8a0827f-030f-4a0d-b7e5-338996c09a5b/index.m3u8
- Mazhavil Manorama — Backup — https://mumt03.tangotv.in/Dsly5z3HMAZHAVILMANORAMAINT/index.m3u8
- Mazhavil Manorama — Backup — https://mumt07.tangotv.in/zHjX9OFlMAZHAVILMANORAMAHD/index.m3u8
### mbcbollywood.ae (2 streams)
- MBC Bollywood — Indian Movies — https://shd-gcp-live.edgenextcdn.net/live/bitmovin-mbc-bollywood/546eb40d7dcf9a209255dd2496903764/index.m3u8
- MBC Bollywood — Backup — http://93.184.10.248/MBCBollywood/index.m3u8
### medinalive.bd (3 streams)
- Medina Live — Religious — https://cdn-globecast.akamaized.net/live/eds/saudi_sunnah/hls_roku/index.m3u8
- Medina Live — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/madina.stream/playlist.m3u8
- Medina Live — Backup — http://m.live.net.sa:1935/live/sunnah/playlist.m3u8
### metv.bd (4 streams)
- ME TV — Bangladesh — https://iptvbd.live/metv1080/1080.m3u8
- ME TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/me-tv-1/index.m3u8
- ME TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/me-tv-2/index.m3u8
- ME TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/me-tv-3/index.m3u8
### mhonedilse.in@sd (2 streams)
- MH One Dil Se — Indian Music — https://mumt01.tangotv.in/O5aw8Zn3MHONEDILSE/index.m3u8
- MH One Dil Se — Backup — https://streams.tangotv.in/MHONEDILSE/ORIGIN/index.m3u8
### mhonemovies.in@sd (2 streams)
- MH One Movies — Indian Movies — https://mumt03.tangotv.in/Dsly5z3HMHONEMOVIE/index.m3u8
- MH One Movies — Backup — https://mumt03.tangotv.in/Dsly5z3HMHONEMOVIE/tracks-v1a1/mono.m3u8
### mksix.in (2 streams)
- MK Six — Indian Entertainment — https://mumt06.tangotv.in/qYyB8fXVMKSIX/index.m3u8
- MK Six — Backup — https://cdn.pishow.tv/ott/live/1253/master.m3u8
### mohonatv.bd (3 streams)
- Mohona TV — Bangladesh — https://tvsen6.aynaott.com/AkyX5dunzju4cpo26dr7/tracks-v1a1/mono.ts.m3u8
- Mohona TV — Backup — https://stream.ottplus.live/live/mohona_tv_abr/index.m3u8
- Mohona TV — Backup — https://tvsen6.aynaott.com/AkyX5dunzju4cpo26dr7/index.m3u8
### moviebangla.bd (4 streams)
- Movie Bangla — Bangladesh — http://alvetv.com/moviebanglatv/8080/index.m3u8
- Movie Bangla — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/moviebanglalink2.stream/tracks-v1a1/mono.m3u8
- Movie Bangla — Backup — https://iptvlive.ahmed-bd-org.workers.dev/movie-bangla-1/index.m3u8
- Movie Bangla — Backup — https://stream.ottplus.live/live/movie_bangla_abr/index.m3u8
### musicindia.in@sd (2 streams)
- Music India — Indian Music — https://streams.tangotv.in/MUSICINDIA/ORIGIN/index.m3u8
- Music India — Backup — https://cdn.pishow.tv/ott/live/226/master.m3u8
### mytv.bd (5 streams)
- My TV — Bangladesh — https://tvsen6.aynaott.com/XMpHaEf0ANBhv8w6NWR7/index.m3u8
- My TV — Backup — http://116.204.149.16/mytv/index.m3u8
- My TV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/mytv-up-off.stream/index.m3u8
- My TV — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/mytv-up-off.stream/live-orgin/mytv-up-off.stream/playlist.m3u8
- My TV — Backup — https://tvsen6.aynaott.com/XMpHaEf0ANBhv8w6NWR7/tracks-v1a1/mono.ts.m3u8
### nagoriktv.bd (2 streams)
- Nagorik TV — Bangladesh — https://box.bbaria.net/Nagorik_TV/tracks-v1a1/mono.m3u8
- Nagorik TV — Backup — https://box.bbaria.net:8083/Nagorik_TV/video.m3u8
### natgeotv.us (2 streams)
- Nat Geo TV — Documentary & Wildlife — http://103.135.253.32:8080/NATGEO-HD/index.m3u8
- Nat Geo TV — Backup — http://iptv.prosto.tv:7000/ch83/video.m3u8
### news24.bd (5 streams)
- News 24 — Bangladesh — https://tvsen6.aynaott.com/cdgr3tw6WoG7JyRnLbi0/index.m3u8
- News 24 — Backup — https://amg13643-amg13643c1-amgplt0016.playout.now3.amagi.tv/ts-eu-w1-n2/playlist/amg13643-amg13643c1-amgplt0016/playlist.m3u8
- News 24 — Backup — https://iptvlive.ahmed-bd-org.workers.dev/news-24-1/index.m3u8
- News 24 — Backup — https://iptvlive.ahmed-bd-org.workers.dev/news-24-hd-1/index.m3u8
- News 24 — Backup — https://tvsen6.aynaott.com/cdgr3tw6WoG7JyRnLbi0/tracks-v1a1/mono.ts.m3u8
### nexustv.bd (2 streams)
- Nexus TV — Bangladesh — https://stream.ottplus.live/live/nexus_tv_abr/index.m3u8
- Nexus TV — Backup — https://tvsen6.aynaott.com/Epm7WrFa/index.m3u8
### nhbollyflix.in (4 streams)
- NH BollyFlix — Indian Movies — https://cc-r5hupcym5oehh.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-r5hupcym5oehh/SBUM/RunnTV/BollyFlix_IN/BollyFlix_IN.m3u8
- NH BollyFlix — Backup — https://cc-r5hupcym5oehh.akamaized.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-r5hupcym5oehh/d47d1910-8862-4b83-a8a6-00ac11307859/0.m3u8
- NH BollyFlix — Backup — https://cc-r5hupcym5oehh.akamaized.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-r5hupcym5oehh/ece6e311-8eb0-4fdf-8378-d337cba07ec2/0.m3u8
- NH BollyFlix — Backup — https://jmp2.uk/stvp-IN46000140Q
### nhbollyraga.in (3 streams)
- NH BollyRaga — Indian Music — https://cc-up9j649x4thrj.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-up9j649x4thrj/SBUM/RunnTV/BollyRaga_IN/BollyRaga_IN.m3u8
- NH BollyRaga — Backup — https://cc-up9j649x4thrj.akamaized.net/v1/manifest/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-up9j649x4thrj/f935ee75-bf1b-4bf6-a30c-1f096a0083c5/0.m3u8
- NH BollyRaga — Backup — https://jmp2.uk/stvp-IN460001373
### ntv.bd (6 streams)
- NTV — Bangladesh — https://tvsen5.aynaott.com/xV4jEKf3D9zc/index.m3u8
- NTV — Backup — https://2-fss-1.streamhoster.com/pl_122/201748-1431018-1/chunklist.m3u8
- NTV — Backup — https://iptv-proxy.ahmed-bd-org.workers.dev/ntv/index.m3u8
- NTV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/ntv-1/index.m3u8
- NTV — Backup — https://tvsen5.aynaott.com/JHPxHAWonztVucyc4GzF/index.m3u8
- NTV — Backup — https://tvsen5.aynaott.com/xV4jEKf3D9zc/tracks-v1a1/mono.ts.m3u8
### ntveurope.bd (2 streams)
- NTV Europe — Bangladesh — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/ntvuk00332211.stream/playlist.m3u8
- NTV Europe — Backup — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/ntvuk00332211.stream/live-orgin/ntvuk00332211.stream/chunks.m3u8
### pardesitv.ca (2 streams)
- Pardesi TV — Indian Entertainment — http://stream.pardesitv.online/pardesi/index.m3u8
- Pardesi TV — Backup — http://stream.pardesitv.online/pardesi/tracks-v1a1/mono.m3u8
### pitaara.in@sd (4 streams)
- Pitaara TV — Indian Movies — https://d2lk5u59tns74c.cloudfront.net/out/v1/500a6b45f5ae41dda445d912b59eaa09/index.m3u8
- Pitaara TV — Backup — https://d2lk5u59tns74c.cloudfront.net/out/v1/500a6b45f5ae41dda445d912b59eaa09/index_5.m3u8
- Pitaara TV — Backup — https://streams.tangotv.in/PITAARA/ORIGIN/index.m3u8
- Pitaara TV — Backup — https://vg-pitaaratvlive.akamaized.net/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/vglive-sk-583798/playlist.m3u8
### pocketfilms.in (2 streams)
- Pocket Films — Indian Movies — https://vglivessai.akamaized.net/sg/v1/manifest/611d79b11b77e2f571934fd80ca1413453772ac7/b8ada260-bb81-472b-b7c1-3a79213a84b8/e02a0ce5-6c42-4cca-bb53-e5cfecff74a9/0.m3u8
- Pocket Films — Backup — https://vglivessai.akamaized.net/sg/v1/manifest/611d79b11b77e2f571934fd80ca1413453772ac7/b8ada260-bb81-472b-b7c1-3a79213a84b8/6408f97591ee7861ab0d4839eefdbbee/0.m3u8
### pogo.in@sd (2 streams)
- Pogo — Kids — https://drk6xq0vhn.gpcdn.net/live/pogo_sd_abr/index.m3u8
- Pogo — Backup — https://stream.ottplus.live/live/pogo_sd_abr/index.m3u8
### probashitv.bd (2 streams)
- Probashi TV — Bangladesh — http://158.69.24.53:8080/probashi_tv/index.m3u8
- Probashi TV — Backup — http://158.69.24.53:8080/probashi_tv/tracks-v1a1/mono.m3u8
### ptcmusic.in@sd (2 streams)
- PTC Music — Indian Music — https://d2lk5u59tns74c.cloudfront.net/out/v1/f913cf893c594f73b114216e74a2efbc/index.m3u8
- PTC Music — Backup — https://iptvlive.ahmed-bd-org.workers.dev/ptc-music-1/index.m3u8
### ptcpunjabi.in@sd (3 streams)
- PTC Punjabi — Indian Entertainment — https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/3e22a9c278db4e3eb779afd42e41b0a6/index.m3u8
- PTC Punjabi — Backup — https://cdn.pishow.tv/ott/live/1604/master.m3u8
- PTC Punjabi — Backup — https://streams.tangotv.in/PTCPUNJABI/ORIGIN/index.m3u8
### publicmovies.in@sd (2 streams)
- Public Movies — Indian Movies — https://mumt04.tangotv.in/m18aqlK4PUBLICMOVIES/index.m3u8
- Public Movies — Backup — https://mumt04.tangotv.in/m18aqlK4PUBLICMOVIES/tracks-v1a1/mono.m3u8
### publicmusic.in@sd (2 streams)
- Public Music — Indian Music — https://mumt04.tangotv.in/m18aqlK4PUBLICMUSIC/index.m3u8
- Public Music — Backup — https://cdn.pishow.tv/ott/live/441/master.m3u8
### punjabihits.in (2 streams)
- Punjabi Hits — Indian Music — https://stream.ottlive.co.in/punjabihits/index.m3u8
- Punjabi Hits — Backup — https://legitpro.co.in/punjabihits/punjabihits/index.m3u8
### punjabishorts.in (2 streams)
- Punjabi Shorts — Indian Entertainment — https://vglivessai.akamaized.net/ptnr-yupptv/title-Punjabi_Shorts/in/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/27c3fd7a-b01f-4b00-ac03-557ac77acd47/index.m3u8
- Punjabi Shorts — Backup — https://gtc.ottlive.co.in/punjabshort/index.m3u8
### qtv.in (2 streams)
- Q TV — Indian Entertainment — https://mumt05.tangotv.in/87NeALx2THEQ/index.m3u8
- Q TV — Backup — https://samitaorigin.tangotv.in/THEQ/SAMITAORIGIN/index.m3u8
### qurantv.iq (2 streams)
- Quran TV — Religious — https://live.kwikmotion.com/sharjahtvquranlive/shqurantv.smil/sharjahtvquranpublish/shqurantv_source/chunks.m3u8
- Quran TV — Backup — https://live.kwikmotion.com/sharjahtvquranlive/shqurantv.smil/playlist.m3u8
### rajdhanitv.bd (2 streams)
- Rajdhani TV — Bangladesh — http://stream.shariarsuvo.com/hls5/rajdhanicable.m3u8
- Rajdhani TV — Backup — https://drk6xq0vhn.gpcdn.net/live/rajdhani_tv/index.m3u8
### rajtv.in@sd (2 streams)
- Raj TV — Indian Music — https://livestream.rajtv.tv/hlslive/Admin/px08241087/live/RAJTV/master_1.m3u8
- Raj TV — Backup — https://d3kdywbtdfbp9z.cloudfront.net/v1/manifest/93ce20f0f52760bf38be911ff4c91ed02aa2fd92/dff423e0-3c82-46d6-9ecb-3baa96b5694a/b8640d6b-d131-4401-9451-944e1e65fe79/0.m3u8
### ramdhenu.in@sd (2 streams)
- Ramdhenu — Indian Music — https://mumt01.tangotv.in/O5aw8Zn3RAMDHENU/mpegts
- Ramdhenu — Backup — https://mumt01.tangotv.in/O5aw8Zn3RAMDHENU/index.m3u8
### rengoni.in@sd (2 streams)
- Rengoni — Indian Entertainment — https://d1msejlow1t3l4.cloudfront.net/fta/rengonitv/playlist.m3u8
- Rengoni — Backup — https://streams.tangotv.in/RENGONI/ORIGIN/index.m3u8
### rongeentv.in@sd (4 streams)
- Rongeen TV — Indian Bangla — https://server.thelegitpro.in/rongeentv/rongeentv/index.m3u8
- Rongeen TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/rongeen-tv-1/index.m3u8
- Rongeen TV — Backup — https://mumbai-edge.smartplaytv.in/RongeenTV/index.m3u8
- Rongeen TV — Backup — https://server.thelegitpro.in/rongeentv/rongeentv/tracks-v1a1/mono.m3u8
### rplus.in@sd (2 streams)
- R Plus — Indian Bangla — https://thelegitpro.in/pntv/rplusnews24x7/index.m3u8
- R Plus — Backup — https://vglivessai.akamaized.net/sg/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/e5dcc9dc-3a33-4b19-a361-5a5b3aa022f7/index.m3u8
### rplusgold.in@sd (5 streams)
- R Plus Gold — Indian Bangla — https://vglivessai.akamaized.net/sg/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/cf883da3-f9f5-4c70-b0ef-b3ac2e2ad1e3/index.m3u8
- R Plus Gold — Backup — https://cdn.pishow.tv/ott/live/1231/master.m3u8
- R Plus Gold — Backup — https://stream.ottlive.co.in/rplusgold/index.m3u8
- R Plus Gold — Backup — https://thelegitpro.in/pntv/rplusnews24x7/tracks-v1a1/mono.m3u8
- R Plus Gold — Backup — https://vglivessai.akamaized.net/sg/v1/manifest/611d79b11b77e2f571934fd80ca1413453772ac7/cf883da3-f9f5-4c70-b0ef-b3ac2e2ad1e3/5552ef1c-ee8a-4743-8321-08b260d3b1f3/0.m3u8
### rtv.bd (6 streams)
- RTV — Bangladesh — https://tvsen5.aynaott.com/RtvHD/index.m3u8
- RTV — Backup — http://116.204.149.16/rtvhd/index.m3u8
- RTV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/rtv-sg.stream/index.m3u8
- RTV — Backup — https://j6nfugukcl.gpcdn.net/tile_6/master.m3u8
- RTV — Backup — https://tvsen5.aynaott.com/ba47dHpDk3Se/index.m3u8
- RTV — Backup — https://tvsen6.aynaott.com/rtv/tracks-v1a1/mono.ts.m3u8
### rupasibangla.in@sd (5 streams)
- Ruposhi Bangla — Indian Bangla — https://mumt05.tangotv.in/87NeALx2RUPASIBANGLA/index.m3u8
- Ruposhi Bangla — Backup — http://103.175.73.12:8080/live/664/664_0.m3u8
- Ruposhi Bangla — Backup — https://cdn.pishow.tv/ott/live/1039/master.m3u8
- Ruposhi Bangla — Backup — https://da86m1sqpm3o0.cloudfront.net/28072023/smil:rupashibangla.smil/playlist.m3u8
- Ruposhi Bangla — Backup — https://mumt05.tangotv.in/87NeALx2RUPASIBANGLA/tracks-v1a1/mono.m3u8
### sanandatv.in (4 streams)
- Sananda — Indian Bangla — https://iptvlive.ahmed-bd-org.workers.dev/sananda-tv-1/index.m3u8
- Sananda — Backup — http://115.187.41.216:8080/hls/sanandatv/index.m3u8
- Sananda — Backup — http://27.124.71.27/Sun_Bangla/index.m3u8
- Sananda — Backup — https://live.sanandatelevision.in/sananda/tracks-v1a1/mono.m3u8
### sanaplus.in@sd (2 streams)
- Sana Plus — Indian Music — https://mumbai-edge.smartplaytv.in/SanaPlusHD/index.m3u8
- Sana Plus — Backup — https://galaxyott.live/hls/sanaplus.m3u8
### sangeetbangla.in@sd (4 streams)
- Sangeet Bangla — Indian Bangla — https://mumt05.tangotv.in/87NeALx2SANGEETBANGLA/index.m3u8
- Sangeet Bangla — Backup — http://103.175.73.12:8080/live/379/379_0.m3u8
- Sangeet Bangla — Backup — https://cdn.pishow.tv/ott/live/1143/master.m3u8
- Sangeet Bangla — Backup — https://mumt05.tangotv.in/87NeALx2SANGEETBANGLA/tracks-v1a1/mono.m3u8
### satv.bd (6 streams)
- SA TV — Bangladesh — http://116.204.149.16/satv/index.m3u8
- SA TV — Backup — http://app24.jagobd.com.bd/c3VydmVyX8RpbEU9Mi8xNy8yMFDEEHGcfRgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcEdsEfeDeKiNkVN3PTOmdFseWRtaW51aiPhnPTI2/satvoff5666.stream/playlist.m3u8
- SA TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/sa-tv-1/index.m3u8
- SA TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/sa-tv-2/index.m3u8
- SA TV — Backup — https://j6nfugukcl.gpcdn.net/tile_5/master.m3u8
- SA TV — Backup — https://tvsen6.aynaott.com/rELXiuUXqbgzPb06Npom/index.m3u8
### shansontv.ru (3 streams)
- Shanson TV — International — http://catchup.videoline.ru/shanson/index.m3u8
- Shanson TV — Backup — http://hls-shansontv.cdnvideo.ru/shansontv/shansontv-sd.smil/playlist.m3u8
- Shanson TV — Backup — https://streaming.thestream.cyou/live/7009.m3u8
### shemaroobollywood.us (2 streams)
- Shemaroo Bollywood — Indian Movies — https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg00864-shemarooenterta-shemabollywood-ono/playlist.m3u8
- Shemaroo Bollywood — Backup — https://amg00864-shemarooenterta-shemabollywood-ono-nlwbw.amagi.tv/playlist/amg00864-shemarooenterta-shemabollywood-ono/playlist.m3u8
### shemaroojosh.in@sd (3 streams)
- Shemaroo Josh — Indian Movies — https://airtelapp.shemaroo.com/shemarooChumbakTV/smil:shemarooChumbakTVadp.smil/playlist.m3u8
- Shemaroo Josh — Backup — https://cdn.pishow.tv/ott/live/337/master.m3u8
- Shemaroo Josh — Backup — https://mumt04.tangotv.in/m18aqlK4SHEMAROOJOSH/index.m3u8
### shubhcinematv.in (2 streams)
- Shubh Cinema TV — Indian Movies — https://d393sxaxig6bax.cloudfront.net/out/v1/589cf2cf44bf42bb941e817a2240d62e/index.m3u8
- Shubh Cinema TV — Backup — https://d393sxaxig6bax.cloudfront.net/out/v1/589cf2cf44bf42bb941e817a2240d62e/index_8.m3u8
### somoynewstv.bd (3 streams)
- Somoy TV — Bangladesh — https://tvsen6.aynaott.com/4XcqdovJzbbC9WdJA9gk/index.m3u8
- Somoy TV — Backup — https://drk6xq0vhn.gpcdn.net/live/somoy_tv_abr/index.m3u8
- Somoy TV — Backup — https://iptvlive.ahmed-bd-org.workers.dev/somoy-tv-2/index.m3u8
### sonyaath.in@sd (2 streams)
- Sony Aath — Indian Bangla — https://stream.ottplus.live/live/sony_aath_abr/index.m3u8
- Sony Aath — Backup — https://drk6xq0vhn.gpcdn.net/live/sony_aath_abr/index.m3u8
### southstation.in (2 streams)
- South Station — Indian Movies — https://cc-yw7ztecy8do3q.akamaized.net/v1/master/3722c60a815c199d9c0ef36c5b73da68a62b09d1/cc-yw7ztecy8do3q/SS_IN.m3u8
- South Station — Backup — https://jmp2.uk/stvp-IN3800008CX
### srk.bd (2 streams)
- SRK — Bangladesh — https://srknowapp.ncare.live/srktvhlswodrm/srktv.stream/playlist.m3u8
- SRK — Backup — https://srktv.net/srktvhls/cdnlive_srktv.m3u8
### star.jalsha.in (3 streams)
- Star Jalsha — Indian Bangla — https://catchup.yuppcdn.net/amazonv2/36/preview/starjalsha/master/chunklist.m3u8
- Star Jalsha — Backup — http://103.135.253.32:8080/STAR-JALSHA-HD/index.m3u8
- Star Jalsha — Backup — https://da86m1sqpm3o0.cloudfront.net/28072023/smil:starjalsha.smil/chunklist_b1928000.m3u8
### star.jalsha.movies.in (2 streams)
- Jalsha Movies — Indian Bangla — https://box.bbaria.net:8083/Jalsha_Movie/tracks-v1a1/mono.m3u8
- Jalsha Movies — Backup — http://103.135.253.32:8080/Jalsha_movies-HD/index.m3u8
### starmoviesselect.in@hd (2 streams)
- Star Movies Select — Indian Movies — http://103.135.253.32:8080/STAR-MOVIES-SEL/index.m3u8
- Star Movies Select — Backup — https://livetv.shamon-cable.net:8443/Star-movies-select/index.m3u8
### starsports2.in (2 streams)
- Star Sports 2 — Sports — https://tvsen7.aynaott.com/ssport2hd/index.m3u8
- Star Sports 2 — Backup — https://tvsen7.aynaott.com/ssport2hd/tracks-v1a1/mono.ts.m3u8
### studioyuva.in (2 streams)
- Studio Yuva — Indian Entertainment — https://mumt01.tangotv.in/O5aw8Zn3STUDIOYUVA/index.m3u8
- Studio Yuva — Backup — https://d2gvyg6lvauoko.cloudfront.net/230226/studioyuva/playlist.m3u8?hdnts=[REDACTED]
### suriyantv.in@sd (2 streams)
- Suriyan TV — Indian Entertainment — https://hlslive.olidigital.in/suriyantv/suriyantv/index.m3u8
- Suriyan TV — Backup — https://stream.ottlive.co.in/suriyantvtamil/index.m3u8
### taazatv.in@sd (2 streams)
- Taaza TV — Indian Entertainment — https://live.we2live.in/taazatv/live/playlist.m3u8
- Taaza TV — Backup — https://tvsen3.aynaott.com/yRMLky2j/index.m3u8
### tabbarhits.in (2 streams)
- Tabbar Hits — Indian Music — https://vglivessai.akamaized.net/sg/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/e11b0319-52e8-4190-ab03-3931cc68eac9/index.m3u8
- Tabbar Hits — Backup — https://livingindiaottlive.akamaized.net/tabbarhits/index.m3u8
### themovieclub.in@hd (2 streams)
- The Movie Club — Indian Movies — https://sis-global.prod.samsungtv.plus/v1/tvpprd/sc-mp2ar4ca425xo.m3u8
- The Movie Club — Backup — https://mumbai-edge.smartplaytv.in/TheMovieClub/index.m3u8
### tlc.in@hd (2 streams)
- TLC (India) — Documentary & Wildlife — https://drk6xq0vhn.gpcdn.net/live/tlc_hd_abr/index.m3u8
- TLC (India) — Backup — https://drk6xq0vhn.gpcdn.net/live/tlc_sd_abr/index.m3u8
### totalmusic.uk (2 streams)
- Totalmusic — International — https://cdn.global.elektamedia.com/live/c7eds/Totalmusic/SA_LIVE_hls_enc/master.m3u8
- Totalmusic — Backup — https://cdn.40mediagroup.com/live/c7eds/Totalmusic/SA_LIVE_hls_enc/master.m3u8
### ubangla.in (2 streams)
- U Bangla — Indian Bangla — https://stream.ottlive.co.in/ubangla/index.m3u8
- U Bangla — Backup — https://stream.ottlive.co.in/ubangla/tracks-v1a1/mono.m3u8
### ultimatetv.in@sd (2 streams)
- Ultimate TV — Indian Music — https://stream.ottlive.co.in/utvtamil/index.m3u8
- Ultimate TV — Backup — https://mumbai-edge.smartplaytv.in/utv/index.m3u8
### utvpalakkad.in@sd (2 streams)
- UTV Palakkad — Indian Entertainment — https://em4qj6nedyvg-hls-live.wmncdn.net/utv/ab2de115318ae40bdd434e193a2f2e7f.sdp/playlist.m3u8
- UTV Palakkad — Backup — https://em4qj6nedyvg-hls-live.wmncdn.net/liveunit/89b1e919eed04e59383cf820d644c20e.sdp/playlist.m3u8
### vanithatv.in@sd (2 streams)
- Vanitha TV — Indian Entertainment — https://mumt01.tangotv.in/O5aw8Zn3VANITHA/index.m3u8
- Vanitha TV — Backup — https://cdn.pishow.tv/ott/live/393/master.m3u8
### vendhartv.in@sd (2 streams)
- Vendhar TV — Indian Entertainment — https://mumt04.tangotv.in/m18aqlK4VENDHARTV/index.m3u8
- Vendhar TV — Backup — https://cdn.pishow.tv/ott/live/1271/master.m3u8
### yrfmusic.in (2 streams)
- YRF Music — Indian Music — https://amg01412-xiaomiasia-yrfmusic-xiaomi-1rmk2.amagi.tv/playlist/amg01412-xiaomiasia-yrfmusic-xiaomi/playlist.m3u8
- YRF Music — Backup — https://cdn-uw2-prod.tsv2.amagi.tv/linear/amg01412-xiaomiasia-yrfmusic-xiaomi/playlist.m3u8
### zeebangla.in@hd (6 streams)
- Zee Bangla — Indian Bangla — https://tvsen6.aynaott.com/ZeeBangla/index.m3u8
- Zee Bangla — Backup — https://iptvlive.ahmed-bd-org.workers.dev/zee-bangla-hd-2/index.m3u8
- Zee Bangla — Backup — https://livetv.shamon-cable.net:8443/ZEE-Bangla/index.m3u8
- Zee Bangla — Backup — https://raw.githubusercontent.com/ahan443/vibe-tv/refs/heads/main/ZeeBanglaHD.m3u8
- Zee Bangla — Backup — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/in/YuppTV/ZeeBanglaHD.m3u8
- Zee Bangla — Backup — https://yupptvcatchupire.yuppcdn.net/preview/zeebangla/2500.m3u8
### zeetelugu.in@hd (2 streams)
- Zee Telugu — Indian Entertainment — https://raw.githubusercontent.com/amazeyourself/adaptive-streams/refs/heads/main/streams/in/YuppTV/ZeeTeluguHD.m3u8
- Zee Telugu — Backup — https://listas-m3u8.github.io/iptv/128.19.173.10:8888/ZEETELUGUHD.m3u8
### zeetv.in@sd (3 streams)
- Zee TV — Indian Entertainment — http://41.205.93.154/ZEE-TV/index.m3u8
- Zee TV — Backup — http://103.135.253.32:8080/ZEE-TV/index.m3u8
- Zee TV — Backup — https://d47ddb99.wurl.com/master/f36d25e7e52f1ba8d7e56eb859c636563214f541/U2Ftc3VuZy1kZV9aZWVUVkhEVUtHZXJtYW55X0hMUw/playlist.m3u8
### zoom.in (3 streams)
- Zoom — Indian Music — https://d2esfk1pb9cdob.cloudfront.net/master.m3u8
- Zoom — Backup — https://dai.google.com/linear/hls/event/JCAm25qkRXiKcK1AJMlvKQ/master.m3u8
- Zoom — Backup — https://pubads.g.doubleclick.net/ssai/event/JCAm25qkRXiKcK1AJMlvKQ/master.m3u8

## Duplicate Primary Identities

None.

## Potential Near-Duplicate Primary Names (Review Only)

- Discovery [discovery.us] (Documentary & Wildlife); Discovery Channel (India) [discoverychannel.in@sd] (Documentary & Wildlife)

These are review suggestions only. The audit does not merge identities, change channel order, or remove streams.

## Primary Channel-Number Collisions

None.

## Primary Channel-Number Sequence

Contiguous numbering verified: 1–674.

## Malformed EXTINF Entries

None.

## Ordering

Category block order: OK.
Primary-category alphabetical/channel-number order: OK.
Backup/Review/New Channels/New Backups internal order is preserved for manual review and is intentionally not auto-enforced.

## Suspicious URLs

None.

## Signed / Tokenized Stream URLs

- **ETV Cinema** — Indian Movies — https://yupplivegcpusa.yuppcdn.net/100823/smil:etvcinema.smil/playlist.m3u8?hdnts=[REDACTED]
- **Songdew TV** — Indian Music — https://yuppnimrestreammum.akamaized.net/181224/smil:songdewtv.smil/playlist.m3u8?hdnts=[REDACTED]
- **Colors Super** — Indian Entertainment — https://d1rc86nwwc9fag.cloudfront.net/260723/smil:colorssuper1.smil/playlist.m3u8?hdnts=[REDACTED]
- **Zee Kannada** — Indian Entertainment — https://yuppnimresmum.akamaized.net/28072023/smil:zeekannadahd.smil/playlist.m3u8?hdnts=[REDACTED]
- **WOW Kidz Hindi** — Kids — https://yuppparoriglin.akamaized.net/181224/smil:wowkidzhindi.smil/playlist.m3u8?hdnts=[REDACTED]
- **WOW Kidz Tamil** — Kids — https://yuppparoriglin.akamaized.net/181224/smil:wowkidztam.smil/playlist.m3u8?hdnts=[REDACTED]
- **WOW Kidz Telugu** — Kids — https://yuppparoriglin.akamaized.net/181224/smil:wowkidztelgu.smil/playlist.m3u8?hdnts=[REDACTED]
- **Studio Yuva** — Backup — https://d2gvyg6lvauoko.cloudfront.net/230226/studioyuva/playlist.m3u8?hdnts=[REDACTED]

## Embedded Xtream-Style Credential Paths (redacted)

None.

## Logo Integrity

- Healthy/local references: **1005**
- External references (review only): **0**

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
