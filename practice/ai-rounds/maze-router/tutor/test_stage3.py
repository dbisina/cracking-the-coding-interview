"""Stage 3 tests: fleet routing. Copy next to router.py when stage 3 starts.

New API: route_many(grid, starts) -> list[int], the distance from each start to E (-1 if unreachable).
Stage 3 maps contain walls and arrow tiles but no keys or doors.
"""
import random
import time

from grid import Grid, parse
from router import route_many, shortest_path

LIMIT_SECONDS = 6.0


def random_map(n: int, wall_ratio: float, arrow_ratio: float, seed: int) -> str:
    rng = random.Random(seed)
    rows = []
    for _ in range(n):
        row = []
        for _ in range(n):
            x = rng.random()
            if x < wall_ratio:
                row.append("#")
            elif x < wall_ratio + arrow_ratio:
                row.append(rng.choice("^v<>"))
            else:
                row.append(".")
        rows.append(row)
    rows[0][0] = "S"
    rows[n - 1][n - 1] = "E"
    return "\n".join("".join(r) for r in rows)


def with_start(grid: Grid, start: tuple[int, int]) -> Grid:
    return Grid(grid.rows, start, grid.end)


def test_matches_single_queries_on_small_maps():
    for seed in range(20):
        grid = parse(random_map(8, 0.25, 0.15, seed))
        starts = [(r, c) for r in range(8) for c in range(8) if grid.rows[r][c] != "#"]
        expected = [shortest_path(with_start(grid, s)) for s in starts]
        assert route_many(grid, starts) == expected, f"seed {seed}"


def test_start_on_exit_is_zero():
    grid = parse("S.E")
    assert route_many(grid, [(0, 2), (0, 0)]) == [0, 2]


def test_arrow_pointing_away_is_unreachable():
    grid = parse("S<E")
    assert route_many(grid, [(0, 1), (0, 0)]) == [-1, -1]


def test_fleet_on_large_map_is_fast():
    n = 400
    grid = parse(random_map(n, 0.2, 0.05, seed=11))
    rng = random.Random(5)
    starts = [(rng.randrange(n), rng.randrange(n)) for _ in range(5000)]
    starts = [s for s in starts if grid.rows[s[0]][s[1]] != "#"]
    t0 = time.perf_counter()
    result = route_many(grid, starts)
    elapsed = time.perf_counter() - t0
    assert len(result) == len(starts)
    assert elapsed < LIMIT_SECONDS, f"{elapsed:.2f}s for {len(starts)} robots"
