# BDIX-IPTV Automation V2 — Python Script Dependency Audit

**Static baseline:** `46275f5ebafa2ae1b56f3e480f684ac1e85ae45e`  
**Scope:** The 79-file `scripts/` inventory, workflow call-sites, and source-level imports of critical mutation, validation, discovery, logo, EPG, and scheduling modules.  
**Method:** Python import statements were inspected in core paths; workflow YAML script references and git staging scopes were mapped separately. This is a static graph: runtime imports, dynamically constructed subprocess calls, and behavior hidden in dependencies require execution-level verification.

## 1. Local Python import edges observed

Historical note: the one-time owner-requested IPTV queue migration and its probe script were retired on 2026-11-14 after the owner approved the owner-curated playlist boundary. They are not part of the active automation dependency graph.

| Importing module | Local module dependencies |
|---|---|
| `audit_playlist.py` | `playlist_order_policy`, `country_verification`, `restore_protected_review`, `stream_url_identity` |
| `augment_epg_mapping_from_additional_sources.py` | `epg_coverage`, `generate_epg` |
| `augment_epg_mapping_from_iptv_org.py` | `fetch_iptv_org_epg`, `generate_epg` |
| `discover_bd_in_new_queues.py` | `country_verification`, `stream_url_identity` |
| `enforce_primary_backup_integrity.py` | `permanent_removals`, `stream_url_identity`, `logo_asset_naming` |
| `epg_coverage.py` | `official_epg_sources`, `epg_source_cache`, `epg_mapping_policy`, `generate_epg` |
| `fetch_iptv_org_epg.py` | `generate_epg` |
| `final_playlist_hardening.py` | `stream_url_identity`, `country_verification`, `discover_bd_in_new_queues` |
| `maintenance_helpers.py` | `logo_asset_naming`, `stream_url_identity`, `permanent_removals`, `restore_protected_review` |
| `migrate_external_logos_fixed.py` | `logo_asset_naming`, `logo_embedded_png` |
| `playlist_policy_repair.py` | `permanent_removals`, `stream_url_identity` |
| `probe_bangladesh_official_schedule_pages.py` | `official_epg_sources` |
| `reclassify_main_playlist_groups.py` | `country_verification`, `discover_bd_in_new_queues` |
| `reconcile_playlist_consistency.py` | `stream_url_identity` |
| `restore_protected_review.py` | `permanent_removals`, `stream_url_identity` |
| `run_bd_discovery_with_policy.py` | `discover_bd_in_new_queues` |
| `run_generate_epg.py` | `generate_epg`, `augment_epg_mapping_from_additional_sources` |
| `reorganize_international_playlist.py` | `discover_international_channels`, `discover_bd_in_new_queues`, `stream_url_identity` |
| `international_stream_health.py` | `reorganize_international_playlist` |
| `validate_discovery_run.py` | `discover_international_channels`, `discover_bd_in_new_queues`, `stream_url_identity` |
| `validate_international_health_output.py` | `international_stream_health` |

Other inspected scripts have no direct local Python import edge in their inspected source, but may still be called by workflows or subprocesses. No direct import does not mean unused.

## 2. High-coupling modules

- **Discovery/classification:** `discover_bd_in_new_queues.py` is imported by International reorganization, final hardening, main-playlist group reclassification and the discovery wrapper. International discovery is imported by reorganization and discovery-run validation.
- **Playlist safety:** `stream_url_identity.py` is a shared primitive across maintenance, audit, protection, migration, reorganization, health and repair. Keep it pure and deterministic.
- **Country policy:** `country_verification.py` is reused across discovery, migration, reclassification, hardening and audit. Shared evidence parsing should feed separate playlist-specific policies.
- **EPG:** The generator is a dependency of mapping augmentation and fetch modules. Coverage imports the generator, source registry/cache and mapping policy. Split acquisition, mapping qualification, XMLTV generation and publication.
- **International health:** `international_stream_health.py` imports `reorganize_international_playlist.py`, which imports discovery code. Health probing can therefore invoke broad playlist rewriting; V2 should make health produce evidence, then let a separate policy stage apply transitions.
- **Logos:** Logo migration imports asset naming and embedded-image recovery; the source catalog is consumed by the separate repair workflow. Consolidate into one catalog/resolver and one scoped writer.

## 3. Structural issues and recommended boundaries

1. Do not make workflow entrypoints import one another as shared services.
2. Separate pure policy from mutation: parsers, identity normalizers and classifiers return structured decisions; only the scoped publisher writes.
3. No cross-playlist mutator imports. Shared pure utilities are allowed.
4. Health probing must not invoke broad reorganization as an implicit side effect.
5. EPG source probes and mapping enrichment must not publish the production guide directly.
6. Keep workflow YAML thin; Python engine entrypoints own testable orchestration.
7. Declare file ownership; reporting must never stage playlists.
8. Use versioned schemas for discovery candidates, probe results, migration approvals, logo provenance and EPG mappings.
9. Machine-readable central policy must drive engine behavior, validator expectations and docs.

## 4. V2 target module layout

```text
automation/
  policy/
    schema.json
    playlists.yml
    groups.yml
    protected_fields.yml
  core/
    playlist_parser.py
    stream_identity.py
    transaction.py
    run_ledger.py
    publisher.py
  engines/
    iptv_maintenance/
    international_maintenance/
    discovery/
    logos/
    stream_health/
    epg/
    reporting/
  validators/
    playlist_invariants.py
    policy_conformance.py
    artifact_freshness.py
tests/
  fixtures/
  contract/
  integration/
```

This is a target, not a deletion plan. Reuse/move code only after contracts and fixture tests establish equivalent or safer behavior.

## 5. Conclusion

The issue is not just script count. Workflow entrypoints, policy, validation and mutation are entangled through shared imports and overlapping writers. V2 should retain valuable pure utilities while replacing cross-coupled orchestration and mutation boundaries.

No production files were changed during this audit.
