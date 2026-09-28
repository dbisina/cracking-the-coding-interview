"""Reference solution covering stages 1-3. Drop-in replacement for ../../resolver.py (uses the original graph.py)."""
import heapq

from graph import CycleError, DependencyGraph


def _closure(graph: DependencyGraph, targets: list[str]) -> set[str]:
    needed: set[str] = set()
    stack = list(targets)
    while stack:  # iterative: stage 3 graphs are too deep for recursion
        pkg = stack.pop()
        if pkg in needed:
            continue
        if pkg not in graph.packages:
            raise KeyError(f"unknown package {pkg!r}")
        needed.add(pkg)
        stack.extend(graph.dependencies(pkg))
    return needed


def _find_cycle(graph: DependencyGraph, remaining: set[str]) -> list[str]:
    """Every leftover node after Kahn still has a leftover dependency, so walking deps must loop."""
    pos: dict[str, int] = {}
    path: list[str] = []
    node = min(remaining)
    while node not in pos:
        pos[node] = len(path)
        path.append(node)
        node = min(d for d in graph.dependencies(node) if d in remaining)
    return path[pos[node]:] + [node]


def install_plan(graph: DependencyGraph, targets: list[str] | None = None) -> list[str]:
    """Stage 2+3: Kahn's algorithm with a min-heap.

    - only the targets and their transitive dependencies (all packages if targets is None)
    - among packages that are ready, install the alphabetically smallest first
    - cycles raise CycleError with `.cycle` = [a, b, ..., a] where each depends on the next
    O((V + E) log V), no recursion.
    """
    needed = set(graph.packages) if targets is None else _closure(graph, targets)
    waiting_on = {p: sum(1 for d in graph.dependencies(p) if d in needed) for p in needed}
    dependents: dict[str, list[str]] = {p: [] for p in needed}
    for p in needed:
        for d in graph.dependencies(p):
            if d in needed:
                dependents[d].append(p)

    ready = [p for p, n in waiting_on.items() if n == 0]
    heapq.heapify(ready)
    order: list[str] = []
    while ready:
        pkg = heapq.heappop(ready)
        order.append(pkg)
        for nxt in dependents[pkg]:
            waiting_on[nxt] -= 1
            if waiting_on[nxt] == 0:
                heapq.heappush(ready, nxt)

    if len(order) != len(needed):
        cycle = _find_cycle(graph, needed - set(order))
        err = CycleError("dependency cycle: " + " -> ".join(cycle))
        err.cycle = cycle
        raise err
    return order


def install_order(graph: DependencyGraph) -> list[str]:
    """Stage 1 fix: cycles are detected (Kahn leaves nodes behind) instead of silently ignored."""
    return install_plan(graph)
