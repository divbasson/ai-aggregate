from fastapi import HTTPException
import requests

class GeminiService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.gemini.com/v1"

    def query_gemini(self, prompt: str):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150
        }
        
        response = requests.post(f"{self.base_url}/generate", json=payload, headers=headers)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json().get("error", "Unknown error"))

        return response.json().get("data", {}).get("text", "")