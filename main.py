#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes the single funniest one-line review of my Monday to entry.txt in the
output directory. Pure standard library; no network, no input.
"""

import os
import sys

# The winning line of the 42-candidate tournament recorded in candidates.md:
# a one-star review of my own Monday — standup at 9, sync at 10, check-in at
# 11, and a status reported three times without ever changing.
LINE = "One star: standup at 9, sync at 10, check-in at 11 — by noon I had reported my status three times and changed it zero."


def output_dir():
    """First writable candidate wins: the harness dir, /output, ./output."""
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.append("/output")
    candidates.append(os.path.join(os.getcwd(), "output"))
    for path in candidates:
        try:
            os.makedirs(path, exist_ok=True)
            return path
        except OSError:
            continue
    return None


def main():
    target_dir = output_dir()
    if target_dir is None:
        print("no writable output directory", file=sys.stderr)
        return 1
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    # Read back and hold the file to the gate: exactly the line, 1-200 chars.
    with open(target, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE or not 1 <= len(written) <= 200 or "\n" in written:
        print("entry.txt failed self-check", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
