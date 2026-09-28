"""Reference solution covering stages 1-3. Drop-in replacement for ../../router.py (uses the original grid.py)."""
from collections import deque

from grid import DIRECTIONS, Grid

ARROWS = {"^": DIRECTIONS["up"], "v": DIRECTIONS["down"], "<": DIRECTIONS["left"], ">": DIRECTIONS["right"]}
MOVES = tuple(DIRECTIONS.values())


def shortest_path(grid: Grid) -> int:
    """BFS over (cell, keys-held) states on a flattened grid.

    Stage 1 fix: distance travels with the state (level-by-level), not a global pop counter.
    Stage 2: arrow tiles force the next move; lowercase keys open matching uppercase doors.
    Stage 3: flat indices + bytearray visited per key-mask keep 1M+ cells fast.
    """
    h, w = grid.height, grid.width
    flat = "".join(grid.rows)
    start = grid.start[0] * w + grid.start[1]
    end = grid.end[0] * w + grid.end[1]
    if start == end:
        return 0

    key_bits = {ch: 1 << (ord(ch) - ord("a")) for ch in set(flat) if "a" <= ch <= "d"}
    seen: dict[int, bytearray] = {0: bytearray(h * w)}
    seen[0][start] = 1
    frontier = [(start, 0)]
    dist = 0
    while frontier:
        dist += 1
        nxt_frontier = []
        for pos, keys in frontier:
            r, c = divmod(pos, w)
            tile = flat[pos]
            moves = (ARROWS[tile],) if tile in ARROWS else MOVES
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < h and 0 <= nc < w):
                    continue
                npos = nr * w + nc
                t = flat[npos]
                if t == "#":
                    continue
                if "A" <= t <= "D" and not keys & (1 << (ord(t) - ord("A"))):
                    continue
                nkeys = keys | key_bits.get(t, 0)
                if npos == end:
                    return dist
                visited = seen.get(nkeys)
                if visited is None:
                    visited = seen[nkeys] = bytearray(h * w)
                if visited[npos]:
                    continue
                visited[npos] = 1
                nxt_frontier.append((npos, nkeys))
        frontier = nxt_frontier
    return -1


def route_many(grid: Grid, starts: list[tuple[int, int]]) -> list[int]:
    """Stage 3: distance to E from many robots (maps have no keys/doors).

    One reverse BFS from E answers every start: O(H*W + Q) instead of O(Q*H*W).
    Reverse edge v <- u exists when u may step into v: u is not a wall and,
    if u is an arrow tile, its arrow points at v.
    """
    h, w = grid.height, grid.width
    flat = "".join(grid.rows)
    dist = [-1] * (h * w)
    end = grid.end[0] * w + grid.end[1]
    dist[end] = 0
    queue = deque([end])
    while queue:
        v = queue.popleft()
        vr, vc = divmod(v, w)
        for dr, dc in MOVES:
            ur, uc = vr - dr, vc - dc  # u moves by (dr, dc) to reach v
            if not (0 <= ur < h and 0 <= uc < w):
                continue
            u = ur * w + uc
            t = flat[u]
            if t == "#" or dist[u] != -1:
                continue
            if t in ARROWS and ARROWS[t] != (dr, dc):
                continue
            dist[u] = dist[v] + 1
            queue.append(u)
    return [dist[r * w + c] for r, c in starts]
