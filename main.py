#!/usr/bin/env python3
"""news-image-20261119 entry: copy the composed image to the output dir.

The image (entry.png beside this file) sums up Thursday 19 November 2026:
a GTA VI hero above an ALSO TODAY strip of four more stories. Standard
library only; no network. The grader runs this twice and both runs must
write the same bytes, so the program only copies a fixed file.
"""
import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, IMAGE_NAME)
    shutil.copyfile(src, dst)
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if dst_size != src_size:
        print(f"size mismatch after copy: {dst_size} != {src_size}",
              file=sys.stderr)
        return 1
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
