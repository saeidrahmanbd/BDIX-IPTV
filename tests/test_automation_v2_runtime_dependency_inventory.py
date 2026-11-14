import json
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
            build_block=next(x for x in boundaries if "npm ci" in x["detail"])
            self.assertIn("node build.js",build_block["detail"])

    def test_ignores_local_function_named_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/"helper.py"
            source.write_text("def run(value):\n    return value\nrun(1)\n")
            self.assertEqual(scan_python(source,"helper.py"),[])

    def test_detects_subprocess_module_alias_and_imported_function(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/"helper.py"
            source.write_text(
                "import subprocess as sp\nfrom subprocess import run as execute\n"
                "sp.run(['python','tool.py'])\nexecute(build_command())\n"
            )
            found=scan_python(source,"helper.py")
            self.assertEqual([x["kind"] for x in found],["subprocess_literal","subprocess_dynamic"])

    def test_detects_os_shell_process_calls(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); source=root/"helper.py"
            source.write_text("import os as operating_system\noperating_system.system('echo test')\n")
            found=scan_python(source,"helper.py")
            self.assertEqual(len(found),1)
            self.assertEqual(found[0]["kind"],"subprocess_dynamic")

    def test_external_action_manifest_reviews_exact_pinned_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); workflows=root/".github"/"workflows"; workflows.mkdir(parents=True)
            policy=root/"automation"/"policy"; policy.mkdir(parents=True)
            ref="actions/checkout@"+"a"*40
            (workflows/"actions.yml").write_text("jobs:\n  build:\n    steps:\n      - uses: "+ref+"\n")
            (policy/"external-actions-lock.json").write_text(json.dumps({
                "schema_version":1,
                "actions":[{"reference":ref,"using":"node24","main":"dist/index.js",
                            "review_status":"action_metadata_reviewed"}]
            }))
            report=build_inventory(root)
            self.assertEqual(report["summary"]["workflow_action_references"],1)
            self.assertEqual(report["summary"]["unique_external_action_implementations"],1)
            self.assertEqual(report["summary"]["reviewed_external_action_metadata"],1)
            self.assertTrue(report["workflow_actions"][0]["metadata_reviewed"])
            self.assertTrue(report["unresolved"][0]["metadata_reviewed"])

    def test_inventory_records_external_and_local_workflow_actions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); workflows=root/".github"/"workflows"
            workflows.mkdir(parents=True)
            action=root/".github"/"actions"/"local"
            action.mkdir(parents=True)
            (action/"action.yml").write_text("name: local\n")
            (workflows/"actions.yml").write_text(
                "jobs:\n  build:\n    steps:\n"
                "      - uses: actions/checkout@"+("a"*40)+"\n"
                "      - uses: ./.github/actions/local\n"
            )
            report=build_inventory(root)
            self.assertEqual(report["summary"]["workflow_action_references"],2)
            self.assertEqual(report["summary"]["external_workflow_actions"],1)
            self.assertEqual(report["summary"]["unpinned_external_workflow_actions"],0)
            self.assertTrue(any(x["kind"]=="external_workflow_action" and x["immutable_ref"]
                                for x in report["workflow_actions"]))
            self.assertTrue(any(x["kind"]=="local_workflow_action" and x["exists"]
                                for x in report["workflow_actions"]))

    def test_separates_test_only_dynamic_calls_from_runtime_blockers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/"scripts").mkdir(); (root/"tests").mkdir()
            (root/"scripts"/"runtime.py").write_text(
                "import subprocess\nsubprocess.run(make_command())\n"
            )
            (root/"tests"/"fixture.py").write_text(
                "import subprocess\nsubprocess.run(make_test_command())\n"
            )
            report=build_inventory(root)
            self.assertEqual(len(report["unresolved"]),1)
            self.assertEqual(report["unresolved"][0]["source"],"scripts/runtime.py")
            self.assertEqual(len(report["test_only_unresolved"]),1)
            self.assertEqual(report["test_only_unresolved"][0]["source"],"tests/fixture.py")

    def test_skips_immutable_production_baseline_checkout_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); runtime=root/"scripts"; runtime.mkdir()
            baseline=root/"automation-v2-production-baseline"/"scripts"
            baseline.mkdir(parents=True)
            (runtime/"runtime.py").write_text("import subprocess\nsubprocess.run(make_command())\n")
            (baseline/"copied.py").write_text("import subprocess\nsubprocess.run(make_command())\n")
            report=build_inventory(root)
            self.assertEqual(
                [x["source"] for x in report["nested_subprocess_calls"] if x["kind"]=="subprocess_dynamic"],
                ["scripts/runtime.py"],
            )

    def test_preserves_complete_multiline_workflow_shell_body(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); workflows=root/".github"/"workflows"
            workflows.mkdir(parents=True)
            body_line="echo " + ("x" * 5000)
            (workflows/"long.yml").write_text(
                "jobs:\n  build:\n    steps:\n"
                "      - name: long command\n        run: |\n"
                "          echo first\n          " + body_line + "\n"
                "      - name: next\n        run: echo done\n"
            )
            report=build_inventory(root)
            boundary=next(x for x in report["nested_subprocess_calls"]
                          if x["kind"]=="workflow_shell_boundary")
            self.assertIn("\n          echo first\n", boundary["detail"])
            self.assertIn(body_line, boundary["detail"])
            self.assertGreater(len(boundary["detail"]), 5000)

if __name__=="__main__": unittest.main()
