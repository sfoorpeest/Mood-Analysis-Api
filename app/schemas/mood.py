from pydantic import BaseModel
from datetime import datetime

class MoodRequest(BaseModel):
    text: str


class MoodResponse(BaseModel):
    label: str
    score: float


class MoodHistory(BaseModel):
    text: str
    label: str
    score: float
    created_at: datetime
