# EPG Coverage & Mapping Report

Updated: **2026-10-27**

## Status: BLOCKED — public guide publication is not authorized yet

The public XMLTV file `epg/epg.xml` is not published. The source inventory still lacks documented public-redistribution approval for every active source. Historical mapping counts are not presented as current coverage.

- Public guide: **not published**
- Redistribution approval: **not confirmed**
- Current published coverage percentage: **not available**
- Previous mapping statistics: **historical diagnostics only**

## Pipeline changes prepared

- The generator and mapping scanner now share a synchronized source list.
- EPG.PW feeds, which do not have established re-hosting permission, were removed from the active configuration.
- The official RTV schedule parser is included as a candidate source for exact `RTV.bd` mapping. Actual new coverage must be measured by a successful, authorized refresh; no improvement percentage is claimed yet.
- Twenty-five additional IPTV-EPG.org country feeds have been registered as candidates for international channel matching. They remain blocked from public redistribution until each source is cleared.
- Legacy `epgpw:` mapping IDs are removed during the next refresh.
- A source-level rights register and fail-closed checker now cover active XMLTV feeds, schedule-site scrapers, the supplemental source repository and any configured private feed.

See [`epg/README.md`](../epg/README.md) and [`epg/source-rights-register.csv`](../epg/source-rights-register.csv) for the exact status and re-enable checklist.

**Do not set `EPG_REDISTRIBUTION_APPROVED=true` until every active source is explicitly approved for public redistribution.** A successful technical fetch or a channel-ID match does not grant those rights.
