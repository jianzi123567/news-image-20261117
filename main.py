#!/usr/bin/env python3
"""Write the 17 November 2026 world-news image to /output/entry.png.

Deterministic: copies the bytes of entry.png (shipped in the repo root)
verbatim. No network, no randomness, no time, no environment.
The same bytes are written on every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(src, "rb") as f:
        data = f.read()
    assert len(data) <= 1024 * 1024, len(data)
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
    with open(os.path.join(out_dir, "entry.png"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
