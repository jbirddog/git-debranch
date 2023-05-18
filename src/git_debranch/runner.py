from SpiffWorkflow.task import TaskState

def run_workflow(workflow):
    while not workflow.is_completed():
        tasks = workflow.get_tasks(TaskState.READY)
        task = tasks[0] if len(tasks) > 0 else None
        if task is None:
            break
        task.run()
        workflow.refresh_waiting_tasks()
    return workflow.data
