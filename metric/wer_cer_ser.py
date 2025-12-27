from jiwer import wer, cer
from metric.normalization import normalize_text

def run_custom(ref_path, hyp_path):
    ref = open(ref_path).read()
    hyp = open(hyp_path).read()

    ref_n = normalize_text(ref)
    hyp_n = normalize_text(hyp)

    print("WER:", round(wer(ref_n, hyp_n), 3))
    print("CER:", round(cer(ref_n, hyp_n), 3))
