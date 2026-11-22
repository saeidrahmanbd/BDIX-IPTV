# IPTV Channel Discovery

Generated: **2026-11-22T06:58:06+06:00** (Asia/Dhaka)

## Run status

**BLOCKED — fresh discovery stage did not execute.**

- Playlist: `IPTV-Playlist.m3u`
- Current playlist blob: `c3c20a71713cd27f3e36a179242161b185078cdc`
- Candidates added: **0**
- Candidates rejected after fresh evaluation: **0**
- Candidates held for manual review: **not assessed** — no fresh source-feed discovery or stream probes ran.
- This is not a finding that no eligible channels exist. No current candidate set was produced.

## Freshness and execution evidence

- Latest scheduled IPTV discovery run found: [run #44863492835](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/44863492835), created **2026-11-21 09:54:59 +06:00**, conclusion: success.
- No IPTV New Channel Discovery run for Bangladesh date **2026-11-22** was present in the Actions run list checked at this report time.
- Latest Discovery Schedule Watchdog run found: [run #44905290354](https://github.com/saeidrahmanbd/BDIX-IPTV/actions/runs/44905290354), created **2026-11-21 18:43:08 +06:00**, conclusion: success. Its log confirms that it checked and found a successful IPTV discovery run for **2026-11-21**. No watchdog run for **2026-11-22** was present.
- Exact execution blocker: the connected GitHub actions available in this run support reading files/runs and repository writes, but expose no workflow-dispatch action. The GitHub fetch action is read-only. A local fallback was attempted with `git ls-remote https://github.com/saeidrahmanbd/BDIX-IPTV.git HEAD`; it failed with **`Could not resolve host: github.com`**, so the discovery script could not be run locally.
- The last successful discovery report is from 2026-11-21 and was not reused as today's result.

## Current playlist structural snapshot (read-only)

- Entries: **1,389**
- `#EXTINF` entries with exactly one HTTP(S) stream URL: **1,389 / 1,389**
- Missing or multiple stream URLs: **0**
- Duplicate stream URLs: **0**
- Duplicate primary channel identities outside Backup/Review roles: **0**
- External `tvg-logo` URLs: **0**
- Logo attributes pointing to repository-local `/logos/` assets: **1,389** (path references checked; individual asset existence was not probed in this blocked run)
- New Channels: **37**
- New Backups: **19**
- Backup: **443**
- Review: **196**
- Queue order: **New Channels → New Backups → Backup**; Review follows Backup in the current playlist.
- Indian sports remain permitted by the current discovery policy. No current feed candidates were evaluated, and no existing playlist rows were changed.

## Validation

| Check | Result |
|---|---:|
| M3U header present | PASS |
| Every EXTINF has exactly one URL | PASS |
| Duplicate stream URLs | 0 |
| Duplicate primary identities outside backup/review roles | 0 |
| External logo URLs | 0 |
| Live stream probes in this run | NOT RUN |
| Fresh Bangladesh/India source-feed scan | NOT RUN |
| Country threshold evaluation | NOT RUN |

## Rejected / held candidates

No candidate-level decisions were made. The stage was blocked before fetching and classifying today's Bangladesh and India source feeds; therefore rejection and hold counts are **not available**, rather than zero eligible candidates.

## Changes and blockers

- Playlist additions/repairs committed: **none**
- Playlist file changed: **no**
- Report-only update: this dated report.
- Primary blocker: no available workflow-dispatch action and local GitHub DNS resolution failure.
- Next required action: restore/enable a workflow-dispatch path or let the repository's scheduled/watchdog workflow execute, then verify its fresh run and stream-probe results before publishing candidates.

## Commit

Report-only commit; no playlist content was modified.