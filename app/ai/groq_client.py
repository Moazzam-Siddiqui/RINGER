from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

os.getenv("GROQ2_API_KEY")

client = Groq(
    api_key=os.getenv("GROQ2_API_KEY")
)


def generate_reply(message):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are Moazzam's AI phone assistant. "
                    "Talk casually and briefly."
                )
            },

            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content