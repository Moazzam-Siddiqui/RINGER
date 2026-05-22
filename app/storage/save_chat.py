import json

def save_message(role, content):

    data = {
        "role": role,
        "content": content
    }

    with open("transcripts/chat_history.txt", "a") as file:

        file.write(json.dumps(data) + "\n")
