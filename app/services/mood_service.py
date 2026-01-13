from datetime import datetime
from typing import List

from app.schemas.mood import MoodHistory, MoodResponse
from app.services.ai_service import analyze_sentiment
_fake_history: List[MoodHistory] = []


def analyze_mood(text: str) -> MoodResponse:
    result = analyze_sentiment(text)

    history = MoodHistory(
        text=text,
        label=result["label"],
        score=result["score"],
        created_at=datetime.now()
    )

    _fake_history.insert(0, history)

    return MoodResponse(
        label=result["label"],
        score=result["score"]
    )


def get_mood_history(limit: int = 10) -> List[MoodHistory]:
    return _fake_history[:limit]
