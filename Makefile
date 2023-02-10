lint:
	poetry run pylint hc_pyconsul/
	poetry run flake8 .
	poetry run mypy hc_pyconsul/

test: tests
	poetry run pytest --cov=hc_pyconsul tests/ --junitxml=report.xml --cov-report xml:coverage.xml

pre-commit:
	make lint
	make test

dev: pyproject.toml
	poetry install --no-root --no-interaction

lint-ci:
	make dev
	make lint

test-ci:
	make dev
	make test

dev-pip:
	pip install . && pip install ".[testing]"
