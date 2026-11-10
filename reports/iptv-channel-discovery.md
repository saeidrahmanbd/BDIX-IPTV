# IPTV Channel Discovery

Generated: **2026-11-10T12:35:42.655446+00:00**

- Sources: Bangladesh + India iptv-org country feeds
- **STRICT POLICY: Only verified Bangladesh and India channels are eligible. Bangladesh channels of all genres are eligible; Indian News, Religious (including Islamic), Educational/Knowledge and Business/Finance channels are prohibited; Indian Kids and Sports channels are prohibited.**
- Permanent denylist: E-Vidya 4–12, Friends TV, HSTV, and 31 additional channel IDs/names listed in the canonical permanent denylist.
- Country-group threshold: **5** legitimate primary identities
- Existing prohibited review-queue rows removed: **0**
- New channels: **11**
- New backups: **10**
- Rejected/held candidates: **860**
- Country policy: only candidates verified as BD/IN (valid `.bd`/`.in` id, or repository-mapping evidence when the id is missing/malformed) are queued; conflicting or unverifiable candidates are held.

## Rejection reasons

- Indian business/finance channel is prohibited: 8
- Indian educational channel is prohibited: 7
- Indian knowledge channel is prohibited: 14
- Indian news channel is prohibited: 289
- Indian religious channel is prohibited: 115
- country not verified: id carries a non-BD/IN country suffix: 27
- country not verified: id country IN conflicts with BD source feed: 10
- duplicate stream URL: 311
- known Indian prohibited MH One Prime channel is prohibited: 1
- known Indian prohibited brand/category is prohibited: 19
- permanently banned channel: 30
- proxy/worker host: 3
- tokenized URL: 12
- unsupported stream path: 14

## New Channels

- ATN Music (360p) (Bangladesh) — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI/atnmusic.stream/playlist.m3u8
- Anmol TV (720p) (India) — https://drk6xq0vhn.gpcdn.net/live/zee_anmol_abr/index.m3u8
- Captain (576p) (India) — https://fta.ektv.in/live/173/master.m3u8
- ETV Life (1080p) (India) — https://mumbai-edge.smartplaytv.in/ETVLIFE/index.m3u8
- ETV Telugu HD (1080p) (India) — https://mumbai-edge.smartplaytv.in/ETVHD/index.m3u8
- Jaya Plus (576p) (India) — https://mumbai-edge.smartplaytv.in/JayaPLus/index.m3u8
- MBC TV (576p) (India) — https://cdn.pishow.tv/ott/live/1017/master.m3u8
- Punjabi Beats HD (720p) (India) — https://mumt01.tangotv.in/O5aw8Zn3PUNJABIBEATSHD/index.m3u8
- TV 100 (India) (576p) (India) — https://fta.ektv.in/live/310/master.m3u8
- Win TV (576p) (India) — https://mumbai-edge.smartplaytv.in/WINTV/index.m3u8
- Zee Action (576p) (India) — https://fta.ektv.in/live/270/master.m3u8

## New Backups

- T Sports (1080p) (Bangladesh) — https://tvsen5.aynaott.com/TnMn5kZz8aLm/index.m3u8
- DD Assam (576p) (India) — https://fta.ektv.in/live/672/master.m3u8
- DD Manipur (576p) (India) — https://fta.ektv.in/live/671/master.m3u8
- DD Nagaland (576p) (India) — https://fta.ektv.in/live/670/master.m3u8
- DD Punjabi (576p) (India) — https://fta.ektv.in/live/177/master.m3u8
- DD Tripura (576p) (India) — https://fta.ektv.in/live/661/master.m3u8
- ETV Music (1080p) (India) — https://mumbai-edge.smartplaytv.in/ETVABHIRUCHI/index.m3u8
- FashionTV (India) (576p) (India) — https://fta.ektv.in/live/144/144_0.m3u8
- Jaihind TV (576p) (India) — https://fta.ektv.in/live/700/master.m3u8
- Vanitha TV (576p) (India) — https://mumbai-edge.smartplaytv.in/VanithaTV/index.m3u8

## Stream verification

- Run timestamp: 2026-11-10T12:35:47+00:00
- Mode: iptv
- New entries and discovery queues probed: 27
- Verified live media responses: 7
- Verified new primary channels automatically promoted: 0
- Verified alternate streams moved to Backup: 0
- Inconclusive candidates moved to Review: 0
- Primary entries retained but not conclusively verified: 1
- Definitively dead/invalid candidates removed: 19
- Inconclusive primary/backup candidates retained for manual review: 1
- Duplicate discovery entries removed: 0
- Country-group rows consolidated after stream probing: 0
- Logo references localized to authentic repository assets: 0
- Candidates without local logos moved to Review: 0
- Candidates removed for missing local logos (IPTV mode): 0

### Stream probe details
- Removed FashionTV from Review — HTTP 404.
- Removed Anmol TV from New Channels — HTTP 404.
- Removed Aryan TV National from New Channels — HTTP 404.
- Removed ATN Music from New Channels — HTTP 404.
- Removed Captain from New Channels — HTTP 404.
- Removed ETV Life from New Channels — HTTP 404.
- Removed ETV Telugu from New Channels — HTTP 404.
- Removed Jaya Plus from New Channels — HTTP 404.
- Removed Punjabi Beats from New Channels — HTTP 404.
- Moved Vokta TV to Review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Removed Win TV from New Channels — HTTP 404.
- Removed Zee Action from New Channels — HTTP 404.
- Removed DD Assam from New Backups — HTTP 404.
- Removed DD Manipur from New Backups — HTTP 404.
- Removed DD Nagaland from New Backups — HTTP 404.
- Removed DD Punjabi from New Backups — HTTP 404.
- Removed DD Tripura from New Backups — HTTP 404.
- Removed ETV Music from New Backups — HTTP 404.
- Removed T Sports from New Backups — HTTP 404.
- Removed Vanitha TV from New Backups — HTTP 404.

## Final validation

- Run timestamp: 2026-11-10T12:35:47+00:00
- Validation status: PASS
- M3U entries parsed: 1151
- Malformed EXTINF/URL pairs: 0
- Duplicate stream URLs: 0
- Review/New Channels/New Backups/Backup ordering: passed
- Discovery entries missing a logo (left blank rather than using a placeholder): 0
- Non-local discovery logo references: 0
- Geography/content policy issues: 0
- Existing non-discovery entries were not removed by the stream-validation step.
