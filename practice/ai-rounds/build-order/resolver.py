"""Compute an install order: every package after all of its dependencies."""
from graph import CycleError, DependencyGraph


def install_order(graph: DependencyGraph) -> list[str]:
    order: list[str] = []
    visited: set[str] = set()

    def visit(pkg: str) -> None:
        if pkg in visited:
            return
        visited.add(pkg)
        for dep in sorted(graph.dependencies(pkg)):
            visit(dep)
        order.append(pkg)

    for pkg in sorted(graph.packages):
        visit(pkg)
    if len(order) != len(graph.packages):
        raise CycleError("dependency cycle detected")
    return order
