"""make.fun entry: The Most Boring Object, Reviewed in One Line.

Writes a single-line review of a drinks coaster to entry.txt in the
output directory. The coaster is a genuinely boring, everyday object,
and the joke is its own dull job: it protects the table from coffee
rings by catching every ring itself, so it ends up more ring than
coaster. The program is deterministic: same input (none), same bytes.
"""

import os

ENTRY_TEXT = (
    "Five stars. Its whole job is stopping coffee rings from reaching my "
    "table, and it does it by catching every single one itself. It is now "
    "more ring than coaster."
)


MAX_CHARS = 200


def validate(text: str) -> bytes:
    """Check the entry against the competition gate and return its bytes.

    The gate accepts UTF-8 text of 1 to 200 characters that is not only
    whitespace, and the brief demands a single line, so fail loudly here
    rather than let an invalid entry reach the scorer.
    """
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the {MAX_CHARS} cap")
    return text.encode("utf-8")


def main() -> None:
    payload = validate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Binary write: the exact validated bytes land on disk on every
    # platform, with no newline translation and no trailing newline added.
    with open(path, "wb") as fh:
        fh.write(payload)


if __name__ == "__main__":
    main()
