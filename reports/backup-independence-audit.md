# IPTV Playlist Audit — Backup Independence and Claude Observations

Generated from the revised IPTV-Playlist.m3u on main on 2026-10-21. Endpoint path fragments are abbreviated to avoid echoing long token-like identifiers.

## Structural verification

- Playlist entries: **1064**
- Active primary entries: **631**
- Backup entries: **412**
- Not Playing entries: **21**
- Primary channel numbers: **1–631**, sequential and gap-free after category/A–Z sorting
- Active entries missing country or language: **0**
- Remaining entries with no country: **0**
- Remaining entries with no language: **0**
- Country/language fields backfilled from unambiguous primary identities: **135**
- Previously blank metadata fields completed in this pass: **24 fields across 12 records**
- Referenced logo files missing from logos/: **0**
- Attribute presence patterns: **4**; actual attribute order is standardized, optional-field presence still varies

## Direct fixes applied

- Removed **8** records matching the permanent-removal list that remained in the playlist: Grace Network, Jeremiah TV, Joshua TV, King TV, Dios Te Ve Kids, ZB Bhakti, CBN TV USA.
- Removed one Sparkle Movies Backup stream whose host/path matches the active feed and differs only by query parameters.
- Added Grace Network, Joshua TV, King TV, Jeremiah TV, CBN TV USA, Dios Te Ve Kids and ZB Bhakti to the permanent-removal rules because these are confirmed non-Islamic religious services.
- Promoted Sony Aath's existing Backup stream to Indian Bangla with IN/ben metadata; its stream URL was left unchanged.
- Renumbered active primary entries sequentially in category order and natural A–Z within categories; Backup and Not Playing are unnumbered.
- Standardized EXTINF attribute order while keeping channel-id and both URL-tvg/x-tvg-url header aliases for compatibility.
- Backfilled country/language from confirmed channel identity where possible; the still-unidentified Channel 52 is explicitly marked `ZZ/und` rather than assigned a guessed identity.
- Corrected high-confidence metadata: Asianet (Malayalam), DD Goa (Konkani), DD Sahyadri (Marathi), Kairali Arabia (Malayalam), Food Food (Hindi), TRT Müzik (Turkish), Kronehit (Austria/German), Arirang (South Korea), MBC 1/MBC 4 (Arabic), Wild Flix Hindi and XXTreme Jobs Hindi (India/Hindi), and Afarin TV (Iraq/Kurdish).
- Corrected the stream/name mismatch Young Bollywood to Young Hollywood and used the existing young-hollywood.png logo.
- Normalized title case for Love Nature, JTV Classic, Get Factual, Bahrain Quran, GREAT! Movies and GREAT! Romance.
- Re-categorized Wild TV to Documentary & Wildlife; Food Network, Cooking Channel, HGTV and Stingray The Spa to International; Food Food to Indian Entertainment.

## Backup independence

- **90** Backup/primary pairs share a hostname and match by channel identity. Shared hosting alone does not prove that streams are identical.
- **39** of those pairs also share a normalized path or route after ignoring protocol/query and common manifest suffixes.
- Only the exact Sparkle Movies query-only duplicate was removed automatically. Other index/playlist/master/tracks/chunklist variants are reported for manual checking rather than deleted.

| Channel | Host | Primary path suffix | Backup path suffix | Match class |
|---|---|---|---|---|
| Aakaash Aath | mumt03.tangotv.in | /Dsly5z3HAAKASHAATH/index.m3u8 | /Dsly5z3HAAKASHAATH/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Amrita TV | ddash74r36xqp.cloudfront.net | /master.m3u8 | /master_2000.m3u8 | same host only |
| Ananda TV | app24.jagobd.com.bd | /[opaque-id]/anandatv.stream/index.m3u8 | /[opaque-id]/anandatv.stream/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| ARY Q TV | aryqtvm.aryzap.com | /v1/[opaque-id]/[opaque-id]/ARYQTVH264_1080p.m3u8 | /v1/[opaque-id]/[opaque-id]/ARYQTVH264_720p.m3u8 | same host only |
| Asian TV | tvsen6.aynaott.com | /pKb5k6NnzxsKpWUs6E8M/tracks-v1a1/mono.ts.m3u8 | /pKb5k6NnzxsKpWUs6E8M/index.m3u8 | same route with manifest suffix variation |
| ATN Bangla | tvsen5.aynaott.com | /atnbangla/index.m3u8 | /P3y2URgG7LDe/index.m3u8 | same host only |
| ATN Bangla | tvsen5.aynaott.com | /atnbangla/index.m3u8 | /P3y2URgG7LDe/tracks-v1a1/mono.ts.m3u8 | same host only |
| ATN Bangla UK | app.ncare.live | /live-orgin/atnbanglauk-off.stream/playlist.m3u8 | /[opaque-id]/atnbanglauk-off.stream/playlist.m3u8 | same host only |
| ATN News | tvsen6.aynaott.com | /da6WMXAk/index.m3u8 | /da6WMXAk/tracks-v1a1/mono.ts.m3u8 | same route with manifest suffix variation |
| Balle Balle | mcncdndigital.com | /balleballetv/index.m3u8 | /balleballetv/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Bangla Vision | tvsen5.aynaott.com | /banglavision/index.m3u8 | /banglavision/tracks-v1a1/mono.ts.m3u8 | same route with manifest suffix variation |
| Bangla Vision | tvsen5.aynaott.com | /banglavision/index.m3u8 | /tgUzpPc9r6xw/index.m3u8 | same host only |
| Bangla Vision | tvsen5.aynaott.com | /banglavision/index.m3u8 | /tgUzpPc9r6xw/tracks-v1a1/mono.ts.m3u8 | same host only |
| beIN SPORTS XTRA | bein-esp-xumo.amagi.tv | /playlistR1080p.m3u8 | /playlistR720P.m3u8 | same host only |
| BHI Channel | server.livelegitpro.in | /bhichannel/bhichannel/index.m3u8 | /bhichannel/bhichannel/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Bhojpuri Cinema | live-bhojpuri.akamaized.net | /liveabr/playlist.m3u8 | /liveabr/pub-iobhojpuqbu6yj/live_720p/chunks.m3u8 | same host only |
| Boishakhi TV | tvsen6.aynaott.com | /1d3uG9VCgrR9DRtWZM57/index.m3u8 | /1d3uG9VCgrR9DRtWZM57/tracks-v1a1/mono.ts.m3u8 | same route with manifest suffix variation |
| BTV Chattogram | tvsen6.aynaott.com | /TjGR1GcxKetHNVcMVxbq/index.m3u8 | /TjGR1GcxKetHNVcMVxbq/tracks-v1a1/mono.ts.m3u8 | same route with manifest suffix variation |
| CGTN Documentary | english-livebkali.cgtn.com | /live/doccgtn_1.m3u8 | /live/doccgtn.m3u8 | same host only |
| Channel 1 | stream.ottplus.live | /live/channel_1_hd_abr/index.m3u8 | /live/channel_1_hd_abr/live/channel_1_hd_720/chunks.m3u8 | same host only |
| Channel 24 | drk6xq0vhn.gpcdn.net | /live/channel_24_abr/index.m3u8 | /live/channel_24_abr/live/channel_24_720/chunks.m3u8 | same host only |
| Channel I | tvsen6.aynaott.com | /FNHpYvGZ7FkCE10PwTHm/index.m3u8 | /FNHpYvGZ7FkCE10PwTHm/tracks-v1a1/mono.ts.m3u8 | same route with manifest suffix variation |
| Channel S UK | app.ncare.live | /[opaque-id]/chsukoff.stream/playlist.m3u8 | /[opaque-id]/chsukoff.stream/live-orgin/chsukoff.stream/chunks.m3u8 | same host only |
| Colors Bangla | yupptvcatchupire.yuppcdn.net | /preview/colorsbanglahd/2500.m3u8 | /preview/colorsbanglahd/800.m3u8 | same host only |
| Colors Tamil | da86m1sqpm3o0.cloudfront.net | /28072023/smil:colorstamilhd11.smil/playlist.m3u8 | /28072023/smil:colorstamilhd11.smil/chunklist_b2628000.m3u8 | same route with manifest suffix variation |
| Dangal | live-dangal.akamaized.net | /liveabr/playlist.m3u8 | /liveabr/pub-iodang10p4al/live_720p/chunks.m3u8 | same host only |
| DBC News | tvsen6.aynaott.com | /pF66Tkz0qFwP2aMMqHyt/index.m3u8 | /pF66Tkz0qFwP2aMMqHyt/tracks-v1a1/mono.ts.m3u8 | same route with manifest suffix variation |
| DD Bangla | d3qs3d2rkhfqrt.cloudfront.net | /out/v1/[opaque-id]/index.m3u8 | /out/v1/[opaque-id]/index_3.m3u8 | same host only |
| Deewana | live20.bozztv.com | /giatvplayout7/giatv-209592/index.m3u8 | /giatvplayout7/giatv-209592/tracks-v1a1/mono.ts.m3u8 | same route with manifest suffix variation |
| Desi Channel | livestream.unlimitedcdn.com | /agm-dc/desi-channel/index.m3u8 | /agm-dc/desi-channel/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Discovery | drk6xq0vhn.gpcdn.net | /live/discovery_hd_abr/index.m3u8 | /live/discovery_sd_abr/index.m3u8 | same host only |
| Ekattor TV | tvsen6.aynaott.com | /EWDrV5QskgarZEUBb3pU/index.m3u8 | /EWDrV5QskgarZEUBb3pU/tracks-v1a1/mono.ts.m3u8 | same route with manifest suffix variation |
| Enter TV | live1.entertv.com.bd | /entertv/tracks-v1a1/mono.m3u8 | /entertv/index.fmp4.m3u8 | same host only |
| Enter10 Bangla | live-bangla.akamaized.net | /liveabr/pub-iobanglakp3sff/live_360p/chunks.m3u8 | /liveabr/playlist.m3u8 | same host only |
| Enter10 Bangla | live-bangla.akamaized.net | /liveabr/pub-iobanglakp3sff/live_360p/chunks.m3u8 | /liveabr/pub-iobanglakp3sff/live_240p/chunks.m3u8 | same host only |
| Enter10 Bangla | live-bangla.akamaized.net | /liveabr/pub-iobanglakp3sff/live_360p/chunks.m3u8 | /liveabr/pub-iobanglakp3sff/live_720p/chunks.m3u8 | same host only |
| Epic Bhojpuri | mumt01.tangotv.in | /O5aw8Zn3EPICBHOJPURI/index.m3u8 | /O5aw8Zn3EPICBHOJPURI/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Epic Bhojpuri Digital | cc-8hy4a26pz2uos.akamaized.net | /v1/master/[opaque-id]/cc-8hy4a26pz2uos/playlist.m3u8 | /v1/manifest/[opaque-id]/cc-8hy4a26pz2uos/[opaque-id]/3.m3u8 | same host only |
| G Series Drama | vods2.aynaott.com | /gseriesDrama/tracks-v1a1/mono.ts.m3u8 | /gseriesDrama/index.m3u8 | same route with manifest suffix variation |
| Goldmines | streams.tangotv.in | /GOLDMINES/ORIGIN/index.m3u8 | /GOLDMINES/ORIGIN/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Goldmines 2 | mumt03.tangotv.in | /Dsly5z3HGOLDMINES2/index.m3u8 | /Dsly5z3HGOLDMINES2/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Goldmines Action | mumt03.tangotv.in | /Dsly5z3HGOLDMINESACTION/index.m3u8 | /Dsly5z3HGOLDMINESACTION/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Goldmines Bollywood | streams.tangotv.in | /GOLDMINESBOLLYWOOD/ORIGIN/index.m3u8 | /GOLDMINESBOLLYWOOD/ORIGIN/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Goldmines Movies | streams.tangotv.in | /GOLDMINEMOVIES/ORIGIN/index.m3u8 | /GOLDMINEMOVIES/ORIGIN/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Gravitas Movies | d6dg3ebeih71x.cloudfront.net | /Gravitas_Movies.m3u8 | /v1/master/[opaque-id]/cc-jx9exbvh3yi8u/Gravitas_Movies.m3u8 | same host only |
| GREAT! Movies | amg01753-narrativeentert-greatmovies-samsunguk-7z6eh.amagi.tv | /playlist/[opaque-id]/playlist.m3u8 | /ts-eu-w1-n2/playlist/[opaque-id]/playlist.m3u8 | same host only |
| GREAT! Romance | amg01753-narrativeentert-greatchristmas-samsunguk-8atls.amagi.tv | /playlist/[opaque-id]/playlist.m3u8 | /ts-eu-w1-n2/playlist/[opaque-id]/playlist.m3u8 | same host only |
| History TV18 | n18syndication.akamaized.net | /bpk-tv/History_HD_NW18_MOB/output01/master.m3u8 | /bpk-tv/[opaque-id]/output01/master.m3u8 | same host only |
| Hum TV | drk6xq0vhn.gpcdn.net | /live/hum_tv_abr/index.m3u8 | /live/hum_tv_abr/live/hum_tv_720/chunks.m3u8 | same host only |
| Independent TV | drk6xq0vhn.gpcdn.net | /live/independent_tv_abr/index.m3u8 | /live/independent_tv_abr/live/independent_tv_720/chunks.m3u8 | same host only |
| InWild | amg00861-terninternation-inwild-samsunguk-w5wic.amagi.tv | /ts-eu-w1-n2/playlist/[opaque-id]/playlist.m3u8 | /playlist/[opaque-id]/playlist.m3u8 | same host only |
| Jago News 24 | app.ncare.live | /live-orgin/jagonews24.stream/playlist.m3u8 | /live-orgin/jagonews24.stream/live-orgin/jagonews24.stream/chunks.m3u8 | same host only |
| Khushboo Bangla | mumt01.tangotv.in | /[opaque-id]/index.m3u8 | /[opaque-id]/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Kronehit | bitcdn-kronehit.bitmovin.com | /v2/hls/playlist.m3u8 | /v2/hls/chunklist_b3128000.m3u8 | same route with manifest suffix variation |
| Lego Channel | dltiqboxjw21d.cloudfront.net | /index.m3u8 | /v1/master/[opaque-id]/cc-evri8jwgwmxus/index.m3u8 | same host only |
| Maasranga TV | mtv.sunplex.live | /MAASRANGA/index.m3u8 | /MAASRANGA/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Makkah TV | media2.streambrothers.com | /8122/8122/playlist.m3u8 | /8122/8122/chunklist_w1247854077.m3u8 | same route with manifest suffix variation |
| Manoranjan Movies | mumt04.tangotv.in | /[opaque-id]/index.m3u8 | /[opaque-id]/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| MH One Movies | mumt03.tangotv.in | /Dsly5z3HMHONEMOVIE/index.m3u8 | /Dsly5z3HMHONEMOVIE/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Mohona TV | tvsen6.aynaott.com | /AkyX5dunzju4cpo26dr7/tracks-v1a1/mono.ts.m3u8 | /AkyX5dunzju4cpo26dr7/index.m3u8 | same route with manifest suffix variation |
| My TV | tvsen6.aynaott.com | /XMpHaEf0ANBhv8w6NWR7/index.m3u8 | /XMpHaEf0ANBhv8w6NWR7/tracks-v1a1/mono.ts.m3u8 | same route with manifest suffix variation |
| Nagorik TV | box.bbaria.net | /Nagorik_TV/tracks-v1a1/mono.m3u8 | /Nagorik_TV/video.m3u8 | same host only |
| News 24 | tvsen6.aynaott.com | /cdgr3tw6WoG7JyRnLbi0/index.m3u8 | /cdgr3tw6WoG7JyRnLbi0/tracks-v1a1/mono.ts.m3u8 | same route with manifest suffix variation |
| NH BollyFlix | cc-r5hupcym5oehh.akamaized.net | /[opaque-id]/cc-r5hupcym5oehh/SBUM/RunnTV/BollyFlix_IN/BollyFlix_IN.m3u8 | /v1/manifest/[opaque-id]/cc-r5hupcym5oehh/[opaque-id]/0.m3u8 | same host only |
| NH BollyFlix | cc-r5hupcym5oehh.akamaized.net | /[opaque-id]/cc-r5hupcym5oehh/SBUM/RunnTV/BollyFlix_IN/BollyFlix_IN.m3u8 | /v1/manifest/[opaque-id]/cc-r5hupcym5oehh/[opaque-id]/0.m3u8 | same host only |
| NH BollyRaga | cc-up9j649x4thrj.akamaized.net | /[opaque-id]/cc-up9j649x4thrj/SBUM/RunnTV/BollyRaga_IN/BollyRaga_IN.m3u8 | /v1/manifest/[opaque-id]/cc-up9j649x4thrj/[opaque-id]/0.m3u8 | same host only |
| NTV | tvsen5.aynaott.com | /xV4jEKf3D9zc/index.m3u8 | /JHPxHAWonztVucyc4GzF/index.m3u8 | same host only |
| NTV | tvsen5.aynaott.com | /xV4jEKf3D9zc/index.m3u8 | /xV4jEKf3D9zc/tracks-v1a1/mono.ts.m3u8 | same route with manifest suffix variation |
| NTV Europe | app.ncare.live | /[opaque-id]/ntvuk00332211.stream/playlist.m3u8 | que-id]/ntvuk00332211.stream/live-orgin/ntvuk00332211.stream/chunks.m3u8 | same host only |
| Pardesi TV | stream.pardesitv.online | /pardesi/index.m3u8 | /pardesi/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Pitaara TV | d2lk5u59tns74c.cloudfront.net | /out/v1/[opaque-id]/index.m3u8 | /out/v1/[opaque-id]/index_5.m3u8 | same host only |
| Probashi TV | 158.69.24.53 | /probashi_tv/index.m3u8 | /probashi_tv/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Public Movies | mumt04.tangotv.in | /m18aqlK4PUBLICMOVIES/index.m3u8 | /m18aqlK4PUBLICMOVIES/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Quran TV | live.kwikmotion.com | anlive/shqurantv.smil/sharjahtvquranpublish/shqurantv_source/chunks.m3u8 | /sharjahtvquranlive/shqurantv.smil/playlist.m3u8 | same host only |
| R Plus Gold | vglivessai.akamaized.net | /sg/v1/master/[opaque-id]/[opaque-id]/index.m3u8 | /sg/v1/manifest/[opaque-id]/[opaque-id]/[opaque-id]/0.m3u8 | same host only |
| Ramdhenu | mumt01.tangotv.in | /O5aw8Zn3RAMDHENU/mpegts | /O5aw8Zn3RAMDHENU/index.m3u8 | same host only |
| Retro Music TV | stream.mediawork.cz | /retrotv/smil:retrotv2.smil/playlist.m3u8 | /retrotv//retrotvHQ1/playlist.m3u8 | same host only |
| Rongeen TV | server.thelegitpro.in | /rongeentv/rongeentv/index.m3u8 | /rongeentv/rongeentv/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| RTV | tvsen5.aynaott.com | /RtvHD/index.m3u8 | /ba47dHpDk3Se/index.m3u8 | same host only |
| RTV | tvsen5.aynaott.com | /RtvHD/index.m3u8 | /ba47dHpDk3Se/tracks-v1a1/mono.ts.m3u8 | same host only |
| Ruposhi Bangla | mumt05.tangotv.in | /87NeALx2RUPASIBANGLA/index.m3u8 | /87NeALx2RUPASIBANGLA/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Sangeet Bangla | mumt05.tangotv.in | /87NeALx2SANGEETBANGLA/index.m3u8 | /87NeALx2SANGEETBANGLA/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| Shubh Cinema TV | d393sxaxig6bax.cloudfront.net | /out/v1/[opaque-id]/index.m3u8 | /out/v1/[opaque-id]/index_8.m3u8 | same host only |
| Somoy TV | drk6xq0vhn.gpcdn.net | /live/somoy_tv_abr/index.m3u8 | /live/somoy_tv_abr/live/somoy_tv_720/chunks.m3u8 | same host only |
| Sony Entertainment TV | drk6xq0vhn.gpcdn.net | /live/sony_ent_hd_abr/index.m3u8 | /live/sony_ent_sd_abr/index.m3u8 | same host only |
| Sony Max | drk6xq0vhn.gpcdn.net | /live/max_hd_abr/index.m3u8 | /live/sony_max_sd_abr/index.m3u8 | same host only |
| Sony Max 2 | drk6xq0vhn.gpcdn.net | /live/max_2_abr/index.m3u8 | /live/max_2_abr/live/max_2_720/chunks.m3u8 | same host only |
| U Bangla | stream.ottlive.co.in | /ubangla/index.m3u8 | /ubangla/tracks-v1a1/mono.m3u8 | same route with manifest suffix variation |
| WildEarth | wildearth-plex.amagi.tv | /masterR1080p.m3u8 | /master.m3u8 | same host only |
| Zee Bangla | 103.151.60.162 | /play/a02p/index.m3u8 | /play/a011/index.m3u8 | same host only |

## Orphaned Backup migrations

All five previously identified Backup-only feeds were moved into their corresponding published groups without changing their stream URLs:

| Channel | New group | Country / language | Notes |
|---|---|---|---|
| 7X Punjabi | Indian Music | IN / pan | Punjabi-language music |
| Bangla Cinema | Indian Movies | IN / ben | Bengali-language cinema |
| Fashion One | International | GB / eng | Name capitalization normalized |
| PTV Sports | Pakistani | PK / urd | Existing metadata retained |
| Star Sports Select 1 | Sports | IN / eng | Canonical EPG/channel ID set to `StarSportsSelect1.in@SD` |

These are category migrations, not stream replacements. The five original URLs remain present exactly once, the five records are no longer in Backup, and active primary numbering was rebuilt from 1 through 631.

## Not Playing entries without primary or Backup match

Not Playing remains a review queue, not a published channel group:

| Channel | Endpoint host |
|---|---|
| Assam Talks | tvsen7.aynaott.com |
| Channel 52 | str24.l9574.com |
| Channel S | app24.jagobd.com.bd |
| Channel S | app.ncare.live |
| Channel S | app.ncare.live |
| Channel S | iptvlive.ahmed-bd-org.workers.dev |
| Epic Parivar | 103.151.60.162 |
| Nick | homair-tv-production.up.railway.app |
| Star Sports 1 | flussonic.defineatoz.com |
| Star Sports Select 2 | flussonic.defineatoz.com |
| Thikana | 5dd3981940faa.streamlock.net |

## Observations retained for review rather than guessed

- channel-id remains beside tvg-id for Playlist Studio/repository compatibility; both EPG URL aliases remain in the header.
- All referenced logo files exist. nvisionbd-verified prefixes, mixed JPG/PNG formats and local-logo names are not by themselves proof that the underlying image is wrong; these remain for visual/provenance review.
- Similar but distinct IDs/feeds (MyTime regional variants, Willow/Willow TV, Suriya/Suriyan, Baallee/Balle Balle, Goldmines/Goldmines 2, Documentary+ variants and Makkah Live/Makkah TV) were not merged without proof they are identical.
- All 12 previously blank country/language records now have values. The unidentified Channel 52 is explicitly marked `ZZ/und` rather than assigned an invented station identity.
- Tag TV and BSTV were retained because available evidence did not confidently establish these specific feeds as non-Islamic religious services.
- Afarin TV remains in Kids: its broadcaster describes it as a Kurdish children's education service that also includes Islamic programming: https://afarin.tv/About4.

## Non-Islamic religious-channel audit

The permanent-removal policy already covers the seven confirmed non-Islamic religious identities previously found in this playlist: Grace Network, Joshua TV, King TV, Jeremiah TV, CBN TV USA, Dios Te Ve Kids and ZB Bhakti. No matching entry remains in the current playlist. The 22 entries remaining in the `Religious` group are Islamic religious services. TBN24, Tag TV and BSTV were not removed because the playlist entries available for those channels do not establish them as non-Islamic religious services.

## Verification

- Re-parsed the final M3U before publication.
- Confirmed no identity in the permanent-removal allowlist remains.
- Confirmed channel numbers cover the complete primary range with no gaps and Backup/Not Playing entries are unnumbered.
- Confirmed active metadata completeness and all referenced local logo paths before publishing.
