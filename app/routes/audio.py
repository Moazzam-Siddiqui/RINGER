from fastapi import APIRouter
from app.audio.transcribe import transcribe_audio

router = APIRouter()

@router.get("/transcribe")
async def transcribe():

    text = transcribe_audio("recordings/test.mp3")

    return {
        "transcription": text
    }
