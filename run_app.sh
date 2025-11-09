#!/bin/bash

#!/bin/bash

# ========================================
# Script để chạy ECG Analyzer 
# Đã tối ưu cho macOS Apple Silicon (M1/M2/M3)
# ========================================

echo "🫀 ECG Analyzer - Starting Application..."
echo "========================================"

# Thiết lập các biến môi trường để khắc phục lỗi mutex lock
export KMP_DUPLICATE_LIB_OK=TRUE
export GRPC_ENABLE_FORK_SUPPORT=0
export GRPC_POLL_STRATEGY=poll
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

# Kích hoạt môi trường ảo
echo "✓ Activating virtual environment..."
if [ -d ".venv" ]; then
    source .venv/bin/activate
elif [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Please create one with: python3 -m venv .venv"
    exit 1
fi

# Kiểm tra dependencies
echo "✓ Checking dependencies..."
python -c "
try:
    import streamlit
    import google.generativeai
    import tensorflow as tf
    import scipy
    import numpy
    import matplotlib
    from src.visualization import plot_ecg
    print('  ✅ All dependencies installed')
    print('  TensorFlow version:', tf.__version__)
    print('  Streamlit version:', streamlit.__version__)
except ImportError as e:
    print(f'  ❌ Missing dependency: {e}')
    print('  Run: pip install -r requirements.txt')
    exit(1)
"

if [ $? -ne 0 ]; then
    exit 1
fi

# Kiểm tra API Key
if [ -f ".streamlit/secrets.toml" ]; then
    echo "✓ Google Gemini API key found"
else
    echo "⚠ Warning: No API key found. Chatbot will use limited knowledge base."
    echo "  To enable AI features, add your API key to .streamlit/secrets.toml"
fi

echo ""
echo "🚀 Starting Streamlit server..."
echo "🌐 Application will be available at: http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the application"
echo "========================================"
echo ""

# Chạy ứng dụng Streamlit
streamlit run app/main.py

# Nếu lỗi, thử với port khác
# streamlit run app/main.py --server.port 8502

