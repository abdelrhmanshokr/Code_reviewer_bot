from typing import List, Optional
from pydantic import BaseModel


class ReviewRequest(BaseModel):
    language: Optional[str] = "python"
    intent: Optional[str] = None
    code: str


class Improvement(BaseModel):
    title: str
    explanation: str
    suggested_change: Optional[str] = None
    priority: str


class ReviewResponse(BaseModel):
    improvements: List[Improvement]
    positive_note: str
