# Daily IPTV Discovery Report — 2026-11-23

Generated: **2026-11-23 06:56:27 Asia/Dhaka (UTC+06:00)**

Repository: [saeidrahmanbd/BDIX-IPTV](https://github.com/saeidrahmanbd/BDIX-IPTV)  
Snapshot branch: `main`  
Snapshot HEAD: [`c58ef5942f7a1b6bd8463a4d4450d29615c549ec`](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/c58ef5942f7a1b6bd8463a4d4450d29615c549ec)

**Overall result: INCOMPLETE.** The IPTV discovery stage completed successfully. The International discovery stage failed before its source scan and did not add or reject any candidates.

## 1. IPTV-Playlist.m3u

**Status: PASS — discovery completed**

- Workflow: [IPTV New Channel Discovery run #45083236021](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45083236021)
- Run window: 2026-11-23 05:26–05:27 Asia/Dhaka
- Discovery source: current Bangladesh and India iptv-org country feeds
- Playlist/report commit: [`56d0f2580ed933580ba45b41f01570dfec9f7e55`](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/56d0f2580ed933580ba45b41f01570dfec9f7e55)

### Candidates

The source scan staged 14 primary candidates and 10 alternative-stream candidates before probing. After probing, the run reported 14 manual-review candidates retained. The current playlist snapshot contains:

**New Channels (9):**
- Ayush Next Communication Network (576p)
- CCV (480p)
- ETV Life (1080p)
- Gaunda Punjab TV (720p)
- Kabaddi 24x7 (720p)
- Punjab Plus (1080p)
- TLC (India) HD (1080p)
- WeatherSpy (India) (720p)
- Zodiak TV (1080p)

**New Backups (5):**
- DD National HD (1080p)
- MNX HD (1080p)
- Sony Max (720p)
- Sony Sports Ten 1 (576p)
- Unite8 Sports 1 HD (1080p)

These are review-queue entries, not confirmed working additions. The probe summary recorded **0 verified new primary channels and 0 verified alternate streams retained**.

### Rejections and stream checks

- Candidate records rejected/held by policy and URL filtering: **894**
- Indian News: 304; Indian Religious: 121; duplicate stream URLs: 332
- Permanent denylist: 31; Indian Kids: 24; unsupported stream paths: 20
- Indian Knowledge: 15; Indian Business/Finance: 9; Indian Education: 7
- Tokenized URLs: 10; duplicate staged identities: 3; out-of-scope country records: 3; proxy/worker host: 1
- Newly staged/queued streams probed: **24**
- Definitively dead candidates removed: **10** (HTTP 404)
- Inconclusive candidates: **4** — TLC (India) HD remained in New Channels; MNX HD, Sony Sports Ten 1 and Unite8 Sports 1 HD were reported as moved to Review
- Authentic local logos localized: 12; candidates without an authentic local logo at probe time: 2

**Queue reconciliation warning:** the current playlist still shows MNX HD, Sony Sports Ten 1 and Unite8 Sports 1 HD in New Backups, despite the probe report saying they were moved to Review. The report also says no verified alternate streams were retained. These five current New Backups entries therefore need a fresh role/status reconciliation before they can be treated as verified alternatives.

### Validation

At the end of the discovery run, validation reported PASS:

- Malformed EXTINF/URL pairs: 0
- Duplicate stream URLs introduced: 0
- Prohibited Indian rows in New Channels/New Backups: 0
- New Backup identity/duplicate-primary issues: 0
- Non-local/broken discovery-queue logos: 0
- Missing authentic logos among new candidates: 2 warnings
- Country metadata requiring manual review: 1 warning

Current main-branch structural snapshot at 06:56:

- Entries: **1,346**
- Duplicate stream URLs: **0**
- Duplicate primary tvg-id/channel-id values: **0**
- Group order: PASS
- New Channels: 9; New Backups: 5; Backup: 410; Review: 206
- New Channels and New Backups are immediately before Backup in the playlist order.

Existing scope issues were not broadly changed: the playlist still contains 82 entries in International and 14 in Pakistani, plus 8 Indian entries in the Kids group. These are existing playlist content, not additions from today's discovery. They need a separately authorized targeted cleanup.

The 1,346 current logo references resolve to files stored in this repository's `/logos/` directory, with no broken or non-repository references. They are still written as raw GitHub URLs rather than relative `logos/...` paths; strict relative-path normalization remains outstanding.

## 2. International-Playlist.m3u

**Status: FAIL — discovery did not execute**

- First recovery attempt: [run #45084119299](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45084119299), 2026-11-23 05:36 Asia/Dhaka — failed
- Latest recovery attempt: [run #45085459327](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45085459327), 2026-11-23 05:51 Asia/Dhaka — failed
- No International playlist commit was made by either run.

### Exact failure

The policy test step passed (50 tests). The next step, **Test retired endpoint protection**, failed in:

`tests/test_stream_url_identity.py::test_retired_endpoint_registry_covers_removed_star_sports_endpoint_family`

Error:

`FileNotFoundError: config/discovery-retired-endpoints.json`

The JSON file exists in the repository, but `.github/workflows/international-channel-discovery.yml` uses sparse checkout without including the `config` directory. The test therefore cannot see the required file in the runner workspace.

Because that test failed, the following steps were skipped:
- stream validator and country-threshold tests
- discovery source download and candidate classification
- stream probing and local-logo checks
- official International playlist validation
- discovery playlist commit

**Today's International additions: 0. Rejections: not assessed. Held candidates: not assessed.** The old report currently in `reports/international-channel-discovery.md` contains a scan timestamp of 2026-11-22 09:08 Asia/Dhaka. It is stale and was not used as today's discovery result.

The failed run's finalizer also reported a queue-order validation failure. A later current-main audit, after the International stream-health rewrite, now finds the category registry and present group order consistent; this does not change the fact that discovery never ran.

### Current International playlist snapshot

- Entries: **3,294**
- EXTINF/URL pairs: 3,294
- Malformed pairs: 0
- Duplicate stream URLs: 0
- Duplicate primary tvg-id/channel-id values: 0
- Current group order: PASS
- Dynamic country groups: all current groups meet the five-primary threshold
- Adult: 366; Fashion TV: 0; New Channels: 0; New Backups: 0
- Existing News: 11; Kids: 12; Religious: 3; Sports: 8; Review: 1,123; Backup: 361

**Critical logo regression:** the current International playlist has **3,294 entries with no tvg-logo attribute**. The [logo-localization run #45085461793](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45085461793) immediately before the stream-health run had reported only 27 active entries and 44 Review entries missing logos (71 total). The subsequent [`4c612db2` stream-health commit](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/4c612db2a8ff7baa8fc1d892550d1ceb388fd169) rewrote the International playlist; the current snapshot has no logo metadata. The reorganization helper accepts only relative `logos/...` references, while the earlier playlist used repository-hosted raw GitHub logo URLs. Those URLs were treated as invalid and dropped during reorganization. No replacement or placeholder art was added.

### Policy-code mismatches found

Two additional code issues need repair before a compliant International run:

1. `discovery_eligibility()` still explicitly rejects Fashion TV with the reason “Fashion TV is a preserved legacy exception, not a discovery genre,” despite the current discovery policy allowing it.
2. The discovery builder initially assigns a new Adult primary to Adult, but its later normalization branch sends new rows back to New Channels. The final discovery validator also checks candidates with the older `policy()` function, which does not recognize direct Adult placement.

The existing Adult group was preserved; no new Adult or Fashion TV channels were discovered today.

### Recovery watchdog

[Discovery Schedule Watchdog run #45091118194](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/45091118194) completed successfully at 06:51 Asia/Dhaka. It reported that the International workflow's recovery circuit breaker was open after two automatic dispatch attempts, so it did not send a third attempt today.

## 3. Required repairs before the next complete run

1. Add `config/` to the International workflow sparse-checkout paths.
2. Correct Fashion TV discovery eligibility and ensure Fashion TV candidates are routed to the allowed group.
3. Preserve direct Adult placement through the final normalization and validation steps; keep Adult alternatives in New Backups only after verification.
4. Make International reorganization convert valid repository-hosted raw logo URLs to local `logos/...` paths instead of dropping them; then restore authentic logos where exact local assets exist.
5. Reconcile the IPTV New Backups queue against the actual probe outcomes and move inconclusive alternates to Review.
6. Re-run International discovery after those repairs; do not treat the stale 22 November scan as today's result.

**Final decision:** IPTV discovery completed, but its backup queue needs reconciliation. International discovery failed before scanning. The combined daily task is therefore **not successful**.
