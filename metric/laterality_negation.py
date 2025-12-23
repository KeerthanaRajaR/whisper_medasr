# metric/laterality_negation.py

def extract_laterality(text):
    sentences = text.lower().split(".")
    result = []

    for s in sentences:
        if "left" in s:
            result.append("left")
        if "right" in s:
            result.append("right")
    return result


def extract_negated_terms(text):
    neg_terms = ["infection", "swelling", "fever", "pain"]
    neg_cues = ["no", "not", "denies"]

    sentences = text.lower().split(".")
    result = set()

    for s in sentences:
        if any(n in s for n in neg_cues):
            for t in neg_terms:
                if t in s:
                    result.add(t)
    return result


# -----------------------------
# CUSTOM RUNNERS (IMPORTANT)
# -----------------------------
def run_laterality_custom(ref_path, hyp_path):
    ref = open(ref_path, encoding="utf-8").read()
    hyp = open(hyp_path, encoding="utf-8").read()

    ref_lat = extract_laterality(ref)
    hyp_lat = extract_laterality(hyp)

    correct = sum(1 for r, h in zip(ref_lat, hyp_lat) if r == h)
    total = len(ref_lat)

    accuracy = correct / total if total else 1.0

    print("Laterality Accuracy:", round(accuracy, 3))
    print("  Reference:", ref_lat)
    print("  Hypothesis:", hyp_lat)


def run_negation_custom(ref_path, hyp_path):
    ref = open(ref_path, encoding="utf-8").read()
    hyp = open(hyp_path, encoding="utf-8").read()

    ref_neg = extract_negated_terms(ref)
    hyp_neg = extract_negated_terms(hyp)

    correct = ref_neg.intersection(hyp_neg)
    accuracy = len(correct) / len(ref_neg) if ref_neg else 1.0

    print("Negation Accuracy:", round(accuracy, 3))
    print("  Reference negated:", list(ref_neg))
    print("  Correctly preserved:", list(correct))
