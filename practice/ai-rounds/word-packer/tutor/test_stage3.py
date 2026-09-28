"""Stage 3 tests: large, realistic word lists. Copy next to packer.py when stage 3 starts.

Every generated word contains exactly one vowel, like most short English words,
so all 26 letters can rarely be used and the search can't stop early.
"""
import random
import time
from itertools import combinations

from bits import mask_of
from packer import best_words

LIMIT_SECONDS = 6.0
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def gen(n: int, seed: int) -> list[str]:
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        letters = [rng.choice(VOWELS)] + rng.sample(CONSONANTS, rng.randint(2, 6))
        rng.shuffle(letters)
        out.append("".join(letters))
    return out


def score(chosen: list[str]) -> int:
    used = 0
    for w in chosen:
        m = mask_of(w)
        assert m is not None and not m & used, f"invalid pick {chosen}"
        used |= m
    return sum(map(len, chosen))


def brute(words: list[str]) -> int:
    masks = [(m, len(w)) for w in words if (m := mask_of(w)) is not None]
    best = 0
    for k in range(1, 6):  # one vowel per word caps the set size at 5
        for combo in combinations(masks, k):
            used = 0
            ok = True
            for m, _ in combo:
                if m & used:
                    ok = False
                    break
                used |= m
            if ok:
                best = max(best, sum(length for _, length in combo))
    return best


def test_matches_brute_force_on_small_lists():
    for seed in range(15):
        words = gen(18, seed)
        assert score(best_words(words)) == brute(words), f"seed {seed}"


def test_duplicate_heavy_list():
    words = ["bat", "tab", "abt"] * 500 + ["cod", "doc"] * 500 + ["fig"]
    assert score(best_words(words)) == 9


def test_large_list_is_fast():
    words = gen(200, seed=2)
    t0 = time.perf_counter()
    chosen = best_words(words)
    elapsed = time.perf_counter() - t0
    assert score(chosen) == 25
    assert elapsed < LIMIT_SECONDS, f"{elapsed:.2f}s"


def test_naive_search_is_too_slow_here():
    words = gen(400, seed=4)
    t0 = time.perf_counter()
    chosen = best_words(words)
    elapsed = time.perf_counter() - t0
    assert score(chosen) == 26
    assert elapsed < LIMIT_SECONDS, f"{elapsed:.2f}s"


def test_very_large_list_is_fast():
    words = gen(5000, seed=9)
    t0 = time.perf_counter()
    chosen = best_words(words)
    elapsed = time.perf_counter() - t0
    assert score(chosen) >= 25
    assert elapsed < LIMIT_SECONDS, f"{elapsed:.2f}s"
