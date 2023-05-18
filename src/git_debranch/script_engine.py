from SpiffWorkflow.bpmn.PythonScriptEngine import PythonScriptEngine

class CustomScriptEngine(PythonScriptEngine):
    def call_service(self, operation_name, operation_params, task_data):
        operations = {
            "subprocess/Run": subprocess_run,
        }
        return operations[operation_name](operation_params, task_data)

def subprocess_run(params, task_data):
    return "{}"
