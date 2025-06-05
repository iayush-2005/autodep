# autodep/installer.py

import subprocess
import sys
import os

def in_virtualenv() -> bool:
    """Check if running inside a virtual environment."""
    return (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )

def get_pip_executable() -> str:
    """
    Return path to pip executable based on environment.
    If inside venv, use venv's pip, else fallback to 'pip' command.
    """
    if in_virtualenv():
        base_dir = os.path.dirname(sys.executable)
        pip_name = "pip.exe" if os.name == "nt" else "pip"
        pip_path = os.path.join(base_dir, pip_name)
        return pip_path
    else:
        print("⚠️ Warning: Not inside a virtual environment.")
        print("   It's recommended to use manage_venv.py to run this tool safely.")
        return "pip"

def install_module(module_name: str, pip_cmd: str) -> bool:
    """
    Install a Python module using the specified pip command.
    Returns True if successful, else False.
    """
    print(f"[+] Attempting to install: {module_name}")
    try:
        result = subprocess.run(
            [pip_cmd, "install", module_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[x] Failed to install {module_name}:\n{e.stderr}")
        return False

def install_missing_modules(modules: list[str]) -> list[str]:
    """
    Install all missing modules using the appropriate pip.
    Returns list of modules installed successfully.
    """
    pip_cmd = get_pip_executable()
    newly_installed = []

    for module in modules:
        if install_module(module, pip_cmd):
            newly_installed.append(module)

    if newly_installed:
        print("\n🚀 Newly installed modules:")
        for mod in newly_installed:
            print(f"  ✔ {mod}")

    return newly_installed

def export_requirements(project_path: str):
    """
    Save the installed packages in the current venv to requirements.txt
    """
    req_file = os.path.join(project_path, "requirements.txt")
    try:
        with open(req_file, "w") as f:
            subprocess.run(
                [get_pip_executable(), "freeze"],
                stdout=f,
                check=True
            )
        print(f"\n📦 Saved requirements to {req_file}")
    except Exception as e:
        print(f"[!] Failed to generate requirements.txt: {e}")
