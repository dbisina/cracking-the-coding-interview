from grid import parse
from router import shortest_path


def test_straight_corridor():
    assert shortest_path(parse("S...E")) == 4


def test_start_is_exit_neighbor():
    assert shortest_path(parse("SE")) == 1


def test_unreachable():
    grid = parse("""
S.#..
..#.E
""")
    assert shortest_path(grid) == -1


def test_open_room():
    grid = parse("""
S....
.....
....E
""")
    assert shortest_path(grid) == 6


def test_detour_around_wall():
    grid = parse("""
S.#.E
..#..
.....
""")
    assert shortest_path(grid) == 8
