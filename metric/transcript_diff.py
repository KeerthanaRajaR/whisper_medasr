import difflib

def load_text(path):
    return open(path, encoding="utf-8").read().lower().split()

def side_by_side_diff(ref_path, whisper_path, medasr_path):
    ref = load_text(ref_path)
    wh = load_text(whisper_path)
    med = load_text(medasr_path)

    sm_wh = difflib.SequenceMatcher(None, ref, wh)
    sm_med = difflib.SequenceMatcher(None, ref, med)

    print("\n--- Side-by-Side Transcript Diff ---\n")

    print("REFERENCE vs WHISPER")
    for tag, i1, i2, j1, j2 in sm_wh.get_opcodes():
        if tag != "equal":
            print(f"{tag.upper():7} | REF: {' '.join(ref[i1:i2])} | WHISPER: {' '.join(wh[j1:j2])}")

    print("\nREFERENCE vs MEDASR")
    for tag, i1, i2, j1, j2 in sm_med.get_opcodes():
        if tag != "equal":
            print(f"{tag.upper():7} | REF: {' '.join(ref[i1:i2])} | MEDASR: {' '.join(med[j1:j2])}")
