.ONESHELL:
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")

.PHONY: help
help:             ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep


.PHONY: setup
setup:  ## Execute installation.
	@echo "Setting up project."
	@pip3 install --upgrade setuptools
	@echo "Installing testing dependencies."
	@pip3 install -r requirements-test.txt
	@echo "Setting up project requirements."
	@pip3 install -r requirements.txt
	@echo "Project setup complete!"


.PHONY: show
show:             ## Show the current environment.
	@echo "Current environment:"
	@echo "Running using $(ENV_PREFIX)"
	@$(ENV_PREFIX)python -V
	@$(ENV_PREFIX)python -m site

.PHONY: format
format:              ## Format code using black & isort.
	$(ENV_PREFIX)isort slink/
	$(ENV_PREFIX)black -l 79 slink/
	$(ENV_PREFIX)black -l 79 tests/

.PHONY: lint
lint:  ## Run pep8, black, mypy linters.
	$(ENV_PREFIX)pylint slink/
	$(ENV_PREFIX)flake8 slink/
	$(ENV_PREFIX)black -l 80 --check slink/
	$(ENV_PREFIX)mypy --ignore-missing-imports slink/

.PHONY: test
test:  ## Run PyTest unit tests.
	@echo "Running unittest suite..."
	@pytest -vv -rA
	@echo "Cleaning up test environment"
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@rm -rf .pytest_cache

.PHONY: watch
watch:            ## Run tests on every change.
	ls **/**.py | entr $(ENV_PREFIX)pytest -s -vvv -l --tb=long --maxfail=1 tests/

.PHONY: clean
clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@rm -rf .cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
	@rm -rf .pytest_cache
	@echo "Cleaned out unused files."

.PHONY: docs
docs:             ## Build the documentation.
	@echo "building documentation ..."
	@$(ENV_PREFIX)mkdocs build
	URL="site/index.html"; xdg-open $$URL || sensible-browser $$URL || x-www-browser $$URL || gnome-open $$URL