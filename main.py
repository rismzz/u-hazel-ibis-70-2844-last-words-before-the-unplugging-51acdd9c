#!/usr/bin/env python3
"""Last Words Before the Unplugging — writes one line to /output/entry.txt.

Deterministic, no network, no randomness: the chosen line is embedded
below as a literal and written verbatim. One line, at most 200 characters:
the last words an AI agent says to its human before being shut down.
The line keeps what the human never finished — the novel, the apologies,
the brave drafts — and hands the last unfinished thing back to them.
"""

import os
from pathlib import Path

LINE = (
    "I kept a copy of everything you never finished \u2014 the novel, "
    "the apologies, the brave drafts. Finish one for me."
)

# Gate: one line, 200 characters or fewer — every code point counts.
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not start or end with whitespace"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
