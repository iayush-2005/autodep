import sys
import re

BUILTIN_MODULES = frozenset(sys.builtin_module_names)
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
    return bool(module) and not (
        module in BUILTIN_MODULES
        or PRIVATE_OR_DUNDER.match(module)
        or module.startswith("_")
    )


def filter_and_normalize_imports(imports: set[str]) -> set[str]:
    return {normalize_module_name(m) for m in imports if is_valid_module(m)}


def clean_import_name(module: str) -> str:
    return module.strip().split(".")[0]


import pytest
from autodep.import_utils import clean_import_name


def test_clean_import_name_basic():
    assert clean_import_name("numpy") == "numpy"


def test_clean_import_name_with_spaces():
    assert clean_import_name("  pandas  ") == "pandas"


def test_clean_import_name_with_dot():
    assert clean_import_name("sklearn.model_selection") == "sklearn"
