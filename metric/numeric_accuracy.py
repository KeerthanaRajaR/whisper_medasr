import re

# Existing CID-based function (keep this)
def run(cid):
    text = open(f"transcripts/convo{cid}_whisper.txt").read()
    nums = re.findall(r"\d+(?:\.\d+)?", text)
    print("Numbers detected:", nums)


# ✅ NEW: path-based function for comparison pipeline
def run_custom(ref_path, transcript_path):
    text = open(transcript_path).read()
    nums = re.findall(r"\d+(?:\.\d+)?", text)
    print("Numbers detected:", nums)
