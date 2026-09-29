# Comprehensive Playlist Audit

Generated: 2026-09-29

## Scope

Static playlist structure, metadata, duplicate streams/IDs, local logo integrity, current workflow health, stream-health results, EPG coverage, and automation configuration were reviewed.

## Current Playlist Snapshot

- Playlist entries: **870**
- Bangladesh: **52**
- Indian Bangla: **37**
- Indian Movies: **54**
- Indian Music: **42**
- Indian Entertainment: **88**
- International: **57**
- Documentary & Wildlife: **62**
- Kids: **48**
- Religious: **18**
- Sports: **27**
- Backup: **368**
- Not Playing: **17**

## Static Integrity

| Check | Result |
|---|---:|
| Duplicate stream URLs | **0** |
| Duplicate active tvg-id/channel-id | **0** |
| Missing required metadata | **0** |
| External tvg-logo references | **0** |
| Backup entries carrying tvg-chno | **0** |
| HTTP stream URLs | **143** |
| Not Playing entries | **17** |

HTTP URLs are flagged for security/transport review, but were not automatically removed because HTTP alone does not prove a stream is dead.

## Latest Completed Stream Health Audit

Latest completed report checked **870 unique active stream URLs**.

- Healthy: **745**
- Redirect/temporary: **112**
- HTTP error: **7**
- Invalid HLS: **6**
- Timeout: **0**
- Connection error: **0**
- Repeated-failure candidates: **1**

The single repeated-failure candidate was **ETV Cinema**, with 3 consecutive invalid-HLS checks. It is retained because the stream-health policy is deliberately non-destructive and requires confirmed failure before removal; it is also currently represented in the non-playing/maintenance area rather than being silently deleted.

## Latest Completed EPG Programme-Row Audit

The repaired EPG audit successfully ran after the previous syntax failure.

Before the additional source expansion, the completed run reported:

- Active Indian channels audited: **252**
- LIVE/FUTURE EPG: **151**
- Channel ID only: **11**
- No guide hit: **90**
- Current/future programme coverage: **59.9%**

The audit now checks programme rows rather than merely checking whether an EPG channel ID exists.

Additional improvements have been queued:
- IN1 + IN4 EPG sources
- iptv-epg.org
- epg.pw
- removal of two currently unavailable iptv-org guide endpoints that were returning HTTP 404

The refreshed report is being regenerated automatically.

## Automation Audit

Playlist-triggered automation is now enabled for:

- Missing logo restore/fetch
- Metadata normalization
- EPG coverage
- Stream + EPG audit
- Stream health
- Backup health audit
- Live dashboard
- Changelog

Xtream deployment remains triggered by `xtream/**` changes because playlist changes do not require Worker redeployment.

## Improvements Applied During This Audit

1. **Fixed broken EPG coverage script**
   - The previous `norm_id()` implementation had a truncated Python string and caused workflow failure.
   - Replaced it with a complete, validated implementation.

2. **Changed EPG validation semantics**
   - A channel is now counted as covered only when its matched guide has at least one current/future programme row.
   - A guide containing only a channel ID is reported separately.

3. **Expanded EPG source coverage**
   - Added IN4 alongside IN1.
   - Added iptv-epg.org and epg.pw as additional sources.
   - Removed known unavailable iptv-org guide endpoints from the active coverage list.

4. **Improved Xtream EPG aggregation**
   - Added IN4 and iptv-epg.org to the Worker EPG source list.

5. **Logo lifecycle**
   - Missing logos are resolved in this order: active `logos/` → `logos/unused/` restore → external source.
   - Playlist changes automatically trigger the logo workflow.

## Remaining Items

### High priority
- Review the **90 Indian channels without a guide hit**.
- Investigate the **11 guide IDs with no current/future programme rows**.
- Replace or remove streams that accumulate repeated health failures.

### Medium priority
- Gradually replace HTTP-only streams with HTTPS equivalents where an equivalent source exists.
- Review very large backup groups and remove redundant streams only after health evidence supports removal.
- Improve EPG aliases for channels that are known to have guide coverage but currently use local IDs.

### Intentionally not changed
- Existing Sports/Religious/News categories were not bulk-deleted.
- Backup streams were not removed merely because they returned transient errors.
- No stream was declared dead solely from a single failed probe.

## Overall Result

The playlist currently has **no duplicate stream URLs, no duplicate active channel IDs, no missing required metadata, and no external logo references**. The main remaining quality gap is **EPG coverage**, followed by long-term cleanup of unreliable/HTTP-only streams and oversized backup sets.

The EPG refresh triggered by this audit is still being processed by GitHub Actions; its final regenerated report will supersede the interim 59.9% figure above.
