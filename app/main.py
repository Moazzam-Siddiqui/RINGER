from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.routes.audio import router as audio_router
from app.routes.voice_agent import router as voice_router

app = FastAPI()
app.include_router(audio_router)
app.include_router(chat_router)
app.include_router(voice_router)

@app.get("/")
async def root():
    return {"message": "Ringer Running"}
