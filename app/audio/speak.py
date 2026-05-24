from gtts import gTTS

def text_to_speech(text):

    tts = gTTS(
        text=text,
        lang="en"
    )

    output_path = "recordings/ai_reply.mp3"

    tts.save(output_path)

    return output_path
