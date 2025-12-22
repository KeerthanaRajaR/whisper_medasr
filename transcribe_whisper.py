import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribe(audio_path, output_path):
    with open(audio_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3-turbo"
        )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"✅ Whisper transcription saved: {output_path}")
