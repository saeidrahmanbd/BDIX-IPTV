#!/usr/bin/env python3
"""Run BD/India discovery with the repository's explicit religious-content policy.

Policy: Islamic religious channels are allowed; non-Islamic religious channels are prohibited.
India News/Sports/Kids remain prohibited. Bangladesh News remains allowed.
"""
import re
import discover_bd_in_new_queues as d

RELIGIOUS_RE = re.compile(r'\b(?:religious|religion|devotional|bhakti|bhakthi|spiritual|worship|gospel|christian|christ|hindu|hinduism|sanatan|sikh|gurbani|gurubani|church|temple|sermons?|prayer|bible|jesus|krishna|shiva|ganesh|guru|gurudwara|jain|jainism|buddhist|buddhism|buddha|zoroastrian|parsi|jewish|judaism|torah|synagogue|catholic|orthodox|protestant|adventist|anglican|mormon|bahai|baháí)\b', re.I)
ISLAMIC_RE = re.compile(r'\b(?:islam|islamic|muslim|quran|quranic|koran|allah|muhammad|mohammed|prophet|hadith|sunnah|salafi|salaf|sufi|sufism|dawah|daawah|ramadan|eid|mecca|makkah|madinah|medina|masjid|mosque|ummah|deen|din|fiqh|tafsir|azan|adhan|jumuah|jummah|hajj|umrah|kaaba|kaabah|sharia|shariah|peace\s*tv)\b', re.I)


def policy_prohibited(a, name, country=None):
    text = ' '.join((name, a.get('tvg-name', ''), a.get('group-title', ''), a.get('tvg-id', ''), a.get('channel-id', '')))
    if RELIGIOUS_RE.search(text) and not ISLAMIC_RE.search(text):
        return 'non-Islamic religious channel is prohibited'
    reason = d.prohibited_channel(a, name, country)
    if reason and RELIGIOUS_RE.search(text) and ISLAMIC_RE.search(text):
        if reason in {
            'Indian religious channel is prohibited',
            'Indian islamic channel is prohibited',
            'known Indian News, Sports, Kids or Religious brand/category is prohibited',
        }:
            return None
    return reason


d.prohibited_channel = policy_prohibited

d.main()
