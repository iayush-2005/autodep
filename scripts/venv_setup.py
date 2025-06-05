import os
import sys
import subprocess
import platform
from pathlib import Path

def find_or_create_venv(project_path: Path) -> Path:
    """Search for existing .venv in the project tree, or create one at root."""
    for root, dirs, _ in os.walk(project_path):
        if '.venv' in dirs:
            return Path(root) / '.venv'

    # Create .venv at root if none found
    venv_path = project_path / '.venv'
    print(f"[+] No .venv found. Creating one at {venv_path}...")
    subprocess.check_call([sys.executable, '-m', 'venv', str(venv_path)])
    return venv_path

def get_venv_python(venv_path: Path) -> str:
    if platform.system() == "Windows":
        return str(venv_path / "Scripts" / "python.exe")
    else:
        return str(venv_path / "bin" / "python")

def main():
    print("📁 Enter your project path:")
    project_path_input = input("> ").strip()
    project_path = Path(project_path_input).resolve()

    if not project_path.exists() or not project_path.is_dir():
        print("❌ Invalid project path.")
        sys.exit(1)

    venv_path = find_or_create_venv(project_path)
    venv_python = get_venv_python(venv_path)

    main_script = Path(__file__).parent.parent / "main.py"
    if not main_script.exists():
        print("❌ main.py not found.")
        sys.exit(1)

    print(f"\n🚀 Running main.py inside venv: {venv_python}\n")
    subprocess.run([venv_python, str(main_script), str(project_path)])

if __name__ == "__main__":
    main()
