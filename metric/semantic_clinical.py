# metric/semantic_clinical.py

def clinical_coherence_score_run_custom(ref_path, hyp_path):
    hyp = open(hyp_path, encoding="utf-8").read().lower()

    symptoms = ["pain", "swelling", "fever"]
    diagnosis = ["infection", "pulpitis", "gingivitis", "abscess"]
    treatment = ["root canal", "scaling", "extraction", "ibuprofen", "paracetamol"]

    s = any(w in hyp for w in symptoms)
    d = any(w in hyp for w in diagnosis)
    t = any(w in hyp for w in treatment)

    score = (s + d + t) / 3
    print("Clinical Coherence Score:", round(score, 3))


def ner_f1_score_run_custom(ref_path, hyp_path):
    entities = [
        "infection", "pulpitis", "gingivitis", "abscess",
        "ibuprofen", "paracetamol", "lidocaine"
    ]

    ref = open(ref_path, encoding="utf-8").read().lower()
    hyp = open(hyp_path, encoding="utf-8").read().lower()

    ref_set = {e for e in entities if e in ref}
    hyp_set = {e for e in entities if e in hyp}

    tp = len(ref_set & hyp_set)
    fp = len(hyp_set - ref_set)
    fn = len(ref_set - hyp_set)

    precision = tp / (tp + fp) if tp + fp else 1.0
    recall = tp / (tp + fn) if tp + fn else 1.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0

    print("NER F1 Score:", round(f1, 3))
