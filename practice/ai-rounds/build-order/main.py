"""CLI: python main.py manifest.txt"""
import sys
from pathlib import Path

from graph import from_manifest
from resolver import install_order


def main(argv: list[str]) -> None:
    print("\n".join(install_order(from_manifest(Path(argv[1]).read_text()))))


if __name__ == "__main__":
    main(sys.argv)
