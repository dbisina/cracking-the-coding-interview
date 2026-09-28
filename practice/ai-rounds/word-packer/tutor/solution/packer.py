"""Reference solution covering stages 1-3. Drop-in replacement for ../../packer.py."""
from bits import mask_of, popcount


def best_words(words: list[str], max_words: int | None = None) -> list[str]:
    """Stage 2+3: an optimal letter-disjoint word set (at most max_words words).

    Branch and bound over distinct letter-masks, largest first:
    - dedupe identical letter-sets (keep one representative word each)
    - bound: letters used so far + letters still available in the remaining masks
    - stop as soon as all 26 letters are used
    """
    rep: dict[int, str] = {}
    for w in words:
        m = mask_of(w)
        if m is not None and m not in rep:
            rep[m] = w
    masks = sorted(rep, key=popcount, reverse=True)
    n = len(masks)
    limit = n if max_words is None else max_words
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] | masks[i]

    best_score = 0
    best_pick: list[int] = []
    pick: list[int] = []

    def go(start: int, used: int) -> None:
        nonlocal best_score, best_pick
        score = popcount(used)
        if score > best_score:
            best_score, best_pick = score, pick.copy()
        if best_score == 26 or len(pick) == limit:
            return
        for j in range(start, n):
            if score + popcount(suffix[j] & ~used) <= best_score:
                return
            m = masks[j]
            if m & used == 0:
                pick.append(m)
                go(j + 1, used | m)
                pick.pop()

    go(0, 0)
    return [rep[m] for m in best_pick]


def best_pack(words: list[str]) -> int:
    """Stage 1 fix: every word may be skipped, not only conflicting ones."""
    return sum(len(w) for w in best_words(words))
