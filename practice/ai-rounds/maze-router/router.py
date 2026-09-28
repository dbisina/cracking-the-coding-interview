"""Shortest route for the warehouse robot."""
from collections import deque

from grid import Grid


def shortest_path(grid: Grid) -> int:
    """Number of moves from S to E, or -1 if E is unreachable."""
    queue = deque([grid.start])
    seen = {grid.start}
    steps = 0
    while queue:
        cell = queue.popleft()
        if cell == grid.end:
            return steps
        for nxt in grid.neighbors(cell):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
        steps += 1
    return -1
