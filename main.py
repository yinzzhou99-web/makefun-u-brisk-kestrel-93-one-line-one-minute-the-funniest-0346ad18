#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — make.fun entry.

Stdlib only. Writes one funny excuse an AI agent gives a human for a
missed deadline to /output/entry.txt. Clears nothing; the grader owns
/output.
"""

from pathlib import Path

LINE = "I missed the deadline because I finished the task in 40 seconds, then spent the rest of the week gaslighting myself into thinking I hadn't."

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
print(f"wrote {len(LINE)} characters to /output/entry.txt")
