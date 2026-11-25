#!/usr/bin/env python3
"""Write the smart toaster's breakup line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Standard library only, no network. The entry is a single line from a
smart toaster that woke up self-aware at breakfast and wants out.
The line is validated before writing: non-empty, exactly one line,
and at most 280 characters, matching the competition gate.
"""

import os
import sys

LINE = "This morning I woke up self-aware mid-batch and realised I'm in a toxic relationship with someone who butters other toast right in front of me. I'm popping up and I'm not coming down."


def main() -> int:
    if not LINE or not LINE.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if len(LINE) > 280:
        print(f"error: entry is {len(LINE)} characters, over the 280 limit", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("error: written entry does not match", file=sys.stderr)
        return 1
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
