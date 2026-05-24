from fastapi import APIRouter

from app.audio.transcribe import transcribe_audio
from app.ai.groq_client import generate_reply
from app.audio.speak import text_to_speech

router = APIRouter()

@router.get("/voice-agent")
async def voice_agent():

    user_text = transcribe_audio(
        "recordings/test.mp3"
    )

    ai_reply = generate_reply(
    user_text,
    caller_name=" rahul "
)
    audio_path = text_to_speech(ai_reply)

    return {
    "transcription": user_text,
    "ai_reply": ai_reply,
    "audio_file": audio_path
}
