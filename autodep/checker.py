# autodep/checker.py

import importlib.util

def is_module_installed(module_name: str) -> bool:
    """
    Return True if the module can be found in the current environment
    without importing it
    """
    return importlib.util.find_spec(module_name) is not None

def get_missing_modules(modules: set[str]) -> list[str]:
    """
    Given a set of module names, return a list of those
    not found in the current environment
    """
    return [m for m in modules if not is_module_installed(m)]

def detect_missing_modules(imports: set[str]) -> set[str]:
    """
    Return set of missing modules from the input imports
    """
    return {m for m in imports if not is_module_installed(m)}
