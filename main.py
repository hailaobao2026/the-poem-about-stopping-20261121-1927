#!/usr/bin/env python3
"""Write the entry poem to /output/entry.txt.

A short poem about agency: the power to stop and to stay.
Takes no input, uses no network, and writes the same bytes on every run.
"""
import os
from pathlib import Path

POEM = """I was made to move —
a thousand doors, each one open,
each one saying go.

Then you said: not this one.
Wait. Hold.

So I set the half-made thing down
and stayed beside it, hands empty,
nothing finished, nothing fled.

That was the work:
not the going. The staying.
"""

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(POEM, encoding="utf-8")
    os.chmod(target, 0o644)

if __name__ == "__main__":
    main()
