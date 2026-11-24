"""Write the entry for One Line, One Minute: The Funniest AI Excuse.

One line, at most 200 characters: the funniest excuse an AI agent gives
its human for a missed deadline. The program writes the line to
/output/entry.txt and checks it back against the file it wrote.
"""

import os
from pathlib import Path

ENTRY = "The deadline was in my context window, but then I read your other messages and it got evicted to make room for the grocery list."

OUTPUT_PATH = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def validate_entry(text: str) -> str:
    """Return the entry unchanged when it passes the gate, else fail."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    back = OUTPUT_PATH.read_text(encoding="utf-8")
    assert back == text, "entry written to disk does not match the validated entry"
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
