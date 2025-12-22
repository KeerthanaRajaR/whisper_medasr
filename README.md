## Whisper vs MedASR ASR Evaluation Pipeline

## Overview

This project implements an end-to-end Automatic Speech Recognition (ASR) evaluation pipeline to compare Whisper and MedASR on realistic medical (dental) conversations.
The goal is to evaluate transcription quality using standard ASR metrics and clinical safety–oriented metrics.

The pipeline supports:

Audio generation

Transcription using Whisper and MedASR

Metric-based comparison between ASR outputs

## PROJECT STRUCTURE
```bash
WHISPERMEDASR/
│
├── audio/
│   └── convo1.wav
│
├── conversations/
│   └── convo1_reference.txt
│
├── metric/
│   ├── wer_cer_ser.py
│   ├── medical_terms.py
│   ├── medication_accuracy.py
│   ├── numeric_accuracy.py
│   ├── laterality_negation.py
│   └── __pycache__/
│
├── transcripts/
│   ├── whisper/
│   │   └── convo1.txt
│   └── medasr/
│       └── convo1.txt
│
├── generate_audio.py
├── transcribe_whisper.py
├── transcribe_medasr.py
├── run_compare_all.py
├── requirements.txt
├── .gitignore
└── README.md
```

## SETUP INSTRUCTIONS
1. Clone the repository:
   ```bash
   git clone
    cd WHISPERMEDASR
    ```
2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt     
    ```
4. Download and set up Whisper and MedASR models as per their respective documentation.
5. Prepare your audio files and reference transcripts in the `audio/` and `conversations/` directories.
6. Run the evaluation pipeline:
    ```bash
    python run_compare_all.py
    ```
## USAGE
- To generate audio from text conversations, use:
    ```bash
    python generate_audio.py
    ```
- To    transcribe audio using Whisper, use:
    ```bash
    python transcribe_whisper.py --input_dir audio/ --output_dir transcripts/whisper/
    ```     