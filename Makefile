
MY_USER := $(shell id -u)
MY_GROUP := $(shell id -g)
ME := $(MY_USER):$(MY_GROUP)

SPIFF_ARENA_DIR := ../../sartography/spiff-arena
BPMN_SPEC_DIR := $(shell pwd)/src/git_debranch

.PHONY: take-ownership
take-ownership:
	sudo chown -R $(ME) .

.PHONY: check-ownership
check-ownership:
	find . ! -user $(MY_USER) ! -group $(MY_GROUP)

.PHONY: run-editor
run-editor: stop-editor
	cd $(SPIFF_ARENA_DIR) && ./bin/run_editor $(BPMN_SPEC_DIR)

.PHONY: stop-editor
stop-editor:
	cd $(SPIFF_ARENA_DIR) && ./bin/stop_editor

.PHONY: update-editor
update-editor:
	cd $(SPIFF_ARENA_DIR) && ./bin/update_editor
