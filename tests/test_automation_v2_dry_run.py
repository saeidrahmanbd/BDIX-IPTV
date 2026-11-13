import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from scripts.run_automation_v2_dry_run import git_blob_sha

class BaselineDryRunHelpersTests(unittest.TestCase):
    def test_git_blob_sha_uses_git_blob_header(self):
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/"sample.txt"
            path.write_bytes(b"abc")
            self.assertEqual(git_blob_sha(path),"f2ba8f84ab5c1bce84a7b441cb1959cfc7093b7f")

if __name__=="__main__":
    unittest.main()
