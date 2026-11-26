"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes one voicemail greeting, recorded by a cat, to entry.txt in the
output directory named by MAKEFUN_OUTPUT_DIR (default /output).
Deterministic: the same bytes on every run, no time, no randomness,
no network.
"""

import os

ENTRY = (
    "You have reached the cat. I am asleep on your keyboard. "
    "Leave a message after the purr. I will not listen."
)
# Exactly 106 characters, one line. The joke in three beats: the cat
# states its voicemail (asleep on the keyboard, a very cat place to
# nap), swaps the beep for a purr, and refuses to listen — the punch
# lands on the last four words, in the cat's own flat voice.

# Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters.
assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} characters"
assert ENTRY.strip() == ENTRY


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file holds exactly the entry text.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
