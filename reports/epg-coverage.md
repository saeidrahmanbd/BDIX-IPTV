# EPG Coverage & Mapping Report

Updated: **2026-10-27** (status note; live coverage is recalculated by the next successful EPG refresh)

## Status: PIPELINE ENABLED — REFRESH REQUIRED

The refresh workflow is enabled again. It will rebuild and publish `epg/epg.xml` at the public raw URL after source-fetch, freshness and quality checks succeed.

- Public guide: [epg.xml](https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml)
- Automatic refresh: daily at 10:17 Asia/Dhaka and on relevant playlist/EPG input changes
- Current published-guide coverage: **not verified in this status note**
- Rights register: unresolved source reviews remain visible in [source-rights-register.csv](../epg/source-rights-register.csv)

## Source and mapping improvements

- Candidate sources are synchronized between generation and mapping discovery.
- Explicitly prohibited EPG.PW feeds are not active.
- A personalized M3U4U feed is not passed into the public build.
- The official RTV schedule parser is included for possible exact `RTV.bd` matching.
- Twenty-five extra IPTV-EPG.org country feeds are configured as international candidates.
- The generator filters placeholder titles and runs publication freshness/quality gates before committing the guide.

This is a status note rather than a live coverage measurement until a successful refresh replaces it. Do not infer current programme coverage from historical mapping totals.