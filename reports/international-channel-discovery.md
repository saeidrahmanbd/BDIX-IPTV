# International Channel Discovery

- Last scan: 2026-11-01 01:19 UTC
- Source: `https://iptv-org.github.io/iptv/index.category.m3u`
- Source records parsed: 12087
- Existing playlist records: 3307
- Existing logo references localized/repaired: 0
- Existing logo references removed because no safe local asset was available: 0
- Exact source URLs already in playlist: 2407
- Duplicate URLs within source feed: 1
- New eligible source records after URL/policy filtering: 26
- Country threshold: 5 unique primary identities for any retained dynamic country group.
- Automatic discovery is Movie/Music only for every country; News, Sports, Kids, Documentary/Wildlife, Religious, General/Entertainment and all other categories are rejected.
- New alternate streams are staged in New Backup; curated alternates remain in Backup.
- Only discovery queues are filtered; unrelated entries are preserved, with the five-channel threshold applied to dynamic country groups.
- The workflow probes newly discovered and queued stream URLs after candidate selection; inconclusive primary streams are retained for review and unverified backups are removed.
- New primary channels: 24
- New backup review entries: 2
- Category migrations: 0
- Existing discovery-queue entries removed: 2

## New primary channels

- **Komsan TV [Not 24/7]** — New Channels — KH — http://tv.cootel.com.kh:8077/streams/d/Komsan/playlist.m3u8
- **Alegria TV (720p)** — New Channels — ZZ — https://lbgo.bozztv.com/ssh101/ssh101/confirmatv/playlist.m3u8
- **ATN Music (360p)** — Bangladesh — BD — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI/atnmusic.stream/playlist.m3u8
- **D Music (1280p) [Not 24/7]** — New Channels — KH — http://43.252.18.195:5080/live/streams/WCVNews.playlist.m3u8
- **DanceTV EDM Mainstage (1080p)** — Estonia — EE — https://mbit1.worldcast.tv/dancetelevisionseven/multibit.m3u8
- **DanceTV Minimal Tech (1080p)** — Estonia — EE — https://mbit1.worldcast.tv/dancetelevisionsix/multibit.m3u8
- **Farra Play (576p)** — New Channels — ZZ — https://stream.farra.com.py/live/farra_low.m3u8
- **Galactica TV** — Peru — PE — https://stream.neux.site/memfs/e3f59eec-6b93-45e1-a2ab-c82381c2a9ec.m3u8
- **GMTV (1080p)** — United States — US — https://livechannel.mdc.akamaized.net/stitch/livechannel/1341/master1400000.m3u8;session=live_stream_1341
- **GO TV (720p)** — New Channels — ZZ — https://rds3.desdeparaguay.net/gotv/gotv/playlist.m3u8
- **Italianissimo (360p) [Not 24/7]** — New Channels — ZZ — https://vcp.myplaytv.com/italianissimo/italianissimo/playlist.m3u8
- **Jazz TV (1080p) [Not 24/7]** — North Macedonia — MK — https://stream.nasatv.com.mk/jazztv/hls/jazztv_live.m3u8
- **KandelaTV (480p)** — New Channels — ZZ — https://streamtv.intervenhosting.net:3718/live/kandelamedioslive.m3u8
- **La Hermandad Salsera (1080p) [Not 24/7]** — Colombia — CO — https://streamlov.alsolnet.com/hermandadsalsera/live/playlist.m3u8
- **La Voz del Tropico (480p) [Geo-blocked]** — New Channels — ZZ — https://ss2.tvrdomi.com:1936/lavozdeltropico/lavozdeltropico/playlist.m3u8
- **LaPuraCrema Television** — New Channels — ZZ — https://streamlov.alsolnet.com/lapuracrema/live/playlist.m3u8
- **Online TV Nusantara (720p) [Not 24/7]** — New Channels — ID — https://5bf7b725107e5.streamlock.net/onlinetvnusantara/onlinetvnusantara/playlist.m3u8
- **Oxigeno TV (360p) [Not 24/7]** — New Channels — ZZ — https://vcp.myplaytv.com/oxigenotv/oxigenotv/playlist.m3u8
- **Pluto TV Karaoke por Stingray (720p)** — United States — US — https://jmp2.uk/plu-604b99d633a72b00078e05ad.m3u8
- **Pluto TV Karaoke por Stingray LatAm (720p)** — United States — US — https://jmp2.uk/plu-5f85cf621d6d2200079f1de0.m3u8
- **Prattel TV (720p)** — Peru — PE — https://183.bozztv.com/ssh101/ssh101/pratteltvperu/playlist.m3u8
- **Rock TV (North Macedonia) (1080p) [Not 24/7]** — North Macedonia — MK — https://stream.nasatv.com.mk/rocktv/hls/rocktv_live.m3u8
- **Totovision** — New Channels — ZZ — https://cdn.streamhispanatv.net:3652/live/totovisiongtlive.m3u8
- **ZFM Zoetermeer TV (720p)** — Netherlands — NL — https://zfmzoetermeer.nl/live/master.m3u8

## Backup alternates

- **Zee Action** — IN — https://fta.ektv.in/live/270/master.m3u8
- **That's 70s** — GB — http://92.114.85.72:8000/play/a0lc

## Country Migrations


## Existing discovery-queue entries removed

- **YleX (720p)** — `Finland` — known radio station; not a linear TV channel
- **Zo'r TV (576p)** — `Uzbekistan` — general entertainment channel; not a dedicated Movies/Music channel

## Rejections

- TV series channel is not a dedicated Movie/Music channel: 8
- ambiguous Movie/Music classification: 2
- documentary/wildlife channel is prohibited: 170
- general entertainment is not a dedicated Movie/Music channel: 55
- kids channel is prohibited: 252
- news channel is prohibited: 1062
- non-real/test channel: 3
- religious channel is prohibited: 786
- source category is not Movies or Music: 6665
- sports channel is prohibited: 235
- test/VOD/non-TV name: 290
- unsafe or tokenized URL: 125

## Stream verification

- Run timestamp: 2026-11-01T01:20:00+00:00
- Mode: international
- New entries and discovery queues probed: 176
- Verified live media responses: 112
- Primary entries retained but not conclusively verified: 38
- Dead/invalid entries and unverified backups removed: 26
- Duplicate discovery entries removed: 0
- Country-group rows consolidated after stream probing: 0
- Logo references localized to authentic repository assets: 0
- Logo references cleared because no authentic local asset was found: 0

### Stream probe details
- Removed ATN Music (360p) from Bangladesh — HTTP 404.
- Removed La Hermandad Salsera (1080p) [Not 24/7] from Colombia — HTTP 404.
- Removed DanceTV EDM Mainstage (1080p) from Estonia — HTTP 404.
- Removed DanceTV Minimal Tech (1080p) from Estonia — HTTP 404.
- Removed ZFM Zoetermeer TV (720p) from Netherlands — HTTP 404.
- Removed Jazz TV (1080p) [Not 24/7] from North Macedonia — HTTP 404.
- Removed Rock TV (North Macedonia) (1080p) [Not 24/7] from North Macedonia — HTTP 404.
- Removed Galactica TV from Peru — HTTP 404.
- Removed Prattel TV (720p) from Peru — HTTP 404.
- Removed GMTV (1080p) from United States — HTTP 404.
- Removed Pluto TV Karaoke por Stingray (720p) from United States — HTTP 404.
- Removed Pluto TV Karaoke por Stingray LatAm (720p) from United States — HTTP 404.
- Retained 312 Kino for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained ACW UG TV for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Removed Alegria TV (720p) from New Channels — HTTP 404.
- Retained AMC (Afghanistan) for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained AMusic Channel for review — stream could not be conclusively verified (connection could not be confirmed: ConnectionResetError).
- Retained Canal+ Action Europe Slovakia for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Celestial Movies for review — stream could not be conclusively verified (HTTP 401; access/availability could not be confirmed).
- Retained CinemaWorld for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained CTB Perth Movies Channel for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Removed D Music (1280p) [Not 24/7] from New Channels — HTTP 404.
- Retained EBC Foreign Movie for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Removed Farra Play (576p) from New Channels — HTTP 404.
- Retained Galaxy TV [ ] for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Removed GO TV (720p) from New Channels — HTTP 404.
- Retained HBO Asia SD [ ] for review — stream could not be conclusively verified (response did not clearly identify a live media stream).
- Retained Hits 360 TV [ ] for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Removed Italianissimo (360p) [Not 24/7] from New Channels — HTTP 404.
- Retained Juice TV [ ] for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Removed KandelaTV (480p) from New Channels — HTTP 404.
- Retained Kantipur Max [ ] for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Retained Klasik [ ] for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Removed Komsan TV [Not 24/7] from New Channels — HTTP 404.
- Retained La 98.1 TV [ ] for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Removed La Voz del Tropico (480p) [Geo-blocked] from New Channels — HTTP 404.
- Removed LaPuraCrema Television from New Channels — HTTP 404.
- Retained LaXitosa Panama [ ] for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Marina TV for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Movify Kino for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Music [ ] for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Retained Music Information Channel for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained MuzzOne for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained My Cinema [ ] for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained NogoumFMTV for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Removed Online TV Nusantara (720p) [Not 24/7] from New Channels — HTTP 404.
- Retained OSN Movies Action for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Removed Oxigeno TV (360p) [Not 24/7] from New Channels — HTTP 404.
- Retained Pantalla Clasica EC [ ] for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Picosa TV for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Rakuten TV Family Movies Switzerland for review — stream could not be conclusively verified (HTTP 504; access/availability could not be confirmed).
- Retained Rotana Cinema Egypt for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Retained RTV Glas Drine [ ] for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Star Movies (Slovenia) for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Star Tamil Television for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained TeleMusik Senegal for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Thrill for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Removed Totovision from New Channels — HTTP 404.
- Retained Tropical Moon Cumbia TV for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained TV Arberia 4 Muzike for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained TV Arberia Retro Hits for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Zona Music TV (1080p) for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Removed That's 70s from New Backup — backup stream not verified (HTTP 403; access/availability could not be confirmed).
- Removed Zee Action from New Backup — HTTP 404.

## Final validation

- Run timestamp: 2026-11-01T01:20:00+00:00
- Validation status: PASS
- M3U entries parsed: 3305
- Malformed EXTINF/URL pairs: 0
- Duplicate stream URLs: 0
- New Channels/New Backup/Backup ordering: passed
- Discovery entries missing a logo (left blank rather than using a placeholder): 0
- Non-local discovery logo references: 0
- Geography/content policy issues: 0
- Existing non-discovery entries were not removed by the stream-validation step.
