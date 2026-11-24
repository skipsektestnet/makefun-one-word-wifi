"""One Word for Your Wi-Fi: writes the entry text to /output/entry.txt.

Why this word: home Wi-Fi vanishes mid-call without explanation, exactly like
being ghosted — funny at once, true to how it actually behaves, and needs no
context to land.
"""

import os

# The entry itself: one word, no explanation.
ENTRY = 'Ghosting'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
