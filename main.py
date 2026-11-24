"""Write the toaster error message entry to /output/entry.txt.

Reads no input and needs no network: the entry text is fixed, so the
program only resolves where to write it and writes it as UTF-8.
"""

import os
import sys
from pathlib import Path

ENTRY_TEXT = "ERROR 0xBREAD: Toasting failed. The bread has left the building."


def resolve_output_dir(argv):
    if len(argv) > 1:
        return Path(argv[1])
    env_dir = os.environ.get("OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    return Path("/output")


def main(argv=None):
    args = list(sys.argv if argv is None else argv)
    output_dir = resolve_output_dir(args)
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY_TEXT, encoding="utf-8")
    print(f"wrote {len(ENTRY_TEXT.encode('utf-8'))} bytes to {entry_path}")


if __name__ == "__main__":
    main()
