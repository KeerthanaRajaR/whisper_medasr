from pathlib import Path

# =============================
# Transcription backends
# =============================
from transcribe_whisper import transcribe as whisper_transcribe
from transcribe_medasr import transcribe_medasr



# =============================
# Core ASR & clinical metrics (modules)
# =============================
from metric import (
    wer_cer_ser,
    medical_terms,
    medication_accuracy,
    numeric_accuracy,
    laterality_negation,
)

# =============================
# Structure & semantic metrics (functions)
# =============================

# =============================
# System & operational metrics (functions)
# =============================




# =============================
# CONFIG
# =============================
FAST_MODE = True
MODELS = ["whisper", "medasr"]
CONVERSATIONS = [1]   # one conversation (as requested)

Path("transcripts/whisper").mkdir(parents=True, exist_ok=True)
Path("transcripts/medasr").mkdir(parents=True, exist_ok=True)

# =============================
# RUN PIPELINE
# =============================
for cid in CONVERSATIONS:
    print(f"\n🔍 Conversation {cid}")

    audio_path = f"audio/convo{cid}.wav"
    ref_path = f"conversations/convo{cid}_reference.txt"

    for model in MODELS:
        print(f"\n📊 MODEL: {model.upper()}")

        transcript_path = f"transcripts/{model}/convo{cid}.txt"

        # -------- Transcription --------
        if FAST_MODE and Path(transcript_path).exists():
            print("⚡ FAST MODE: Using existing transcript")
        else:
            if model == "whisper":
                whisper_transcribe(audio_path, transcript_path)
            else:
                transcribe_medasr(audio_path, transcript_path)

        # -------- Core ASR metrics --------
        wer_cer_ser.run_custom(ref_path, transcript_path)
        medical_terms.run_custom(ref_path, transcript_path)
        medication_accuracy.run_custom(ref_path, transcript_path)
        numeric_accuracy.run_custom(ref_path, transcript_path)
        laterality_negation.run_custom(ref_path, transcript_path)
        laterality_negation.run_negation_custom(ref_path, transcript_path)

        
        
       
        print("-" * 60)

# =============================
# System-level metrics (once)
# =============================


print("\n✅ WHISPER vs MEDASR COMPARISON COMPLETED")
