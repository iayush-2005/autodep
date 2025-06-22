#!/bin/bash

echo "🚀 Starting autodep project..."

# Step 1: Check if .venv exists
if [ ! -d ".venv" ]; then
  echo "📦 Creating virtual environment at .venv..."
  python3 -m venv .venv
else
  echo "✅ Virtual environment already exists."
fi

# Step 2: Activate venv
echo "🔒 Activating virtual environment..."
source .venv/bin/activate

# Step 3: Upgrade pip and install the project
echo "⬆️  Upgrading pip and installing project..."
pip install --upgrade pip

if [ -f "requirements-dev.txt" ]; then
  pip install -r requirements-dev.txt
fi

pip install -e .

# Step 4: Run autodep CLI
echo "🎯 Running autodep CLI..."
python -m autodep.cli

# Step 5: Done!
echo "✅ Done. Press Ctrl+C to exit if running in a loop."
