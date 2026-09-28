"""CLI: python main.py wordlist.txt"""
import sys

from packer import best_pack
from words import load_words


def main(argv: list[str]) -> None:
    print(best_pack(load_words(argv[1])))


if __name__ == "__main__":
    main(sys.argv)
