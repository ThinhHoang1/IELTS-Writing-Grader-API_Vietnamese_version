# app/chatbot.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Tải biến môi trường từ file .env
load_dotenv()

# Cấu hình khóa API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Khởi tạo mô hình tạo ngôn ngữ và phiên trò chuyện một lần
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest"
)
chat_session = model.start_chat(history=[])

def chat_with_assistant(message: str) -> str:
    """
    Gửi tin nhắn đến chatbot trợ giúp học tiếng Anh và trả về phản hồi.
    """
    try:
        # Gửi tin nhắn và nhận phản hồi
        response = chat_session.send_message(message)
        return response.text.strip()
    except Exception as e:
        return f"Lỗi: {str(e)}"
