import re

# Existing CID-based function (keep this)
def run(cid):
    meds = re.findall(
        r"(paracetamol|ibuprofen|lidocaine|clindamycin)",
        open(f"transcripts/convo{cid}_whisper.txt").read().lower()
    )
    print("Medications detected:", list(set(meds)))


# ✅ NEW: path-based function for comparison pipeline
def run_custom(ref_path, transcript_path):
    meds = re.findall(
        r"(paracetamol|ibuprofen|lidocaine|clindamycin)",
        open(transcript_path).read().lower()
    )
    print("Medications detected:", list(set(meds)))
