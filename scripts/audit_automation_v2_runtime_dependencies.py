#!/usr/bin/env python3
"""Inventory workflow Python entrypoints and nested subprocess targets.

Static inventory only: dynamic commands are reported as unresolved and must be
reviewed before migration cutover. This script never executes repository code.
"""
from __future__ import annotations
import argparse, ast, json, re
from pathlib import Path

WORKFLOW_PYTHON = re.compile(r"(?:python(?:3(?:\.\d+)?)?)\s+([A-Za-z0-9_./-]+\.py)")
WORKFLOW_ACTION = re.compile(r"^\s*(?:-\s*)?uses:\s*([^\s#]+)")
SUBPROCESS_NAMES = {"run", "call", "check_call", "check_output", "Popen"}
OS_PROCESS_NAMES = {"system", "popen"}
ASYNC_PROCESS_NAMES = {"create_subprocess_exec", "create_subprocess_shell"}

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
    subprocess_modules = {"subprocess"}
    os_modules = {"os"}
    asyncio_modules = {"asyncio"}
    imported_process_functions = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "subprocess":
                    subprocess_modules.add(alias.asname or alias.name)
                elif alias.name == "os":
                    os_modules.add(alias.asname or alias.name)
                elif alias.name == "asyncio":
                    asyncio_modules.add(alias.asname or alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module == "subprocess":
                imported_process_functions.update(
                    alias.asname or alias.name for alias in node.names
                    if alias.name in SUBPROCESS_NAMES
                )
            elif node.module == "os":
                imported_process_functions.update(
                    alias.asname or alias.name for alias in node.names
                    if alias.name in OS_PROCESS_NAMES
                )
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
        is_process_call = (
            isinstance(func, ast.Attribute)
            and isinstance(func.value, ast.Name)
            and (
                (func.value.id in subprocess_modules and name in SUBPROCESS_NAMES)
                or (func.value.id in os_modules and name in OS_PROCESS_NAMES)
                or (func.value.id in asyncio_modules and name in ASYNC_PROCESS_NAMES)
            )
        ) or (isinstance(func, ast.Name) and name in imported_process_functions)
        if not is_process_call:
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
    workflow_actions=[]
    for path in sorted(workflows.glob("*.y*ml")):
        try: content=path.read_text(encoding="utf-8")
        except OSError: continue
        for match in WORKFLOW_PYTHON.finditer(content):
            target=match.group(1)
            workflow_entries.append({"workflow":path.relative_to(root).as_posix(),
                                     "target":target,"exists":(root/target).is_file()})
        for line_number,line in enumerate(content.splitlines(),1):
            match=WORKFLOW_ACTION.match(line)
            if not match:
                continue
            reference=match.group(1)
            local=reference.startswith("./")
            local_path=root/reference if local else None
            if local and local_path.is_dir():
                action_file=next((local_path/name for name in ("action.yml","action.yaml") if (local_path/name).is_file()),None)
            else:
                action_file=local_path
            workflow_actions.append({
                "workflow":path.relative_to(root).as_posix(),"line":line_number,
                "kind":"local_workflow_action" if local else "external_workflow_action",
                "reference":reference,"exists":bool(action_file and action_file.is_file()) if local else None,
                "immutable_ref":bool(re.search(r"@[0-9a-fA-F]{40}$",reference)) if not local else None,
            })
    nested=[]
    for path in sorted(root.rglob("*.py")):
        relative = path.relative_to(root).as_posix()
        if any(part in {".git", ".venv", "venv", "__pycache__", "automation-v2-production-baseline"} for part in path.parts):
            continue
        scope = "test_only" if relative.startswith("tests/") else "repository_runtime"
        for item in scan_python(path, relative):
            item["execution_scope"] = scope
            nested.append(item)
    # Record workflow run blocks as opaque execution boundaries. A static
    # inventory must not imply that shell, npm, node, or action behavior was
    # resolved merely because a Python entrypoint was found.
    shell_boundaries=[]
    for workflow in sorted(workflows.glob("*.y*ml")):
        try:
            lines=workflow.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        run_indent=None
        active_boundary=None
        for line_number,line in enumerate(lines,1):
            stripped=line.strip()
            indent=len(line)-len(line.lstrip(" "))
            if run_indent is not None and stripped and indent <= run_indent:
                active_boundary=None
                run_indent=None
            if stripped.startswith("run:") or stripped.startswith("- run:"):
                run_indent=indent
                active_boundary={"source":workflow.relative_to(root).as_posix(),
                    "line":line_number,"kind":"workflow_shell_boundary","target":None,
                    "execution_scope":"workflow_runtime","detail":line.rstrip("\r\n")}
                shell_boundaries.append(active_boundary)
            elif active_boundary is not None:
                # Preserve the actual shell body so reviewers can resolve
                # command chains, npm/node invocations and inline heredocs.
                body=active_boundary["detail"]
                active_boundary["detail"]=(body + "\n" + line.rstrip("\r\n"))
    nested.extend(shell_boundaries)
    action_lock_path=root/"automation"/"policy"/"external-actions-lock.json"
    try:
        action_lock=json.loads(action_lock_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        action_lock={}
    reviewed_actions={
        item.get("reference"):item for item in action_lock.get("actions",[])
        if isinstance(item,dict) and isinstance(item.get("reference"),str)
    }
    for action in workflow_actions:
        if action["kind"]=="external_workflow_action":
            review=reviewed_actions.get(action["reference"])
            action["metadata_reviewed"]=bool(review)
            if review:
                action["metadata"]=review
    external_boundaries={}
    for action in workflow_actions:
        if action["kind"]!="external_workflow_action":
            continue
        record=external_boundaries.setdefault(action["reference"],{
            "kind":"external_action_implementation_boundary",
            "reference":action["reference"],
            "immutable_ref":action["immutable_ref"],
            "metadata_reviewed":action.get("metadata_reviewed",False),
            "workflows":[],
        })
        record["workflows"].append({"workflow":action["workflow"],"line":action["line"]})
    known={item["target"] for item in workflow_entries}
    unresolved_kinds={"subprocess_dynamic","parse_error","dynamic_code_execution","workflow_shell_boundary"}
    runtime_unresolved=[item for item in nested if item.get("execution_scope")!="test_only" and item["kind"] in unresolved_kinds]
    test_only_unresolved=[item for item in nested if item.get("execution_scope")=="test_only" and item["kind"] in unresolved_kinds]
    unresolved=runtime_unresolved + list(external_boundaries.values()) + [
        item for item in workflow_actions
        if item["kind"]=="local_workflow_action" and not item["exists"]
    ]
    missing=[item for item in nested if item.get("execution_scope")!="test_only"
             and item["target"] and not (root/item["target"]).is_file()]
    missing.extend(item for item in workflow_actions if item["kind"]=="local_workflow_action" and not item["exists"])
    return {
        "schema_version":1,
        "report_type":"automation-v2-static-runtime-dependency-inventory",
        "workflow_entrypoints":workflow_entries,
        "workflow_actions":workflow_actions,
        "nested_subprocess_calls":nested,
        "summary":{
            "workflow_python_entrypoints":len(workflow_entries),
            "unique_workflow_targets":len(known),
            "workflow_action_references":len(workflow_actions),
            "external_workflow_actions":sum(1 for item in workflow_actions if item["kind"]=="external_workflow_action"),
            "unique_external_action_implementations":len(external_boundaries),
            "reviewed_external_action_metadata":sum(1 for item in external_boundaries.values() if item["metadata_reviewed"]),
            "unpinned_external_workflow_actions":sum(1 for item in workflow_actions if item["kind"]=="external_workflow_action" and not item["immutable_ref"]),
            "nested_subprocess_calls":len(nested),
            "dynamic_or_unparsed_calls":len(unresolved),
            "test_only_dynamic_or_unparsed_calls":len(test_only_unresolved),
            "missing_literal_targets":len(missing),
        },
        "unresolved":unresolved,
        "test_only_unresolved":test_only_unresolved,
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
