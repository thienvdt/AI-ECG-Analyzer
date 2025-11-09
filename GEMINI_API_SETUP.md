# 🔑 Hướng dẫn thiết lập Gemini API Key

## Bước 1: Lấy API Key miễn phí

1. Truy cập: https://makersuite.google.com/app/apikey
2. Đăng nhập bằng tài khoản Google của bạn
3. Nhấn "Create API key" 
4. Chọn project hoặc tạo project mới
5. Copy API key (bắt đầu bằng "AIza...")

## Bước 2: Cấu hình API Key

1. Mở file `.streamlit/secrets.toml` trong thư mục dự án
2. Thay thế `YOUR_API_KEY_HERE` bằng API key thật của bạn:

```toml
GEMINI_API_KEY = "AIzaSyC_your_actual_api_key_here"
```

## Bước 3: Khởi động lại ứng dụng

```bash
# Dừng ứng dụng (Ctrl+C) và chạy lại
streamlit run app/main.py
```

## ⚠️ Lưu ý quan trọng

- **Không chia sẻ** API key với người khác
- **Không commit** file secrets.toml lên Git/GitHub
- API key có giới hạn sử dụng miễn phí hàng tháng
- Nếu vượt quá giới hạn, bạn cần đăng ký gói trả phí

## 🔧 Khắc phục lỗi thường gặp

### Lỗi "API key not valid"
- Kiểm tra API key có đúng format không (bắt đầu bằng "AIza")
- Tạo API key mới nếu key cũ không hoạt động
- Đảm bảo không có khoảng trắng thừa trong file secrets.toml

### Lỗi "quota exceeded"  
- Bạn đã sử dụng hết giới hạn miễn phí
- Chờ đến tháng tiếp theo hoặc nâng cấp gói trả phí

### Chatbot không hoạt động
- Kiểm tra file `.streamlit/secrets.toml` có tồn tại không
- Restart ứng dụng Streamlit sau khi thay đổi API key
- Kiểm tra kết nối internet

## 💡 Mẹo sử dụng

- API miễn phí có giới hạn số lần gọi mỗi phút
- Nên sử dụng câu hỏi cụ thể để tiết kiệm quota
- Có thể sử dụng ứng dụng mà không cần API key (chỉ mất tính năng chat)

## 📞 Hỗ trợ

Nếu vẫn gặp lỗi, vui lòng tạo issue trên GitHub với thông tin:
- Thông báo lỗi chi tiết
- Hệ điều hành đang sử dụng
- Phiên bản Python
