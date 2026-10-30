# Daily Dual-Playlist Discovery — 2026-10-30

- **Run timestamp:** 2026-10-30T01:04:31Z
- **Status:** PARTIAL / PENDING — fresh GitHub Actions discovery runs were triggered for both playlists, but neither completed report was observable at the time this summary was written.
- **Report freshness:** The reports last generated on 2026-10-29 are historical only and were not reused as today's result.
- **New additions claimed by this summary:** 0. No candidate has been counted as added until the corresponding fresh workflow report and verification are available.

## Workflow triggers

- IPTV discovery workflow trigger commit: [5781190abf052c9128471079a59bece2b4ad3583](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/5781190abf052c9128471079a59bece2b4ad3583) — 2026-10-30T01:04:59Z.
- International discovery workflow trigger commit: [ec82f688a1c873d5f99258cdeb3466ba69a87728](https://github.com/saeidrahmanbd/BDIX-IPTV/commit/ec82f688a1c873d5f99258cdeb3466ba69a87728) — 2026-10-30T01:05:04Z.
- Both commits update only a dated comment in the corresponding workflow file; the workflow files are configured to run on pushes to those paths. Both workflows share the repository's serialized playlist-writer concurrency group.

## IPTV-Playlist.m3u — baseline snapshot

- Existing entries: **1,161**.
- EXTINF/URL pairs: **1,161 / 1,161**.
- Malformed pairs: **0**.
- Duplicate stream URLs: **0**.
- Final groups: **New Channels → New Backup → Backup**.
- Discovery-queue entries: **40**.
- External logo references in discovery queues: **0**.
- Fresh candidate evaluation, live probes, additions, and rejection counts: **pending the newly triggered workflow**.

Policy to be applied by the workflow: Bangladesh and India only; exclude Indian news and non-Islamic religious channels; reject VOD, one-off program/movie streams, fake/nonlinear channels, duplicates, token/proxy-dependent streams, and clearly dead streams. Keep the two discovery queues immediately before Backup and preserve the five-channel country-group threshold.

## International-Playlist.m3u — baseline snapshot

- Existing entries: **3,257**.
- EXTINF/URL pairs: **3,257 / 3,257**.
- Malformed pairs: **0**.
- Duplicate stream URLs: **0**.
- Final groups: **New Channels → New Backup → Backup**.
- Discovery-queue entries: **144**.
- External logo references in discovery queues: **0**.
- Fresh candidate evaluation, live probes, additions, and rejection counts: **pending the newly triggered workflow**.

Policy to be applied by the workflow: Movie/Music only from any country, including Bangladesh and India; reject general entertainment, news, sports, kids, documentary, religious, lifestyle, adult, radio, VOD, and other non-Movie/Music content. Preserve the existing Fashion TV exception and the five-channel country-group threshold.

## Blocker and validation scope

- The connected GitHub actions expose repository reads and file commits, but not a direct workflow-dispatch or workflow-run listing operation. The two push-trigger commits were used to start the repository's own discovery workflows.
- Current baseline structural checks passed for both playlists: one URL per EXTINF, no malformed pairs, no duplicate URLs, correct final group order, and no external logo references in the discovery queues.
- These are baseline checks only, not final post-discovery validation. Live stream probes, current candidate rejections, final logo-file checks, and post-run playlist validation remain pending.
- No old report or old candidate list has been represented as today's discovery result. Update this summary only after fresh reports from both triggered workflows are available.
