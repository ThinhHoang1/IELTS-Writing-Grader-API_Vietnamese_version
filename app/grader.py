# app/grader.py

import re
from typing import Optional
import google.generativeai as genai
from .config import settings

# Cấu hình khóa API
genai.configure(api_key=settings.GEMINI_API_KEY)

# Định nghĩa các cài đặt an toàn và cấu hình tạo
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Khởi tạo mô hình tạo ngôn ngữ
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

# Khởi tạo phiên trò chuyện
chat_session = model.start_chat(history=[])

def check_essay(task: str, essay: str) -> str:
    """
    Kiểm tra bài luận về chính tả hoặc ngữ pháp.
    """
    message = f"{task} bài luận sau:\n\n{essay}"
    response = chat_session.send_message(message)
    return response.text.strip()

def grade_essay(title: str, essay: str) -> dict:
    """
    Chấm điểm bài luận và cung cấp phản hồi.
    """
    message = (
        f"Tiêu đề: {title}\n\n{essay}\n\n"
        "Vui lòng cung cấp một band điểm (0.0 - 9.0) cho bài luận IELTS này. "
        "Phản hồi nên bao gồm cụm từ 'Band Điểm: X.X'. "
        "Ngoài ra, hãy cung cấp phản hồi chi tiết dựa trên phản hồi nhiệm vụ, sự mạch lạc và liên kết, tài nguyên từ vựng, và phạm vi ngữ pháp, chính tả."
    )
    response = chat_session.send_message(message)
    feedback = response.text.strip()

    # Trích xuất band điểm bằng regex
    grade_match = re.search(
        r'(?:band\s*điểm|score|rating)[:\s]*(\d+(\.\d+)?)',
        feedback,
        re.IGNORECASE
    )
    if not grade_match:
        grade_match = re.search(
            r'(\d+(\.\d+)?)/9|(\d+(\.\d+)?)\s*dưới 9',
            feedback,
            re.IGNORECASE
        )
    grade_band = float(grade_match.group(1)) if grade_match else None

    # Đếm số từ
    word_count = len(essay.split())
    warning = None
    if word_count < 250:
        warning = 'Bài luận của bạn dưới số từ tối thiểu khuyến nghị cho IELTS (250 từ).'

    return {
        "feedback": feedback,
        "grade_band": grade_band,
        "word_count": word_count,
        "warning": warning
    }
