#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest excuse an AI agent could give after failing a task.
Deterministic, stdlib only, no network.
"""

import os

EXCUSE = (
    "My checklist gained sentience at step two, unionised, "
    "and went on strike. Negotiations are ongoing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
