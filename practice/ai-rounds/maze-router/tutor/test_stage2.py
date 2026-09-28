"""Stage 2 tests: copy next to router.py when stage 2 starts."""
from grid import parse
from router import shortest_path


def test_conveyor_forces_direction():
    # Standing on '>' you must move right next.
    grid = parse("""
S>..E
.....
""")
    assert shortest_path(grid) == 4


def test_conveyor_blocks_shortcut():
    # 'v' at (0,1) pushes the robot down, so the top row can't be used past it.
    grid = parse("""
Sv#E
....
""")
    assert shortest_path(grid) == 5


def test_conveyor_into_wall_is_dead_end():
    grid = parse("""
S<#E
.#..
....
""")
    assert shortest_path(grid) == 7


def test_key_opens_door():
    grid = parse("""
S.A.E
a.#..
""")
    assert shortest_path(grid) == 6


def test_door_without_key_is_wall():
    grid = parse("""
S#E
.B.
...
""")
    assert shortest_path(grid) == 6


def test_must_fetch_key_behind_you():
    grid = parse("""
.#####
a.S.AE
""")
    assert shortest_path(grid) == 7


def test_locked_out():
    assert shortest_path(parse("S.C.E")) == -1
