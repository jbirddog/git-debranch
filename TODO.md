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
   1. --merged? --no-merged? --remotes?
1. unit test with mock git service task
   1. wait to integration upcoming testing framework
1. CI
   1. run tests (when ready, see above)
1. when there are no branches to delete, don't open $EDITOR
   1. set stdout to "Nothing to do" or similar
1. integrate spiff-element-units
   1. what does it mean for dev flow to get element units into package
1. write spiff logs somewhere? --log?