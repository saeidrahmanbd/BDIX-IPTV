#!/usr/bin/env python3
"""Run Bangladesh/India discovery using the canonical policy in the discovery module.

Bangladesh channels of all genres are eligible. Indian News, Religious (including
Islamic), Educational and Kids channels are excluded; Indian Sports is allowed.
"""
import discover_bd_in_new_queues as d

if __name__ == "__main__":
    d.main()
