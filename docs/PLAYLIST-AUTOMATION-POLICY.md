# Playlist Automation Policy

This policy is mandatory for every scheduled workflow, maintenance script, discovery job, repair utility and future automation change.

## IPTV-Playlist.m3u — owner-curated

Automation may:
- Normalize channel names and display labels.
- Correct channel IDs and metadata, including country and language.
- Replace external logo references with verified repository-local assets.
- Improve EPG identity mappings and report schedule gaps.
- Validate stream URLs and report health/risk findings.
- Discover, filter and add qualifying new channels and alternate streams under the main playlist's discovery policy.
- Repair formatting and metadata without changing existing stream identity or placement.

Automation must never:
- Delete an existing stream row.
- Change an existing row's group.
- Reorder existing rows or change their relative position.
- Automatically demote, promote, migrate or relocate an existing row.

New discoveries may be inserted, but all pre-existing stream URLs must remain present, in their original groups and in their original relative order. Metadata and logo fields may be corrected. An inconclusive stream probe is not authorization to remove a row.

The maintenance workflow snapshots the existing main playlist before mutation and verifies the invariant before publication. Any deletion, URL replacement, group change or reordering blocks the commit.

## International-Playlist.m3u — automation-controlled

Automation has authority to add, filter, delete, move, migrate, deduplicate, promote, demote and reorganize entries according to the established International country/genre eligibility policy. It may reconcile primary and Backup rows, enforce country-group thresholds, maintain discovery/review queues, normalize metadata, localize logos and improve EPG mappings.

The International policy is independent of the main playlist's preservation guard. International maintenance must not use the main playlist's protected-row snapshot as a reason to retain an ineligible International entry.

## Engineering requirements

- Every script must identify its target playlist explicitly; avoid ambiguous all-playlist mutation defaults.
- A workflow may read the main playlist as a metadata/reference source, but must not use that as permission to restructure it.
- Shared writer workflows must continue using the repository's common main-branch concurrency group.
- Tests must cover main-playlist deletion, relocation and reordering protection, plus permitted metadata edits and additions.
- Update this policy and its regression tests whenever automation permissions change.
