# Daily IPTV Discovery Report — 2026-11-26

Generated: **2026-11-26T07:02:35+06:00** (Asia/Dhaka)  
Repository: [saeidrahmanbd/BDIX-IPTV](https://github.com/saeidrahmanbd/BDIX-IPTV)  
Audited main snapshot before this report commit: **cec1cb1eeb22974d8ae49690d44d1a40601f1b6b**

**Overall status: PARTIAL — IPTV discovery completed; International discovery recovery remains pending.** This report uses today's GitHub Actions runs, today's stage reports, the current playlist blobs, and a targeted International queue repair. It does not reuse yesterday's report.

## 1. Stage status

| Stage | Latest run | Result at report time |
|---|---|---|
| IPTV New Channel Discovery | [#45721332314](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45721332314) | **Success** |
| International Channel Discovery | [#45727520586](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45727520586) | **Failed final discovery validation** |
| International recovery attempt | [#45731674403](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45731674403) | **Pending; discover job has not started** |
| Writer holding the shared queue | [Refresh IPTV EPG #45731679974](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45731679974) | **In progress** |

The International recovery job is waiting for the shared main-branch writer concurrency group. The active EPG refresh uses that same writer group. Its daily guard succeeded, but its discovery job remains pending. The International stage is therefore not reported as successful.

## 2. IPTV-Playlist.m3u — Bangladesh and India

- Workflow: [IPTV New Channel Discovery #45721332314](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45721332314) — completed successfully.
- Fresh stage report: [reports/iptv-channel-discovery.md](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/iptv-channel-discovery.md), generated **05:27:26 Bangladesh time**.
- Discovery commit: [82a551f7d9c45adcff305b34015d57f640c27a27](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/82a551f7d9c45adcff305b34015d57f640c27a27).

### Candidate discovery and probing

The Bangladesh and India source feeds produced **4 New Channels candidates** and **4 New Backups candidates**. The workflow recorded **855 rejected or held source candidates**.

New Channels candidates:
- **ATN Music (360p)** — removed; HTTP 404.
- **Malabar Plus (720p)** — live-media response; retained in New Channels without tvg-logo because no authentic local logo was available.
- **Thanima (1080p)** — live-media response; retained in New Channels without tvg-logo because no authentic local logo was available.
- **Win TV (576p)** — removed; HTTP 404.

New Backups candidates:
- **DD Assam (576p)** — removed; HTTP 404.
- **DD Manipur (576p)** — removed; HTTP 404.
- **DD Nagaland (576p)** — removed; HTTP 404.
- **DD Tripura (576p)** — removed; HTTP 404.

Probe totals:
- Newly staged entries probed: **8**
- Live-media responses: **2**
- Definitively dead candidates removed: **6**
- New candidates retained for manual review: **2**
- Verified primary additions to active country groups: **0**
- Verified alternative streams retained in New Backups: **0**

**No justified primary-group or backup additions were made today.** Malabar Plus and Thanima remain candidates in New Channels, not promoted channels. Their logo fields were left blank rather than using external, invented or placeholder artwork.

### Source rejection/hold reasons

| Reason | Count |
|---|---:|
| Duplicate stream URL | 329 |
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
| Duplicate identity already staged in a discovery queue | 3 |
| Country metadata outside Bangladesh/India (CA, NL, PK) | 4 |
| Proxy/worker host | 2 |
| **Total** | **855** |

**Policy caveat:** the discovery report uses the broad rejection label “Indian religious channel is prohibited” for 122 candidates. The current rule excludes non-Islamic religious channels but permits Islamic religious channels. The report does not separate Islamic from non-Islamic candidates, so this filter may be over-restrictive and needs correction.

### Current IPTV playlist snapshot

A later maintenance commit changed IPTV-Playlist.m3u after the 05:27 discovery run. The current snapshot is at [82743bd155451fa90be0f59573a0ec7564daf71a](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/82743bd155451fa90be0f59573a0ec7564daf71a).

| Current group | Entries |
|---|---:|
| Bangladesh | 70 |
| Indian Bangla | 34 |
| Indian Movies | 67 |
| Indian Music | 63 |
| Indian Entertainment | 142 |
| Pakistani | 14 |
| International | 82 |
| Documentary & Wildlife | 57 |
| Kids | 36 |
| Religious | 28 |
| Sports | 102 |
| New Channels | 28 |
| New Backups | 5 |
| Backup | 405 |
| Review | 238 |
| **Total** | **1,371** |

The two candidates from today's discovery, Malabar Plus and Thanima, are in the current New Channels queue. The remaining 26 New Channels rows and all 5 current New Backups rows predate today's discovery stage; they were not counted as today's additions. New Channels and New Backups remain immediately before Backup.

Independent current-file checks:
- EXTINF entries: **1,371**
- Malformed EXTINF/URL pairs: **0**
- Duplicate stream URL groups: **0**
- Duplicate primary tvg-id groups: **0**
- Queue order: **passed**

Legacy scope blockers remain in the existing playlist, including Pakistani, International, Documentary & Wildlife, Kids and Religious groups. They were not broadly deleted or reclassified because the preservation rule prohibits destructive cleanup of unrelated entries. The discovery validator's pass applies to newly staged rows, not a full reclassification of every legacy playlist row.

## 3. International-Playlist.m3u

- First discovery attempt: [International Channel Discovery #45727520586](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45727520586) — discovery and stream probing ran, but the final commit step failed.
- Fresh stage report: [reports/international-channel-discovery.md](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/international-channel-discovery.md), last scan **06:16:58 Bangladesh time**; stream verification **06:17:09 Bangladesh time**.
- Report-only failure commit: [b243c73445c92c5093bd28e6fe57eec1670df801](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/b243c73445c92c5093bd28e6fe57eec1670df801).

### Discovery and stream-probe results

- Source records parsed: **12,164**
- Existing playlist records at scan: **3,321**
- New eligible source records after policy/URL filtering: **149**
- New Channels staged: **50**
- New Backups staged: **4**
- Adult primary channels discovered directly into Adult: **0**
- Fashion TV channels discovered directly into Fashion TV: **0**
- New entries and queued streams probed: **72**
- Live-media responses: **14**
- Verified primary rows retained in New Channels by the combined queue probe: **7**
- Verified alternative rows retained in New Backups by the combined queue probe: **7**
- Inconclusive candidates retained for manual review: **3**
- Unverified backup streams moved to Review: **2**
- Definitively dead new candidates removed: **53**
- Duplicate newly discovered stream entries removed: **0**

The “7 verified primary rows” and “7 verified alternative rows” are the workflow's combined discovery-queue probe counters; they must not be interpreted as seven newly discovered source-feed channels each. The workflow's playlist publication was blocked by final identity validation, so **zero staged International playlist additions from that failed attempt were published**.

### Held and rejected candidates

Inconclusive primary candidates:
- **Galaxy** — URLError; connection could not be confirmed.
- **Galaxy Premium** — URLError; connection could not be confirmed.
- **Komsan TV [Not 24/7]** — URLError; connection could not be confirmed.

Other candidate outcomes:
- **Viasat Kino (Romania) (576i)** — retained in the failed run's working tree without tvg-logo because no authentic local repository logo was available; not published by the failed attempt.
- **TVS Film Noir Network** — HTTP success returned an HTML/error page, not a TV stream; removed from New Channels by the probe.
- **Viasat Kino (Ukraine) Romania** — HTTP success returned an HTML/error page, not a TV stream; removed.
- **Cinema (Russia)** — HTTP 403; unverified alternative moved from New Backups to Review.
- **Dorama** — HTTP 403; unverified alternative moved from New Backups to Review.
- **8XM**, **Kinouzhas**, **M1 (Ukraine)** and **Viasat Kino Action** — HTTP 404; removed from New Backups.

The four newly staged alternative candidates were all rejected after probing. No new Adult or Fashion TV channel was discovered today.

### Source rejection reasons

| Reason | Count |
|---|---:|
| Source category not Movies or Music | 6,600 |
| News | 1,082 |
| Religious | 780 |
| Kids | 315 |
| Sports | 305 |
| Documentary & Wildlife | 189 |
| Unsafe or tokenized URL | 141 |
| Test/VOD/non-TV name | 300 |
| General entertainment | 69 |
| TV series | 24 |
| Permanently banned | 10 |
| Known Indian prohibited brand/category | 12 |
| Indian religious category | 1 |
| Ambiguous Movie/Music classification | 1 |
| Non-real/test channel | 1 |

The full candidate list, stream URLs and probe-by-probe outcomes are preserved in the linked stage report and workflow artifact.

### Exact validation failure and targeted repair

The official International playlist validator completed successfully, but the final discovery-run validator failed with this exact blocker:

**New Channels identity is already represented elsewhere: Rotana Cinema KSA**

The discovery job failed at **Commit discovery changes** because the same channel identity was in New Channels while an existing representation was already present in Review. The workflow committed the fresh failure report only; it did not publish its staged playlist changes.

I applied a targeted, evidence-based repair in [cec1cb1eeb22974d8ae49690d44d1a40601f1b6b](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/cec1cb1eeb22974d8ae49690d44d1a40601f1b6b):

1. Moved the verified Rotana Cinema KSA alternative stream from New Channels to New Backups because that identity is already represented.
2. Moved the unverified Cinema (Russia) and Dorama alternative streams from New Backups to Review, matching their HTTP 403 probe results.
3. Removed TVS Film Noir Network from New Channels because the endpoint returned HTML/error content instead of a TV stream.

No unrelated International entries were changed. The edit removed one invalid row and changed only the three queue roles described above.

### Current International playlist snapshot after repair

| Current group | Entries |
|---|---:|
| Bangladesh | 48 |
| Indian Bangla | 32 |
| Indian Movies | 75 |
| Indian Music | 57 |
| Indian Entertainment | 173 |
| Pakistani | 19 |
| Argentina | 14 |
| Brazil | 15 |
| Bulgaria | 21 |
| Canada | 31 |
| Chile | 10 |
| China | 9 |
| Colombia | 9 |
| Costa Rica | 9 |
| Czech Republic | 23 |
| DO | 11 |
| Estonia | 6 |
| France | 44 |
| Germany | 71 |
| Greece | 8 |
| Hungary | 15 |
| Iran | 13 |
| Italy | 24 |
| Lebanon | 6 |
| Mexico | 17 |
| Netherlands | 17 |
| North Macedonia | 5 |
| Panama | 5 |
| Paraguay | 5 |
| Peru | 9 |
| Poland | 25 |
| Romania | 30 |
| Russia | 76 |
| Saudi Arabia | 9 |
| Singapore | 5 |
| Spain | 17 |
| Sweden | 49 |
| Turkey | 15 |
| Ukraine | 28 |
| United Kingdom | 20 |
| United States | 240 |
| Uzbekistan | 5 |
| Vietnam | 6 |
| International | 102 |
| News | 12 |
| Fashion TV | 3 |
| Documentary & Wildlife | 130 |
| Kids | 151 |
| Religious | 31 |
| Sports | 180 |
| Adult | 366 |
| Review | 645 |
| New Channels | 7 |
| New Backups | 8 |
| Backup | 359 |
| **Total** | **3,320** |

Independent current-file checks after the targeted repair:
- EXTINF entries: **3,320**
- Malformed EXTINF/URL pairs: **0**
- Duplicate stream URL groups: **0**
- Duplicate primary tvg-id groups: **0**
- New Channels/New Backups identity-role checks: **passed**
- Final group order: **Review → New Channels → New Backups → Backup**
- Adult and Fashion TV groups remain intact; no new Adult/Fashion TV additions today.

No new country group was created today. The existing country-specific groups are all retained as shown above. Legacy out-of-scope groups remain, including Indian Entertainment, News, Documentary & Wildlife, Kids, Religious and Sports. They were preserved rather than broadly deleted or reclassified.

### Country-group threshold mismatch

The current International discovery script still states that the five-primary-identity threshold applies to every country **except Bangladesh and India**. The current instruction requires the threshold for every country. No new country group was created in this run, but the code/configuration exception remains a blocker.

### Recovery status

The recovery attempt [#45731674403](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45731674403) has a successful daily guard, but its discover job is still **pending**. It is waiting behind [Refresh IPTV EPG #45731679974](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45731679974), whose XMLTV regeneration/publish step is still in progress in the shared main-branch writer group.

The recovery run has not yet confirmed whether the targeted repair allows the International discovery workflow to complete. The International stage remains incomplete until that run finishes and its final validation passes.

## 4. Shared logo audit

Current playlist logo-path scan:

| Playlist | Relative local logos/ paths | Raw repository URLs under /logos/ | Other external URLs | Blank logo fields | Placeholder-like references |
|---|---:|---:|---:|---:|---:|
| IPTV | 406 | 965 | 0 | 0 | 0 |
| International | 2,919 | 0 | 0 | 401 | 0 |

**IPTV local-path requirement is not passed:** 965 entries still use raw.githubusercontent.com URLs, even though they point into this repository's logos tree. They are external tvg-logo URLs from the playlist client's perspective and need conversion to relative local logos/ paths. No such bulk conversion was attempted in this discovery run.

International currently uses relative logos/ paths for all nonblank logo fields. Its 401 blank logo fields were left blank rather than filled with unverified artwork.

The latest provenance report available at the time of this run was generated **2026-11-26T00:19:41Z**, before the targeted queue-role repair. It reports:

| Playlist | Official verified | Third-party verified | Unofficial fallback | Needs review |
|---|---:|---:|---:|---:|
| IPTV | 0 | 37 | 2 | 1,332 |
| International | 0 | 986 | 0 | 2,335 |

The queue-role repair did not change any remaining logo assets, but the provenance report was not regenerated after that repair. Local path compliance and logo authenticity are separate checks; the large needs-review counts mean authenticity is not fully established.

References:
- [Logo provenance review](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/logo-provenance-review.md)
- [Playlist logo repair results](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/playlist-logo-repair-results.md)

## 5. Validation summary

| Check | IPTV current file | International current file |
|---|---:|---:|
| M3U entries | 1,371 | 3,320 |
| Malformed EXTINF/URL pairs | 0 | 0 |
| Duplicate stream URL groups | 0 | 0 |
| Duplicate primary tvg-id groups | 0 | 0 |
| Required queue placement | Pass | Pass |
| Local-only logo paths | **Fail: 965 raw repository URLs** | Pass for nonblank fields |
| Authenticity provenance fully verified | **No** | **No** |
| Full existing-playlist content policy | **Not passed; legacy groups remain** | **Not passed; legacy groups remain** |
| Daily discovery stage | **Success** | **Recovery pending after failed attempt** |

## 6. Commits and blockers

Commits:
- IPTV discovery: [82a551f7d9c45adcff305b34015d57f640c27a27](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/82a551f7d9c45adcff305b34015d57f640c27a27)
- International failed-run report only: [b243c73445c92c5093bd28e6fe57eec1670df801](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/b243c73445c92c5093bd28e6fe57eec1670df801)
- Targeted International queue repair: [cec1cb1eeb22974d8ae49690d44d1a40601f1b6b](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/cec1cb1eeb22974d8ae49690d44d1a40601f1b6b)

Outstanding blockers:
1. International recovery run is pending behind the active EPG main-writer job.
2. IPTV still has 965 raw GitHub logo URLs rather than relative local logos/ paths.
3. Logo provenance remains incomplete; two IPTV fallback assets remain unofficial.
4. Existing out-of-scope groups remain in both playlists and require separate, carefully scoped policy cleanup.
5. IPTV's broad Indian religious rejection does not distinguish Islamic from non-Islamic channels.
6. International country-threshold configuration exempts Bangladesh and India contrary to the current all-country threshold rule.
7. Existing IPTV New Channels/New Backups queues include older rows not introduced by today's discovery; the discovery pass did not broadly rewrite those rows.

## 7. Final result

- **IPTV:** fresh discovery completed successfully. Two live candidates remain in New Channels without authentic local logos; no verified primary or backup additions were made. Six dead streams were removed.
- **International:** fresh discovery and probing ran, but final validation failed on the Rotana Cinema KSA identity-role collision. That exact blocker and two unverified backup placements were repaired in a targeted commit. The recovery run is still pending behind the EPG writer.
- **Overall:** **PARTIAL — do not treat today's paired discovery as fully successful until International recovery completes and validates.**

This is a fresh 26 November report. No prior day's report was reused.