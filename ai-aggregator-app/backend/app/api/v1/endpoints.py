from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services import chatgpt_service, gemini_service, claude_service, grok_service
from app.core.merge_responses import merge_responses

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

class AIResponse(BaseModel):
    model: str
    response: str

@router.post("/query", response_model=List[AIResponse])
async def query_ai_models(request: QueryRequest):
    try:
        chatgpt_response = await chatgpt_service.get_response(request.query)
        gemini_response = await gemini_service.get_response(request.query)
        claude_response = await claude_service.get_response(request.query)
        grok_response = await grok_service.get_response(request.query)

        responses = [
            AIResponse(model="ChatGPT", response=chatgpt_response),
            AIResponse(model="Gemini", response=gemini_response),
            AIResponse(model="Claude", response=claude_response),
            AIResponse(model="Grok", response=grok_response),
        ]

        merged_response = merge_responses(responses)
        return merged_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))