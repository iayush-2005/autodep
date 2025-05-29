# autodetect_deps/checker.py

import importlib

import importlib.util

def is_module_installed(module_name: str) -> bool:
    """
    Check if a module can be found in the current Python environment.
    """
    return importlib.util.find_spec(module_name) is not None

def get_missing_modules(modules: set[str]) -> list[str]:
    """
    Return a list of modules that are not installed.
    """
    return [m for m in modules if not is_module_installed(m)]


def is_module_available(module_name: str) -> bool:
    """
    Returns True if the given module can be imported without error
    """
    try:
        importlib.import_module(module_name)
        return True
    except ModuleNotFoundError:
        return False
    except Exception:
        # Some modules may throw non-standard errors on import
        return True  # Considered available to avoid false positives

def detect_missing_modules(imports: set[str]) -> set[str]:
    """
    Given a set of module names, return the subset that is not available
    """
    missing = set()
    for module in imports:
        if not is_module_available(module):
            missing.add(module)
    return missing
