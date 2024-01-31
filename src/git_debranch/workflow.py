import json

from dataclasses import dataclass

from SpiffWorkflow.bpmn.serializer.workflow import BpmnWorkflowSerializer
from SpiffWorkflow.bpmn.specs.control import BpmnStartTask
from SpiffWorkflow.spiff.serializer.config import SPIFF_CONFIG

from git_debranch.loader import load_workflow
from git_debranch.runner import run_workflow

@dataclass
class WorkflowResult:
    completed: bool
    stderr: str
    stdout: str
    returncode: int

def run(args):
    workflow = load_workflow()

    for task in workflow.get_tasks_iterator():
        if isinstance(task.task_spec, BpmnStartTask):
            task.set_data(args=args)
            break
    
    completed, data = run_workflow(workflow)
    result = data.get("result", {})
    stderr = result.get("stderr")
    stdout = result.get("stdout")
    returncode = result.get("returncode", 0 if completed else -1)
    return WorkflowResult(completed, stderr, stdout, returncode)
 
def spec_json():
    registry = BpmnWorkflowSerializer.configure(SPIFF_CONFIG)
    serializer = BpmnWorkflowSerializer(registry=registry)
    workflow = load_workflow()
    workflow_dct = serializer.to_dict(workflow)
    workflow_specs_dct = {
        "serializer_version": "jbirddog/git-debranch",
        "spec": workflow_dct["spec"],
        "subprocess_specs": workflow_dct["subprocess_specs"],
    }
    return json.dumps(workflow_specs_dct, sort_keys=True, indent=2)

