import subprocess
from pathlib import Path

def test_autodep_cli_runs():
    result = subprocess.run(["python", "-m", "autodep.cli"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "🔍" in result.stdout or "Scanning" in result.stdout
