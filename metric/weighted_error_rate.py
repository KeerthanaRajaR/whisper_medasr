def weighted_error_rate_run_custom(ref_path, hyp_path):
    ref = open(ref_path).read().lower().split()
    hyp = open(hyp_path).read().lower().split()

    weights = {
        "medication": 10,
        "number": 5,
        "laterality": 5,
        "general": 1
    }

    meds = ["paracetamol", "ibuprofen", "lidocaine"]
    sides = ["left", "right"]

    weighted_error = 0
    total_weight = 0

    for w in ref:
        if w in meds:
            weight = weights["medication"]
        elif w.isdigit():
            weight = weights["number"]
        elif w in sides:
            weight = weights["laterality"]
        else:
            weight = weights["general"]

        total_weight += weight
        if w not in hyp:
            weighted_error += weight

    score = weighted_error / total_weight if total_weight else 0
    print("Weighted Error Rate:", round(score, 3))


def error_weight_distribution_run_custom(ref_path):
    ref = open(ref_path).read().lower().split()

    dist = {"medication": 0, "number": 0, "laterality": 0, "general": 0}

    for w in ref:
        if w.isdigit():
            dist["number"] += 1
        elif w in ["paracetamol", "ibuprofen", "lidocaine"]:
            dist["medication"] += 1
        elif w in ["left", "right"]:
            dist["laterality"] += 1
        else:
            dist["general"] += 1

    print("Error Category Distribution:", dist)
