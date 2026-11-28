# Daily IPTV Discovery Report — 2026-11-28

Generated: **2026-11-28 06:55:31 +06:00 (Asia/Dhaka)**

Repository: [saeidrahmanbd/BDIX-IPTV](https://github.com/saeidrahmanbd/BDIX-IPTV)

Audited main snapshot: `2fffbe53a42a06e7a58ea3583e974fbe8ff32535`

**Overall status: PARTIAL.** IPTV discovery completed and its `daily_guard` and `discover` jobs passed. International discovery has four failed attempts whose final validation blocked publication; the watchdog dispatched a guarded recovery run, but its `discover` job is pending behind an active EPG writer. The EPG writer is currently regenerating and publishing XMLTV. No duplicate individual writers were launched.

This is a fresh 28 November report based on current Actions history, job-level statuses, job logs, stage reports and current playlist blobs. No earlier daily report was reused.

## 1. Today's Actions schedule audit

Bangladesh-date window checked: **2026-11-28 00:00:00–06:55:31 Asia/Dhaka**, equivalent to **2026-11-27T18:00:00Z–2026-11-28T00:55:31Z**.

The first page of the repository's Actions run history contained all 16 runs created within this Bangladesh-date window. **All 16 were event=`workflow_dispatch`; zero event=`schedule` runs were present.** Older runs on the same page were from the previous Bangladesh date.

The current workflow YAMLs still contain their configured schedules:

| Production workflow | Configured Bangladesh time | Required job |
|---|---:|---|
| IPTV New Channel Discovery | 05:07 | `discover` |
| International Channel Discovery | 05:17 | `discover` |
| Playlist Logo Repair and Localization | 05:27 | `localize` |
| International Stream Health | 05:37 | `check` |
| IPTV Playlist Update | 05:47 | `maintain` |
| Refresh IPTV EPG | 06:07 | `refresh` |
| Daily Xtream Health Check | 06:30 | `check` |

The watchdog has independent recovery checkpoints and a `workflow_dispatch` trigger. **Missing schedule events are reported separately from successful manual recovery. This report does not claim cron delivery is fixed.**

### Watchdog recovery

[Discovery Schedule Watchdog #1167](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46090038026) was already invoked through `workflow_dispatch` at **06:50:34 Bangladesh time**. Its `recover_missing_discovery` job completed successfully at 06:51:16.

Its log independently evaluated the required jobs and recorded:

- IPTV maintenance: no dispatch needed; today's required `maintain` job had succeeded in run [#46086971744](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46086971744).
- IPTV discovery: no dispatch needed; today's required `discover` job had succeeded in run [#46082474151](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46082474151).
- International discovery: four prior same-day attempts had all failed; watchdog accepted recovery dispatch attempt 1/2.
- Logo localization: no dispatch needed; required `localize` job succeeded in run [#46084758413](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46084758413).
- International stream health: no dispatch needed; required `check` job succeeded in run [#46085616742](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46085616742).
- EPG refresh: no active/successful required job existed at watchdog evaluation; watchdog accepted recovery dispatch attempt 1/2.
- Xtream health: deferred because International discovery still had an active run for today's Bangladesh date.

The watchdog did not dispatch a duplicate IPTV discovery, maintenance, logo or stream-health writer. No individual writer was manually launched outside the watchdog. The EPG recovery is now active and International discovery is queued behind the shared main-playlist writer lock.

## 2. IPTV-Playlist.m3u — Bangladesh and India

- Workflow: [IPTV New Channel Discovery #392](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46082474151) — event `workflow_dispatch`, completed successfully.
- Required jobs: `daily_guard` **success**; `discover` **success**.
- Stage report generated: **05:27:11 Bangladesh time**.
- Discovery commit: [0554093ec41c5578750f373c4cfaaf7780c9fdbb — Add IPTV candidates to manual review queues](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/0554093ec41c5578750f373c4cfaaf7780c9fdbb).
- Stage report: [reports/iptv-channel-discovery.md](https://github.com/saeidrahmanbd/BDIX-IPTV/blob/main/reports/iptv-channel-discovery.md).

### Discovery and probe results

Sources: Bangladesh and India iptv-org country feeds.

| Metric | Result |
|---|---:|
| New primary candidates staged | 6 |
| New alternative candidates staged | 6 |
| Source candidates rejected/held | 882 |
| Newly staged/queued entries probed | 12 |
| Live-media responses | 1 |
| Definitively dead candidates removed | 11 |
| Verified new primary additions retained | 0 |
| Verified alternative streams retained in New Backups | 0 |
| Inconclusive candidates retained | 0 |

**No justified verified primary-group or New Backup additions were made today.** One live-media response was not counted as a verified primary or alternate addition by the stage report; its candidate-level disposition is not reconciled in the report, so it must not be promoted based on the response alone.

Dead candidates removed:

- New Channels: ATN Music, Green TV, NAN TV, Kasargod Vision, Punjabi Beats HD and Win TV — HTTP 404.
- New Backups: Boishakhi TV, T Sports, DD Manipur, DD Nagaland and DD Tripura — HTTP 404.

The staged candidate list also included DD Assam. The report records one live-media response overall but zero verified alternatives retained; no new backup promotion is claimed.

### Source rejection/hold reasons

| Reason | Count |
|---|---:|
| Duplicate stream URL | 337 |
| Indian news | 307 |
| Indian religious category | 123 |
| Permanently banned | 32 |
| Unsupported stream path | 19 |
| Indian kids | 15 |
| Known prohibited Indian brand/category | 12 |
| Tokenized URL | 10 |
| Indian business | 9 |
| Indian education | 7 |
| Country metadata outside Bangladesh/India | 4 |
| Proxy/worker host | 3 |
| Indian knowledge | 2 |
| Duplicate queued identity | 1 |
| Other known prohibited channel | 1 |
| **Total** | **882** |

Policy caveat: the 123 religious rejections use a broad Indian-religious category. The current rule excludes non-Islamic religious channels but allows Islamic religious channels. The report does not split the 123 by religious type, so possible over-filtering remains unresolved.

### Current IPTV playlist validation

Current file blob: `0e1425e163ab2a40d154722bc1108a3cbb28265d`.

| Check | Result |
|---|---:|
| EXTINF entries | 1,197 |
| Malformed EXTINF/URL pairs | 0 |
| Duplicate stream URLs | 0 |
| Duplicate primary identities | 0 |
| Queue counts | Review 1; New Channels 32; New Backups 22; Backup 434 |
| Required queue placement | **FAIL** |

The actual final contiguous group order is:

`… Sports → Backup → New Channels → New Backups → Review`

The required order is:

`… Review → New Channels → New Backups → Backup`

Thus the IPTV queues are not immediately before Backup in the current whole-file snapshot, even though the discovery-run validator passed its new-row checks. This is an existing whole-playlist ordering blocker. It was not rewritten while the shared main-branch writer was active.

### IPTV logo-path audit

- Relative local `logos/` paths: **434**
- Absolute raw.githubusercontent.com URLs pointing to this repository's `/logos/` tree: **763**
- Other external logo hosts: **0**
- Blank logo fields: **0**

The 763 raw URLs are not local relative paths and violate the strict local-only requirement. No bulk conversion was attempted because the repository's logo-localization workflow has previously rewritten relative paths back to absolute raw URLs; its writer and validator need a coordinated correction.

## 3. International-Playlist.m3u

### Completed attempts and current recovery

Four same-day International discovery attempts completed with failure:

| Run | Bangladesh time | Result |
|---|---:|---|
| [#379 — 46083406650](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46083406650) | 05:36 | Failed |
| [#380 — 46084756382](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46084756382) | 05:51 | Failed |
| [#381 — 46085612243](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46085612243) | 06:01 | Failed |
| [#382 — 46086976456](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46086976456) | 06:16–06:19 | Failed |

For the latest completed attempt #382, the actual jobs were:

- `daily_guard`: **success**
- `discover`: **failure**

The discovery, stream-probe and official playlist-validation steps ran. The final report recorded **Validation status: FAIL**. The commit step intentionally published only the failure report; it did not publish the staged International playlist changes.

The latest report-only commit is [2fffbe53a42a06e7a58ea3583e974fbe8ff32535 — Record International discovery validation blocker](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/2fffbe53a42a06e7a58ea3583e974fbe8ff32535).

### Current guarded recovery

The watchdog dispatched [International Channel Discovery #383](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46090090125) at **06:51:09 Bangladesh time**.

- Event: `workflow_dispatch`
- `daily_guard`: **success**
- `discover`: **pending**

At the same time, the watchdog dispatched [Refresh IPTV EPG #1790](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46090094107).

- Event: `workflow_dispatch`
- `daily_guard`: **success**
- `refresh`: **in progress**
- Actual active publication step: **Regenerate, validate and publish XMLTV**

Both International discovery and EPG use the shared main-playlist writer concurrency group. The EPG refresh currently holds the writer; International `discover` is pending behind it. At the report timestamp the EPG run had not completed, so the recovery's actual discovery, final validation and playlist commit cannot yet be confirmed.

No extra individual writer was started and no concurrency or retry guard was bypassed. The next evidence must come from run #383 after the EPG writer releases the shared lock.

### Latest completed International discovery evidence

The latest completed scan was timestamped **06:18:56 Bangladesh time**.

| Metric | Result |
|---|---:|
| Source records parsed | 12,223 |
| Existing playlist records at scan | 3,328 |
| Exact source URLs already present | 2,186 |
| New eligible source records after policy/URL filtering | 152 |
| New primary candidates staged | 50 |
| New backup candidates staged | 4 |
| Adult primaries routed directly to Adult | 0 |
| Fashion TV primaries routed directly to Fashion TV | 0 |
| New/queued streams probed | 101 |
| Live-media responses | 49 |
| Primary candidates retained in working queue | 25 |
| Alternative streams retained in working queue | 24 |
| Inconclusive candidates held | 6 |
| Definitively dead candidates removed | 46 |
| Duplicate newly discovered stream URLs | 0 |

The 25 primary and 24 alternative stream rows were verified as live-media responses in the failed run's working tree, but **none of those staged playlist changes was published**, because final identity validation failed.

Inconclusive primary candidates:

- BRIDGE Dance — HTTP 403
- BRIDGE Jazz — HTTP 403
- BRIDGE Rap — HTTP 403
- Hollywood Ukraine — URLError
- Prokino — URLError
- Viasat Kino (Ukraine) — URLError

Dead endpoints included multiple Rakuten TV Action/Comedy/Drama/Family/Top Movies variants and other 404 candidates. TVS Film Noir Network returned HTML/error content instead of a TV stream and was removed. Five candidates were left without logos rather than receiving placeholder artwork.

### Exact final validation blockers

The final validation at **06:19:14 Bangladesh time** reported:

- M3U entries parsed: 3,336
- Malformed EXTINF/URL pairs: 0
- Duplicate stream URLs: 0
- Review → New Channels → New Backups → Backup ordering: passed
- Discovery entries without authentic local logos: 5 (left blank)
- Non-local discovery logo references: 0
- Geography/content-policy issues: 0

Two exact identity collisions blocked publication:

1. **AMC Europe Romania** — the staged New Channels identity is already represented elsewhere in the playlist.
2. **Film Cafe Romania** — the staged New Channels identity is already represented elsewhere in the playlist.

These rows must be reconciled with their existing primary identities. If they are genuine alternate streams, they belong in New Backups; if not, they must not remain as duplicate primary candidates. The failed run did not publish them.

### Current International playlist validation

Current file blob: `bc34bbba68a4e1ddb72b712393eb4fb0657997cc`.

| Check | Result |
|---|---:|
| EXTINF entries | 3,328 |
| Malformed EXTINF/URL pairs | 0 |
| Duplicate stream URLs | 0 |
| Duplicate primary identities | 0 |
| Queue counts | Review 930; New Channels 26; New Backups 21; Backup 287 |
| Required queue placement | Pass |

Current tail order:

`… Adult → Review → New Channels → New Backups → Backup`

Existing Adult group: **366** entries. Existing Fashion TV group: **5** entries. No new Adult or Fashion TV channels were discovered today.

The stage configuration still describes the five-primary-identity country threshold as applying to every country **except Bangladesh and India**. The current instruction requires the five-channel threshold for every country, so this is a configuration mismatch even though no new country group was created today.

Legacy out-of-scope groups remain in the current International playlist:

| Existing group | Entries |
|---|---:|
| Indian Entertainment | 159 |
| News | 11 |
| Documentary & Wildlife | 129 |
| Kids | 148 |
| Religious | 31 |
| Sports | 176 |

These legacy groups were preserved rather than broadly deleted or reclassified. They remain whole-playlist policy blockers.

### International logo-path audit

- Relative local `logos/` paths: **2,928**
- Absolute raw repository logo URLs: **0**
- Other external logo hosts: **0**
- Blank logo fields: **400**

The current International nonblank logo paths are relative local paths. Blank fields were left blank rather than filled with invented or placeholder artwork. Authenticity provenance for every existing logo was not independently re-established in this discovery run.

## 4. Other production workflow job verification

| Workflow | Run | Required job result |
|---|---|---|
| IPTV New Channel Discovery | #46082474151 | `daily_guard` success; `discover` success |
| International Channel Discovery | #46086976456 | `daily_guard` success; `discover` failure; recovery #46090090125 pending |
| IPTV Playlist Update | #46086971744 | `daily_guard` success; `maintain` success |
| Playlist Logo Repair and Localization | #46084758413 | `daily_guard` success; `localize` success |
| International Stream Health | #46085616742 | `daily_guard` success; `check` success |
| Refresh IPTV EPG | #46090094107 | `daily_guard` success; `refresh` in progress, XMLTV publication step in progress |
| Daily Xtream Health Check | Not dispatched yet | Watchdog deferred it while International discovery remained active |

## 5. Commits, blockers and final result

### Today's discovery commits

- IPTV discovery queue commit: [0554093ec41c5578750f373c4cfaaf7780c9fdbb](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/0554093ec41c5578750f373c4cfaaf7780c9fdbb).
- International latest failed-run report-only commit: [2fffbe53a42a06e7a58ea3583e974fbe8ff32535](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/2fffbe53a42a06e7a58ea3583e974fbe8ff32535).
- International current recovery run: [#46090090125](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46090090125) — pending behind EPG writer; no recovery commit yet.
- EPG recovery run: [#46090094107](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/46090094107) — active.

### Outstanding blockers

1. **Schedule delivery:** zero `event=schedule` runs were present for the checked Bangladesh date. Manual watchdog recovery is active/successful for the dispatched jobs, but cron delivery is not fixed.
2. **International discovery:** four attempts failed final validation; latest exact blockers are the duplicate primary identities AMC Europe Romania and Film Cafe Romania. Recovery #383 is pending.
3. **Writer contention:** EPG refresh #1790 currently holds the shared writer; International discovery #383 has not reached its actual `discover` job.
4. **IPTV queue order:** current whole-file order is Backup → New Channels → New Backups → Review, not Review → New Channels → New Backups → Backup.
5. **IPTV logos:** 763 absolute raw repository logo URLs remain; strict local-only relative path policy is not passed.
6. **International country threshold:** current code exempts Bangladesh and India from the five-primary-identity rule, contrary to the all-country requirement.
7. **International legacy scope:** existing Indian Entertainment, News, Documentary, Kids, Religious and Sports groups remain.
8. **Logo authenticity:** this run verified path locality, not official broadcaster provenance for every existing logo.
9. **IPTV religious filtering:** 123 Indian religious candidates were rejected under a broad category without a split between Islamic and non-Islamic channels.
10. **IPTV probe accounting:** one live-media response is not reconciled to a named candidate or a verified primary/backup addition in the stage report.

### Final result

- **IPTV:** completed; actual `discover` job and stage validation passed. Six primary and six backup candidates were staged; eleven were removed as HTTP 404. No verified primary or alternative stream addition was justified.
- **International:** incomplete; latest completed discovery failed final validation on two duplicate identities. The watchdog dispatched a guarded recovery run, but its `discover` job remains pending behind EPG publication. No International playlist changes from the failed attempts were committed.
- **Schedule:** no scheduled events were recorded for the checked Bangladesh date; successful workflow_dispatch recovery is separate evidence and does not prove cron delivery is fixed.
- **Overall:** **PARTIAL — do not mark the paired daily discovery successful until International recovery #383 runs, passes final validation and publishes its verified commit.**

No playlist was replaced with a partial list, no broad channel deletion/reclassification was performed, and no duplicate individual writer was manually launched.
