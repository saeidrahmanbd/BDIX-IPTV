# IPTV Channel Discovery

Generated: **2026-11-19T01:11:03.476105+00:00**

- Sources: Bangladesh + India iptv-org country feeds
- **Discovery scope: Bangladesh and India source feeds. Feed context sets content-policy scope; country metadata is retained as supplied and is not a discovery gate.**
- Bangladesh channels of all genres are eligible. Indian Kids and Sports channels are eligible, explicitly including cricket and football; Indian News, Religious (including Islamic), Educational, Knowledge and Business/Finance channels remain prohibited.
- Permanent denylist: E-Vidya 4–12, Friends TV, HSTV, and 31 additional channel IDs/names listed in the canonical permanent denylist.
- Country-group threshold: **5** legitimate primary identities
- Existing manual-review queue rows changed by discovery: **0**
- New channels: **7**
- New backups: **9**
- Rejected/held candidates: **846**
- Country metadata, channel IDs, language and logos are advisory at this stage; retain uncertain values for owner review and repair later.

## Rejection reasons

- Indian business/finance channel is prohibited: 8
- Indian educational channel is prohibited: 7
- Indian knowledge channel is prohibited: 7
- Indian news channel is prohibited: 297
- Indian religious channel is prohibited: 114
- duplicate stream URL: 329
- known Indian prohibited MH One Prime channel is prohibited: 1
- known Indian prohibited brand/category is prohibited: 19
- permanently banned channel: 29
- proxy/worker host: 3
- tokenized URL: 12
- unsupported stream path: 20

## New Channels

- ATN Music (360p) (source feed: Bangladesh) — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI/atnmusic.stream/playlist.m3u8
- Anmol TV (576p) (source feed: India) — https://fta.ektv.in/live/256/master.m3u8
- Captain (576p) (source feed: India) — https://fta.ektv.in/live/173/master.m3u8
- ETV Life (1080p) (source feed: India) — https://mumbai-edge.smartplaytv.in/ETVLIFE/index.m3u8
- ETV Telugu HD (1080p) (source feed: India) — https://mumbai-edge.smartplaytv.in/ETVHD/index.m3u8
- Jaya Plus (576p) (source feed: India) — https://mumbai-edge.smartplaytv.in/JayaPLus/index.m3u8
- Win TV (576p) (source feed: India) — https://mumbai-edge.smartplaytv.in/WINTV/index.m3u8

## New Backups

- Green TV (1080p) (source feed: Bangladesh) — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI2/greentv.stream/live-orgin/greentv.stream/playlist.m3u8
- Peace TV Bangla (1080p) (source feed: Bangladesh) — http://103.135.253.32:8080/Pace-TV-Bangla/index.m3u8
- T Sports (1080p) (source feed: Bangladesh) — https://tvsen5.aynaott.com/TnMn5kZz8aLm/index.m3u8
- DD Assam (576p) (source feed: India) — https://fta.ektv.in/live/672/master.m3u8
- DD Manipur (576p) (source feed: India) — https://fta.ektv.in/live/671/master.m3u8
- DD Nagaland (576p) (source feed: India) — https://fta.ektv.in/live/670/master.m3u8
- DD Tripura (576p) (source feed: India) — https://fta.ektv.in/live/661/master.m3u8
- ETV Music (1080p) (source feed: India) — https://mumbai-edge.smartplaytv.in/ETVABHIRUCHI/index.m3u8
- Vanitha TV (576p) (source feed: India) — https://mumbai-edge.smartplaytv.in/VanithaTV/index.m3u8

## Stream verification

- Run timestamp: 2026-11-19T01:11:05+00:00
- Mode: iptv
- New entries and discovery queues probed: 16
- Verified live media responses: 0
- Verified new primary channels automatically promoted: 0
- Verified alternate streams moved to Backup: 0
- Inconclusive candidates retained for manual review: 1
- Definitively dead new candidates removed: 15
- Duplicate newly discovered stream entries removed: 0
- Country-group rows consolidated after stream probing: 0
- Logo references localized to authentic repository assets: 0
- IPTV manual-review candidates needing later local-logo repair (warning only): 1
- International candidates held for missing local logos: 0

### Stream probe details
- Removed newly discovered ATN Music (360p) from New Channels — HTTP 404.
- Removed newly discovered Anmol TV (576p) from New Channels — HTTP 404.
- Removed newly discovered Captain (576p) from New Channels — HTTP 404.
- Removed newly discovered ETV Life (1080p) from New Channels — HTTP 404.
- Removed newly discovered ETV Telugu HD (1080p) from New Channels — HTTP 404.
- Removed newly discovered Jaya Plus (576p) from New Channels — HTTP 404.
- Removed newly discovered Win TV (576p) from New Channels — HTTP 404.
- Removed newly discovered Green TV (1080p) from New Backups — HTTP 404.
- Retained Peace TV Bangla (1080p) in New Backups for manual review — stream probe was inconclusive (connection could not be confirmed: URLError).
- Peace TV Bangla (1080p) has no verified local logo; kept in New Backups for later repair.
- Removed newly discovered T Sports (1080p) from New Backups — HTTP 404.
- Removed newly discovered DD Assam (576p) from New Backups — HTTP 404.
- Removed newly discovered DD Manipur (576p) from New Backups — HTTP 404.
- Removed newly discovered DD Nagaland (576p) from New Backups — HTTP 404.
- Removed newly discovered DD Tripura (576p) from New Backups — HTTP 404.
- Removed newly discovered ETV Music (1080p) from New Backups — HTTP 404.
- Removed newly discovered Vanitha TV (576p) from New Backups — HTTP 404.

## Final validation

- Run timestamp: 2026-11-19T01:11:05+00:00
- Validation status: PASS
- New manual-review candidates retained: 1
- New malformed EXTINF/URL pairs: 0
- New duplicate stream URL occurrences: 0
- New candidates missing an authentic local logo: 1 (warning only)
- New candidates with non-local logo references: 1 (warning only)
- New candidates with country metadata requiring manual review: 1 (warning only)
- New candidates outside New Channels/New Backups: 0
- Existing playlist defects, country metadata and logo completeness do not block discovery.
- New candidates remain in New Channels/New Backups for owner review; only definitively dead streams are removed.

## Post-run targeted correction

- 2026-11-19T01:18:00+00:00 — Reused the existing authentic repository asset `logos/peace-tv-bangla.png` for **Peace TV Bangla (1080p)** in New Backups. The new candidate no longer uses an external logo URL. Its stream probe remained inconclusive, so it stays in New Backups for manual review.
