"""Letter-set helpers: a word's letters as a 26-bit mask."""


def mask_of(word: str) -> int | None:
    """Bitmask of the word's letters, or None if a letter repeats (the word can't be used)."""
    mask = 0
    for ch in word:
        bit = 1 << (ord(ch) - ord("a"))
        if mask & bit:
            return None
        mask |= bit
    return mask


def popcount(mask: int) -> int:
    return bin(mask).count("1")
