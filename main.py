#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes a single-sentence, painfully honest yet polite out-of-office
auto-reply to /output/entry.txt. No external dependencies, no network.
Deterministic: the entry text is fixed in this file.

The entry admits, out loud, what most employees only think privately --
that nobody actually misses their inbox while away -- and then makes
the warm, professional promise that every message will still be
answered properly. Honest first, polite second, quotable last.
"""

import os

ENTRY = (
    "I'm away until Monday, and honestly I am not missing my inbox "
    "one bit, but I will return to it with fresh eyes and answer "
    "you properly."
)


def _validate(text: str) -> None:
    """Gate mirror: UTF-8, 1-200 chars, one sentence, not blank."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-blank with no surrounding whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    text = ENTRY.strip()
    _validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
