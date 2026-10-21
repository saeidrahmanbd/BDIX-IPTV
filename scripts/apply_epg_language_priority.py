#!/usr/bin/env python3
"""Apply the EPG multilingual title-selection policy to the generator.

Preference when several title languages describe the same channel/programme:
English > Bengali > other valid languages. Other languages remain eligible so
coverage is never lost merely because English/Bengali text is unavailable.
The patch is idempotent and is run by the report-sync workflow before EPG
regeneration so the repository stays self-healing.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "scripts" / "generate_epg.py"

OLD_POLICY = '''# The published guide accepts English (Latin script) or Bengali (Bengali script).\n# Reject unsupported language tags/scripts such as Hindi, Arabic, Cyrillic, and Han.\nimport unicodedata\n\nTEXT_FIELDS = {"title", "sub-title", "desc"}\nXML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"\n\n\n# Guide text policy: English (Latin script) or Bengali (Bengali script) only.\n# Any other language tag or script is rejected. Keep identical in epg_coverage.py,\n# generate_epg.py and epg_publish_gate.py (tests/test_language_policy.py checks this).\nALLOWED_LANGS = {"en", "eng", "bn", "ben"}\nALLOWED_LANG_PREFIXES = ("en-", "en_", "bn-", "bn_")\nALLOWED_SCRIPTS = ("LATIN", "BENGALI")\n\n\ndef _script_allowed(char):\n    name = unicodedata.name(char, "")\n    return any(s in name for s in ALLOWED_SCRIPTS)\n\n\ndef is_english_text_element(elem):\n    text = (elem.text or "").strip()\n    if not text:\n        return True\n    lang = (elem.attrib.get(XML_LANG) or elem.attrib.get("lang") or "").strip().lower()\n    if lang and not (lang in ALLOWED_LANGS or lang.startswith(ALLOWED_LANG_PREFIXES)):\n        return False\n    for char in text:\n        if unicodedata.category(char).startswith("L"):\n            if not _script_allowed(char):\n                return False\n    return True\n'''

NEW_POLICY = '''import unicodedata\n\nTEXT_FIELDS = {"title", "sub-title", "desc"}\nXML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"\n\n# All legitimate programme languages remain eligible. When several languages\n# are available for the same channel/time, title selection prefers English,\n# then Bengali, then another valid language. This prevents coverage loss while\n# keeping the published guide easy to read for the primary audience.\nLANG_PRIORITY = {"en": 3, "eng": 3, "bn": 2, "ben": 2}\nLANG_PREFIXES = (("en-", 3), ("en_", 3), ("bn-", 2), ("bn_", 2))\n\ndef _script_rank(text):\n    scripts = set()\n    for char in text:\n        if unicodedata.category(char).startswith("L"):\n            name = unicodedata.name(char, "")\n            if "LATIN" in name:\n                scripts.add("latin")\n            elif "BENGALI" in name:\n                scripts.add("bengali")\n            elif name:\n                scripts.add("other")\n    if scripts == {"latin"} or scripts == {"latin", "bengali"}:\n        return 3 if scripts == {"latin"} else 3\n    if scripts == {"bengali"}:\n        return 2\n    return 1 if scripts else 0\n\ndef language_priority(elem):\n    text = (elem.text or "").strip()\n    lang = (elem.attrib.get(XML_LANG) or elem.attrib.get("lang") or "").strip().lower()\n    if lang in LANG_PRIORITY:\n        return LANG_PRIORITY[lang]\n    for prefix, rank in LANG_PREFIXES:\n        if lang.startswith(prefix):\n            return rank\n    if lang:\n        return 1\n    return _script_rank(text)\n\ndef is_english_text_element(elem):\n    # Backward-compatible function name used by the coverage/test code. It now\n    # means "valid XMLTV text", not "English-only text". Empty text is handled\n    # by callers that require a visible programme title.\n    text = (elem.text or "").strip()\n    if not text:\n        return True\n    lang = (elem.attrib.get(XML_LANG) or elem.attrib.get("lang") or "").strip().lower()\n    if lang and any(lang.startswith(prefix) for prefix, _ in LANG_PREFIXES):\n        return True\n    if lang in LANG_PRIORITY:\n        return True\n    # Accept normal Unicode letters/numbers/punctuation from any script.\n    # XMLTV feeds occasionally use symbols in otherwise valid titles.\n    return any(unicodedata.category(char).startswith("L") for char in text)\n\ndef preferred_title_element(elem):\n    titles = [x for x in elem.findall("title") if (x.text or "").strip()]\n    if not titles:\n        return None\n    return max(titles, key=lambda x: (language_priority(x), len((x.text or "").strip()), -(titles.index(x))))\n'''

CLONE_OLD = '''def clone_children(elem):\n    return [ET.fromstring(ET.tostring(child, encoding="utf-8")) for child in list(elem)]\n'''

CLONE_NEW = '''def clone_children(elem):\n    """Clone programme fields while retaining only the best available title.\n\n    If a source contains English, Bengali and another language title for the\n    same programme, publish English; if English is absent publish Bengali;\n    otherwise publish the best remaining valid title.\n    """\n    preferred = preferred_title_element(elem)\n    children = []\n    for child in list(elem):\n        if child.tag == "title":\n            if child is preferred:\n                children.append(ET.fromstring(ET.tostring(child, encoding="utf-8")))\n            continue\n        children.append(ET.fromstring(ET.tostring(child, encoding="utf-8")))\n    return children\n'''

OLD_TITLE = '                title_elem = elem.find("title")\n                title = (title_elem.text or "").strip() if title_elem is not None else ""\n                children = clone_children(elem)\n'
NEW_TITLE = '                title_elem = preferred_title_element(elem)\n                title = (title_elem.text or "").strip() if title_elem is not None else ""\n                children = clone_children(elem)\n'

OLD_WEIGHT = '''    # Prefer real programme names over placeholders such as "Movie".\n    if title_score(record["title"]) > 0:\n        weight += 8.0\n\n    # Earlier approved sources win close quality ties, but source priority\n'''
NEW_WEIGHT = '''    # Prefer real programme names over placeholders such as "Movie".\n    if title_score(record["title"]) > 0:\n        weight += 8.0\n\n    # When providers overlap, prefer English titles, then Bengali, then other\n    # valid languages. This is a tie-breaker only; it never removes a\n    # non-overlapping programme from another provider.\n    weight += {3: 30.0, 2: 20.0, 1: 10.0}.get(record.get("language_rank", 1), 10.0)\n\n    # Earlier approved sources win close quality ties, but source priority\n'''

OLD_QUALITY = '            old_quality = (title_score(old["title"]), -old["source_index"])\n            new_quality = (title_score(r["title"]), -r["source_index"])\n'
NEW_QUALITY = '            old_quality = (old.get("language_rank", 1), title_score(old["title"]), -old["source_index"])\n            new_quality = (r.get("language_rank", 1), title_score(r["title"]), -r["source_index"])\n'

text = TARGET.read_text(encoding="utf-8")
changed = False
for old, new in ((OLD_POLICY, NEW_POLICY), (CLONE_OLD, CLONE_NEW), (OLD_TITLE, NEW_TITLE), (OLD_WEIGHT, NEW_WEIGHT), (OLD_QUALITY, NEW_QUALITY)):
    if old in text:
        text = text.replace(old, new, 1)
        changed = True

# Add language_rank to every generated record that already carries title_elem.
needle = '                        "title": title,\n'
replacement = '                        "title": title,\n                        "language_rank": language_priority(title_elem),\n'
if text.count(needle) >= 2 and '"language_rank": language_priority(title_elem)' not in text:
    text = text.replace(needle, replacement, 2)
    changed = True

if changed:
    TARGET.write_text(text, encoding="utf-8")
    print(f"Updated {TARGET} with English > Bengali > other language priority.")
else:
    print(f"{TARGET} already has the language-priority patch; no changes needed.")
