# app/models.py

from pydantic import BaseModel, Field
from typing import Optional

class EssayInput(BaseModel):
    title: Optional[str] = Field(None, example="Tác Động Của Công Nghệ Đến Giáo Dục")
    essay: str = Field(..., example="Nội dung bài luận IELTS của bạn ở đây.")

class CheckResponse(BaseModel):
    result: str

class GradeResponse(BaseModel):
    feedback: str
    grade_band: Optional[float] = None
    word_count: int
    warning: Optional[str] = None

class ChatInput(BaseModel):
    message: str = Field(..., example="Chào bạn, làm thế nào để tôi có thể nâng cao kỹ năng viết tiếng Anh?")

class ChatResponse(BaseModel):
    response: str
