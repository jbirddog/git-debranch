import os
import subprocess
import tempfile

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
    _edit_task_data(task.data, config["edit"])
    task.run()

def _edit_task_data(task_data, variable_to_edit):
    value = task_data[variable_to_edit]
    editor = os.environ.get("EDITOR", "vi")
    with tempfile.NamedTemporaryFile() as tf:
        tf.write(value.encode("utf-8"))
        tf.flush()
        subprocess.run([editor, tf.name])
        tf.seek(0)
        value = tf.read().decode("utf-8")
    task_data[variable_to_edit] = value
