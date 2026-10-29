# IPTV Channel Discovery

Generated: **2026-10-29T01:09:19.381069+00:00**

- Sources: Bangladesh + India iptv-org country feeds
- **STRICT POLICY: Only verified Bangladesh and India channels are eligible. Bangladeshi news is allowed; Indian News and non-Islamic Religious channels are prohibited; Indian Kids and Sports channels are allowed.**
- Permanent denylist: E-Vidya 4, 5, 6, 7, 8, 9, 10, 11, 12 and Friends TV.
- Country-group threshold: **5** legitimate primary identities
- Existing prohibited review-queue rows removed: **0**
- New channels: **1**
- New backups: **1**
- Rejected/held candidates: **836**
- Country policy: only candidates verified as BD/IN (valid `.bd`/`.in` id, or repository-mapping evidence when the id is missing/malformed) are queued; conflicting or unverifiable candidates are held.

## Rejection reasons

- Indian news channel is prohibited: 266
- country not verified: id carries a non-BD/IN country suffix: 27
- country not verified: id country IN conflicts with BD source feed: 11
- duplicate stream URL: 377
- known Indian News or non-Islamic religious brand/category is prohibited: 21
- non-Islamic religious channel is prohibited: 107
- permanently banned channel: 10
- proxy/worker host: 2
- tokenized URL: 10
- unsupported stream path: 5

## New Channels

- Network 10 (720p) (India) — https://mumbai-edge.smartplaytv.in/Network10/index.m3u8

## New Backups

- Jalsha Movies HD (1080p) (India) — http://103.151.60.162:2122/play/a00x/index.m3u8?hls

## Stream verification

- Run timestamp: 2026-10-29T01:10:10+00:00
- Mode: iptv
- New entries and discovery queues probed: 58
- Verified live media responses: 26
- Primary entries retained but not conclusively verified: 14
- Dead/invalid entries and unverified backups removed: 18
- Duplicate discovery entries removed: 0
- Logo references localized to authentic repository assets: 0
- Logo references cleared because no authentic local asset was found: 0

### Stream probe details
- Retained Disney Channel (India) for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained HSTV for review — stream could not be conclusively verified (connection could not be confirmed: TimeoutError).
- Retained Nick Jr (India) for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Nickelodeon (India) for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Sonic for review — stream could not be conclusively verified (connection could not be confirmed: URLError).
- Retained Sony Sports Ten 1 for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Retained Sony Sports Ten 2 for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Retained Sony Sports Ten 3 Hindi for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Retained Sony Sports Ten 4 Kannada for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Retained Sony Sports Ten 5 for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Removed Star Sports 2 Hindi from New Channels — HTTP 404.
- Retained Star Sports 3 for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Retained Ten Cricket for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Retained Unite8 Sports 2 for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Removed VCV (720p) [Not 24/7] from New Channels — HTTP 404.
- Retained Vokta TV for review — stream could not be conclusively verified (HTTP 403; access/availability could not be confirmed).
- Removed Gyandarshan from New Backup — HTTP 404.
- Removed Hungama TV from New Backup — backup stream not verified (connection could not be confirmed: URLError).
- Removed Jalsha Movies from New Backup — backup stream not verified (HTTP 403; access/availability could not be confirmed).
- Removed Pogo from New Backup — backup stream not verified (HTTP 403; access/availability could not be confirmed).
- Removed Sony Sports Ten 1 from New Backup — backup stream not verified (connection could not be confirmed: URLError).
- Removed Star Jalsha from New Backup — backup stream not verified (HTTP 403; access/availability could not be confirmed).
- Removed Star Movies (India) from New Backup — backup stream not verified (HTTP 403; access/availability could not be confirmed).
- Removed Star Sports 2 from New Backup — backup stream not verified (HTTP 403; access/availability could not be confirmed).
- Removed Star Sports 2 from New Backup — HTTP 404.
- Removed Star Sports Select 1 from New Backup — backup stream not verified (HTTP 403; access/availability could not be confirmed).
- Removed Star Sports Select 2 from New Backup — backup stream not verified (HTTP 403; access/availability could not be confirmed).
- Removed StarPlus (India) from New Backup — backup stream not verified (connection could not be confirmed: URLError).
- Removed T Sports from New Backup — HTTP 404.
- Removed Travelxp from New Backup — backup stream not verified (HTTP 403; access/availability could not be confirmed).
- Removed Zee Bangla from New Backup — backup stream not verified (HTTP 403; access/availability could not be confirmed).
- Removed Zee Cinema from New Backup — backup stream not verified (HTTP 403; access/availability could not be confirmed).

## Final validation

- Run timestamp: 2026-10-29T01:10:11+00:00
- Validation status: PASS
- M3U entries parsed: 1161
- Malformed EXTINF/URL pairs: 0
- Duplicate stream URLs: 0
- New Channels/New Backup/Backup ordering: passed
- Discovery entries missing a logo (left blank rather than using a placeholder): 2
- Non-local discovery logo references: 0
- Geography/content policy issues: 0
- Existing non-discovery entries were not removed by the stream-validation step.
