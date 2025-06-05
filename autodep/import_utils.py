# autodetect_deps/import_utils.py

import sys
import re

BUILTIN_MODULES = frozenset(sys.builtin_module_names)

# Simplified regex: matches modules starting with _ or __ or named builtins/dunder patterns
PRIVATE_OR_DUNDER = re.compile(r"^(_|__|builtins|__\w+__)$")

NORMALIZATION_MAP = {
    "PIL": {"PIL", "PIL.Image", "PIL.JpegImagePlugin", "PIL.TiffImagePlugin"},
    "OpenSSL": {"OpenSSL", "OpenSSL.SSL"},
    "IPython": {"IPython", "ipython"},
    "PyQt6": {"PyQt6"},
    "PySide6": {"PySide6"},
    "MySQLdb": {"MySQLdb", "_mysql"},
}

def normalize_module_name(module: str) -> str:
    if not module:
        return module
    for top_level, variants in NORMALIZATION_MAP.items():
        if module in variants:
            return top_level
    return module.split(".")[0]

def is_valid_module(module: str) -> bool:
    if not module:
        return False
    if module in BUILTIN_MODULES:
        return False
    if PRIVATE_OR_DUNDER.match(module):
        return False
    if module.startswith("_"):
        return False
    return True

def filter_and_normalize_imports(imports: set[str]) -> set[str]:
    cleaned = set()
    for module in imports:
        if not is_valid_module(module):
            continue
        cleaned.add(normalize_module_name(module))
    return cleaned
# autodep/import_utils.py

import sys
import re

BUILTIN_MODULES = frozenset(sys.builtin_module_names)

# Simplified regex: matches modules starting with _ or __ or named builtins/dunder patterns
PRIVATE_OR_DUNDER = re.compile(r"^(_|__|builtins|__\w+__)$")

NORMALIZATION_MAP = {
    "PIL": {"PIL", "PIL.Image", "PIL.JpegImagePlugin", "PIL.TiffImagePlugin"},
    "OpenSSL": {"OpenSSL", "OpenSSL.SSL"},
    "IPython": {"IPython", "ipython"},
    "PyQt6": {"PyQt6"},
    "PySide6": {"PySide6"},
    "MySQLdb": {"MySQLdb", "_mysql"},
}

def normalize_module_name(module: str) -> str:
    if not module:
        return module
    for top_level, variants in NORMALIZATION_MAP.items():
        if module in variants:
            return top_level
    return module.split(".")[0]

def is_valid_module(module: str) -> bool:
    if not module:
        return False
    if module in BUILTIN_MODULES:
        return False
    if PRIVATE_OR_DUNDER.match(module):
        return False
    if module.startswith("_"):
        return False
    return True

def filter_and_normalize_imports(imports: set[str]) -> set[str]:
    cleaned = set()
    for module in imports:
        if not is_valid_module(module):
            continue
        cleaned.add(normalize_module_name(module))
    return cleaned
