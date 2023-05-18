from git_debranch.loader import load_workflow
from git_debranch.runner import run_workflow

def run():
    workflow = load_workflow()
    print(f"git-debranch: {run_workflow(workflow)}")
