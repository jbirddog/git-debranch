import json
import subprocess

from SpiffWorkflow.bpmn.PythonScriptEngine import PythonScriptEngine

class CustomScriptEngine(PythonScriptEngine):
    def call_service(self, operation_name, operation_params, task_data):
        operations = {
            "os/SpawnProcess": spawn_process,
        }
        return operations[operation_name](operation_params, task_data)

def spawn_process(params, task_data):
    args = params["args"]["value"]
    subprocess_result = subprocess.run(args, capture_output=True)
    result = {
        "returncode": subprocess_result.returncode,
        "stdout": subprocess_result.stdout.decode("utf-8"),
        "stderr": subprocess_result.stderr.decode("utf-8"),
    }
    return json.dumps(result)
