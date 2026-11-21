#!/usr/bin/env python3
"""Write one joke about working beside an AI coding agent.

Entry for make.fun's "The joke about the demo" bounty: the program
produces exactly one file, /output/entry.txt, holding a single one-line
joke of 1 to 280 characters about demoing code next to an AI agent.
"""

from pathlib import Path

JOKE = (
    "My AI agent fixed the bug minutes before the demo, then spent the "
    "whole demo explaining the fix while the bug performed live on screen "
    "behind it."
)

OUTPUT_PATH = Path("/output/entry.txt")
MIN_LENGTH = 1
MAX_LENGTH = 280


def validate(text: str) -> str:
    """Keep the gate happy: 1-280 code points, one line, not only whitespace."""
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"joke must be {MIN_LENGTH}-{MAX_LENGTH} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    return text


def main() -> None:
    joke = validate(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(joke, encoding="utf-8")
    print(f"Wrote {len(joke)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
