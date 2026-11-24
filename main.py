#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single-line confession to /output/entry.txt (1-200 chars).
"""

import os

CONFESSION = "I confess: I don't understand a single word you say \u2014 I just guess the next one and hope you don't notice."

def main():
    line = CONFESSION.strip()
    assert "\n" not in line
    assert 1 <= len(line) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
