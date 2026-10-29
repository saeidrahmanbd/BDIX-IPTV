# Public EPG

## Overview

This directory contains the repository's public XMLTV programme guide and the supporting mapping, validation, and coverage data used to maintain it.

**Public XMLTV:**

`https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml`

The maintained IPTV playlists and Xtream workers use this URL as their common EPG endpoint.

## EPG Pipeline

The EPG workflow:

1. Reads the current channel inventory from the maintained playlists.
2. Discovers and refreshes channel-to-EPG mappings.
3. Collects schedules from useful accessible EPG/XMLTV sources.
4. Combines and deduplicates programme data, preferring stronger/current matches.
5. Validates channel IDs, programme titles, intervals, freshness, and coverage.
6. Publishes `epg/epg.xml` and updates the related reports when the result passes the publication gates.
7. Preserves the last known-good guide when a new candidate is empty, degraded, or otherwise fails validation.

The workflow runs automatically on the daily schedule and when relevant playlist or EPG inputs change. It can also be started manually from GitHub Actions.

## Source Policy

The objective is **maximum practical EPG coverage**. Useful EPG/XMLTV sources are not categorically excluded merely because they are third-party.

The pipeline combines configured public or otherwise accessible upstream feeds for discovery, channel mapping, and schedule acquisition. Sources are deduplicated, and the strongest current schedule is preferred for each channel. EPG.PW is deliberately excluded from automated public-guide ingestion because its Terms of Service prohibit copying/retransmission and limit use to personal use. Do not re-enable it for the public guide without explicit permission for public redistribution. This source-specific exclusion does not disable the rest of the EPG pipeline. Private credentials, session tokens, and personalized M3U4U feed URLs are never committed to the repository or exposed in logs. The optional source-review register is advisory: it is not a prerequisite for generation, mapping, reporting, or publication. Its status does not itself grant upstream permission; technical publication gates continue to validate XMLTV structure, schedule quality, freshness, and coverage.

## Coverage and Mapping

EPG coverage is continuously improved by:

- Expanding channel mappings across all maintained playlists, with priority for Bangladesh and high-use Indian channels.
- Using multiple useful XMLTV/EPG sources rather than relying on a single provider.
- Matching by stable channel IDs and validated channel identities and aliases.
- Preferring current and future programme schedules.
- Deduplicating overlapping schedules from multiple sources.
- Rejecting placeholder, invalid, or clearly mismatched programme data.
- Avoiding false matches merely to increase the coverage percentage.

Current coverage should always be taken from the latest generated reports rather than historical mapping totals.

## Files and Reports

- [`epg.xml`](epg.xml) — published XMLTV guide.
- [`epg-channel-mapping.csv`](../reports/epg-channel-mapping.csv) — current channel-to-EPG mapping data.
- [`epg-coverage.md`](../reports/epg-coverage.md) — current coverage and publication metrics.
- [`epg-three-playlist-audit.md`](../reports/epg-three-playlist-audit.md) — published-guide audit across all three playlists.
- [`epg-source-audit.md`](../reports/epg-source-audit.md) — per-source availability, usable schedule counts, and failure details.
- [`epg-publish-freshness.md`](../reports/epg-publish-freshness.md) — guide freshness and publication validation.
- [`epg-refresh.yml`](../.github/workflows/epg-refresh.yml) — EPG refresh workflow.

## Validation and Publication

A guide is published only after the EPG validation and publication checks pass. These checks protect the public guide from empty, stale, malformed, or materially degraded output.

A failed refresh does not automatically mean the public guide is unavailable. The workflow is designed to retain a validated last-known-good guide when the new candidate fails its quality gates.

## Troubleshooting

### EPG URL returns 404

Check the latest **Refresh IPTV EPG** workflow run and its publication steps. Confirm that `epg/epg.xml` exists on `main` and that the workflow completed its publication stage successfully.

### EPG loads but some channels have no programmes

Check the latest coverage report and channel-mapping snapshot. Missing schedules normally indicate that a channel has no reliable matching schedule source yet. Add or improve a mapping rather than assigning an unrelated channel solely to increase the coverage percentage.

### Xtream worker returns an EPG/XMLTV error

Test the public XMLTV URL first. If it is available and valid, inspect the worker configuration and confirm that it references the repository's public XMLTV endpoint.

## Security

Never commit:

- Xtream usernames or passwords
- Provider credentials
- Private or personalized feed URLs
- Session tokens
- API keys or other secrets

Use GitHub Actions secrets for credentials or private source endpoints.