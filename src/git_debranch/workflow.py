from dataclasses import dataclass

from git_debranch.loader import load_workflow
from git_debranch.runner import run_workflow

@dataclass
class WorkflowResult:
    completed: bool
    stderr: str
    stdout: str
    returncode: int

def run():
    workflow = load_workflow()
    completed, data = run_workflow(workflow)
    result = data.get("result", {})
    stderr = result.get("stderr")
    stdout = result.get("stdout")
    returncode = result.get("returncode", 0 if completed else -1)
    return WorkflowResult(completed, stderr, stdout, returncode)
 
