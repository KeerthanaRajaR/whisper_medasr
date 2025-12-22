def transcribe_medasr(audio_path, output_path):
    """
    Placeholder for MedASR transcription.
    Replace this with actual API / SDK call.
    """

    # Example: assume transcript returned from MedASR API
    medasr_transcript = """
    doctor: you have an infection in the lower right molar
    patient: i have pain but no swelling
    """

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(medasr_transcript)

    print("✅ MedASR transcription saved")
