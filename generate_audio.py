import pyttsx3
from pathlib import Path

engine = pyttsx3.init()
engine.setProperty('rate', 150)

text = Path("conversations/convo1_reference.txt").read_text()
engine.save_to_file(text, "audio/convo1.wav")
engine.runAndWait()
