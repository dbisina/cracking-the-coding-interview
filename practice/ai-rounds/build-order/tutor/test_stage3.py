"""Stage 3 tests: monorepo-scale graphs. Copy next to resolver.py when stage 3 starts."""
import random
import time

import pytest

from graph import CycleError, DependencyGraph
from resolver import install_plan

LIMIT_SECONDS = 6.0


def name(i: int) -> str:
    return f"pkg{i:06d}"


def test_very_deep_chain():
    n = 200_000
    g = DependencyGraph()
    for i in range(n - 1):
        g.add_dependency(name(i), name(i + 1))  # pkg000000 sits on top of a 200k-deep chain
    t0 = time.perf_counter()
    order = install_plan(g, [name(0)])
    assert time.perf_counter() - t0 < LIMIT_SECONDS
    assert order[0] == name(n - 1) and order[-1] == name(0) and len(order) == n


def test_wide_random_dag():
    rng = random.Random(42)
    n, edges = 100_000, 400_000
    g = DependencyGraph()
    for i in range(n):
        g.add_package(name(i))
    for _ in range(edges):
        a, b = rng.randrange(n), rng.randrange(n)
        if a != b:
            hi, lo = max(a, b), min(a, b)
            g.add_dependency(name(hi), name(lo))  # edges only point to lower ids: acyclic
    t0 = time.perf_counter()
    order = install_plan(g)
    assert time.perf_counter() - t0 < LIMIT_SECONDS
    pos = {p: i for i, p in enumerate(order)}
    for p in rng.sample(sorted(g.packages), 2000):
        for d in g.dependencies(p):
            assert pos[d] < pos[p]


def test_deep_cycle_reported_fast():
    n = 150_000
    g = DependencyGraph()
    for i in range(n - 1):
        g.add_dependency(name(i), name(i + 1))
    g.add_dependency(name(n - 1), name(0))
    t0 = time.perf_counter()
    with pytest.raises(CycleError) as info:
        install_plan(g)
    assert time.perf_counter() - t0 < LIMIT_SECONDS
    assert len(info.value.cycle) == n + 1
