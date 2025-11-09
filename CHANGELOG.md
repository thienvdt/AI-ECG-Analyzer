# 📋 Changelog - AI ECG Analyzer

## [Version 2.0] - Tháng 11, 2025

### ✨ Tính năng mới

#### 1. 🔑 Nhập API Key trực tiếp trên giao diện
- ✅ Người dùng có thể nhập API key ngay trên UI
- ✅ Không cần chỉnh sửa file cấu hình
- ✅ Hướng dẫn chi tiết ngay trong ứng dụng
- ✅ Collapsible instructions panel

#### 2. 💾 LocalStorage Integration  
- ✅ API key được lưu tự động trong trình duyệt
- ✅ Không mất API key khi refresh trang
- ✅ Lịch sử chat được lưu tự động
- ✅ Khôi phục chat history sau khi refresh

#### 3. 🎨 Giao diện Chat mới
**Cải tiến:**
- ✅ Tin nhắn người dùng: Gradient tím (bên phải)
- ✅ Tin nhắn bot: Gradient hồng/đỏ (bên trái)
- ✅ Avatar icons cho mỗi loại tin nhắn
- ✅ Bubble chat design hiện đại
- ✅ Thanh cuộn custom đẹp mắt
- ✅ Tự động cuộn đến tin nhắn mới nhất
- ✅ Max height 500px với scroll

**Buttons:**
- ✅ Nút "🚀 Hỏi Trợ lý Tim mạch" với primary styling
- ✅ Nút "🗑️ Xóa chat" để xóa lịch sử
- ✅ Nút "🗑️ Xóa" cho API key
- ✅ Hiển thị số lượng tin nhắn trong header

#### 4. 📝 Placeholder và Help Text
- ✅ Placeholder examples trong ô nhập câu hỏi
- ✅ Help text cho các trường input
- ✅ Tooltips cho các nút

### 🔧 Cải tiến kỹ thuật

#### API Key Management
- JavaScript functions cho localStorage operations
- Session state management
- Fallback về secrets.toml cho admin
- Clear API key functionality

#### Chat History
- JSON serialization cho chat messages
- Auto-save sau mỗi tin nhắn
- Load từ localStorage khi khởi động
- Clear history với confirmation

#### UI/UX
- Responsive 2-column layout cho buttons
- Better spacing và padding
- Gradient backgrounds cho messages
- Shadow effects cho depth
- Color-coded messages

### 📚 Tài liệu mới

1. **HUONG_DAN_API_KEY.md**
   - Hướng dẫn chi tiết lấy API key
   - FAQ đầy đủ
   - Troubleshooting guide

2. **QUICK_START_API.md**
   - Hướng dẫn nhanh 2 phút
   - Simple 3-step process

3. **HUONG_DAN_NGUOI_DUNG.md**
   - Hướng dẫn toàn diện cho người dùng cuối
   - Không cần kiến thức kỹ thuật

4. **HUONG_DAN_LOCALSTORAGE.md**
   - Giải thích tính năng localStorage
   - Hướng dẫn quản lý dữ liệu

5. **DANH_MUC_TAI_LIEU.md**
   - Index tất cả tài liệu
   - Quick reference guide

### 🐛 Bug Fixes

- ✅ Fixed Gemini model compatibility issues
- ✅ Updated model name to "gemini-pro-latest"
- ✅ Improved error handling for API calls
- ✅ Better error messages in Vietnamese

### 🔒 Security

- ✅ API key chỉ lưu client-side
- ✅ Không gửi API key qua network (trừ Google API)
- ✅ Clear data functionality
- ✅ Password-type input cho API key

### 💡 Best Practices

- ✅ Separation of concerns
- ✅ Clean code structure
- ✅ Comprehensive documentation
- ✅ User-friendly error messages
- ✅ Accessibility improvements

---

## [Version 1.0] - Initial Release

### Features
- ECG classification với AI
- File upload (.mat format)
- Sample ECG files
- Basic chatbot với fallback knowledge base
- Vietnamese interface

---

## 🚀 Upcoming Features (Roadmap)

### Version 2.1 (Planned)
- [ ] Export chat history to PDF
- [ ] Voice input for questions
- [ ] Multi-language support
- [ ] Dark mode
- [ ] Mobile responsive improvements

### Version 3.0 (Future)
- [ ] User accounts
- [ ] Cloud storage for chat history  
- [ ] Advanced ECG analysis features
- [ ] Integration with wearable devices
- [ ] Collaborative features

---

**Made with ❤️ by BS. Nguyễn Lê Hoài Linh**
