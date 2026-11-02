#!/usr/bin/env python3
"""Keep the legacy playlist audit aligned with the protected review queues."""
from pathlib import Path
import re

p = Path("scripts/audit_playlist.py")
s = p.read_text(encoding="utf-8")
s = re.sub(
    r'(?m)^REGISTRY_ORDER = \[x for x in CATEGORY_ORDER if x not in \{"New Channels", "New Backup"\}\].*$',
    "REGISTRY_ORDER = CATEGORY_ORDER",
    s,
)
s = re.sub(
    r'(?m)^        if any\(value in actual_registry for value in \("New Channels", "New Backup"\)\):\n            category_registry_issues\.append\("review queue categories must not be registered"\)\n',
    "",
    s,
)
p.write_text(s, encoding="utf-8")
print("Audit policy updated: New Channels/New Backup are registered review queues.")
