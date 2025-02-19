import os

class Config:
    API_KEYS = {
        "chatgpt": os.getenv("CHATGPT_API_KEY"),
        "gemini": os.getenv("GEMINI_API_KEY"),
        "claude": os.getenv("CLAUDE_API_KEY"),
        "grok": os.getenv("GROK_API_KEY"),
    }
    
    BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
    DEBUG = os.getenv("DEBUG", "false").lower() in ("true", "1", "t")