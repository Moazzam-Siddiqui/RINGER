from groq import Groq
from dotenv import load_dotenv
import os
from app.storage.save_chat import save_message
from app.agent.contact_manager import get_contact

load_dotenv()

groqi =os.getenv("GROQ2_API_KEY")

client = Groq(
    api_key = groqi
)

conversation_history = []

def generate_reply(message, caller_name="Unknown"):

    conversation_history.append(
        {
            "role": "user",
            "content": message
        }
    )
    contact = get_contact(caller_name)

    relation = contact["relation"]
    tone = contact["tone"]
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content": (
    f"You are Moazzam's AI phone assistant.\n"
    f"The caller is {caller_name}.\n"
    f"They are Moazzam's {relation}.\n"
    f"Speak in a {tone} tone.\n"
    f"Keep replies short and natural."
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
