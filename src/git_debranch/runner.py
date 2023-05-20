from SpiffWorkflow.task import TaskState

from git_debranch.loader import load_manual_task_config

def run_workflow(workflow):
    while not workflow.is_completed():
        tasks = workflow.get_tasks(TaskState.READY)
        task = tasks[0] if len(tasks) > 0 else None
        if task is None:
            break
        if task.task_spec.manual:
            _run_manual_task(task)
        else:
            task.run()
        workflow.refresh_waiting_tasks()
    return workflow.is_completed(), workflow.data

def _run_manual_task(task):
    config = load_manual_task_config(task.task_spec.name)
    variable_to_edit = config["edit"]
    variable = task.data[variable_to_edit]
    print(variable)
    input()
    task.run()
