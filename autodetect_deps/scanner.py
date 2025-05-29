# autodetect_deps/scanner.py

import os
import ast

def extract_imports_from_file(filepath: str) -> set[str]:
    """
    Extract top-level module names from a single Python file and
    handles both 'import x' and 'from x import y'.
    """
    imports = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            node = ast.parse(f.read(), filename=filepath)
        
        for stmt in ast.walk(node):
            if isinstance(stmt, ast.Import):
                for alias in stmt.names:
                    imports.add(alias.name)
            elif isinstance(stmt, ast.ImportFrom):
                if stmt.module:
                    imports.add(stmt.module)
    except Exception as e:
        print(f"[!] Failed to parse {filepath}: {e}")
    return imports

def extract_imports_from_directory(directory: str) -> set[str]:
    """
    Recursively extract imports from all .py files in a given directory
    """
    all_imports = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                all_imports.update(extract_imports_from_file(filepath))
    return all_imports
