from fastapi import APIRouter, HTTPException
from typing import Any

from .models import ReviewRequest, ReviewResponse, Improvement
from ..core.rule_engine import RuleEngine
from ..ai.review_generator import generate_review

router = APIRouter()


@router.get("/health")
def health() -> Any:
    return {"status": "ok"}


@router.get("/rules")
def get_rules() -> Any:
    engine = RuleEngine()
    return engine.get_all_rules()


@router.post("/review", response_model=ReviewResponse)
def review_snippet(req: ReviewRequest):
    if not req.code or len(req.code.strip()) == 0:
        raise HTTPException(status_code=400, detail="`code` is required in the request body")

    # For now use the deterministic stub generator
    result = generate_review(req.code, language=req.language or "python")

    # Normalize to expected response model
    improvements = [Improvement(**i) for i in result.get("improvements", [])]
    positive = result.get("positive_note", "")
    return ReviewResponse(improvements=improvements, positive_note=positive)
