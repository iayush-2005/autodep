# main.py

from autodetect_deps.scanner import extract_imports_from_directory
from autodetect_deps.import_utils import filter_and_normalize_imports
from autodetect_deps.checker import detect_missing_modules

def main():
    print("🔍 AutoDep: Python Dependency Detector")
    project_path = input("Enter the path to the project directory: ").strip()

    print(f"\n📁 Scanning: {project_path}")
    raw_imports = extract_imports_from_directory(project_path)
    print(f"🔎 Raw imports found: {len(raw_imports)}")

    cleaned_imports = filter_and_normalize_imports(raw_imports)
    print(f"✅ Filtered imports: {len(cleaned_imports)}")

    missing = detect_missing_modules(cleaned_imports)

    print("\n📋 Detected missing third-party dependencies:")
    if not missing:
        print("🎉 All imports are either built-in or already installed!")
    else:
        for m in sorted(missing):
            print(f" - {m}")

if __name__ == "__main__":
    main()
