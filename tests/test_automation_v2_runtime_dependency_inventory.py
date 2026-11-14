from __future__ import annotations
import tempfile, unittest
from pathlib import Path
from scripts.audit_automation_v2_runtime_dependencies import build_inventory, scan_python

class RuntimeDependencyInventoryTests(unittest.TestCase):
    def test_detects_literal_and_dynamic_subprocess_targets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); scripts=root/"scripts"; scripts.mkdir()
            (scripts/"child.py").write_text("print('child')\n")
            source=scripts/"parent.py"
            source.write_text(
                "import subprocess\n"
                "subprocess.run(['python', 'scripts/child.py'], check=True)\n"
                "subprocess.run(build_command(), check=True)\n"
            )
            found=scan_python(source,"scripts/parent.py")
            self.assertEqual(found[0]["target"],"scripts/child.py")
            self.assertEqual(found[1]["kind"],"subprocess_dynamic")
    def test_inventory_reports_workflow_entrypoints_and_missing_targets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/".github/workflows").mkdir(parents=True)
            (root/"scripts").mkdir()
            (root/".github/workflows"/"sample.yml").write_text("run: python scripts/missing.py\n")
            report=build_inventory(root)
            self.assertEqual(report["summary"]["workflow_python_entrypoints"],1)
            self.assertFalse(report["workflow_entrypoints"][0]["exists"])
            self.assertFalse(report["safety"]["repository_code_executed"])
    def test_scanner_does_not_execute_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/"danger.py"
            marker=root/"executed"
            source.write_text("open(%r, 'w').write('bad')\n" % str(marker))
            scan_python(source,"danger.py")
            self.assertFalse(marker.exists())

    def test_detects_shell_and_dynamic_execution_boundaries(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/"opaque.py"
            source.write_text(
                "import subprocess, os\n"
                "subprocess.run('python child.py', shell=True)\n"
                "os.system('python another.py')\n"
                "eval('print(1)')\n"
            )
            found=scan_python(source,"opaque.py")
            kinds={item["kind"] for item in found}
            self.assertIn("subprocess_dynamic",kinds)
            self.assertIn("dynamic_code_execution",kinds)

    def test_inventory_scans_python_outside_scripts_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/"automation").mkdir()
            (root/"automation"/"engine.py").write_text(
                "import subprocess\nsubprocess.run(make_command())\n"
            )
            report=build_inventory(root)
            self.assertTrue(any(item["source"]=="automation/engine.py"
                for item in report["nested_subprocess_calls"]))

    def test_inventory_records_workflow_shell_execution_boundaries(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); workflows=root/".github"/"workflows"
            workflows.mkdir(parents=True)
            (workflows/"sample.yml").write_text(
                "jobs:\n  build:\n    steps:\n"
                "      - name: build\n        run: |\n"
                "          npm ci\n          node build.js\n"
                "      - name: next\n        run: echo done\n"
            )
            report=build_inventory(root)
            boundaries=[x for x in report["nested_subprocess_calls"]
                        if x["kind"]=="workflow_shell_boundary"]
            self.assertEqual(len(boundaries),2)
            self.assertGreaterEqual(report["summary"]["dynamic_or_unparsed_calls"],2)

if __name__=="__main__": unittest.main()
