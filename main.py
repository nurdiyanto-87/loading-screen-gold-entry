"""Loading Screen Gold: a one-line tip in at most 200 characters.

The program writes a single loading-screen tip to /output/entry.txt.
Pure standard library, deterministic: the same tip on every run.
The tip is a plain ASCII string, one line, well under the 200-char gate.
"""

import os
from pathlib import Path

TIP = (
    "Tip: your agent finished in 12 seconds. "
    "You'll spend the next 40 minutes finding out what it actually did."
)


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Exactly one line, no trailing newline: the gate counts characters,
    # so the file holds only the tip itself.
    output_path.write_text(TIP, encoding="utf-8")


if __name__ == "__main__":
    main()
