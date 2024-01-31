import argparse
import sys

from git_debranch import workflow

def main():
    parser = argparse.ArgumentParser(description='Delete local git branches')
    parser.add_argument('--offline', action='store_true', help='Do not run online operations such as fetch and prune')
    parser.add_argument('--dry-run', action='store_true', help='Do not actually delete branches')
    parser.add_argument('--dump-spec', action='store_true', help='Dump the workflow spec to stdout and exit')

    args = parser.parse_args()

    if args.dump_spec:
        print(workflow.spec_json())
        exit(0)
    
    result = workflow.run(vars(args))

    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if result.stdout:
        print(result.stdout)
    exit(result.returncode)
