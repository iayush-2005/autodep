# autodetect_deps/installer.py

import subprocess

def install_module(module_name: str) -> bool:
    """
    Attempts to install a module using pip and 
    return True if installed successfully, False otherwise
    """
    print(f"[+] Attempting to install: {module_name}")
    try:
        result = subprocess.run(
            ["pip", "install", module_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            print(f"[✓] Successfully installed: {module_name}")
            return True
        else:
            print(f"[x] Failed to install {module_name}:\n{result.stderr}")
            return False
    except Exception as e:
        print(f"[!] Error while installing {module_name}: {e}")
        return False

def install_missing_modules(modules: set[str]) -> list[str]:
    """
    Installs all missing modules and 
    returns a list of successfully installed ones
    """
    installed = []
    for module in modules:
        if install_module(module):
            installed.append(module)
    return installed
