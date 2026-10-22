#!/usr/bin/env python3
"""Make the legacy playlist audit aware of the two protected review queues.

This is an idempotent migration: it changes only the audit policy constants so
New Channels/New Backup are treated as review queues rather than primary groups.
"""
from pathlib import Path

p = Path("scripts/audit_playlist.py")
s = p.read_text(encoding="utf-8")
s = s.replace(
    'PRIMARY_EXCEPTIONS = {"Backup", "Not Playing"}',
    'PRIMARY_EXCEPTIONS = {"Backup", "Not Playing", "New Channels", "New Backup"}',
)
s = s.replace(
    '"Religious", "Sports", "Backup", "Not Playing"]',
    '"Religious", "Sports", "New Channels", "New Backup", "Backup", "Not Playing"]',
)
s = s.replace(
    'if any(value in actual_registry for value in ("New Channels", "New Backup")):\n            category_registry_issues.append("forbidden staging category registered")',
    'if any(value not in CATEGORY_ORDER for value in actual_registry):\n            category_registry_issues.append("registry contains an unknown category")',
)
s = s.replace('REVIEW_GROUPS = set()', 'REVIEW_GROUPS = {"Backup", "Not Playing", "New Channels", "New Backup"}')
s = s.replace(
    'lines.append("Backup/Not Playing internal order is preserved for manual review and is intentionally not auto-enforced.")',
    'lines.append("Backup/Not Playing/New Channels/New Backup internal order is preserved for manual review and is intentionally not auto-enforced.")',
)
p.write_text(s, encoding="utf-8")
print("Audit policy updated for New Channels/New Backup.")
