# BDIX-IPTV Automation V2 — Python Script Dependency Audit

**Static baseline:** `46275f5ebafa2ae1b56f3e480f684ac1e85ae45e`  
**Scope:** The repository's 79-file `scripts/` inventory, workflow call-sites, and a source-level import audit of the core mutation, validation, discovery, logo, EPG, and scheduling modules.  
**Method:** Python import statements were inspected in the critical paths; workflow YAML script references and git staging scopes were mapped separately. This is a static graph: runtime imports, subprocess calls constructed dynamically, and behavior hidden in downloaded dependencies require later execution-level verification.

## 1. Local Python import edges observed

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
| `migrate_owner_requested_main_queues.py` | `discover_bd_in_new_queues`, `country_verification` |
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

Other inspected scripts have no direct local Python import edge in the inspected source, but may still be called from workflows or subprocesses. Absence of a direct import does not mean a script is unused.

## 2. High-coupling modules

### Discovery and classification

`discover_bd_in_new_queues.py` is imported by owner-requested migration, International playlist reorganization, final playlist hardening, main-playlist group reclassification, and the thin discovery wrapper. The International discovery module is imported by International reorganization and discovery-run validation. The same discovery code therefore participates in multiple workflow owners and validation paths.

### Playlist policy and safety

`stream_url_identity.py` is a shared identity primitive used by maintenance helpers, audit, protection, migration, reorganization, health and repair modules. It should remain a small, pure, deterministic library with extensive contract tests. It must not contain playlist mutation behavior.

`country_verification.py` is imported by main playlist discovery, migration, reclassification, hardening and audit. Country policy differs by playlist, so a common evidence parser should feed separate IPTV and International policy decisions rather than a single implicit country allowlist.

### EPG

The EPG generator is a central dependency of EPG mapping augmentation and fetching. `epg_coverage.py` imports the generator, source registry/cache and mapping policy. This forms a tightly coupled generation/coverage subsystem; V2 should split source acquisition, normalized channel identity, mapping qualification, XMLTV generation, and publication gating into separate deterministic stages.

### International health and reorganization

`international_stream_health.py` imports `reorganize_international_playlist.py`, which in turn imports discovery code. This means a stream-health operation can invoke a broad reorganization pipeline. V2 should make health evaluation produce a result set; a separate policy application stage can then decide Review recovery or three-day retirement.

### Logo management

Logo migration imports asset naming and embedded-image recovery. The logo source catalog is consumed by the separate logo repair workflow. This can be consolidated into a read-only catalog/resolver plus a narrowly scoped logo-attribute writer.

## 3. Structural issues and recommended boundaries

1. **Avoid workflow scripts importing other workflow entrypoints.** A script named for one workflow should expose pure library functions to the engine, not act as an implicit shared service.
2. **Separate pure policy from mutation.** Parsers, identity normalizers, classifiers and policy resolvers should return structured decisions; only the scoped publisher may write.
3. **No cross-playlist mutator imports.** IPTV and International engine entrypoints must not import one another's mutation modules. Shared pure utilities are allowed.
4. **No health-to-reorganization side effect.** Health probing should not directly invoke broad playlist rewriting.
5. **EPG candidate-first.** Source probes and mapping enrichment should not directly publish the production guide.
6. **Make CLI wrappers thin.** Workflow YAML should call a small number of stable engine commands; Python modules own the testable orchestration.
7. **Declare file ownership.** Each engine must publish only its explicitly assigned artifacts; a report/dashboard generator must never stage playlist files.
8. **Use typed artifacts between stages.** Discovery candidates, probe results, migration approvals, logo provenance and EPG mappings should have versioned schemas.
9. **Keep policy in one place.** The same machine-readable policy should drive engine behavior, validator expectations and documentation checks.

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

The exact module split is a design target, not a deletion plan. Existing code should be moved/reused only after its contract is understood and fixture tests demonstrate equivalent or safer behavior.

## 5. Dependency audit conclusion

The problem is not merely the number of scripts. The key structural issue is that workflow entrypoints, policy logic, validation and mutation are entangled through shared imports and overlapping writers. The V2 rebuild should retain valuable pure utilities (especially stream identity, playlist parsing, source registries and safety invariants) while replacing the cross-coupled orchestration and mutation boundaries.

No production files were changed during this audit.
