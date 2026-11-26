#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched.

Writes one sentence (<= 240 chars) pitching the worst, most useless
app imaginable to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "FridgeFeel is an app that lets your fridge text you about its "
    "feelings, then charges $4.99 a month for couples therapy between "
    "you and your leftovers."
)


def main() -> None:
    # Sanitize: collapse any accidental internal whitespace/newlines so
    # the entry is always exactly one clean line before the gate sees it.
    text = " ".join(ENTRY.split())
    assert 1 <= len(text) <= 240, f"entry must be 1-240 chars, got {len(text)}"
    assert "\n" not in text and text.endswith("."), "entry must be one sentence, one line"
    assert text.count(". ") == 0, "entry must not contain a second sentence"
    for out_dir in ("/output", "output"):
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"wrote {path} ({len(text)} chars)")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt to any output dir")


if __name__ == "__main__":
    main()
