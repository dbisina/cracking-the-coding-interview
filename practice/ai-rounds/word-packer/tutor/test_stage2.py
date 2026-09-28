"""Stage 2 tests: copy next to packer.py when stage 2 starts.

New API: best_words(words, max_words=None) -> list[str], an optimal set of words
(no shared letters, no repeated letters, at most max_words words).
"""
from itertools import combinations

from bits import mask_of
from packer import best_pack, best_words


def is_valid(chosen: list[str], pool: list[str]) -> bool:
    used = 0
    for w in chosen:
        m = mask_of(w)
        if w not in pool or m is None or m & used:
            return False
        used |= m
    return True


def brute(words: list[str], max_words: int | None) -> int:
    best = 0
    k_max = len(words) if max_words is None else max_words
    for k in range(k_max + 1):
        for combo in combinations(words, k):
            if is_valid(list(combo), words):
                best = max(best, sum(map(len, combo)))
    return best


CASES = [
    ["ab", "cd", "cdefgh"],
    ["cha", "r", "act", "ers"],
    ["abcdefghijklm", "nopqrstuvwxyz", "abc"],
    ["aa", "bb"],
    ["jump", "fox", "quick", "brown", "lazy", "dog", "the"],
    ["ab", "ab", "ab"],
]


def test_best_words_is_optimal_and_valid():
    for words in CASES:
        chosen = best_words(words)
        assert is_valid(chosen, words), (words, chosen)
        assert sum(map(len, chosen)) == brute(words, None), words


def test_best_pack_agrees():
    for words in CASES:
        assert best_pack(words) == brute(words, None)


def test_max_words_limit():
    words = ["ab", "cd", "ef", "ghijk"]
    for k in range(0, 5):
        chosen = best_words(words, max_words=k)
        assert len(chosen) <= k
        assert is_valid(chosen, words)
        assert sum(map(len, chosen)) == brute(words, k)


def test_limit_changes_the_choice():
    words = ["abcd", "efgh", "ijklmnop"]
    assert sum(map(len, best_words(words, max_words=1))) == 8
    assert sum(map(len, best_words(words, max_words=2))) == 12
