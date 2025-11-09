# 🔑 Hướng dẫn Sử dụng Gemini API Key

## 📖 Giới thiệu

Để sử dụng tính năng **Trợ lý AI Tim mạch**, bạn cần có một API key miễn phí từ Google Gemini. Đây là hướng dẫn chi tiết từng bước.

---

## 🎯 Cách lấy API Key miễn phí (5 phút)

### Bước 1: Truy cập Google AI Studio

Mở trình duyệt và truy cập: **https://makersuite.google.com/app/apikey**

Hoặc: **https://aistudio.google.com/app/apikey**

### Bước 2: Đăng nhập Google

- Click vào nút **"Sign in"** hoặc **"Đăng nhập"**
- Đăng nhập bằng tài khoản Google của bạn
- Nếu chưa có tài khoản Google, tạo tài khoản miễn phí tại [accounts.google.com](https://accounts.google.com)

### Bước 3: Tạo API Key

1. Sau khi đăng nhập, bạn sẽ thấy trang **API Keys**
2. Click nút **"Create API key"** hoặc **"Get API key"**
3. Chọn một trong hai:
   - **Create API key in new project** (Tạo API key trong project mới) - Khuyến nghị cho người mới
   - **Create API key in existing project** (Tạo trong project có sẵn)
4. Click **"Create API key"**

### Bước 4: Copy API Key

- API key sẽ hiển thị dạng: `AIzaSyC...` (khoảng 39 ký tự)
- Click nút **"Copy"** để copy API key
- **LƯU Ý:** Lưu API key ở nơi an toàn, vì bạn có thể không xem lại được sau này

---

## 💻 Cách sử dụng API Key trong ứng dụng

### Cách 1: Nhập trực tiếp trên giao diện (Khuyến nghị)

1. Mở ứng dụng ECG Analyzer
2. Chuyển sang tab **"💬 Hỏi đáp Tim mạch"**
3. Tìm phần **"🔑 Cấu hình API Key"**
4. Nhấn vào **"📖 Hướng dẫn lấy API Key miễn phí"** để xem hướng dẫn
5. Paste API key vào ô **"Nhập Gemini API Key của bạn"**
6. Khi thấy thông báo ✅ "API key đã được cấu hình!", bạn đã sẵn sàng!

**Ưu điểm:**
- ✅ Dễ dàng, không cần chỉnh sửa file
- ✅ Mỗi người dùng có thể dùng API key riêng
- ✅ API key chỉ lưu trong phiên làm việc hiện tại

### Cách 2: Cấu hình trong file (Cho admin/developer)

Nếu bạn muốn cấu hình API key cố định cho toàn bộ ứng dụng:

1. Mở file `.streamlit/secrets.toml`
2. Thay đổi dòng:
   ```toml
   GEMINI_API_KEY = "YOUR_API_KEY_HERE"
   ```
   Thành:
   ```toml
   GEMINI_API_KEY = "AIzaSyC_your_actual_api_key_here"
   ```
3. Lưu file và khởi động lại ứng dụng

---

## ❓ Câu hỏi thường gặp

### 1. API key có mất phí không?

**Không!** API key hoàn toàn miễn phí với giới hạn sử dụng hợp lý:
- Khoảng 60 request/phút
- Khoảng 1,500 request/ngày

Đối với sử dụng cá nhân, giới hạn này là đủ.

### 2. API key có hết hạn không?

Không, API key không có thời hạn. Tuy nhiên, Google có thể thay đổi chính sách trong tương lai.

### 3. API key của tôi có an toàn không?

- ✅ Khi nhập trực tiếp trên giao diện, API key chỉ được lưu trong phiên làm việc của bạn
- ✅ Ứng dụng không gửi API key đến bất kỳ server nào khác ngoài Google
- ⚠️ Tuy nhiên, **không chia sẻ API key** với người khác

### 4. Tôi không thấy API key sau khi tạo?

Truy cập lại: https://makersuite.google.com/app/apikey
- Bạn sẽ thấy danh sách API keys đã tạo
- Nếu cần, tạo API key mới

### 5. Lỗi "API key not valid"?

**Nguyên nhân:**
- API key sai hoặc có khoảng trắng thừa
- API key chưa được kích hoạt (chờ vài phút)
- API key đã bị vô hiệu hóa

**Giải pháp:**
- Kiểm tra lại API key (copy đầy đủ, không có khoảng trắng)
- Tạo API key mới
- Thử lại sau vài phút

### 6. Lỗi "quota exceeded"?

Bạn đã vượt quá giới hạn sử dụng miễn phí:
- Chờ đến ngày hôm sau để quota reset
- Hoặc tạo API key mới với tài khoản Google khác

### 7. Chatbot không trả lời?

**Kiểm tra:**
1. ✅ Đã nhập API key chưa?
2. ✅ Có thông báo lỗi nào không?
3. ✅ Kết nối internet ổn định không?

Nếu vẫn lỗi, tạo API key mới.

---

## 🔒 Bảo mật API Key

### ✅ NÊN:
- Giữ API key cho riêng bạn
- Sử dụng API key cho mục đích cá nhân
- Tạo API key mới nếu nghi ngờ bị lộ

### ❌ KHÔNG NÊN:
- Chia sẻ API key trên mạng xã hội
- Commit API key lên GitHub/GitLab
- Chia sẻ API key với người lạ

---

## 📞 Hỗ trợ

Nếu gặp vấn đề:

1. **Đọc lại hướng dẫn** - Hầu hết vấn đề đều được giải quyết ở phần FAQ
2. **Tạo API key mới** - Đây là cách nhanh nhất khắc phục lỗi
3. **Kiểm tra kết nối internet** - Đảm bảo kết nối ổn định
4. **Liên hệ hỗ trợ** - Tạo issue trên GitHub repository

---

## 🎓 Video hướng dẫn

*(Tùy chọn: Bạn có thể thêm link video hướng dẫn ở đây)*

---

## 📚 Tài liệu tham khảo

- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [API Key Best Practices](https://support.google.com/googleapi/answer/6310037)

---

**Cập nhật:** Tháng 11, 2025

**Made with ❤️ for Healthcare AI**
