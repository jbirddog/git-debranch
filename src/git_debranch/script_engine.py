import json
import subprocess

from SpiffWorkflow.bpmn.PythonScriptEngine import PythonScriptEngine

class CustomScriptEngine(PythonScriptEngine):
    def call_service(self, operation_name, operation_params, task_data):
        operations = {
            "git/FetchAndPrune": git_fetch_and_prune,
            "subprocess/Run": subprocess_run,
        }
        return operations[operation_name](operation_params, task_data)

def git_fetch_and_prune(_params, task_data):
    run_args = ["git", "fetch", "-p"]
    params = {"args": {"value": run_args, "type": "any"}}
    return subprocess_run(params, task_data)
    
def subprocess_run(params, task_data):
    args = params["args"]["value"]
    subprocess_result = subprocess.run(args, capture_output=True)
    result = {
        "returncode": subprocess_result.returncode,
        "stdout": subprocess_result.stdout.decode("utf-8"),
        "stderr": subprocess_result.stderr.decode("utf-8"),
    }
    return json.dumps(result)
