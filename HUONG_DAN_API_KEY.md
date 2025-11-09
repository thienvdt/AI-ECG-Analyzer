# 🔑 Hướng dẫn sử dụng Gemini API Key (cách mới khuyến nghị)

Từ bản cập nhật 11/2025, ứng dụng hỗ trợ cấu hình API key trực tiếp trong giao diện, an toàn và nhanh chóng. Bạn không cần sửa file nếu dùng cách này.

---

## 1) Tạo API key miễn phí (3–5 phút)

- Trang chính thức: https://aistudio.google.com/app/apikey  
- Link cũ (vẫn hoạt động): https://makersuite.google.com/app/apikey

Các bước:
1. Đăng nhập tài khoản Google (Sign in).
2. Ở mục API keys, bấm Create API key hoặc Get API key.
3. Chọn “Create API key in new project” (khuyến nghị) và xác nhận.
4. Copy API key (bắt đầu bằng AIza...). Hãy giữ kín API key của bạn.

---

## 2) Cấu hình API key trực tiếp trong ứng dụng (UI)

1. Mở ứng dụng ECG Analyzer, chuyển sang tab “💬 Hỏi đáp Tim mạch”.
2. Ở thanh trên cùng của tab:
   - Bấm nút 🔑 để mở ô nhập API key, hoặc
   - Bấm nút ❓ để mở trang hướng dẫn này (mở tab mới).
3. Mở phần “🔑 Cấu hình API Key”, dán API key vào ô “Nhập Gemini API Key:”.
4. Sau khi nhập, ứng dụng hiển thị ✅ “API key đã được cấu hình”. Bạn có thể bắt đầu chat.

Ghi chú an toàn:
- API key được lưu cục bộ trong trình duyệt của bạn (localStorage). Ứng dụng không gửi key đi nơi khác ngoài Google.
- Bạn có thể xóa key bất kỳ lúc nào bằng nút 🗑️ ở góc phải thanh cấu hình.

---

## 3) Xoá/Đổi API key

- Bấm 🗑️ để xóa key hiện tại (key trên trình duyệt cũng bị xóa).
- Bấm 🔑 để nhập key mới và dán giá trị bạn vừa tạo từ AI Studio.

---

## 4) Ứng dụng tự phát hiện lỗi API key và cách khắc phục

Ứng dụng đã tích hợp bắt lỗi và hướng dẫn trực tiếp:

- 403 Your API key was reported as leaked
  - Ứng dụng tự động xoá key khỏi phiên và mở ô nhập.
  - Cách khắc phục: Tạo API key mới tại https://aistudio.google.com/app/apikey rồi dán lại. Tránh chia sẻ công khai.

- API key not valid / invalid API key
  - Key sai hoặc hết hiệu lực. Hãy tạo key mới và nhập lại.

- Quota exceeded
  - Đã vượt giới hạn dùng miễn phí. Hãy chờ reset (thường theo ngày) hoặc dùng tài khoản Google khác để tạo key mới.

Mẹo: Nếu bạn dán key nhưng vẫn lỗi, hãy xoá khoảng trắng thừa, chắc chắn copy đủ toàn bộ ký tự và thử lại.

---

## 5) Cách cũ (tuỳ chọn cho quản trị viên/dev): cấu hình qua file secrets

Bạn vẫn có thể cấu hình key dùng chung cho server:

1. Tạo file `.streamlit/secrets.toml` (nếu chưa có).
2. Thêm:
   ```toml
   GEMINI_API_KEY = "YOUR_API_KEY_HERE"
   ```
3. Khởi động lại ứng dụng.

Lưu ý:
- Khi có cả key trong `secrets` và key người dùng nhập trên giao diện, ứng dụng ưu tiên key người dùng.
- Trên môi trường deploy, hãy quản lý secrets qua cơ chế bảo mật của nền tảng (không commit lên Git).

---

## 6) Câu hỏi thường gặp (FAQ)

- API key có mất phí?  
  Không. Google cung cấp hạn mức miễn phí phù hợp cho sử dụng cá nhân/thử nghiệm.

- API key có hết hạn?  
  Không có hạn cứng, nhưng chính sách có thể thay đổi. Bạn có thể thu hồi/đổi key bất cứ lúc nào.

- Tôi muốn xoá toàn bộ dấu vết key và lịch sử chat?  
  Bấm 🗑️ để xoá key. Với lịch sử chat, dùng nút “🗑️ Xóa” trong khu vực chat.

- Vì sao nên dùng cách mới qua giao diện?  
  Không cần sửa file, mỗi người dùng có key riêng, nhanh và an toàn (lưu cục bộ trên trình duyệt).

---

## 7) Thực hành bảo mật cơ bản

- Không chia sẻ API key công khai hoặc commit lên Git.
- Thu hồi và tạo key mới nếu nghi ngờ bị lộ (ứng dụng sẽ cảnh báo và yêu cầu bạn nhập key mới nếu phát hiện vấn đề).
- Dùng key riêng cho từng người dùng/từng ứng dụng khi có thể.

---

Cập nhật: 11/2025  
Made with ❤️ for Healthcare AI
