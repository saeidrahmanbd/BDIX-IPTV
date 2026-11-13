import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.engines.epg.validator import validate_xmltv

GOOD = """<?xml version="1.0"?><tv><channel id="c1"><display-name>Channel 1</display-name></channel><programme channel="c1" start="20261113090000 +0600" stop="20261113100000 +0600"><title>News</title></programme></tv>"""

class EpgValidatorTests(unittest.TestCase):
    def test_valid_xmltv(self):
        result=validate_xmltv(GOOD)
        self.assertTrue(result.valid)
        self.assertEqual((result.channel_count,result.programme_count),(1,1))

    def test_malformed_xml_rejected(self):
        self.assertFalse(validate_xmltv("<tv>").valid)

    def test_orphan_programme_rejected(self):
        result=validate_xmltv('<tv><channel id="c1"/><programme channel="unknown" start="20261113090000" stop="20261113100000"/></tv>')
        self.assertFalse(result.valid)
        self.assertTrue(any("unknown channel" in e for e in result.errors))

    def test_duplicate_channel_ids_rejected(self):
        result=validate_xmltv('<tv><channel id="c1"/><channel id="c1"/><programme channel="c1" start="20261113090000" stop="20261113100000"/></tv>')
        self.assertFalse(result.valid)
        self.assertTrue(any("duplicate channel" in e for e in result.errors))

    def test_invalid_time_range_rejected(self):
        result=validate_xmltv('<tv><channel id="c1"/><programme channel="c1" start="20261113100000" stop="20261113090000"/></tv>')
        self.assertFalse(result.valid)

    def test_invalid_timezone_offset_rejected(self):
        xml='<tv><channel id="c1"/><programme channel="c1" start="20261113090000 +2560" stop="20261113100000 +0600"/></tv>'
        result=validate_xmltv(xml)
        self.assertFalse(result.valid)
        self.assertTrue(any("timezone offset" in e for e in result.errors))

    def test_different_offsets_compared_as_absolute_time(self):
        xml='<tv><channel id="c1"/><programme channel="c1" start="20261113090000 +0600" stop="20261113040000 +0100"/></tv>'
        result=validate_xmltv(xml)
        self.assertFalse(result.valid)

    def test_empty_guide_rejected(self):
        self.assertFalse(validate_xmltv("<tv/>").valid)

if __name__=="__main__":
    unittest.main()
