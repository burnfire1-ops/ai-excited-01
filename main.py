"""Timmy's LEGO Dragon — ai-excited-01 entry program.

Copies the entry image (entry.png) into the output directory.
Standard library only. Deterministic: two runs write byte-identical
output.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    # The grader sets MAKEFUN_OUTPUT_DIR; outside it, /output is the default.
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)


if __name__ == "__main__":
    main()
