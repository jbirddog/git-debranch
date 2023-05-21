# TODOs

## v0.1.1

1. fix spaces before/after branch name issue
1. move def main out of __init__.py, into some package that matches setup.py key?
1. bump version
1. when PyPI comes back online for new projects releast v0.1.1

## unordered

1. look at having something like an embedded el-rodeo so you can `make edits`
1. don't fetch and prune by default?
1. command line args
   1. --dry-run
   1. --fetch-and-prune
1. unit test with mock git service task
   1. wait to integration upcoming testing framework
1. README.md
   1. installing
   1. development, using arena to edit
1. CI
   1. run tests (when ready, see above)
   1. push to pypi
1. git/DeleteBranch should get `branches_to_delete` via param instead of task data
1. --no-merge doesn't do exactly what I thought when squash+merge
   1. may be better to remove the merge/no-merge distinction?
   1. default is --all, add comand line args for --merged and --no-merged?
1. need to treat branches like `main` differently show they don't show up in the
   same section as local branches that have been merged but have a remote