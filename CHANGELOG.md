# CHANGELOG

## v0.1.7

1. Removed hack when loading bpmn file content

## v0.1.6

1. Fixed bug when not on a HEAD branch an empty report could be shown
1. Fixed issue where terminate end events inside a bpmn subprocess did not do what I thought they did
1. Added --dry-run to prevent actually deleting branches
1. Added --offline to prevent running fetch and prune

## v0.1.5

1. Updated editor support to deep link to process model
2. Added logic so `$EDITOR` is not opened if there are no branches to delete
3. Added CHANGELOG.md

## v0.1.4

1. Now using SpiffWorkflow 2.0.0rc0
2. Attempt to abort workflow with result of failed called to git
3. Simplify git response parsing
4. Better handling of `HEAD` and remote branches
5. Added `make run-editor` to integrate with the editor from [SpiffArena](https://github.com/sartography/spiff-arena/)

## v0.1.3
## v0.1.2

_Note: it is not recommended to use these versions._

1. Failed attempts to use non release version of SpiffWorkflow with PyPI

## v0.1.1

1. Better location for the pip console script
2. Fix an issue with leading/trailing spaces in branch names after user selection
3. Added proper README.md

## v0.1.0

1. Initial project set up and development
