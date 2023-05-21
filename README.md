# git-debranch

Remove branches that are no longer needed.

## Installation

```
pip install git-debranch
```

_Note: PyPI is currently blocking new uploads. Once resolved this will work._

### Development Installation

```
pip install -r dev_requirements.txt
```

You likely want to be inside a venv. This wlll give you an editable installation so you can run the program 
and see changes. If you add a new bpmn/json file then you need to re-run this command.

## Usage

```
git debranch
```

From inside a git repository, running `git debranch` will present you with a list of branches that could 
be deleted. This list is presented using `$EDITOR`. If the environment variable is not set `vi` is used 
as the fallback.

## Editing the Branch List

When `$EDITOR` is invoked, it will contain a series of lines. Comment lines begin with `#` and any line that 
is not empty or a comment is assumed to be the name of a branch to delete locally. You can update this list 
by either removing or commenting branches that you want to keep. Branches that appear safe to delete are 
uncommented by default. Branches that may not be safe to delete are left commented by default. When you save 
and close `$EDITOR` any uncommented branches will be deleted using `git branch -D`.
