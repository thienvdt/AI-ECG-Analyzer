#!/bin/bash

# ECG Analyzer - Run Script
# Chạy ứng dụng ECG Analyzer với môi trường đã cấu hình

echo "🫀 Starting ECG Analyzer..."
echo "📂 Working directory: $(pwd)"

# Activate virtual environment and run the app
export KMP_DUPLICATE_LIB_OK=TRUE

# Kiểm tra môi trường ảo
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first."
    echo "Run: python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

echo "🔧 Using virtual environment..."
echo "🌐 Starting Streamlit app..."
echo "📱 App will open at: http://localhost:8501"
echo ""
echo "💡 Tips:"
echo "   - To stop: Press Ctrl+C"
echo "   - To configure Gemini API: Edit .streamlit/secrets.toml"
echo "   - See GEMINI_API_SETUP.md for detailed API setup instructions"
echo ""

# Run the application
.venv/bin/streamlit run app/main.py
