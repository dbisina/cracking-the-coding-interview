"""Pick words for a sign-maker who owns exactly one tile per letter.

A set of words can be printed together only if no letter is needed twice
(within a word or across words). Maximise the number of tiles used.
"""
from bits import mask_of, popcount


def best_pack(words: list[str]) -> int:
    """Largest total number of letters over word sets that share no letter."""
    masks = [m for m in map(mask_of, words) if m is not None]

    def go(i: int, used: int) -> int:
        if i == len(masks):
            return popcount(used)
        if masks[i] & used == 0:
            return go(i + 1, used | masks[i])
        return go(i + 1, used)

    return go(0, 0)
