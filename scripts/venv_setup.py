import os
import sys
import subprocess
import platform
from pathlib import Path
from autodep.logger import get_logger

logger = get_logger("venv_setup")


def find_project_root_with_venv(start_path: Path) -> Path | None:
    """Walk upwards from start_path to locate a `.venv` directory."""
    current = start_path.resolve()
    while current != current.parent:
        if (current / '.venv').is_dir():
            return current
        current = current.parent
    return None


def create_venv_at(project_root: Path) -> Path:
    """Create a new .venv at the project root if it doesn't exist."""
    venv_path = project_root / '.venv'
    logger.info("➕ Creating virtual environment at: %s", venv_path)
    subprocess.check_call([sys.executable, '-m', 'venv', str(venv_path)])
    return venv_path


def get_venv_python(venv_path: Path) -> str:
    """Get path to the python executable in the venv."""
    return str(venv_path / ("Scripts" if platform.system() == "Windows" else "bin") / "python")


def main():
    cwd = Path.cwd()
    logger.info("🔍 Searching for .venv from: %s", cwd)

    project_root = find_project_root_with_venv(cwd)

    if project_root:
        logger.info("✅ Found existing .venv at: %s", project_root / ".venv")
    else:
        logger.warning("⚠️  No .venv found. Assuming current directory is project root.")
        project_root = cwd
        create_venv_at(project_root)

    venv_python = get_venv_python(project_root / ".venv")

    cli_entry = Path(__file__).parent.parent / "cli.py"
    logger.info("🚀 Launching CLI from: %s", cli_entry)
    subprocess.run([venv_python, str(cli_entry)], check=True)


if __name__ == "__main__":
    main()
