#!/usr/bin/env python3
"""Run Bangladesh/India discovery using the canonical policy in the discovery module.

Bangladesh channels of all genres are eligible. Indian News, Kids, Education, Knowledge,
Business/Finance and non-Islamic Religious channels are excluded; Indian Sports channels are allowed.
Islamic religious channels remain eligible. International has a separate policy.
"""
import discover_bd_in_new_queues as d

if __name__ == "__main__":
    d.main()
