# International Channel Discovery

Generated: **2026-11-22T06:58:06+06:00** (Asia/Dhaka)

## Run status

**BLOCKED — fresh International discovery stage did not execute.**

- Playlist: `International-Playlist.m3u`
- Current playlist blob: `2217bb66c8914bedf6f7c782b1e56693ffaad5b5`
- Candidates added: **0**
- Candidates rejected after fresh evaluation: **0**
- Candidates held for manual review: **not assessed** — no fresh source-feed scan or stream probes ran.
- This is not a finding that no eligible worldwide Movies, Music, Fashion TV or Adult channels exist.

## Freshness and execution evidence

- Latest scheduled International discovery run found: [run #44863672876](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/44863672876), created **2026-11-21 09:57:14 +06:00**, conclusion: success.
- The existing report's last scan was **2026-11-21 09:57:51 +06:00**. It is historical only and was not reused as today's result.
- No International Channel Discovery run for Bangladesh date **2026-11-22** was present in the Actions run list checked at this report time.
- Latest Discovery Schedule Watchdog run found: [run #44905290354](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/44905290354), created **2026-11-21 18:43:08 +06:00**, conclusion: success. Its log confirms that it checked the successful International discovery run for **2026-11-21**. No watchdog run for **2026-11-22** was present.
- Exact execution blocker: the connected GitHub actions available in this run support reading files/runs and repository writes, but expose no workflow-dispatch action. The GitHub fetch action is read-only. A local fallback was attempted with `git ls-remote https://github.com/saeidrahmanbd/BDIX-IPTV.git HEAD`; it failed with **`Could not resolve host: github.com`**, so the discovery script could not be run locally.

## Current playlist structural snapshot (read-only)

- Entries: **3,304**
- `#EXTINF` entries with exactly one HTTP(S) stream URL: **3,304 / 3,304**
- Missing or multiple stream URLs: **0**
- Duplicate stream URLs: **0**
- Duplicate primary channel identities outside Backup/Review roles: **0**
- External `tvg-logo` URLs: **0**
- Repository-local `/logos/` logo references: **2,860**
- Blank logo attributes: **444** (no invented or external artwork was added; individual local asset existence was not probed in this blocked run)
- Adult group: **366**
- Review: **1,117**
- Backup: **372**
- New Channels entries: **0**
- New Backups entries: **0**
- The current channel-group tail is **Adult → Review → Backup**. The New Channels/New Backups category names remain in the playlist category registry, but there are no channel rows in either queue at this snapshot.
- Existing News, Kids, Religious and Sports groups remain untouched; this run made no broad deletion or reclassification.

## Policy blocker found: Fashion TV

The repository discovery code is inconsistent with the requested exception. In `scripts/discover_international_channels.py`, `discovery_eligibility()` explicitly returns **“Fashion TV is a preserved legacy exception, not a discovery genre”** and then rejects the Fashion TV target. The report text describes Fashion TV as allowed, but the executable candidate filter still blocks new Fashion TV discoveries. A separate code-and-test repair is required before a future run can fully honor the Fashion TV exception. No playlist rows were changed here.

## Validation

| Check | Result |
|---|---:|
| M3U header present | PASS |
| Every EXTINF has exactly one URL | PASS |
| Duplicate stream URLs | 0 |
| Duplicate primary identities outside backup/review roles | 0 |
| External logo URLs | 0 |
| Fresh source-category feed scan | NOT RUN |
| Adult/Fashion/Movie/Music candidate classification | NOT RUN |
| Live stream probes | NOT RUN |
| Five-channel country threshold evaluation | NOT RUN |

## Rejected / held candidates

No candidate-level decisions were made. Today's source feed was not fetched or classified; rejection and hold counts are **not available**, rather than zero eligible candidates.

## Changes and blockers

- Playlist additions/repairs committed: **none**
- Playlist file changed: **no**
- Report-only update: this dated report.
- Primary blocker: no available workflow-dispatch action and local GitHub DNS resolution failure.
- Additional policy blocker: Fashion TV is still rejected by the executable discovery code.
- Next required action: restore/enable a workflow-dispatch path and repair/test the Fashion TV exception before the next complete International discovery publication.

## Commit

Report-only commit; no playlist content was modified.