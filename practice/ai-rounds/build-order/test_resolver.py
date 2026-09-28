import pytest

from graph import CycleError, from_manifest
from resolver import install_order


def assert_valid(order, graph):
    pos = {p: i for i, p in enumerate(order)}
    assert set(order) == graph.packages
    for pkg in graph.packages:
        for dep in graph.dependencies(pkg):
            assert pos[dep] < pos[pkg], f"{dep} must come before {pkg}"


def test_chain():
    g = from_manifest("""
app: web
web: http
http:
""")
    assert install_order(g) == ["http", "web", "app"]


def test_diamond():
    g = from_manifest("""
app: web db
web: core
db: core
core:
""")
    assert_valid(install_order(g), g)


def test_independent_packages():
    g = from_manifest("""
a:
b:
c:
""")
    assert sorted(install_order(g)) == ["a", "b", "c"]


def test_self_cycle_rejected():
    g = from_manifest("a: a")
    with pytest.raises(CycleError):
        install_order(g)


def test_cycle_rejected():
    g = from_manifest("""
a: b
b: c
c: a
""")
    with pytest.raises(CycleError):
        install_order(g)
