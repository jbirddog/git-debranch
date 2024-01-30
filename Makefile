
MY_USER := $(shell id -u)
MY_GROUP := $(shell id -g)
ME := $(MY_USER):$(MY_GROUP)

SPIFF_ARENA_DIR := ../../sartography/spiff-arena
BPMN_SPEC_DIR := $(shell pwd)/src/git_debranch

venv:
	python -m venv env

dev-reqs:
	pip install -r dev_requirements.txt

dev-env: venv dev-reqs
	@/bin/true

take-ownership:
	sudo chown -R $(ME) .

check-ownership:
	find . ! -user $(MY_USER) ! -group $(MY_GROUP)

run-editor: stop-editor
	cd $(SPIFF_ARENA_DIR) && \
		SPIFF_EDITOR_URL_PATH=/admin/process-models/bpmn:git-debranch \
		./bin/run_editor $(BPMN_SPEC_DIR)

stop-editor:
	cd $(SPIFF_ARENA_DIR) && ./bin/stop_editor

update-editor:
	cd $(SPIFF_ARENA_DIR) && ./bin/update_editor

.PHONY: take-ownership check-ownership \
	run-editor stop-editor update-editor \
	dev-env venv dev-reqs
