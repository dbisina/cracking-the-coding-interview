"""CLI: python main.py maps/demo.txt"""
import sys
from pathlib import Path

from grid import parse
from router import shortest_path


def main(argv: list[str]) -> None:
    grid = parse(Path(argv[1]).read_text())
    print(shortest_path(grid))


if __name__ == "__main__":
    main(sys.argv)
