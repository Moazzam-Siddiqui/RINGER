from faster_whisper import WhisperModel

model = WhisperModel(
    "medium",
    device="cuda",
    compute_type="float16"
)

def transcribe_audio(audio_path):

    segments, info = model.transcribe(
        audio_path,
        language="en"
    )

    final_text = ""

    for segment in segments:
        final_text += segment.text

    return final_text

