#!/bin/bash

echo "🚀 Setting up your Python project environment..."

# Step 1: Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Step 2: Activate virtual environment
echo "⚙️ Activating virtual environment..."
source venv/bin/activate

# Step 3: Upgrade pip
echo "⬆️ Upgrading pip..."
pip3 install --upgrade pip

# Step 4: Install dependencies
echo "📚 Installing required packages..."
pip3 install Pillow selenium

# Step 5: Create requirements.txt for reproducibility
echo "📝 Freezing requirements to requirements.txt..."
pip3 freeze > requirements.txt

# Step 6: Final message
echo
echo "✅ Setup complete!"
echo "👉 To activate the environment later, run:"
echo "   source venv/bin/activate"
echo
echo "⚠️  NOTE: Selenium is installed, but you still need to have Firefox and Geckodriver installed on your system."
echo "🔗 Download Geckodriver: https://github.com/mozilla/geckodriver/releases"

# macOS-specific suggestion
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "💡 On macOS, you can install Geckodriver with Homebrew:"
    echo "   brew install geckodriver"
fi
