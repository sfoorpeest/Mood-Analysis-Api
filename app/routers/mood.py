from fastapi import APIRouter
from typing import List

from app.schemas.mood import MoodRequest, MoodResponse, MoodHistory
from app.services.mood_service import analyze_mood, get_mood_history

router = APIRouter(prefix="/api/mood", tags=["Mood Analysis"])


@router.post(
    "/analyze",
    response_model=MoodResponse,
    summary="Analyze mood from text"
)
def analyze(request: MoodRequest):
    return analyze_mood(request.text)


@router.get(
    "/history",
    response_model=List[MoodHistory],
    summary="Get mood analysis history"
)
def history(limit: int = 10):
    return get_mood_history(limit)
