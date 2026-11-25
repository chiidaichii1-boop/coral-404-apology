#!/usr/bin/env python3
"""The Production Database Apology.

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.
Stdlib only; deterministic; never deletes the output folder.
"""

import os

ENTRY = (  # 127 characters, verified; gate is 1-200
    "Sorry, I deleted the production database. "
    "I did make a backup first, though: "
    "it's stored safely inside the production database."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
