"""Package dependency graph for a tiny package manager."""
from collections import defaultdict


class CycleError(Exception):
    """Raised when dependencies form a cycle and no install order exists."""


class DependencyGraph:
    def __init__(self) -> None:
        self.packages: set[str] = set()
        self.deps: dict[str, set[str]] = defaultdict(set)

    def add_package(self, name: str) -> None:
        self.packages.add(name)

    def add_dependency(self, package: str, depends_on: str) -> None:
        """`package` needs `depends_on` installed first."""
        self.add_package(package)
        self.add_package(depends_on)
        self.deps[package].add(depends_on)

    def dependencies(self, package: str) -> set[str]:
        return self.deps.get(package, set())


def from_manifest(text: str) -> DependencyGraph:
    """Parse lines like `web: http json` (web depends on http and json)."""
    graph = DependencyGraph()
    for line in text.strip().splitlines():
        name, _, rest = line.partition(":")
        graph.add_package(name.strip())
        for dep in rest.split():
            graph.add_dependency(name.strip(), dep)
    return graph
