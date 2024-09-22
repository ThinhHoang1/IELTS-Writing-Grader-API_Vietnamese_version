# IELTS-Writing-Grader-API_Vietnamese_version

Đây là một ứng dụng FastAPI cung cấp các endpoint để kiểm tra chính tả, ngữ pháp và chấm điểm bài luận IELTS sử dụng Google Generative AI, cùng với một chatbot trợ giúp học tiếng Anh.

## Cấu Trúc Dự Án

Dự án được tổ chức như sau:

#### ielts_grader_api/
#### ├── app/                    Chứa mã ứng dụng chính
#### │   ├── __init__.py         Khởi tạo package app 
#### │   ├── main.py             Điểm vào cho ứng dụng FastAPI
#### │   ├── models.py           Các mô hình dữ liệu cho API
#### │   ├── config.py           Cài đặt cấu hình 
#### │   ├── grader.py           Các hàm để kiểm tra và chấm điểm bài luận
#### │   └── chatbot.py          Các hàm để tương tác với chatbot trợ giúp học tiếng Anh
#### ├── .env                    Biến môi trường (ví dụ: API keys)
#### ├── requirements.txt        Các phụ thuộc của Python
#### └── README.md               Project documentation


## Tính Năng

- **Kiểm Tra Chính Tả:** Xác định và sửa lỗi chính tả trong bài luận.
- **Kiểm Tra Ngữ Pháp:** Xác định và sửa lỗi ngữ pháp trong bài luận.
- **Chấm Điểm Bài Luận:** Cung cấp band điểm và phản hồi chi tiết về bài luận.
- **Chat với Chatbot Trợ Giúp Học Tiếng Anh:** Thực hành hội thoại tiếng Anh với trợ lý AI.

## Yêu Cầu

- Python 3.9 trở lên
- pip (trình cài đặt gói Python)

## Cài Đặt

1. **Clone repository:**
 ```bash
git clone https://github.com/yourusername/ielts_grader_api.git
cd ielts_grader_api
```
## Cài đặt các phụ thuộc:
```bash
pip install -r requirements.txt
```

## Cài đặt biến môi trường:
Tạo một file .env trong thư mục gốc và thêm khóa API của Google Generative AI:
```python
GEMINI_API_KEY=your_api_key_here
```

## Để chạy ứng dụng FastAPI cục bộ, sử dụng Uvicorn:
```bash
uvicorn app.main:app --reload
```





