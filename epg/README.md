# Public EPG

## Overview

This directory contains the repository's public XMLTV programme guide and the supporting mapping, source, validation, and coverage data used to maintain it.

**Public XMLTV:**

`https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/epg/epg.xml`

The maintained IPTV playlists and Xtream workers use this URL as their common EPG endpoint.

## EPG Pipeline

The EPG workflow:

1. Reads the current channel inventory from the maintained playlists.
2. Discovers and refreshes channel-to-EPG mappings.
3. Collects schedules from available EPG/XMLTV sources.
4. Combines and deduplicates programme data.
5. Validates channel IDs, programme titles, intervals, freshness, and coverage.
6. Publishes `epg/epg.xml` and updates the related reports when the result passes the publication gates.
7. Preserves the last known-good guide when a new candidate is empty, degraded, or otherwise fails validation.

The workflow runs automatically on the daily schedule and when relevant playlist or EPG inputs change. It can also be started manually from GitHub Actions.

## Source Policy

The objective is **maximum practical EPG coverage**. Useful EPG/XMLTV sources are not categorically excluded by provider name.

Sources may be used for discovery, mapping, schedule acquisition, or publication according to their accessibility and applicable usage or redistribution conditions. Sources explicitly marked `PROHIBITED` are not used. Unresolved sources remain visible in the source-rights register and are handled according to the repository's runtime policy.

Personalized or credential-bearing feed URLs must be supplied through GitHub Actions secrets and must never be committed to the repository or exposed in logs.

## Coverage and Mapping

EPG coverage is continuously improved by:

- Expanding channel mappings across all maintained playlists.
- Using multiple useful XMLTV/EPG sources rather than relying on a single provider.
- Matching by stable channel IDs and validated channel identities and aliases.
- Preferring current and future programme schedules.
- Deduplicating overlapping schedules from multiple sources.
- Rejecting placeholder, invalid, or clearly mismatched programme data.
- Avoiding false matches merely to increase coverage.

Current coverage should always be taken from the latest generated reports rather than historical mapping totals.

## Files and Reports

- [`epg.xml`](epg.xml) — published XMLTV guide.
- [`source-rights-register.csv`](source-rights-register.csv) — source-by-source usage and rights status.
- [`epg-channel-mapping.csv`](../reports/epg-channel-mapping.csv) — current channel-to-EPG mapping data.
- [`epg-coverage.md`](../reports/epg-coverage.md) — current coverage and publication metrics.
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
