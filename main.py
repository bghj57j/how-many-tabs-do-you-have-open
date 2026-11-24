# Writes the one number to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# Gate is digits only, so no trailing newline is written.
import os
NUMBER = "0"  # honest count: no browser window is open right now.
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(NUMBER)  # same output on every run
