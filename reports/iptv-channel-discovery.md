# IPTV Channel Discovery

Generated: **2026-11-21T07:42:56+06:00** (Asia/Dhaka)

- Sources: Bangladesh + India iptv-org country feeds
- **Discovery scope: Bangladesh and India source feeds. Feed context sets content-policy scope; country metadata is retained as supplied and is not a discovery gate.**
- Bangladesh channels of all genres are eligible. Indian News, Sports, Kids, Education, Knowledge, Business/Finance and non-Islamic Religious channels are prohibited in this IPTV playlist; Islamic religious channels remain eligible.
- Previously admitted prohibited Indian queue rows purged: **13**
- Existing orphan New Backups moved to New Channels: **9**
- Existing New Channels moved to New Backups because a primary channel already exists: **0**
- Duplicate queue rows removed during role normalization: **2**
- Existing discovery-queue logo URLs were converted to verified local /logos/ paths or removed when no matching local asset existed; no placeholder art was used.
- Permanent denylist: E-Vidya 4–12, Friends TV, HSTV, and 31 additional channel IDs/names listed in the canonical permanent denylist.
- Country-group threshold: **5** legitimate primary identities
- Only discovery queue rows were purged, reclassified or logo-normalized; unrelated primary playlist entries were preserved.
- New channels: **5**
- New backups: **5**
- Rejected/held candidates: **908**
- Country metadata, channel IDs, language and logos are advisory at this stage; retain uncertain values for owner review and repair later.

## Rejection reasons

- Indian business channel is prohibited: 9
- Indian education channel is prohibited: 7
- Indian kids channel is prohibited: 24
- Indian knowledge channel is prohibited: 15
- Indian news channel is prohibited: 304
- Indian religious channel is prohibited: 121
- Indian sports channel is prohibited: 16
- channel country CA is outside Bangladesh/India: 1
- channel country NL is outside Bangladesh/India: 2
- channel country PK is outside Bangladesh/India: 1
- duplicate channel identity already staged in a discovery queue: 4
- duplicate stream URL: 329
- known Indian prohibited MH One Prime channel is prohibited: 1
- known Indian prohibited brand/category is prohibited: 12
- permanently banned channel: 31
- proxy/worker host: 1
- tokenized URL: 10
- unsupported stream path: 20

## New Channels

- ATN Music (360p) (source feed: Bangladesh) — https://app.ncare.live/c3VydmVyX8RpbEU9Mi8xNy8yMDE0GIDU6RgzQ6NTAgdEoaeFzbF92YWxIZTO0U0ezN1IzMyfvcGVMZEJCTEFWeVN3PTOmdFsaWRtaW51aiPhnPTI/atnmusic.stream/playlist.m3u8
- Anmol TV (576p) (source feed: India) — https://fta.ektv.in/live/256/master.m3u8
- Captain (576p) (source feed: India) — https://fta.ektv.in/live/173/master.m3u8
- Jaya Plus (576p) (source feed: India) — https://mumbai-edge.smartplaytv.in/JayaPLus/index.m3u8
- Win TV (576p) (source feed: India) — https://mumbai-edge.smartplaytv.in/WINTV/index.m3u8

## New Backups

- DD Assam (576p) (source feed: India) — https://fta.ektv.in/live/672/master.m3u8
- DD Manipur (576p) (source feed: India) — https://fta.ektv.in/live/671/master.m3u8
- DD Nagaland (576p) (source feed: India) — https://fta.ektv.in/live/670/master.m3u8
- DD Tripura (576p) (source feed: India) — https://fta.ektv.in/live/661/master.m3u8
- Vanitha TV (576p) (source feed: India) — https://mumbai-edge.smartplaytv.in/VanithaTV/index.m3u8

## Existing queue-role corrections

- Moved from New Backups to New Channels: ETV Plus HD (1080p)
- Moved from New Backups to New Channels: &pictures HD (1080p)
- Moved from New Backups to New Channels: Sony Max HD (1080p)
- Moved from New Backups to New Channels: Travelxp 4K HDR (2160p) [Geo-blocked]
- Moved from New Backups to New Channels: Sony SAB HD (1080p)
- Moved from New Backups to New Channels: Star Gold HD (1080p)
- Moved from New Backups to New Channels: Star Gold Select HD (1080p)
- Moved from New Backups to New Channels: Star Movies (India) HD (1080p)
- Moved from New Backups to New Channels: Star Movies Select HD (1080p)
- Duplicate queue row removed: MNX HD (1080p)
- Duplicate queue row removed: Sony Max (720p)

## Stream verification

- Run timestamp: 2026-11-21T07:42:57+06:00
- Mode: iptv
- New entries and discovery queues probed: 10
- Verified live media responses: 0
- Verified new primary channels retained in New Channels: 0
- Verified alternate streams retained in New Backups: 0
- Inconclusive candidates retained for manual review: 0
- Unverified backup streams moved to Review: 0
- Definitively dead new candidates removed: 10
- Duplicate newly discovered stream entries removed: 0
- Country-group rows consolidated after stream probing: 0
- Logo references localized to authentic repository assets: 0
- Candidates retained without authentic local logos (no placeholder used): 0

### Stream probe details
- Removed newly discovered DD Assam (576p) from New Backups — HTTP 404.
- Removed newly discovered DD Manipur (576p) from New Backups — HTTP 404.
- Removed newly discovered DD Nagaland (576p) from New Backups — HTTP 404.
- Removed newly discovered DD Tripura (576p) from New Backups — HTTP 404.
- Removed newly discovered Vanitha TV (576p) from New Backups — HTTP 404.
- Removed newly discovered ATN Music (360p) from New Channels — HTTP 404.
- Removed newly discovered Anmol TV (576p) from New Channels — HTTP 404.
- Removed newly discovered Captain (576p) from New Channels — HTTP 404.
- Removed newly discovered Jaya Plus (576p) from New Channels — HTTP 404.
- Removed newly discovered Win TV (576p) from New Channels — HTTP 404.

## Final validation

- Run timestamp: 2026-11-21T07:42:58+06:00
- Validation status: PASS
- New manual-review candidates retained: 0
- New malformed EXTINF/URL pairs: 0
- New duplicate stream URL occurrences: 0
- New candidates missing an authentic local logo: 0 (warning only)
- New candidates with non-local logo references: 0 (warning only)
- New candidates with country metadata requiring manual review: 0 (warning only)
- New candidates outside New Channels/New Backups or approved Review holds: 0
- Out-of-scope/prohibited Indian rows remaining in New Channels/New Backups: 0
- Discovery queue rows with non-local/broken logos: 0
- New Backup identity/duplicate-primary issues: 0
- Existing unrelated playlist defects and incomplete nonessential country metadata do not block discovery.
- New Channels retains primary candidates for owner review; only verified alternates remain in New Backups, and inconclusive alternates are held in Review.
