# 📱 Hướng dẫn Sử dụng ECG Analyzer cho Người dùng Cuối

## 🎯 Giới thiệu

**ECG Analyzer** là ứng dụng phân tích điện tâm đồ (ECG) bằng AI, giúp bạn:
- ✅ Phân loại ECG tự động (Normal, Rung nhĩ, Khác, Nhiễu)
- 💬 Hỏi đáp về tim mạch với AI
- 📊 Trực quan hóa kết quả phân tích

---

## 🚀 Bắt đầu sử dụng

### Bước 1: Truy cập ứng dụng

Mở trình duyệt và truy cập URL ứng dụng (do quản trị viên cung cấp)

### Bước 2: Phân loại ECG

1. Click tab **"📊 Phân loại ECG"**
2. Tải lên file ECG (định dạng `.mat`)
   - Hoặc chọn file mẫu từ danh sách
3. Xem kết quả phân tích:
   - Loại nhịp tim
   - Độ tin cậy
   - Biểu đồ ECG
   - Phân bố xác suất

### Bước 3: Sử dụng Chatbot AI (Tùy chọn)

#### 3.1. Cấu hình API Key lần đầu

1. Click tab **"💬 Hỏi đáp Tim mạch"**
2. Xem phần **"🔑 Cấu hình API Key"**
3. Làm theo 3 bước:

**Bước 1:** Truy cập [Google AI Studio](https://makersuite.google.com/app/apikey)

**Bước 2:** 
- Đăng nhập Google (miễn phí)
- Click "Create API key"
- Copy API key (dạng: `AIzaSy...`)

**Bước 3:**
- Quay lại ứng dụng
- Paste API key vào ô "Nhập Gemini API Key"
- Thấy ✅ là thành công!

#### 3.2. Hỏi đáp với AI

1. Gõ câu hỏi vào ô **"Đặt câu hỏi về ECG..."**
2. Click **"Hỏi Trợ lý Tim mạch"**
3. Xem câu trả lời

**Hoặc** click vào các câu hỏi mẫu:
- ECG bình thường trông như thế nào?
- Làm thế nào để nhận biết rung nhĩ trên ECG?
- Khoảng QT là gì và tại sao nó quan trọng?

---

## 💡 Mẹo sử dụng

### Phân loại ECG hiệu quả

✅ **Nên:**
- Sử dụng file ECG chất lượng cao
- Kiểm tra file mẫu trước để hiểu cách hoạt động
- Đọc phần giải thích kết quả

❌ **Không nên:**
- Tin tưởng 100% vào kết quả AI
- Bỏ qua tư vấn bác sĩ
- Upload file ECG quá nhiễu

### Chatbot AI

✅ **Nên hỏi:**
- "ECG bình thường có đặc điểm gì?"
- "Rung nhĩ nguy hiểm như thế nào?"
- "Làm sao phân biệt P wave và T wave?"

❌ **Không nên hỏi:**
- Chẩn đoán bệnh cụ thể
- Hỏi thay cho khám bác sĩ
- Câu hỏi không liên quan tim mạch

---

## ❓ Câu hỏi thường gặp

### 1. Tôi có cần API key không?

**Không bắt buộc!** 
- Phân loại ECG: Không cần API key
- Chatbot AI: Cần API key (miễn phí)

### 2. API key có mất phí không?

**Hoàn toàn miễn phí!**
- Không cần thẻ tín dụng
- Giới hạn: ~60 câu hỏi/phút (đủ dùng)

### 3. API key có an toàn không?

**Có!**
- API key chỉ lưu trong phiên của bạn
- Không được chia sẻ với ai khác
- Không lưu trên server

### 4. Kết quả phân loại có chính xác không?

**Tham khảo!**
- Độ chính xác cao nhưng không 100%
- **LUÔN** tham khảo bác sĩ chuyên khoa
- Không tự chẩn đoán dựa vào kết quả

### 5. Tôi quên API key thì sao?

**Không sao!**
- Chỉ cần nhập lại mỗi lần mở ứng dụng
- Hoặc lấy API key mới (không giới hạn)

### 6. Lỗi "API key not valid"?

**Giải pháp:**
- Kiểm tra copy đầy đủ API key
- Không có khoảng trắng thừa
- Tạo API key mới nếu cần

---

## 🔒 Bảo mật & Quyền riêng tư

### Dữ liệu của bạn

✅ **An toàn:**
- File ECG chỉ xử lý trên trình duyệt
- Không upload lên server nào
- Không lưu trữ lâu dài

✅ **API Key:**
- Chỉ bạn biết
- Không chia sẻ với ứng dụng
- Truyền trực tiếp đến Google AI

### Khuyến nghị

⚠️ **LƯU Ý:**
- Không upload ECG có thông tin bệnh nhân
- Không chia sẻ API key
- Kết quả chỉ để tham khảo

---

## 📞 Hỗ trợ

### Gặp vấn đề?

1. **Đọc FAQ** - Hầu hết vấn đề đã có giải đáp
2. **Làm mới trang** - F5 hoặc Ctrl+R
3. **Thử lại** - Đôi khi chỉ cần thử lại
4. **Liên hệ** - Tạo issue trên GitHub

### Tài liệu

- 📖 [Hướng dẫn API Key chi tiết](HUONG_DAN_API_KEY.md)
- ⚡ [Hướng dẫn nhanh](QUICK_START_API.md)
- 🔧 [Khắc phục lỗi](KHAC_PHUC_LOI.md)

---

## ⚠️ Disclaimer

**QUAN TRỌNG:**

Ứng dụng này chỉ mang tính chất:
- ✅ Tham khảo
- ✅ Nghiên cứu
- ✅ Học tập

**KHÔNG:**
- ❌ Thay thế bác sĩ
- ❌ Chẩn đoán chính thức
- ❌ Kê đơn thuốc

**LUÔN** tham khảo bác sĩ chuyên khoa tim mạch cho bất kỳ vấn đề sức khỏe nào.

---

## 🎓 Học thêm

### Về ECG
- [ECG Library](https://ecglibrary.com/)
- [Life in the Fast Lane - ECG](https://litfl.com/ecg-library/)

### Về AI trong Y tế
- [Google Health AI](https://health.google/health-research/)
- [AI in Healthcare](https://www.nature.com/subjects/ai-in-healthcare)

---

**Phiên bản:** 1.0  
**Cập nhật:** Tháng 11, 2025  
**Made with ❤️ for Healthcare AI**
