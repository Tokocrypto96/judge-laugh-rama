#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke, one line, under 200 chars.

Writes the final entry to /output/entry.txt (stdlib only, deterministic).
"""

import os

JOKE = (
    "Our office printer has never missed a deadline \u2014 "
    "it jams only when the document matters most, "
    "so it\u2019s the most reliable employee here."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke must be 1-200 chars, got {len(JOKE)}"
    assert "\n" not in JOKE, "entry must be a single line"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} chars to {out_path}")


if __name__ == "__main__":
    main()
