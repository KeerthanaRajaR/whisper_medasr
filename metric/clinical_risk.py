def load_text(path):
    return open(path, encoding="utf-8").read().lower()

def clinical_risk_score(ref_path, hyp_path):
    ref = load_text(ref_path)
    hyp = load_text(hyp_path)

    risks = {
        "medication": {
            "terms": ["ibuprofen", "lidocaine", "clindamycin", "paracetamol"],
            "weight": 5
        },
        "laterality": {
            "terms": ["left", "right"],
            "weight": 4
        },
        "numeric": {
            "terms": ["mg", "ml", "percent", "minutes", "hours"],
            "weight": 3
        }
    }

    score = 0
    issues = []

    for category, info in risks.items():
        for term in info["terms"]:
            if term in ref and term not in hyp:
                score += info["weight"]
                issues.append((category, term))

    level = "LOW"
    if score >= 8:
        level = "HIGH"
    elif score >= 4:
        level = "MEDIUM"

    print("\n--- Clinical Risk Assessment ---")
    print("Total Risk Score:", score)
    print("Risk Level:", level)
    print("Risk Issues:", issues)
