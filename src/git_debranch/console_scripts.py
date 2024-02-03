import sys

from git_debranch import workflow

def main():
    argv = sys.argv
    if "--dump-spec" in argv:
        print(workflow.spec_json())
        exit(0)

    result = workflow.run(argv)

    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if result.stdout:
        print(result.stdout)
    exit(result.returncode)
