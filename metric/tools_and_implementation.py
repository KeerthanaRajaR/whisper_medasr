from jiwer import wer
import difflib
from collections import Counter

def asr_library_consistency_run_custom(ref_path, hyp_path):
    score = 1 - wer(
        open(ref_path).read(),
        open(hyp_path).read()
    )
    print("ASR Library Consistency Score:", round(score, 3))

def medical_nlp_coverage_run_custom(hyp_path):
    terms = [
        "infection", "pulpitis", "gingivitis",
        "abscess", "ibuprofen", "paracetamol", "lidocaine"
    ]
    hyp = open(hyp_path).read().lower()
    detected = sum(1 for t in terms if t in hyp)

    score = detected / len(terms)
    print("Medical NLP Coverage Score:", round(score, 3))

def string_alignment_score_run_custom(ref_path, hyp_path):
    ref = open(ref_path).read()
    hyp = open(hyp_path).read()

    score = difflib.SequenceMatcher(None, ref, hyp).ratio()
    print("String Alignment Score:", round(score, 3))

def error_distribution_run_custom(ref_path, hyp_path):
    ref = ref_path and open(ref_path).read().split()
    hyp = open(hyp_path).read().split()

    deletions = [w for w in ref if w not in hyp]
    insertions = [w for w in hyp if w not in ref]

    print("Error Distribution:",
          {"deletions": len(deletions), "insertions": len(insertions)})

def cicd_readiness_run_custom(ref_path, hyp_path):
    quality_gate = wer(
        open(ref_path).read(),
        open(hyp_path).read()
    ) < 0.5

    print("CI/CD Quality Gate Passed:", quality_gate)
