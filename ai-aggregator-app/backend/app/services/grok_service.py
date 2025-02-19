from fastapi import HTTPException
import requests

class GrokService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.grok.ai/v1"  # Replace with the actual Grok API base URL

    def query_grok(self, prompt: str):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": prompt
        }
        
        try:
            response = requests.post(f"{self.base_url}/query", json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise HTTPException(status_code=response.status_code, detail=str(http_err))
        except Exception as err:
            raise HTTPException(status_code=500, detail=str(err))