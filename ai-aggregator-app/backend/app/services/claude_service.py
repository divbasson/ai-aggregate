from fastapi import HTTPException
import requests

class ClaudeService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://api.anthropic.com/v1/claude"

    def generate_response(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150
        }

        response = requests.post(self.api_url, headers=headers, json=payload)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())

        return response.json().get("completion", "").strip()