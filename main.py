#!/usr/bin/env python3
"""news-image-20261117: write the 17 November 2026 world-news infographic to /output/entry.png.

Deterministic: copies the bundled PNG byte-for-byte, so every run writes
identical bytes. No network, no randomness, no timestamps in the output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")
DST = "/output/entry.png"


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
