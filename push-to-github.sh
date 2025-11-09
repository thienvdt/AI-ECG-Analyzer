#!/bin/bash

# Script để push code lên GitHub repository mới
# Cách sử dụng: ./push-to-github.sh YOUR_GITHUB_USERNAME

echo "🚀 Đang chuẩn bị push code lên GitHub..."
echo ""

# Kiểm tra xem có truyền username không
if [ -z "$1" ]; then
    echo "⚠️  Vui lòng cung cấp GitHub username của bạn"
    echo "Cách dùng: ./push-to-github.sh YOUR_GITHUB_USERNAME"
    echo ""
    echo "Ví dụ: ./push-to-github.sh vatallus"
    exit 1
fi

GITHUB_USERNAME=$1
REPO_NAME="AI-ECG-Analyzer"

echo "📝 GitHub Username: $GITHUB_USERNAME"
echo "📦 Repository: $REPO_NAME"
echo ""

# Chuyển remote sang repository mới
echo "🔄 Đang thay đổi remote repository..."
git remote set-url origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

echo "✓ Remote đã được cập nhật"
echo ""

# Hiển thị remote mới
echo "📍 Remote repository hiện tại:"
git remote -v
echo ""

# Push code lên GitHub
echo "⬆️  Đang push code lên GitHub..."
echo ""

git push -u origin main

echo ""
if [ $? -eq 0 ]; then
    echo "✅ Push thành công!"
    echo ""
    echo "🎉 Repository của bạn:"
    echo "👉 https://github.com/$GITHUB_USERNAME/$REPO_NAME"
    echo ""
    echo "📋 Bạn có thể:"
    echo "   - Xem code tại: https://github.com/$GITHUB_USERNAME/$REPO_NAME"
    echo "   - Clone về: git clone https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"
    echo "   - Share với người khác"
else
    echo "❌ Có lỗi xảy ra khi push"
    echo ""
    echo "🔧 Kiểm tra lại:"
    echo "   1. Đã tạo repository 'AI-ECG-Analyzer' trên GitHub chưa?"
    echo "   2. Username GitHub có đúng không?"
    echo "   3. Đã đăng nhập Git chưa? (git config --global user.name)"
fi

