.DEFAULT_GOAL := all

.PHONY: .uv
.uv:
	@uv --version || echo 'Please install uv: https://docs.astral.sh/uv/getting-started/installation/'

.PHONY: sync
sync: .uv
	uv sync --frozen --extra test --extra dev

.PHONY: format
format: .uv
	uv run ruff format
	uv run ruff check --fix --fix-only

.PHONY: lint
lint: .uv
	uv run ruff format --check
	uv run ruff check

.PHONY: docs
docs:
	# python scripts/generate_api_docs.py
	mkdocs build

.PHONY: docs-serve
docs-serve:
	# python scripts/generate_api_docs.py
	mkdocs serve

.PHONY: docstring-coverage
docstring-coverage:
	# python scripts/check_docstring_coverage.py

.PHONY: docstring-style
docstring-style:
	uv add pydocstyle
	uv run pydocstyle --convention=google src/openmisp/

.PHONY: generate-enums
generate-enums:
	python scripts/generate_enums.py

.PHONY: clean
clean:
	rm -rf site/
	rm -rf docs/api-reference/
