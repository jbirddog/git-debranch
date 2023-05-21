import sys

from git_debranch import workflow

def main():
    result = workflow.run()

    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if result.stdout:
        print(result.stdout)
    exit(result.returncode)
