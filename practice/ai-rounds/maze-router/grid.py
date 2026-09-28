"""Grid model for the warehouse robot router.

Map legend:
    .  open floor
    #  wall
    S  robot start (exactly one)
    E  exit (exactly one)
"""
from dataclasses import dataclass

Cell = tuple[int, int]

DIRECTIONS: dict[str, Cell] = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


@dataclass(frozen=True)
class Grid:
    rows: list[str]
    start: Cell
    end: Cell

    @property
    def height(self) -> int:
        return len(self.rows)

    @property
    def width(self) -> int:
        return len(self.rows[0]) if self.rows else 0

    def tile(self, cell: Cell) -> str:
        r, c = cell
        return self.rows[r][c]

    def in_bounds(self, cell: Cell) -> bool:
        r, c = cell
        return 0 <= r < self.height and 0 <= c < self.width

    def walkable(self, cell: Cell) -> bool:
        return self.in_bounds(cell) and self.tile(cell) != "#"

    def neighbors(self, cell: Cell) -> list[Cell]:
        r, c = cell
        out = []
        for dr, dc in DIRECTIONS.values():
            nxt = (r + dr, c + dc)
            if self.walkable(nxt):
                out.append(nxt)
        return out


def parse(text: str) -> Grid:
    rows = [line for line in text.strip().splitlines()]
    if len({len(r) for r in rows}) != 1:
        raise ValueError("grid must be rectangular")
    start = end = None
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == "S":
                start = (r, c)
            elif ch == "E":
                end = (r, c)
    if start is None or end is None:
        raise ValueError("grid needs one S and one E")
    return Grid(rows, start, end)
