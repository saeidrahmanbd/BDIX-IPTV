# Programme-guide data: publication disabled pending rights review

## Current status

**The public XMLTV guide is not published.** Redistribution rights have not been confirmed for every source feed, so the repository has disabled automated guide publication and removed public playlist-header references to `epg/epg.xml`. Do not re-add an EPG URL to a playlist or deploy a worker that serves programme-guide data until documented permission covers the actual schedule data from every included source.

A feed being reachable, or its source-code repository using an MIT licence, does not establish rights to redistribute the feed's programme data. The SunDirect GO feed added on 2026-10-26 has no confirmed schedule-data redistribution permission and is excluded from the source configuration.

## Re-enable checklist

Publication may be re-enabled only after all of the following have been recorded:

1. Source-specific terms or written permission explicitly allow the intended retrieval, transformation, and public redistribution of programme listings.
2. Rights have been reviewed separately for every source, including any supplemental/private M3U4U feed.
3. Unapproved feeds and any aliases that depend on them have been removed from both analysis and generation source lists.
4. A licence/permission register is checked into the repository, and tests fail closed when any active source lacks approval.
5. The guide passes XMLTV structure, programme-title, time-window, provenance and source-policy tests.
6. The owner explicitly sets the repository Actions variable `EPG_REDISTRIBUTION_APPROVED=true` and updates the code paths that intentionally gate publication.

Until then, the variable must remain unset or set to `false`; the EPG refresh workflow will skip, maintenance will not fetch/generate/publish guide data, and both Xtream `xmltv.php` endpoints report that the service is disabled.

## Internal diagnostic scripts

The `scripts/epg_coverage.py` and `scripts/generate_epg.py` sources remain as non-publishing tooling for later rights review. Source lists and old coverage reports are technical diagnostics only; their schedule counts are not evidence of permission and must not be presented as current guide availability. A playlist's `tvg-id` is not a promise that programme listings are available.

The all-playlist identity mapping is named `reports/epg-channel-mapping.csv`. It excludes Adult-group rows from public reporting to avoid listing named performers; regenerate it only through the approved internal workflow.

## Privacy and credentials

Never commit personalized M3U4U endpoint URLs, usernames, passwords, session tokens, or other private provider credentials. Keep any future supplemental feed URL in the repository secret `M3U4U_XMLTV_URL`, and use it only after its retrieval and redistribution permissions have been confirmed.
