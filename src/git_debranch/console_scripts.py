import argparse
import sys

from git_debranch import workflow

def main():
    parser = argparse.ArgumentParser(description='Delete local git branches')
    parser.add_argument('--offline', action='store_true', help='Do not run online operations such as fetch and prune')
    parser.add_argument('--dry-run', action='store_true', help='Do not actually delete branches')

    args = vars(parser.parse_args())
    
    result = workflow.run(args)

    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if result.stdout:
        print(result.stdout)
    exit(result.returncode)
