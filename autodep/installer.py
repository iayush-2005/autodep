import subprocess
import sys
import os


def in_virtualenv() -> bool:
    return hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )


def install_missing_modules(modules: list[str]) -> bool:
    print(f"\n📦 Installing {len(modules)} modules...\n")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", *modules])
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install some modules.")
        return False


def export_requirements(project_path: str):
    print("\n📜 Exporting requirements.txt")
    try:
        with open(os.path.join(project_path, "requirements.txt"), "w") as f:
            subprocess.run(
                [sys.executable, "-m", "pip", "freeze"], stdout=f, check=True
            )
        print("✅ requirements.txt generated successfully.")
    except Exception as e:
        print(f"❌ Failed to generate requirements.txt: {e}")
