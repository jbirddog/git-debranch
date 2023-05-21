# TODOs

1. command line args
   1. --dry-run
1. unit test with mock git service task
   1. wait to integration upcoming testing framework
1. README.md
   1. installing
   1. development, using arena to edit
1. CI
   1. run tests (when ready, see above)
   1. push to pypi
1. move main out of __init__.py, into some package that matches setup.py key?
1. git/DeleteBranch should get `branches_to_delete` via param instead of task data
1. --no-merge doesn't do exactly what I thought when squash+merge
   1. may be better to remove the merge/no-merge distinction?