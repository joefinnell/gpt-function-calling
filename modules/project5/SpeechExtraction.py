from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def get_text_from_speech(audio_file):
    audio_file = open(audio_file, "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )
    return transcript