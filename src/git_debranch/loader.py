import io
import json
import os
import pkgutil

from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
from SpiffWorkflow.spiff.parser.process import SpiffBpmnParser

from git_debranch.script_engine import CustomScriptEngine
    
def load_workflow():
    parser = _parser()
    process_name = "git-debranch"
    top_level = parser.get_spec(process_name)
    subprocesses = parser.get_subprocess_specs(process_name)
    script_engine = CustomScriptEngine()
    return BpmnWorkflow(top_level, subprocesses, script_engine=script_engine)

def load_manual_task_config(task_name):
    filename = f"{task_name}.json"
    json_str = _get_data_str(_bpmn_data_path(filename))
    return json.loads(json_str)

def _bpmn_data_path(filename):
    return os.path.join("bpmn", "git-debranch", filename)

def _bpmn_data_paths():
    bpmn_filenames = [
        "git-debranch.bpmn",
        "all_branches.bpmn",
        "branch_parser.bpmn",
        "deletion_prompt.bpmn",
        "delete_branches.bpmn",
        "spawn.bpmn",
    ]
    return map(_bpmn_data_path, bpmn_filenames)

def _get_data(data_path):
    return pkgutil.get_data("git_debranch", data_path)

def _get_data_str(data_path):
    return _get_data(data_path).decode("utf-8")

def _bpmn_data():
    return map(_get_data, _bpmn_data_paths())

def _parser():
    parser = SpiffBpmnParser()
    for data in _bpmn_data():
        parser.add_bpmn_io(io.BytesIO(data))
    return parser
