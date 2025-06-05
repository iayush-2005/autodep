from autodep.scanner import extract_imports_from_directory
from autodep.import_utils import filter_and_normalize_imports
from autodep.checker import get_missing_modules
from autodep.installer import install_missing_modules, in_virtualenv, export_requirements

import os
import sys

def warn_if_venv_exists(project_path: str):
    """Warn the user if a .venv already exists in the given path."""
    venv_path = os.path.join(project_path, ".venv")
    if os.path.isdir(venv_path):
        print(f"⚠️  A virtual environment already exists at {venv_path}")
        print("   Using existing environment.\n")

def main():
    if len(sys.argv) < 2:
        print("❗ main.py requires the project path as an argument.")
        sys.exit(1)

    project_path = sys.argv[1]
    warn_if_venv_exists(project_path)

    if not in_virtualenv():
        print("❌ This script must be run inside a virtual environment.")
        sys.exit(1)

    print(f"\n🔍 Scanning project at: {project_path}...")
    raw_imports = extract_imports_from_directory(project_path)
    print(f"📦 Found {len(raw_imports)} raw imports.")

    cleaned_imports = filter_and_normalize_imports(raw_imports)
    print(f"✅ After filtering/normalizing: {len(cleaned_imports)} modules")

    missing = get_missing_modules(cleaned_imports)
    installed = sorted(set(cleaned_imports) - set(missing))

    if installed:
        print("\n✅ Already installed modules:")
        for mod in installed:
            print(f"  ✔ {mod}")
    else:
        print("\nℹ️  No modules were already installed.")

    if missing:
        print("\n🚨 Missing modules:")
        for mod in missing:
            print(f"  ✖ {mod}")

        newly_installed = install_missing_modules(missing)
        if newly_installed:
            export_requirements(project_path)
    else:
        print("\n🎉 All required modules are already installed!")

if __name__ == "__main__":
    main()
