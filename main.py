# main.py

from autodetect_deps.scanner import extract_imports_from_directory
from autodetect_deps.import_utils import filter_and_normalize_imports
from autodetect_deps.checker import get_missing_modules

def main():
    project_path = input("Enter the path to your Python project: ").strip()
    
    print(f"\n📦 Scanning project at: {project_path}...")
    raw_imports = extract_imports_from_directory(project_path)
    print(f"🔍 Found {len(raw_imports)} raw imports.")

    cleaned_imports = filter_and_normalize_imports(raw_imports)
    print(f"✅ After filtering/normalizing: {len(cleaned_imports)} modules")

    missing = get_missing_modules(cleaned_imports)
    installed = sorted(cleaned_imports - set(missing))

    print("\n✅ Installed modules:")
    for mod in installed:
        print(f"  ✔ {mod}")

    print("\n❌ Missing modules:")
    for mod in missing:
        print(f"  ✖ {mod}")

if __name__ == "__main__":
    main()
