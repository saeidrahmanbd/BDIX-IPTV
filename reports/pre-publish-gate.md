# Pre-Publish Safety Gate

Generated: **2026-11-11T08:34:03+00:00**
Source playlist SHA-256: **34f9bc33c915a05f01807e768ede043d93d7e59798afa56826f95acd3cf0fbde**

Status: **BLOCK**

- Current entries: **1143**
- Duplicate stream URLs: **0**
- Primary streams removed: **0**
- Primary streams intentionally removed as known bad: **0**
- Primary streams quarantined: **0**
- Review entries reclassified: **0**
- Review entries promoted: **0**
- Authorized review promotions: **0**
- Review entries deleted: **0**
- Duplicate primary channel numbers: **0**
- Primary entries missing channel numbers: **22**
- Primary channel-number sequence issues (non-blocking; existing row order is protected): **543**
- Numbered review entries: **17**
- Same-ID metadata name conflicts: **0**
- Orphan Backup entries: **3**
- Active rows with incomplete required metadata: **0**
- tvg-id/channel-id inconsistencies: **0**
- Entries missing tvg-language: **0**
- Raw resolution/geoblock name tags: **0**
- Missing logos in active groups: **0**
- Missing logos deferred in review groups (Review/New Channels/New Backups): **0**
- External logo URLs: **0**
- Incorrect/placeholder/generic logos: **0**
- Missing referenced local logo files: **0**
- Entries added this run: **0**
- Entries removed this run: **0**
- Entries modified this run: **0**

## Protected-queue policy
New Channels and New Backups are active BD/IN-only review queues used by discovery and validation. Backup and Review are protected queues; orphan Backup streams may be quarantined into Review without URL loss. Review, New Channels and New Backups are excluded from Xtream. A maintenance run must not silently delete, promote, or reclassify them.

## Channel-Number Sequence Review
Existing playlist row order is preserved; numbering sequence discrepancies are reported for review and do not trigger automatic reordering. Issues found: **543**.

## Blocking Reasons
- duplicate primary identities: 1
- orphan Backup entries: 3
- primary entries missing tvg-chno: 22
- review entries still numbered: 17

## Review-queue logo gaps

These entries have no verified local logo available yet. They remain in the review queue without an external or placeholder logo.

None.

## Metadata conflicts

None.

## Raw name tags

None.

## Queue validation

New Channels/New Backups contain only validated BD/IN entries.

## Missing local logo files

| Channel | Group | Referenced filename |
|---|---|---|
| — | — | none |

## Blocked logo references

| Channel | Group | Blocked filename |
|---|---|---|
| — | — | none |
