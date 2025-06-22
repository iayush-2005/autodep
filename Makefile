# Makefile for autodep

# Virtual environment activation
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: help install run test format lint clean

help:
	@echo "📦  autodep Makefile Commands:"
	@echo "make install   → Setup venv and install the project"
	@echo "make run       → Run the autodep CLI tool"
	@echo "make test      → Run pytest on test suite"
	@echo "make format    → Auto-format code using black"
	@echo "make lint      → Run lint checks with flake8"
	@echo "make clean     → Remove venv and __pycache__ files"

install:
	@echo "🚀 Setting up virtual environment and installing project..."
	@python3 -m venv $(VENV)
	@$(PIP) install --upgrade pip
	@$(PIP) install -e .
	@$(PIP) install -r requirements-dev.txt || true

run:
	@echo "🎯 Running autodep..."
	@$(VENV)/bin/python -m autodep.cli

test:
	@echo "🧪 Running tests..."
	@$(PYTHON) -m pytest -v tests/

format:
	@echo "🧼 Formatting code with black..."
	@$(PYTHON) -m black autodep/ tests/

lint:
	@echo "🔎 Linting code with flake8..."
	@$(PYTHON) -m flake8 autodep/ tests/

clean:
	@echo "🧹 Cleaning up..."
	@rm -rf $(VENV) __pycache__ */__pycache__ .pytest_cache .mypy_cache

# Auto-fix lint issues
fix-lint:
	@echo "🔧 Auto-fixing lint issues..."
	@.venv/bin/autopep8 --in-place --aggressive --aggressive --recursive autodep
	@.venv/bin/isort autodep
