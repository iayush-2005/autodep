# cli.py
from autodep.main import run_autodep
import sys
from pathlib import Path


def main():
    # Read project path (interactive or via sys.argv)
    if len(sys.argv) > 1:
        project_path = Path(sys.argv[1])
    else:
        print("📁 Enter your project path:")
        project_path = Path(input("> ").strip())

    run_autodep(project_path)


if __name__ == "__main__":
    main()
