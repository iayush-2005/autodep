# main.py

from autodetect_deps.scanner import scan_project_for_imports

if __name__ == "__main__":
    project_path = input("Enter the path to your Python project: ")
    imports = scan_project_for_imports(project_path)
    print("\n📦 Detected imports:")
    for imp in imports:
        print(f" - {imp}")
