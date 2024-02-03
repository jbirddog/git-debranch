from dataclasses import dataclass

from SpiffWorkflow.bpmn.specs.control import BpmnStartTask

from git_debranch.loader import load_workflow
from git_debranch.runner import run_workflow

@dataclass
class WorkflowResult:
    completed: bool
    stderr: str
    stdout: str
    returncode: int

def run(argv):
    workflow = load_workflow()

    for task in workflow.get_tasks_iterator():
        if isinstance(task.task_spec, BpmnStartTask):
            task.set_data(argv=argv)
            break
    
    completed, data = run_workflow(workflow)
    result = data.get("result", {})
    stderr = result.get("stderr")
    stdout = result.get("stdout")
    returncode = result.get("returncode", 0 if completed else -1)
    return WorkflowResult(completed, stderr, stdout, returncode)
 
