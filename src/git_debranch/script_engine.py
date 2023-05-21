import json
import subprocess

from SpiffWorkflow.bpmn.PythonScriptEngine import PythonScriptEngine

class CustomScriptEngine(PythonScriptEngine):
    def call_service(self, operation_name, operation_params, task_data):
        operations = {
            "git/DeleteBranches": git_delete_branches,
            "git/FetchAndPrune": git_fetch_and_prune,
            "git/ListAllMergedBranches": git_list_all_merged_branches,
            "git/ListAllUnmergedBranches": git_list_all_unmerged_branches,
        }
        return operations[operation_name](operation_params, task_data)

def git_delete_branches(params, task_data):
    run_args = ["git", "branch", "-D"]
    branches_to_delete = task_data["branches_to_delete"]
    run_args += branches_to_delete
    params = {"args": {"value": run_args, "type": "any"}}
    return subprocess_run(params, task_data)
    
def git_fetch_and_prune(params, task_data):
    run_args = ["git", "fetch", "-p"]
    params = {"args": {"value": run_args, "type": "any"}}
    return subprocess_run(params, task_data)

def git_list_all_merged_branches(params, task_data):
    run_args = ["git", "branch", "--all", "--merged"]
    params = {"args": {"value": run_args, "type": "any"}}
    return subprocess_run(params, task_data)

def git_list_all_unmerged_branches(params, task_data):
    run_args = ["git", "branch", "--all", "--no-merged"]
    params = {"args": {"value": run_args, "type": "any"}}
    return subprocess_run(params, task_data)

# TODO: once git/DeleteBranches is in, make this return a func
# not sure how task_data plays in yet
def subprocess_run(params, task_data):
    args = params["args"]["value"]
    subprocess_result = subprocess.run(args, capture_output=True)
    result = {
        "returncode": subprocess_result.returncode,
        "stdout": subprocess_result.stdout.decode("utf-8"),
        "stderr": subprocess_result.stderr.decode("utf-8"),
    }
    return json.dumps(result)
