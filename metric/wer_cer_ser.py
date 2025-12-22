from jiwer import wer, cer

def run_custom(ref_path, hyp_path):
    ref = open(ref_path, encoding="utf-8").read()
    hyp = open(hyp_path, encoding="utf-8").read()

    wer_score = wer(ref, hyp)
    cer_score = cer(ref, hyp)

    ref_sentences = ref.strip().split("\n")
    hyp_sentences = hyp.strip().split("\n")

    ser = sum(
        1 for r, h in zip(ref_sentences, hyp_sentences) if r.strip() != h.strip()
    ) / max(len(ref_sentences), 1)

    print(f"WER: {round(wer_score, 3)}")
    print(f"CER: {round(cer_score, 3)}")
    print(f"SER: {round(ser, 3)}")
