import re

def section_heading_accuracy_run_custom(ref_path, hyp_path):
    ref = open(ref_path, encoding="utf-8").read()
    hyp = open(hyp_path, encoding="utf-8").read()

    pattern = r"(Doctor:|Patient:)"

    ref_heads = re.findall(pattern, ref)
    hyp_heads = re.findall(pattern, hyp)

    correct = sum(1 for r, h in zip(ref_heads, hyp_heads) if r == h)
    total = len(ref_heads)

    score = correct / total if total else 1.0
    print("Section Heading Accuracy:", round(score, 3))


def punctuation_accuracy_run_custom(ref_path, hyp_path):
    critical = [".", "?", ":"]

    ref = open(ref_path).read()
    hyp = open(hyp_path).read()

    ref_count = sum(ref.count(p) for p in critical)
    hyp_count = sum(hyp.count(p) for p in critical)

    score = min(hyp_count, ref_count) / ref_count if ref_count else 1.0
    print("Punctuation Accuracy (Critical):", round(score, 3))
