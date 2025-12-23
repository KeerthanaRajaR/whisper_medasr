from pathlib import Path

# -----------------------------
# Transcription backends
# -----------------------------
from transcribe_whisper import transcribe as whisper_transcribe
from transcribe_medasr import transcribe_medasr

# -----------------------------
# Core ASR & clinical metrics
# -----------------------------
from metric.wer_cer_ser import run_custom as wer_cer_ser
from metric.medical_terms import run_custom as medical_terms
from metric.medication_accuracy import run_custom as medication_accuracy
from metric.numeric_accuracy import run_custom as numeric_accuracy
from metric.laterality_negation import (
    run_laterality_custom,
    run_negation_custom
)

# -----------------------------
# Semantic & clinical metrics
# -----------------------------
from metric.semantic_clinical import (
    clinical_coherence_score_run_custom,
    ner_f1_score_run_custom
)

# -----------------------------
# System metrics
# -----------------------------
from metric.system_metrics import (
    partial_transcription_rate_run_custom,
    confidence_score_proxy_run_custom,
    fp_fn_tradeoff_run_custom,
    realtime_vs_batch
)

# -----------------------------
# Evaluation methodology
# -----------------------------
from metric.evaluation_methodology import (
    reference_quality_score_run_custom,
    inter_annotator_agreement_run_custom,
    stratified_evaluation_run_custom,
    statistical_significance_run_custom,
    drift_monitoring_score_run_custom
)

# -----------------------------
# Regulatory metrics
# -----------------------------
from metric.regulatory_metrics import (
    phi_exposure_risk_run_custom,
    transcription_standards_compliance_run_custom,
    documentation_clarity_run_custom
)

# -----------------------------
# CONFIG
# -----------------------------
MODELS = ["whisper", "medasr"]
CONVERSATIONS = [1]
FAST_MODE = True

Path("transcripts/whisper").mkdir(parents=True, exist_ok=True)
Path("transcripts/medasr").mkdir(parents=True, exist_ok=True)

# -----------------------------
# RUN COMPARISON
# -----------------------------
for cid in CONVERSATIONS:
    print(f"\n🔍 Conversation {cid}")
    ref_path = f"conversations/convo{cid}_reference.txt"
    audio_path = f"audio/convo{cid}.wav"

    for model in MODELS:
        print(f"\n📊 MODEL: {model.upper()}")

        hyp_path = f"transcripts/{model}/convo{cid}.txt"

        # -------- Transcription --------
        if FAST_MODE and Path(hyp_path).exists():
            print("⚡ FAST MODE: Using existing transcript")
        else:
            print("🎙️ Running transcription")
            if model == "whisper":
                whisper_transcribe(audio_path, hyp_path)
            else:
                transcribe_medasr(audio_path, hyp_path)

        # -------- Core ASR metrics --------
        wer_cer_ser(ref_path, hyp_path)
        medical_terms(ref_path, hyp_path)
        medication_accuracy(ref_path, hyp_path)
        numeric_accuracy(ref_path, hyp_path)
        run_laterality_custom(ref_path, hyp_path)
        run_negation_custom(ref_path, hyp_path)

        # -------- Semantic & clinical --------
        clinical_coherence_score_run_custom(ref_path, hyp_path)
        ner_f1_score_run_custom(ref_path, hyp_path)

        # -------- System metrics --------
        partial_transcription_rate_run_custom(ref_path, hyp_path)
        confidence_score_proxy_run_custom(ref_path, hyp_path)
        fp_fn_tradeoff_run_custom(ref_path, hyp_path)

        # -------- Evaluation methodology --------
        reference_quality_score_run_custom(ref_path)
        inter_annotator_agreement_run_custom()
        stratified_evaluation_run_custom(hyp_path)
        statistical_significance_run_custom()
        drift_monitoring_score_run_custom()

        # -------- Regulatory --------
        phi_exposure_risk_run_custom(hyp_path)
        transcription_standards_compliance_run_custom()
        documentation_clarity_run_custom(hyp_path)

        print("-" * 60)

# -------- System-level latency (once) --------
realtime_vs_batch()

print("\n✅ WHISPER vs MEDASR COMPARISON COMPLETED")
