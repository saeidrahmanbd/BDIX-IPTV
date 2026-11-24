# Channel Identity Audit — 2026-11-07

## Scope and method

- Audited the current `main` versions of `IPTV-Playlist.m3u` and `International-Playlist.m3u`.
- Excluded every row whose `group-title` is `Adult`; no Adult entry was inspected or changed.
- Compared normalized channel names, `tvg-id`, group, and exact stream URL.
- Stream URLs are intentionally omitted from this report to avoid publishing credentials or signed tokens.

## Structural results

| Measure | Result |
|---|---:|
| Non-Adult playlist rows | 3,683 |
| Distinct normalized channel names | 2,296 |
| Distinct non-empty `tvg-id` values | 2,431 |
| Exact stream URLs assigned multiple `tvg-id` values | 168 |
| Exact stream URLs listed under different channel names | 82 |
| Normalized channel-name groups with multiple stream URLs | 358 |
| `tvg-id` values associated with multiple stream URLs | 327 |

These are structural conflict counts, not counts of confirmed wrong broadcasts. Multiple URLs may be legitimate mirrors, regional feeds, or quality variants. A feed ID such as `@HD`, `@SD`, or a region suffix can be meaningful and must not be stripped automatically.

## High-priority identity conflicts

| Playlist rows | Names / IDs | Finding |
|---|---|---|
| IPTV: 67; International: 570 | Ekushey TV / `EkusheyTV.bd` vs ETV / `custom.etv-yddbw` | Same exact stream URL, different channel names and IDs; ETV is also categorized as Indian Entertainment. |
| IPTV: 71; International: 62 | G Series Drama / `GSeriesDrama.bd` vs Drama 24 / `custom.bdix.drama-24` | Same exact stream URL is assigned to two different channel identities. |
| IPTV: 275; International: 316 | NH BollyFlix / `NHBollyFlix.in` vs The Movie Club / `TheMovieClub.in@HD` | Same exact stream URL is labelled as two different services. |
| IPTV: 337; International: 330 | 7X Punjabi / `7XPunjabi.in` vs 7X Music / `7XMusic.in@SD` | Same exact stream URL is assigned to different channel identities. |
| IPTV: 1035; International: 5146 | Discovery / `Discovery.us` vs Discovery Channel (India) / `DiscoveryChannel.in@SD` | Same exact stream URL is assigned US and India identities. |
| IPTV: 651; International: 5844 | NTV Malayalam / `NTV.in` vs NTV / `NTV.bd` | Same exact stream URL is labelled as two different channels. |
| IPTV: 443; International: 314 | Thalaa TV / `ThalaaTV.in` vs Thalaa TV / `ThalaaTV.in@HD` | Same exact stream URL appears in Indian Music and Indian Movies. |
| IPTV: 461; International: 340 | Aaryaa TV / `AaryaaTV.in` vs Aaryaa TV / `AaryaaTV.in@SD` | Same exact stream URL appears in Indian Entertainment and Indian Music. |
| IPTV: 641; International: 632 | MNTV (Tamil) / `MarutamTV.in` vs Marutam TV / `MarutamTV.in@SD` | Same exact stream URL, different IDs and display names. |
| IPTV: 193, 1966; International: 182, 184, 5260 | Star Jalsha / `Star.Jalsha.in` and `StarJalsha.in@HD` | Multiple feed URLs and two IDs are present across the playlists; verify the alternate feed before treating it as an equivalent backup. |

## Interpretation

1. **Same URL, different channel identity** is the strongest metadata defect. The rows share one stream endpoint but advertise different channel identities. Correct the identity only after confirming which broadcaster is actually carried.
2. **Same channel name, different URLs** is not automatically an error. It is expected for genuine backup mirrors, regional feeds, SD/HD feeds, or time-shift feeds. These require playback comparison.
3. **Same ID, different URLs** is also not automatically an error. The URLs may be legitimate alternate sources for one channel, but should not be treated as equivalent until verified.
4. Category mismatches should be reviewed separately from broadcast identity.

## What has not been verified

This audit did not decode live video, capture frames, read on-screen channel logos, or compare simultaneous programme content. Playlist metadata and HTTP reachability cannot establish that two feeds broadcast the same programme. A media probe such as FFprobe can establish that a media stream is readable and expose technical stream metadata, but semantic channel identity still requires frame/logo/programme inspection.

## Safe remediation policy

- No playlist rows, URLs, logos, EPG mappings, or channel IDs were changed by this audit.
- Do not delete a row solely because it shares a name or ID with another row.
- Do not normalize away meaningful feed IDs such as HD/SD/region variants.
- Keep uncertain entries in place and mark them for human review rather than silently replacing them.
- Adult entries remain completely out of scope.
- Next verification stage: sample live frames from the high-priority pairs at the same time, compare on-screen logos/programme text, then classify each pair as same feed, legitimate regional/quality variant, different channel, or inconclusive.
