import os
import sys
from pathlib import Path

from autodep.scanner import extract_imports_from_directory
from autodep.import_utils import filter_and_normalize_imports
from autodep.checker import get_missing_modules
from autodep.installer import (
    install_missing_modules,
    in_virtualenv,
    export_requirements,
)
from autodep.logger import get_logger

logger = get_logger("main")


def warn_if_venv_exists(project_path: str | Path):
    venv_path = Path(project_path) / ".venv"
    if venv_path.is_dir():
        logger.warning("⚠️  A virtual environment already exists at: %s", venv_path)
        logger.debug("Using existing environment.")


def run_autodep(project_path: str | Path, force_run: bool = False):
    warn_if_venv_exists(project_path)

    if not in_virtualenv() and not force_run:
        logger.error("❌ This script must be run inside a virtual environment.")
        sys.exit(1)

    logger.info("🔍 Scanning project at: %s", project_path)
    raw_imports = extract_imports_from_directory(project_path)
    logger.info("📦 Found %d raw imports", len(raw_imports))

    cleaned_imports = filter_and_normalize_imports(raw_imports)
    logger.info("✅ After filtering/normalizing: %d modules", len(cleaned_imports))

    missing = get_missing_modules(cleaned_imports)
    installed = sorted(set(cleaned_imports) - set(missing))

    if installed:
        logger.info("✅ Already installed modules:")
        for mod in installed:
            logger.info("  ✔ %s", mod)
    else:
        logger.info("ℹ️  No modules were already installed.")

    if missing:
        logger.warning("🚨 Missing modules:")
        for mod in missing:
            logger.warning("  ✖ %s", mod)

        newly_installed = install_missing_modules(missing)
        if newly_installed:
            export_requirements(project_path)
    else:
        logger.info("🎉 All required modules are already installed!")
