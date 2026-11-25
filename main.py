"""The word I would delete from the dictionary: irregardless.

Entry for the make.fun bounty "The Word You'd Delete From the Dictionary"
(slug: u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2).

Why this word: "irregardless" is a double negative wearing a tuxedo. The
"ir-" prefix and the "-less" suffix both negate, so the word cancels itself
out before it even starts meaning anything — and yet it keeps showing up in
otherwise perfectly good sentences. It adds nothing that "regardless" does
not already say, cleaner. Delete it and the language loses nothing.

What this program does: writes the entry word to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt) and prints the
same word to stdout.

Bounty gate (enforced here with assertions, so a bad entry fails loudly
instead of submitting silently):
  * /output/entry.txt must be UTF-8,
  * 1-77 characters,
  * not only whitespace,
  * exactly one word.

Pure Python 3.13 standard library only. Deterministic, no network access.
"""

import os

# The entry text, verbatim. Written with no trailing newline.
ENTRY = "irregardless"


def gate_check(text):
    """Assert the bounty gate: 1-77 chars, not only whitespace, one word."""
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= 77, f"entry must be 1-77 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert len(text.split()) == 1, f"entry must be exactly one word, got {text!r}"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def main():
    entry = gate_check(ENTRY)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names a directory; entry.txt lives inside it.
    # (If it already ends in entry.txt, treat it as the file path.)
    path = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    # Write as UTF-8 with newline="" and no trailing newline: the file
    # contains exactly the entry text and nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)

    # Verify what landed on disk matches the gate, byte for byte.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw == entry.encode("utf-8"), "entry.txt bytes do not match entry text"

    print(entry)


if __name__ == "__main__":
    main()
