"""ai-excited-01 entry.

Reads the image bundled next to this script (entry.png) and writes those
exact bytes to entry.png inside the output directory. Standard library
only, no network, no randomness: the output is a byte-for-byte copy of the
bundled image, so two runs always produce identical files.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    dest = os.path.join(out_dir, "entry.png")
    with open(source, "rb") as src, open(dest, "wb") as dst:
        shutil.copyfileobj(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
