# Vigenere Cipher CLI Tool

## Giới thiệu

Đây là công cụ dòng lệnh (CLI) để mã hóa và giải mã văn bản bằng thuật toán Vigenere. Dự án giữ nguyên giao diện thân thiện giống bản Caesar, nhưng tập trung vào 2 chức năng chính: mã hóa và giải mã theo khóa chuỗi ký tự.

## Tính năng

- Mã hóa văn bản bằng thuật toán Vigenere với khóa chữ cái tùy ý
- Giải mã văn bản Vigenere với cùng khóa
- Brute-force gợi ý khóa/độ dài khóa (Kasiski + Index of Coincidence + phân tích tần suất)
- Nhập văn bản trực tiếp, từ stdin (pipe) hoặc từ file
- Giao diện dòng lệnh thân thiện, có tùy chọn copy ra clipboard / lưu file
- Xử lý chữ hoa thường, giữ nguyên ký tự không phải chữ cái

## Yêu cầu

- Python 3.7+ (được định nghĩa trong `pyproject.toml`)

## Cài đặt và chạy

1. **Cài đặt** (ở chế độ editable):
   ```bash
   pip install -e .
   ```

2. **Chạy chương trình**:
   ```bash
   vigenere
   ```

3. Làm theo hướng dẫn trên màn hình để nhập plaintext/ciphertext và khóa, hoặc thử brute-force nếu không biết khóa.

## Đóng góp

Mọi góp ý/đóng góp vui lòng tạo issue hoặc pull request.
