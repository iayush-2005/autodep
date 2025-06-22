import importlib.util


def is_module_installed(module_name: str) -> bool:
    return importlib.util.find_spec(module_name) is not None


def get_missing_modules(modules: set[str]) -> list[str]:
    return [m for m in modules if not is_module_installed(m)]


def detect_missing_modules(imports: set[str]) -> set[str]:
    return {m for m in imports if not is_module_installed(m)}
