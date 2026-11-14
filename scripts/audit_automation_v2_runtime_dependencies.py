#!/usr/bin/env python3
"""Inventory workflow Python entrypoints and nested subprocess targets.

Static inventory only: dynamic commands are reported as unresolved and must be
reviewed before migration cutover. This script never executes repository code.
"""
from __future__ import annotations
import argparse, ast, json, re
from pathlib import Path

WORKFLOW_PYTHON = re.compile(r"(?:python(?:3(?:\.\d+)?)?)\s+([A-Za-z0-9_./-]+\.py)")
SUBPROCESS_NAMES = {"run", "call", "check_call", "check_output", "Popen", "system", "popen"}

def _literal_command(node):
    if isinstance(node, (ast.List, ast.Tuple)):
        values=[]
        for item in node.elts:
            if isinstance(item, ast.Constant) and isinstance(item.value, str):
                values.append(item.value)
            else:
                return None
        return values
    return None

def scan_python(path: Path, relative: str) -> list[dict]:
    try:
        tree=ast.parse(path.read_text(encoding="utf-8"), filename=relative)
    except (OSError, UnicodeDecodeError, SyntaxError) as exc:
        return [{"source":relative,"kind":"parse_error","target":None,"detail":type(exc).__name__}]
    found=[]
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func=node.func
        name=func.attr if isinstance(func, ast.Attribute) else (func.id if isinstance(func, ast.Name) else "")
        if name in {"eval", "exec"}:
            found.append({"source":relative,"line":node.lineno,"kind":"dynamic_code_execution",
                          "target":None,"detail":name + "() prevents static call-graph resolution"})
            continue
        if name not in SUBPROCESS_NAMES:
            continue
        command=_literal_command(node.args[0]) if node.args else None
        shell_boundary = name in {"system", "popen"} or any(
            keyword.arg == "shell" and isinstance(keyword.value, ast.Constant)
            and keyword.value.value is True for keyword in node.keywords
        )
        if command and not shell_boundary:
            target=next((part for part in command[1:] if part.endswith(".py")), None)
            found.append({"source":relative,"line":node.lineno,"kind":"subprocess_literal",
                          "target":target,"command":command})
        else:
            found.append({"source":relative,"line":node.lineno,"kind":"subprocess_dynamic",
                          "target":None,"detail":"shell or dynamically constructed command"})
    return found

def build_inventory(root: Path) -> dict:
    root=root.resolve(strict=True)
    workflows=root/".github"/"workflows"
    scripts=root/"scripts"
    workflow_entries=[]
    for path in sorted(workflows.glob("*.y*ml")):
        try: content=path.read_text(encoding="utf-8")
        except OSError: continue
        for match in WORKFLOW_PYTHON.finditer(content):
            target=match.group(1)
            workflow_entries.append({"workflow":path.relative_to(root).as_posix(),
                                     "target":target,"exists":(root/target).is_file()})
    nested=[]
    for path in sorted(root.rglob("*.py")):
        nested.extend(scan_python(path,path.relative_to(root).as_posix()))
    known={item["target"] for item in workflow_entries}
    unresolved=[item for item in nested if item["kind"] in {"subprocess_dynamic","parse_error","dynamic_code_execution"}]
    missing=[item for item in nested if item["target"] and not (root/item["target"]).is_file()]
    return {
        "schema_version":1,
        "report_type":"automation-v2-static-runtime-dependency-inventory",
        "workflow_entrypoints":workflow_entries,
        "nested_subprocess_calls":nested,
        "summary":{
            "workflow_python_entrypoints":len(workflow_entries),
            "unique_workflow_targets":len(known),
            "nested_subprocess_calls":len(nested),
            "dynamic_or_unparsed_calls":len(unresolved),
            "missing_literal_targets":len(missing),
        },
        "unresolved":unresolved,
        "missing_targets":missing,
        "limitations":[
            "Static analysis records dynamic execution and shell boundaries but does not resolve imports, runtime-generated paths, external actions, package scripts or network-loaded code.",
            "Every unresolved dynamic call and workflow shell block must be traced before legacy workflow retirement.",
        ],
        "safety":{"repository_code_executed":False,"production_files_modified":False,"publication_performed":False},
    }

def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",type=Path,default=Path("."))
    parser.add_argument("--output",type=Path,default=Path("reports/automation-v2/runtime-dependency-inventory.json"))
    args=parser.parse_args()
    root=args.root.resolve(strict=True)
    output=args.output if args.output.is_absolute() else root/args.output
    output=output.absolute()
    if not output.is_relative_to(root): parser.error("output must remain inside repository root")
    current=root
    for part in output.relative_to(root).parts:
        current=current/part
        if current.is_symlink(): parser.error("output path cannot contain symlinks")
    result=build_inventory(root)
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(result["summary"],indent=2))
    return 0

if __name__=="__main__": raise SystemExit(main())
