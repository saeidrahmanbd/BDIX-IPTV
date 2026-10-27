# EPG data: rights review and publication gate

## Current status

**Public XMLTV publication remains disabled.** The previous `epg/epg.xml` file was removed because public redistribution permission is not documented for the full set of programme-data sources. Public accessibility, a free personal-use feed, or an open-source fetcher does not itself grant permission to re-host the underlying listings in a public guide.

The old EPG.PW feeds have been removed from the active source pipeline. The EPG.PW terms restrict copying or distributing site content unless expressly allowed: [EPG.PW terms](https://epg.pw/terms.html). Do not restore those feeds without explicit written permission for public redistribution.

## What has been improved

- Coverage and generation now use the same source list across all three maintained playlists.
- The existing official RTV schedule parser is now included in the candidate mapping/generation source list. It can map the exact `RTV.bd` channel identity when current schedule rows are available; the next approved refresh must verify actual coverage.
- Legacy `epgpw:` mapping IDs are discarded during the next mapping refresh, so a stale mapping cannot quietly resurrect a removed feed.
- A source-by-source register is maintained in [`source-rights-register.csv`](source-rights-register.csv).
- `scripts/check_epg_source_rights.py` and its tests enforce a fail-closed rule: every active XMLTV feed, scraped schedule website, supplemental source repository, and configured private feed must have explicit approval before public guide generation can run.

## Why it is not switched on yet

The current register marks active sources as `REVIEW_REQUIRED` until there is evidence allowing public redistribution. A feed that can be downloaded or pasted into a personal IPTV player is not automatically licensed for public re-hosting. The targeted `iptv-org/epg` workflow also aggregates third-party schedule sources, so the repository's software licence alone cannot clear every underlying programme feed.

The register's `APPROVED` status requires all of the following for each active source:

1. An evidence URL to explicit source terms or written permission.
2. A review date.
3. A positive description of the permitted scope, specifically including retrieval, transformation and **public redistribution** of schedule data.
4. Removal from the active pipeline if the source is prohibited or its terms do not cover the intended use.

The source-rights checker must pass before setting the repository Actions variable `EPG_REDISTRIBUTION_APPROVED=true`. Do not set that variable while active sources remain unapproved. The guide must then pass the XMLTV structure, programme-title, time-window, provenance and quality gates before publication.

## Current coverage versus mapping

The technical mapping registry is `reports/epg-channel-mapping.csv`. It is a historical/diagnostic snapshot, not evidence that a current public guide exists. A channel ID match is not usable coverage unless the current feed has valid programme intervals and real, non-placeholder titles. Do not report old mapping percentages as current coverage while the pipeline is blocked.

There is no verified general-purpose public XMLTV source for the domestic Bangladesh channel set. The newly configured RTV schedule is one useful official-site candidate, not a substitute for full Bangladesh coverage. Other domestic channels should remain unmapped unless an exact channel-specific guide is found and its terms permit the intended use. Never map a Bangladeshi service to a similarly named Indian or foreign channel just to inflate percentages.

## How to re-enable safely

1. Review [the source rights register](source-rights-register.csv) and the actual terms or written permission for each feed and scraper site.
2. Remove sources without suitable rights, or record explicit permission and mark them `APPROVED` with evidence.
3. Run:
   ```bash
   python scripts/check_epg_config.py
   python -m unittest discover -s tests -p 'test_epg_config.py'
   python -m unittest discover -s tests -p 'test_epg_source_rights.py'
   python scripts/check_epg_source_rights.py
   ```
4. Once the rights checker passes, deliberately set the repository Actions variable `EPG_REDISTRIBUTION_APPROVED=true` and run the **Refresh IPTV EPG** workflow.
5. Verify `reports/epg-coverage.md`, `reports/epg-publish-freshness.md` and the generated guide before re-adding the EPG URL to playlist headers or enabling the Xtream XMLTV endpoints.

Until these checks pass, the public guide stays unavailable and the Xtream `xmltv.php` endpoints remain disabled.

## Privacy and credentials

Never commit personalized M3U4U endpoint URLs, usernames, passwords, session tokens or other private provider credentials. Keep any private endpoint in the GitHub Actions secret `M3U4U_XMLTV_URL`; the checker records only the secret's key name, never its value. Its data must have explicit public-redistribution permission too.
