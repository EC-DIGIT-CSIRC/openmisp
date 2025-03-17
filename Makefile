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
	mkdocs build
	mkdocs serve

.PHONY: generate-code
generate-code:
	python scripts/generate_misp_models.py
	python scripts/generate_taxonomy_models.py
