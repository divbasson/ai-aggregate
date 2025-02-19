from fastapi import HTTPException
import requests
from app.core.config import settings

class ChatGPTService:
    def __init__(self):
        self.api_url = settings.CHATGPT_API_URL
        self.api_key = settings.CHATGPT_API_KEY

    def send_request(self, prompt: str):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(self.api_url, headers=headers, json=data)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        return response.json()

    def process_response(self, response_data):
        return response_data.get("choices", [{}])[0].get("message", {}).get("content", "")