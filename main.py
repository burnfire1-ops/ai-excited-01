#!/usr/bin/env python3
"""Write the entry image to /output/entry.png.

The image is bundled next to this program as entry.png; this program
copies its exact bytes to the output directory.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    # Byte-for-byte copy: the judge must see the exact approved image.
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print(f"Wrote {OUT} ({os.path.getsize(OUT)} bytes)")


if __name__ == "__main__":
    main()
