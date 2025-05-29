# autodetect_deps/import_utils.py

import sys
import re

# Use a frozen set for fast membership testing
BUILTIN_MODULES = frozenset(sys.builtin_module_names)

# Pattern to filter out private/dunder/internal modules
PRIVATE_OR_DUNDER = re.compile(r"^(_|__|builtins|__\w+__)$")

# Common namespace simplifications
NORMALIZATION_MAP = {
    "PIL": {"PIL", "PIL.Image", "PIL.JpegImagePlugin", "PIL.TiffImagePlugin"},
    "OpenSSL": {"OpenSSL", "OpenSSL.SSL"},
    "IPython": {"IPython", "ipython"},
    "PyQt6": {"PyQt6"},
    "PySide6": {"PySide6"},
    "MySQLdb": {"MySQLdb", "_mysql"},
}

def normalize_module_name(module: str) -> str:
    """
    Normalize submodules into top-level packages using known mappings.
    """
    for top_level, variants in NORMALIZATION_MAP.items():
        if module in variants:
            return top_level
    return module.split(".")[0]  # Default to top-level module

def is_valid_module(module: str) -> bool:
    """
    Checks if a module is not built-in, private, or dunder-named.
    """
    if module in BUILTIN_MODULES:
        return False
    if PRIVATE_OR_DUNDER.match(module):
        return False
    if module.startswith("_") or module.startswith("__"):
        return False
    return True

def filter_and_normalize_imports(imports: set[str]) -> set[str]:
    """
    Filters and normalizes a set of import names.
    Returns a cleaned set of module names ready for availability checking.
    """
    cleaned = set()
    for module in imports:
        if not is_valid_module(module):
            continue
        normalized = normalize_module_name(module)
        cleaned.add(normalized)
    return cleaned
