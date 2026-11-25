# Daily IPTV Discovery Report — 2026-11-25

Generated: **2026-11-25T07:00:55+06:00** (Asia/Dhaka)  
Repository: [saeidrahmanbd/BDIX-IPTV](https://github.com/saeidrahmanbd/BDIX-IPTV)  
Audited main snapshot: **d630b7d2ae352f1308f1ecd6857fc3e2ed592c79**

**Overall status: PARTIAL.** Both discovery stages completed successfully and produced fresh dated reports. Independent checks found policy and validation blockers, so workflow success must not be interpreted as full playlist compliance.

This report uses the 25 November stage reports and current playlist blobs. It does not reuse the 24 November report.

## 1. IPTV-Playlist.m3u — Bangladesh and India

- Workflow: [IPTV New Channel Discovery #45509956351](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45509956351) — **completed successfully**
- Stage report: [iptv-channel-discovery.md](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/iptv-channel-discovery.md), generated 05:27:17 Bangladesh time
- Discovery commit: [7077d28 — Add IPTV candidates to manual review queues](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/7077d28cbc20d9365977de9058e2b38a3f1aed3c)

### Discovery and stream-probe results

The Bangladesh and India country feeds produced **13 New Channels candidates and 9 New Backups candidates**. The report recorded **823 rejected or held source candidates**.

The workflow probed 22 newly discovered/queued streams:

| Probe result | Count |
|---|---:|
| Live-media responses reported | 14 |
| Definitively dead candidates removed | 6 |
| Inconclusive alternative streams moved to Review | 2 |
| Duplicate newly discovered URLs removed | 0 |

Dead streams removed:
- ATN Music — HTTP 404
- Win TV — HTTP 404
- DD Assam — HTTP 404
- DD Manipur — HTTP 404
- DD Nagaland — HTTP 404
- DD Tripura — HTTP 404

Inconclusive alternatives:
- Duronto TV — TimeoutError
- B4U Music — URLError

The stage report records **0 verified new primary channels and 0 verified alternate streams retained**, even though 14 live-media responses were observed. The retained rows therefore remain manual-review candidates; do not treat the probe total as proof that every queued channel is fully verified.

### Current queue snapshot

| Group | Current entries |
|---|---:|
| New Channels | 11 |
| New Backups | 5 |
| Backup | 396 |
| Review | 238 |

New Channels currently contains:
- NAN TV
- Ayush Next Communication Network
- CCV
- Fast1
- Jaihind TV
- Kabaddi 24x7
- Metro TV (India)
- N Vision
- Wayanad Vision
- WeatherSpy (India)
- Zodiak TV

New Backups currently contains:
- Duronto TV
- B4U Music
- Epic Bharat Digital
- INWILD
- Mazhavil Manorama

The queues are in the required order: **New Channels → New Backups → Backup**. No new country group was created.

### Confirmed policy exceptions still in New Channels

Two retained candidates conflict with the explicit Indian-content exclusions:

1. **Ayush Next Communication Network** — the channel describes itself as a dedicated educational television platform. It is therefore outside the allowed IPTV discovery scope. Sources: [ANCN official channel description](https://www.youtube.com/channel/UCK-q1SXZ1kjiy1N1_iYR1bA) and [DD Free Dish channel/category information](https://www.freedish.in/2026/07/watch-ayush-next-channel-on-dd-free-dish.html).
2. **Jaihind TV** — its official live page identifies the live service as Malayalam news, and its official About page describes its journalism/news role. It is therefore an Indian news channel and must be excluded. Sources: [Jaihind TV Live](https://jaihindtv.in/live-tv) and [Jaihind TV About Us](https://www.jaihindtv.in/index.php/about).

These two rows were still present in New Channels in the audited snapshot. The workflow's final statement that zero prohibited Indian rows remain in the queues is therefore not supported by the channel-level evidence.

The other nine New Channels rows remain candidates for owner review; this report does not promote them to primary groups.

### Rejection reasons

| Rejection reason in stage report | Count |
|---|---:|
| Duplicate stream URL | 297 |
| Indian news | 293 |
| Indian religious category | 122 |
| Permanently banned candidates | 30 |
| Unsupported stream path | 19 |
| Indian kids | 13 |
| Known prohibited brand/category | 12 |
| Tokenized URL | 10 |
| Indian business | 9 |
| Indian education | 7 |
| Indian knowledge | 1 |
| Known prohibited MH One Prime | 1 |
| Duplicate identity already in discovery queue | 3 |
| Country metadata outside Bangladesh/India (CA, NL, PK) | 4 |
| Proxy/worker host | 2 |
| **Total** | **823** |

**Policy note:** the rejection label is the broad phrase “Indian religious channel is prohibited” for 122 records. The current rule excludes non-Islamic religious channels, not Islamic religious channels. The stage report does not provide an Islamic/non-Islamic split, so the exception is not demonstrated and possible over-filtering remains a blocker.

### Independent playlist checks

- Entries parsed: **1,354**
- Malformed EXTINF/URL pairs: **0**
- Duplicate stream URLs: **0**
- Queue placement: **passed**
- Four exact primary channel-ID groups have multiple rows outside Backup/New Backups: Dhoom Music, Sangeet Bangla, Colors Bangla Cinema and Jalsha Movies. These are existing primary-group identity collisions and need a targeted primary-versus-backup review; they were not auto-merged.
- Legacy scope warning: the playlist still contains a **Pakistani** group with 14 PK-country entries and an **International** group with 82 entries, 81 of whose country metadata values are outside Bangladesh/India. These existing rows were not broadly removed or reclassified.

## 2. International-Playlist.m3u

- Workflow: [International Channel Discovery #45511355409](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45511355409) — **completed successfully**
- Stage report: [international-channel-discovery.md](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/international-channel-discovery.md), stream verification completed 05:37:11 Bangladesh time
- Discovery commit: [f7e8b41 — International discovery changes](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/f7e8b41f26817e24ef64c60d990f4a48980b6701)

### Discovery and stream-probe results

- Source records parsed: **12,125**
- Existing playlist records at scan: **3,319**
- Eligible source records after policy/URL filtering: **148**
- New primary candidates staged before probing: **50**
- New backup candidates staged before probing: **5**
- Newly discovered/queued streams probed: **71**
- Live-media responses: **15**
- Verified new primary channels retained: **6**
- Verified alternative streams retained: **9**
- Definitively dead candidates removed: **53**
- Inconclusive candidates retained: **3**
- Duplicate newly discovered stream entries removed: **0**

### Current New Channels

Nine rows are currently present:

- Aurora Media Films
- BRIDGE Dance
- BRIDGE Jazz
- FMH Movies
- Galaxy
- Galaxy Premium
- Kinosvidanie
- Rotana Cinema KSA
- TVS Film Noir Network

Six were counted as verified new primaries. Three remain inconclusive:
- Galaxy — URLError
- Galaxy Premium — URLError
- TVS Film Noir Network — TimeoutError

Galaxy and Galaxy Premium use the proxy-named host proxy-v.rctiplus.id; neither stream was confirmed by the probe. TVS Film Noir Network also timed out. These three are held candidates, not verified additions. The detailed probe log leaves them in New Channels, although a summary sentence in the stage report says inconclusive primaries are held in Review; that wording does not match the actual queue.

BRIDGE Dance and BRIDGE Jazz are explicitly marked **Geo-blocked**. They are music-channel candidates, but access from Bangladesh is not established.

### Current New Backups

Nine alternative streams are present:

- Cinema (Russia)
- Dom kino
- Dorama
- Epic Music
- iFilm Persian
- Indiyskoye Kino
- KinoHit
- Muzyka Pervogo
- TRT Muzik

The stage report counts nine verified alternatives. No duplicate stream URLs were found.

### Adult and Fashion TV handling

- New Adult primary channels added directly to Adult: **0**
- New Fashion TV channels added directly to Fashion TV: **0**
- Existing Adult group: **366**
- Existing Fashion TV group: **5**

No Adult candidate was incorrectly placed in New Channels, and no Fashion TV candidate was discovered in this run.

### Rejection reasons

| Rejection reason in stage report | Count |
|---|---:|
| Source category not Movies or Music | 6,574 |
| News | 1,072 |
| Religious | 780 |
| Kids | 311 |
| Sports | 296 |
| Documentary & Wildlife | 191 |
| Unsafe or tokenized URL | 140 |
| Test/VOD/non-TV name | 300 |
| General entertainment | 68 |
| TV series | 24 |
| Permanently banned | 10 |
| Known Indian prohibited brand/category | 12 |
| Other specific/ambiguous categories | 3 |

The stage report's rejection and stream-probe details contain the full candidate-level list.

### Independent playlist checks

- Entries parsed: **3,321**
- Malformed EXTINF/URL pairs: **0**
- Duplicate stream URLs: **0**
- Duplicate primary channel IDs: **0**
- Queue placement: **passed**
- Country threshold: no new country group was created today. The current workflow configuration exempts Bangladesh and India from the five-identity threshold, whereas the current instruction requires five qualifying primary identities for every country. This is a configuration mismatch even though no new under-threshold group was created in this run.
- Fifteen same-display-name groups were identified across primary groups. IDs differ, so these are review signals rather than confirmed exact-ID duplicates; examples include Sony Movies, Trace Latina and several Adult entries.

### Legacy content-policy blockers

The discovery filter correctly rejects new out-of-scope source categories, but existing groups remain in the playlist. Current counts include:

| Existing group | Entries |
|---|---:|
| Indian Entertainment | 175 |
| News | 11 |
| Documentary & Wildlife | 129 |
| Kids | 149 |
| Religious | 30 |
| Sports | 183 |

These groups conflict with the current International Movies/Music/Fashion TV/Adult scope. They were not broadly deleted or reclassified because the preservation instruction prohibits a broad destructive cleanup. The workflow's PASS applies to its discovery validation, not to whole-playlist policy compliance.

## 3. Shared structure, queues and logo audit

### M3U and duplicate checks

| Validation | IPTV | International |
|---|---:|---:|
| Entries parsed | 1,354 | 3,321 |
| Malformed EXTINF/URL pairs | 0 | 0 |
| Duplicate stream URL groups | 0 | 0 |
| Exact duplicate primary channel-ID groups | 4 | 0 |
| Required queue order | Passed | Passed |

Both playlists retain their existing entries and group order. This run did not perform a broad playlist cleanup.

### Logo authenticity and locality

The current provenance report is [logo-provenance-review.md](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/logo-provenance-review.md), generated 06:21 Bangladesh time. Its counts are:

| Playlist | Officially verified | Third-party verified | Generated fallback | Needs review |
|---|---:|---:|---:|---:|
| IPTV-Playlist.m3u | 0 | 23 | 2 | 1,329 |
| International-Playlist.m3u | 0 | 988 | 0 | 2,333 |

The two IPTV generated-fallback assets are:
- Shikor TV Canada
- Ten TV Prime

The current logo-reference audit also finds four playlist-referenced Imgur missing-image placeholders in International:
- Armenia Premium
- CCTV-9
- TVS Music Network
- TVS Sports Bureau

The four placeholder files must not be treated as authentic broadcaster logos. The International playlist also has 401 rows without a logo attribute; blank is safer than inventing artwork.

All current nonblank logo attributes use raw GitHub URLs under this repository's logos tree, but the validators disagree about whether those URLs satisfy the strict local-only rule: the localization workflow logged zero non-repository references, while the latest IPTV logo repair report marks all 1,354 IPTV logo references as external/non-repository. The current provenance manifest also has no officially verified logo in either playlist. Therefore the authentic-local-logo requirement is **not passed**. See [playlist-logo-repair-results.md](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/playlist-logo-repair-results.md) and [logo-authenticity-manifest.json](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/logo-authenticity-manifest.json).

## 4. Operational blockers and safe next actions

At the audit snapshot, two separate main-branch workflows were still active:
- [IPTV Playlist Update #45521311291](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45521311291) — pending
- [Refresh IPTV EPG #45521322609](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45521322609) — in progress

No additional playlist write was attempted while the separate playlist writer was pending. The current playlist snapshot may be superseded when those runs finish.

Priority follow-up repairs:
1. Remove Ayush Next Communication Network and Jaihind TV from IPTV New Channels because official evidence confirms the excluded educational/news categories.
2. Reconcile the 122 broad Indian-religious rejections with the explicit Islamic-religious exception.
3. Keep the three inconclusive International primaries out of the verified count and move them to the appropriate manual-review location after the active writer finishes; review the two geo-blocked BRIDGE streams for Bangladesh usability.
4. Replace or blank the two generated fallback logos and four known placeholder logos; do not invent replacement artwork.
5. Resolve logo provenance and the raw-URL/local-path validator disagreement.
6. Audit the four IPTV primary identity collisions and the legacy out-of-scope groups in a separate targeted cleanup, without deleting unrelated entries.

## 5. Final result

- **IPTV discovery stage:** completed successfully; 11 New Channels and 5 New Backups are present in the current snapshot. Two New Channels candidates are confirmed policy-ineligible; retained candidates are still manual-review items.
- **International discovery stage:** completed successfully; 6 verified new primaries and 9 verified alternative streams are retained, with 3 inconclusive candidates still held. No new Adult or Fashion TV channels were found.
- **Structural validation:** passed for both playlists.
- **Full policy compliance:** not passed because of the identified queue, legacy-content, duplicate-identity and logo-provenance blockers.

The stage reports and workflow logs are linked above. This combined report is a fresh 25 November record; no prior day's report was reused.
