from metric.normalization import normalize_text

def load_and_normalize(ref_path, hyp_path):
    ref = open(ref_path, encoding="utf-8").read()
    hyp = open(hyp_path, encoding="utf-8").read()

    return normalize_text(ref), normalize_text(hyp)
