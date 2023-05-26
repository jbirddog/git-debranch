# git-debranch

Git subcommand that uses [SpiffWorkflow](https://github.com/sartography/SpiffWorkflow) to remove branches that are no longer needed.

## Installation

```
pip install git-debranch
```

## Usage

```
git debranch
```

From inside a git repository, running `git debranch` will present you with a list of branches that could 
be deleted. This list is presented using `$EDITOR`. If the environment variable is not set `vi` is used 
as the fallback.

*Please note `git fetch -p` is run before the branch list is presented.*

## Editing the Branch List

When `$EDITOR` is invoked, it will contain a series of lines. Comment lines begin with `#` and any line that 
is not empty or a comment is assumed to be the name of a branch to delete locally. You can update this list 
by either removing or commenting branches that you want to keep. Branches that appear safe to delete are 
uncommented by default. Branches that may not be safe to delete are left commented by default. When you save 
and close `$EDITOR` any uncommented branches will be deleted using `git branch -D`.

## Developing

In my opinion this project turned out to be quite pleasurable to work with. Please feel free to play with 
the code. `TODO.md` has some loose TODO items that may turn into issues at some point.

### Development Installation

```
pip install -r dev_requirements.txt
```

You likely want to be inside a venv. This wlll give you an editable installation so you can run the program 
and see changes. If you add a new bpmn/json file then you need to re-run this command.

### Using SpiffArena for BPMN edits

[SpiffArena](https://github.com/sartography/spiff-arena) is used to make edits to the BPMN files that are 
bundled with this program. To start the editor run `make run-editor`. You will be presented with a message
once started to go to `http://localhost:8001` (assuming the default configuration is used). The editor
requires `docker` and `docker compose` to run.

From there you can edit the diagrams but you cannot run them from within SpiffArena at this time. Some work 
would need to be done to support our custom `Connector Proxy` that is not http based. You can however run 
the `Script Task` unit tests, which were very helpful during development.

When finished you can `make stop-editor`. If you would like to pull the latest version of SpiffArena use
`make update-editor`.
