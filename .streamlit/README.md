# 🔑 Cấu hình API Key (Tùy chọn)

## Cho người dùng cuối

**Bạn KHÔNG cần chỉnh sửa file này!**

Thay vào đó:
1. Mở ứng dụng
2. Chuyển sang tab "💬 Hỏi đáp Tim mạch"
3. Nhập API key trực tiếp trên giao diện

📖 **Hướng dẫn:** [HUONG_DAN_API_KEY.md](../HUONG_DAN_API_KEY.md)

---

## Cho quản trị viên

Nếu bạn muốn cấu hình API key mặc định cho toàn hệ thống:

1. Mở file `secrets.toml`
2. Thay đổi:
   ```toml
   GEMINI_API_KEY = "YOUR_API_KEY_HERE"
   ```
   Thành:
   ```toml
   GEMINI_API_KEY = "AIzaSyC_your_actual_api_key_here"
   ```
3. Lưu file và restart ứng dụng

⚠️ **Lưu ý:** Không commit file secrets.toml lên Git!
