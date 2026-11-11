# Primary / Backup Integrity Audit

- Based on commit: **cc790abe1819eaa31110b1ca07910bddba025d2d**
- Stream entries after M3U normalization: **1380**
- Misattributed duplicate URL lines removed from wrong channel entries: **14**
- Repeated URL references deduplicated: **0**
- Formerly empty primary rows restored from matching working streams: **7**
- Exact-English primary channels assigned to International: **157**
- Duplicate primary rows retained as Backup: **3**
- Backup links reconciled by ID: **454**
- Backup links reconciled by unique channel name: **0**
- Orphan Backup streams promoted: **0**
- Unresolved Backup streams kept in Review: **0**
- Logos repaired: **0**
- Unverifiable logo entries quarantined: **0**
- Unknown-country entries quarantined: **0**

## Final checks

- One HTTP(S) URL per EXTINF record: **PASS**
- All unique stream URLs preserved: **PASS**
- Duplicate URL references: **0**
- Duplicate primary channel IDs: **0**
- Orphan Backup rows: **0**
- Required primary metadata gaps: **0**
- Missing/nonlocal/blocked active logos: **0**
- English-only primary rows outside International: **0**
- Sequential primary numbering: **PASS**

Unverified metadata was not guessed. Review entries retain their stream URLs. Repeated URLs that were listed under an unrelated channel record were removed only from the incorrect duplicate placement. EPG mapping and XMLTV regeneration are handled by the post-commit EPG refresh workflow; no unsupported EPG IDs were fabricated.
