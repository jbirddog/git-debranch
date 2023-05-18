import os
import pkgutil

from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser
from SpiffWorkflow.task import TaskState

def run():
    workflow = _workflow()
    print(f"git-debranch: {_run(workflow)}")

#
# extract to runner.py
#

def _run(workflow):
    while not workflow.is_completed():
        tasks = workflow.get_tasks(TaskState.READY)
        task = tasks[0] if len(tasks) > 0 else None
        if task is None:
            break
        task.run()
        workflow.refresh_waiting_tasks()
    return workflow.data
    
#
# extract to loader.py
#
    
def _bpmn_data_path(filename):
    return os.path.join("bpmn", "git-debranch", filename)

def _bpmn_data_paths():
    bpmn_filenames = ["git-debranch.bpmn"]
    return map(_bpmn_data_path, bpmn_filenames)

def _get_data(data_path):
    return pkgutil.get_data("git_debranch", data_path)

def _get_data_str(data_path):
    return _get_data(data_path).decode("utf-8")

def _bpmn_strs():
    return map(_get_data_str, _bpmn_data_paths())

def _parser():
    parser = SpiffBpmnParser()
    for bpmn_str in _bpmn_strs():
        # TODO: hack - replace with better solution - add_bpmn_str doesn't allow:
        bpmn_str = bpmn_str.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
        parser.add_bpmn_str(bpmn_str)
    return parser
    
def _workflow():
    parser = _parser()
    process_name = "git-debranch"
    top_level = parser.get_spec(process_name)
    subprocesses = parser.get_subprocess_specs(process_name)
    return BpmnWorkflow(top_level, subprocesses)
