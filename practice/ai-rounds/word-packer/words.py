"""Loading and cleaning word lists."""
from pathlib import Path


def normalize(word: str) -> str:
    return "".join(ch for ch in word.strip().lower() if "a" <= ch <= "z")


def load_words(path: str | Path) -> list[str]:
    words = (normalize(line) for line in Path(path).read_text().splitlines())
    return [w for w in words if w]
