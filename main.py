"""ai-excited-01 entry.

Reads the image file bundled next to this script and writes those exact
bytes to entry.png inside the output directory. Pure standard library,
no network access, fully deterministic: the same input bytes always
produce the same output bytes.
"""

import os
import sys


def main() -> int:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, "entry.png")

    with open(source_path, "rb") as handle:
        image_bytes = handle.read()

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)

    destination = os.path.join(output_dir, "entry.png")
    with open(destination, "wb") as handle:
        handle.write(image_bytes)

    return 0


if __name__ == "__main__":
    sys.exit(main())
