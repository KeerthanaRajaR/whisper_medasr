# metric/normalization.py
import re

def normalize_text(text):
    text = text.lower()

    text = re.sub(r"(doctor|patient)\s*[:,-]?", " ", text)
    text = re.sub(r"(euro trademark|a euro trademark|ia euro trademark)", " ", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text
