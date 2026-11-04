#!/usr/bin/env python3
"""Run Bangladesh/India discovery using the single canonical playlist policy.

The policy is implemented in discover_bd_in_new_queues.py:
Bangladesh follows its existing rules; Indian News, Religious (including Islamic),
Educational and Kids channels are rejected. Indian Sports remain allowed.
"""
import discover_bd_in_new_queues as discovery


if __name__ == "__main__":
    raise SystemExit(discovery.main())
