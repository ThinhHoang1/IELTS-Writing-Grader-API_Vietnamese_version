# app/config.py

import os
from dotenv import load_dotenv

# Tải biến môi trường từ file .env
load_dotenv()

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")

settings = Settings()
