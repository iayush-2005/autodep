# autodetect_deps/scanner.py

import ast
import os

def get_python_files(directory):
    """ Recursively collect all .py files in the directory """
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

def extract_imports_from_file(filepath):
    """ Extract all imported modules from a single Python file """
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            tree = ast.parse(f.read(), filename=filepath)
        except SyntaxError:
            print(f"Skipping {filepath} due to syntax error.")
            return []

    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split('.')[0])  # e.g., "os.path" → "os"
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    return list(imports)

def scan_project_for_imports(project_path):
    """ Scan all .py files in a project and collect unique imports """
    all_imports = set()
    for py_file in get_python_files(project_path):
        imports = extract_imports_from_file(py_file)
        all_imports.update(imports)
    return sorted(all_imports)
