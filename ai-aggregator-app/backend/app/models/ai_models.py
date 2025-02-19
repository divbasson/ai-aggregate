from pydantic import BaseModel
from typing import List, Optional

class AIRequest(BaseModel):
    query: str
    model: str

class AIResponse(BaseModel):
    model: str
    response: str
    confidence: Optional[float] = None

class AggregatedResponse(BaseModel):
    responses: List[AIResponse]
    best_response: AIResponse
    merged_text: str