# Primary / Backup Integrity Audit

- Based on commit: **a123ced31a6cb4107e38e54aff1f12f5b1e628c3**
- Original EXTINF blocks: **1407**
- Zero-URL malformed records removed: **27** (these contained no playable stream URL)
- Playable stream entries retained: **1380**
- Primary entries: **678**
- Backup entries: **451**
- Review entries: **251**
- Exact-English primary channels moved to International: **112**
- Duplicate primary copies retained as Backup: **8**
- Backup rows reconciled by ID: **451**
- Backup rows reconciled by unique normalized name: **31**
- Orphan Backup streams promoted to a primary group: **5**
- Unresolved Backup streams moved to Review: **4**
- Logo references repaired to verified local assets: **11**
- Rows moved to Review for missing/unverified logos: **46**
- Rows moved to Review for unknown country: **20**

## Final invariant checks

- Required active metadata: **PASS**
- Existing local non-placeholder logos for primary: **PASS**
- Duplicate primary identities: **0**
- Orphan Backup rows: **0**
- Duplicate stream URLs: **0**
- English-only channels outside International: **0**
- All playable stream URLs preserved: **PASS**
- Every Backup row matches exactly one primary: **PASS**
- Sequential primary numbering: **PASS**
- Review queue unnumbered; blocked logos cleared: **PASS**

Unverified language was not guessed. Entries with unresolved country/logo metadata remain in Review. No stream URL was removed; the 27 malformed EXTINF blocks removed had no associated playable URL. EPG mapping and XMLTV regeneration are delegated to the post-push EPG refresh workflow; no unsupported EPG IDs were invented.
