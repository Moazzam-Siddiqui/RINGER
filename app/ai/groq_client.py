from groq import Groq
from dotenv import load_dotenv
import os
from app.storage.save_chat import save_message

load_dotenv()

groqi =os.getenv("GROQ2_API_KEY")

client = Groq(
    api_key = groqi
)

conversation_history = []

def generate_reply(message):

    conversation_history.append(
        {
            "role": "user",
            "content": message
        }
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are Moazzam's AI phone assistant. "
                    "Talk casually and briefly."
                )
            }
        ] + conversation_history
    )

    ai_reply = response.choices[0].message.content
    save_message("assistant", ai_reply)

    conversation_history.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )
    save_message("user", message)

    return ai_reply
