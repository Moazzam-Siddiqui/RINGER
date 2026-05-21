from fastapi import APIRouter
from app.ai.groq_client import generate_reply

router = APIRouter()

@router.get("/chat")
async def chat(message: str):

    ai_reply = generate_reply(message)

    return {
        "user": message,
        "ai": ai_reply
    }
