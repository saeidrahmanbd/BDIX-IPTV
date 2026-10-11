#!/usr/bin/env python3
"""Update reports/maintenance-history.json from the latest audit/health reports."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

AUDIT_PATH = Path('reports/playlist-audit.md')
HEALTH_PATH = Path('reports/stream-health.md')
HISTORY_PATH = Path('reports/maintenance-history.json')

def metric(text: str, label: str) -> int | None:
    match = re.search(rf'- {re.escape(label)}: \*\*(\d+)\*\*', text)
    return int(match.group(1)) if match else None

def load_history() -> list:
    try:
        data = json.loads(HISTORY_PATH.read_text(encoding='utf-8')) if HISTORY_PATH.exists() else []
    except (OSError, json.JSONDecodeError):
        data = []
    return data if isinstance(data, list) else []

def metrics_from_reports(health_optional: bool) -> dict:
    audit = AUDIT_PATH.read_text(encoding='utf-8')
    if health_optional:
        health = HEALTH_PATH.read_text(encoding='utf-8') if HEALTH_PATH.exists() else ''
    else:
        health = HEALTH_PATH.read_text(encoding='utf-8')
    return {
        'timestamp_utc': datetime.now(timezone.utc).isoformat(),
        'entries': metric(audit, 'Playlist entries'),
        'unique_channel_ids': metric(audit, 'Unique channel IDs'),
        'duplicate_ids': metric(audit, 'IDs with multiple streams'),
        'duplicate_urls': metric(audit, 'Duplicate stream URLs'),
        'metadata_conflicts': metric(audit, 'Metadata conflicts'),
        'logo_exceptions': metric(audit, 'Logo exceptions'),
        'primary_number_collisions': metric(audit, 'Primary channel-number collisions'),
        'protected_primary_changes': metric(audit, 'Protected primary-entry changes'),
        'health_tested': metric(health, 'Streams tested'),
        'health_failures': metric(health, 'Failed this check'),
        'health_persistent': metric(health, 'Persistent failures (3+ consecutive)'),
    }

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--refresh', action='store_true', help='Refresh the latest history record after a rollback')
    args = parser.parse_args()
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    history = load_history()
    if args.refresh:
        if isinstance(history, list) and history:
            history[-1].update(metrics_from_reports(health_optional=False))
            HISTORY_PATH.write_text(json.dumps(history[-180:], indent=2) + '\n', encoding='utf-8')
        return
    history.append(metrics_from_reports(health_optional=True))
    HISTORY_PATH.write_text(json.dumps(history[-180:], indent=2) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
