"""Stage 2 tests: copy next to resolver.py when stage 2 starts.

New API: install_plan(graph, targets=None) -> list[str]
- installs only `targets` plus everything they (transitively) depend on; None means all packages
- deterministic: whenever several packages are ready, the alphabetically smallest goes first
- on a cycle, raises CycleError with attribute `cycle`: [a, b, ..., a], each depending on the next
"""
import pytest

from graph import CycleError, from_manifest
from resolver import install_order, install_plan

MANIFEST = """
app: web db
web: http json
db: net
http: net
json:
net:
cli: json
docs:
"""


def test_smallest_ready_first():
    g = from_manifest(MANIFEST)
    assert install_plan(g) == ["docs", "json", "cli", "net", "db", "http", "web", "app"]


def test_only_what_targets_need():
    g = from_manifest(MANIFEST)
    assert install_plan(g, ["web"]) == ["json", "net", "http", "web"]
    assert install_plan(g, ["cli", "docs"]) == ["docs", "json", "cli"]


def test_unknown_target():
    g = from_manifest(MANIFEST)
    with pytest.raises(KeyError):
        install_plan(g, ["nope"])


def test_install_order_still_works():
    g = from_manifest(MANIFEST)
    assert install_order(g) == install_plan(g)


def check_cycle(err: CycleError, graph) -> None:
    cycle = err.cycle
    assert len(cycle) >= 2 and cycle[0] == cycle[-1]
    for a, b in zip(cycle, cycle[1:]):
        assert b in graph.dependencies(a), f"{a} does not depend on {b}"


def test_cycle_is_reported():
    g = from_manifest("""
app: web
web: auth
auth: session
session: web
""")
    with pytest.raises(CycleError) as info:
        install_plan(g)
    check_cycle(info.value, g)
    assert set(info.value.cycle) == {"web", "auth", "session"}


def test_cycle_outside_targets_is_ignored():
    g = from_manifest("""
app: lib
lib:
x: y
y: x
""")
    assert install_plan(g, ["app"]) == ["lib", "app"]
    with pytest.raises(CycleError):
        install_plan(g)
