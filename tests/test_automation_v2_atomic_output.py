import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from automation.core.atomic_output import atomic_write_v2_output

class AtomicOutputTests(unittest.TestCase):
    def test_candidate_output_written_atomically(self):
        with tempfile.TemporaryDirectory() as temp:
            path=atomic_write_v2_output(temp,"reports/automation-v2/candidates/run-1/IPTV-Playlist.m3u","#EXTM3U\n")
            self.assertEqual(path.read_text(encoding="utf-8"),"#EXTM3U\n")
            self.assertTrue((Path(temp)/"reports/automation-v2/state/.publisher.lock").exists())

    def test_existing_candidate_replaced_atomically(self):
        with tempfile.TemporaryDirectory() as temp:
            relative="reports/automation-v2/state/run-ledger.json"
            atomic_write_v2_output(temp,relative,'{"runs":[]}\n')
            atomic_write_v2_output(temp,relative,'{"runs":[1]}\n')
            self.assertEqual((Path(temp)/relative).read_text(encoding="utf-8"),'{"runs":[1]}\n')

    def test_replace_failure_preserves_last_known_good_and_cleans_temp(self):
        with tempfile.TemporaryDirectory() as temp:
            relative="reports/automation-v2/state/run-ledger.json"
            target=Path(temp)/relative
            atomic_write_v2_output(temp,relative,'{"version":1}\n')
            with patch("automation.core.atomic_output.os.replace",side_effect=OSError("simulated replace failure")):
                with self.assertRaisesRegex(OSError,"simulated"):
                    atomic_write_v2_output(temp,relative,'{"version":2}\n')
            self.assertEqual(target.read_text(encoding="utf-8"),'{"version":1}\n')
            self.assertEqual(list(target.parent.glob(".v2-tmp-*")),[])

    def test_lock_file_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as temp, tempfile.TemporaryDirectory() as outside:
            root=Path(temp)
            state=root/"reports"/"automation-v2"/"state"
            state.mkdir(parents=True)
            lock=state/".publisher.lock"
            lock.symlink_to(Path(outside)/"outside.lock")
            with self.assertRaisesRegex(ValueError,"lock file"):
                atomic_write_v2_output(root,"reports/automation-v2/state/run-ledger.json","{}")

    def test_production_playlist_path_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError,"outside"):
                atomic_write_v2_output(temp,"IPTV-Playlist.m3u","danger")

    def test_parent_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError,"outside|escapes"):
                atomic_write_v2_output(temp,"reports/automation-v2/candidates/../../IPTV-Playlist.m3u","danger")

    def test_symlinked_state_directory_rejected(self):
        with tempfile.TemporaryDirectory() as temp, tempfile.TemporaryDirectory() as outside:
            root=Path(temp)
            state=root/"reports"/"automation-v2"/"state"
            state.parent.mkdir(parents=True)
            state.symlink_to(outside,target_is_directory=True)
            with self.assertRaisesRegex(ValueError,"lock directory"):
                atomic_write_v2_output(root,"reports/automation-v2/candidates/run/file.txt","x")

    def test_state_file_symlink_cannot_overwrite_production_playlist(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            production=root/"IPTV-Playlist.m3u"
            production.write_text("production")
            state=root/"reports"/"automation-v2"/"state"
            state.mkdir(parents=True)
            (state/"run-ledger.json").symlink_to(production)
            with self.assertRaisesRegex(ValueError,"approved V2 output directory"):
                atomic_write_v2_output(root,"reports/automation-v2/state/run-ledger.json","tampered")
            self.assertEqual(production.read_text(),"production")

    def test_reports_root_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as temp, tempfile.TemporaryDirectory() as outside:
            root=Path(temp)
            (root/"reports").symlink_to(outside,target_is_directory=True)
            with self.assertRaisesRegex(ValueError,"symlink|escapes"):
                atomic_write_v2_output(root,"reports/automation-v2/state/run-ledger.json","x")

    def test_symlink_escape_rejected(self):
        with tempfile.TemporaryDirectory() as temp, tempfile.TemporaryDirectory() as outside:
            root=Path(temp)
            (root/"reports"/"automation-v2").mkdir(parents=True)
            (root/"reports"/"automation-v2"/"candidates").symlink_to(outside,target_is_directory=True)
            with self.assertRaisesRegex(ValueError,"escapes|symlink"):
                atomic_write_v2_output(root,"reports/automation-v2/candidates/file.txt","danger")

if __name__=="__main__":
    unittest.main()
