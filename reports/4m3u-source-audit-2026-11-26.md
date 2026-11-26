# Full source playlist audit — 2026-11-26

Source: uploaded `4.m3u` (SM IPTV MAIN PLAYLIST), 2,550 entries.

## Final candidate result

| Classification | Count | Handling |
|---|---:|---|
| Genuine new channel identity | **1** | Staged in `New Channels` |
| New alternative streams for existing identities | **11** | 4 already staged in open PR #389; 7 staged in `New Backups` |
| New backup entries staged by this PR | **7** | Hidden from Xtream pending playback verification |

## New channel candidate

| Channel | Country | Genre | Source line | Stream |
|---|---|---|---:|---|
| PowerTürk TV | TR | Turkish music | 921 | https://livetv.powerapp.com.tr/powerturkTV/powerturkhd.smil/playlist.m3u8 |

The source identity was absent from the repository's channel identity index. PowerApp's official page identifies PowerTürk TV and offers live viewing; independent channel listings classify it as a Turkish music channel and list the same stream endpoint. It therefore fits the non-Bangladesh/India music eligibility rule. Playback from the repository runner has not been independently confirmed, so it remains in the hidden `New Channels` queue.

References:
- Official PowerApp channel page: https://www.powerapp.com.tr/tvs/power-tvs/powerturktv/
- Channel schedule: https://www.powerapp.com.tr/powerturk/sayfalar/powerturk-tv-yayin-akisi-1.html
- Independent public playlist listing the same endpoint and Turkish metadata: https://github.com/tecobaba/tecom3u/blob/main/guncel.m3u

## Alternative streams for existing identities

### Already staged in open PR #389 (4)

| Channel | Source line | Status |
|---|---:|---|
| 9X Tashan | 17 | In PR #389; owner-reported playback verified |
| FIFA+ | 549 | In PR #389; owner-reported playback verified |
| T Sports | 663 | In PR #389; owner-reported playback verified |
| Goldmines Bollywood | 899 | In PR #389; owner-reported playback verified |

### Newly staged in `New Backups` by this PR (7)

| Existing channel identity | Source label | Source line |
|---|---|---:|
| Asian TV | Asian TV | 35 |
| Dangal 2 | Dangal 2 | 115 |
| Goldmines | Goldmines | 177 |
| Mohona TV | Mohona TV | 239 |
| Independent TV | Independent TV | 449 |
| The Q India | TheQ | 379 |
| Travelxp English | Travel XP | 927 |

The seven streams reuse the existing channel IDs, country/language metadata and repository-local logos. They are staged in `New Backups`, not promoted to live `Backup`, because this audit did not independently confirm playback. The queue is excluded from Xtream publication.

## Source filtering and accounting

| Filter/result | Count |
|---|---:|
| Source entries | 2,550 |
| Credential/token-pattern URLs (including `uid` / `deviceMac`) | 1,398 |
| Proxy/worker routes | 27 |
| VOD/non-live endpoints | 4 |
| Repeated URL occurrences removed after retaining one copy | 53 |
| **Unique direct stream URLs remaining** | **1,068** |

Explicit default ports were canonicalized for duplicate comparison. For example, Thikana's source URL with `:443` is the same endpoint as the existing URL without the default HTTPS port; it is not counted as a new backup.

## Other reviewed unmatched entries

- `G series` / `Drama 24`: VOD host and duplicate URL; rejected.
- `Test Live TV`: duplicate of the existing Deepto TV URL; not a new candidate.
- `BBC News`, `Talk Sport`, and `Enter 10 Bangla`: source URLs already exist in the repository playlist.
- `DW News`, `OAN`, `CNBC TV`, `Assam Talks`, `Kolkata TV`, and `TV9 Bangla`: news/business or other non-eligible genres under the current country/genre rules.
- `3ABN Kids`, `Dios Te Ve Kids`, and `TVC Arabic Kids`: Kids category; not eligible under the applicable foreign-country rules.
- `CMAC TV`: foreign community/public-access channel, not an eligible movie/music channel.
- `Thikana`: same stream endpoint as the existing Thikana TV primary after default-port normalization.

## Safeguards

- Missing `tvg-id`, country metadata, or logo was never a disqualification.
- The source playlist's group labels were treated as hints only; its `Bnagla` label is demonstrably misapplied.
- Review entries in the existing playlist were not treated as rejected identities.
- Existing primary streams were not replaced.
- Removed one pre-existing empty Zoom `#EXTINF` record with no following stream URL; no stream URL was deleted.
- The seven unverified alternatives and PowerTürk TV are staged only in the hidden queues; no unverified candidate was exposed in the live Xtream output.
