.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: build
build: ## Create a Docker image for the CLI
	docker build -t icli .

.PHONY: run
run: ## Dummy run with Batman
	docker run icli --name=Batman --count=3

.PHONY: cli-help
cli-help: ## Show CLI help
	docker run icli --help

local-install: ## (it requires 'poetry' installed)
	python -m pip install -e .

publish: ## Publish in PyPI
	poetry publish --build -u islomar