from fastapi import FastAPI
from app.routers.mood import router as mood_router

app = FastAPI(
    title="AI Mood Analysis API",
    description="Analyze mood and emotions using AI",
    version="1.0.0"
)

app.include_router(mood_router)
