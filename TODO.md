# TODOs

## v0.1.4

1. bump version
1. blocked on SpiffWorkflow 2.0?
   1. or vendor in the short term?

## unordered

1. don't fetch and prune by default?
1. command line args
   1. --dry-run
   1. --fetch-and-prune
1. unit test with mock git service task
   1. wait to integration upcoming testing framework
1. CI
   1. run tests (when ready, see above)
   1. push to pypi
1. git/DeleteBranch should get `branches_to_delete` via param instead of task data
1. --no-merge doesn't do exactly what I thought when squash+merge
   1. may be better to remove the merge/no-merge distinction?
   1. default is --all, add comand line args for --merged and --no-merged?
1. when there are no branches to delete, don't open $EDITOR
   1. set stdout to "Nothing to do" or similar