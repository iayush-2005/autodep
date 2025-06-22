@echo off
echo 🚀 Starting autodep project...

IF NOT EXIST .venv (
    echo 📦 Creating virtual environment...
    python -m venv .venv
)

echo 🔒 Activating virtual environment...
call .venv\Scripts\activate.bat

echo ⬆️ Upgrading pip and installing project...
pip install --upgrade pip

IF EXIST requirements-dev.txt (
    pip install -r requirements-dev.txt
)

pip install -e .

echo 🎯 Running autodep CLI...
python -m autodep.cli
