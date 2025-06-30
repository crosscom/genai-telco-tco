#!/bin/bash
# Installation script for GenAI Telco TCO Builder

set -e

echo "🚀 Installing GenAI Telco TCO Builder..."

# Check prerequisites
echo "📋 Checking prerequisites..."

# Check Python version
if ! python3 --version | grep -E "Python 3\.[8-9]|Python 3\.1[0-9]" > /dev/null; then
    echo "❌ Python 3.8+ required. Please install Python 3.8 or higher."
    exit 1
fi

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 not found. Please install pip3."
    exit 1
fi

# Check AWS CLI (optional but recommended)
if ! command -v aws &> /dev/null; then
    echo "⚠️  AWS CLI not found. Install AWS CLI for full functionality."
fi

# Check Amazon Q CLI
if ! command -v q &> /dev/null; then
    echo "❌ Amazon Q CLI not found. Please install Amazon Q CLI first."
    echo "   Visit: https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/cli-install.html"
    exit 1
fi

echo "✅ Prerequisites check passed"

# Install the package
echo "📦 Installing GenAI Telco TCO Builder..."

# If installing from source
if [ -f "setup.py" ]; then
    echo "Installing from source..."
    pip3 install -e .
else
    echo "Installing from PyPI..."
    pip3 install genai-telco-tco
fi

# Verify installation
echo "🔍 Verifying installation..."

if python3 -c "import genai_telco_tco; print('✅ Package imported successfully')" 2>/dev/null; then
    echo "✅ Installation successful!"
else
    echo "❌ Installation verification failed"
    exit 1
fi

# Test CLI integration
echo "🧪 Testing CLI integration..."

if q telco --help > /dev/null 2>&1; then
    echo "✅ Amazon Q CLI integration successful!"
else
    echo "⚠️  Amazon Q CLI integration not detected. You may need to restart your shell."
fi

echo ""
echo "🎉 GenAI Telco TCO Builder installation complete!"
echo ""
echo "📚 Quick Start:"
echo "   q telco build-tco --vcpu 96 --memory 384 --user-plane region --peak-bandwidth 10.0 --monthly-tonnage 1000"
echo ""
echo "📖 Documentation:"
echo "   q telco --help"
echo "   See docs/user-guide.md for detailed usage"
echo ""
echo "🔧 Examples:"
echo "   Check examples/ directory for sample configurations"