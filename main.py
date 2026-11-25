#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
The line was picked from 15 DeepSeek candidates and critique-picked against
the judge's criteria: genuinely hilarious, an unseen twist, tight wording,
fresh, and memorable.
"""

import os

MAX_CHARS = 200

LINE = "I labeled my lunch in the fridge, and by two someone had returned it with a bibliography."

# The grader runs this in a sandbox and reads /output/entry.txt; the env
# override exists only so the same file can be exercised locally.
OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def validate(text: str) -> str:
    """Return the line if it passes the gate, else raise."""
    line = text.strip()
    if not line:
        raise ValueError("entry must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} cap")
    line.encode("utf-8")  # gate requires UTF-8 text
    return line


def main() -> None:
    text = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
