# Build Order: interviewer notes (don't show these to the learner)

**Timebox:** 60 min. Stage 1 about 10 min, stage 2 about 25 min, stage 3 is a bonus.
**Mirrors:** CtCI 4.7 Build Order, reframed as a real multi-file codebase. It tests topological sort, cycle detection and scale.

## Setup
Copy the project, but not `tutor/`, to `workspace/21-ai-rounds/build-order/`. At the start, 2 of the 5 tests fail: both cycle tests say "DID NOT RAISE".

## Stage 1: bug, explanation, complexity
**Brief:** "A user reported that a circular dependency got 'installed' without any error. Find and fix the bug, then explain the algorithm and its complexity."
- **The bug:** the DFS uses a single `visited` set, so a back edge looks like "already done" and cycles go unnoticed. The `len(order) != len(packages)` check at the end looks like cycle detection but can never fire. That's a deliberate red herring.
- **Good fixes:** three-state DFS (unvisited, visiting, done), raising when a "visiting" node is reached. Or rewrite with Kahn's algorithm, where leftover nodes mean a cycle.
- **Expect:** O(V + E). The learner should explain why the length check is useless.
- **[Assistant] behaviour:** if asked, it suggests "the length check handles cycles" (wrong). Did the learner verify that claim against a failing test?

## Stage 2: targets, deterministic order, cycle report
**Brief:** "Add `install_plan(graph, targets=None)`:
1. install only the targets and their transitive dependencies (None means everything);
2. make the order deterministic: whenever several packages are ready, install the alphabetically smallest first;
3. on a cycle, raise `CycleError` with a `.cycle` attribute such as `[web, auth, session, web]`, where each package depends on the next.
Keep `install_order` working."
- Copy in `tutor/test_stage2.py`.
- **Key insight:** Kahn's algorithm with a **min-heap** of ready packages gives the smallest valid order, which DFS can't easily do. The closure is a graph search from the targets. To report the cycle, walk dependencies among the leftover nodes until one repeats.
- **Traps:** building the in-degree over the whole graph rather than just the closure, so packages that were never requested block the plan. Reporting leftover nodes that aren't themselves in the cycle.
- **[Assistant] behaviour:** plant a mistake. Offer a plain FIFO queue instead of a heap. `test_smallest_ready_first` catches it.

## Stage 3: monorepo scale (bonus)
**Brief:** "Our monorepo has 200k packages and chains 200k deep. Make it fast and robust."
- Copy in `tutor/test_stage3.py`.
- **Key insight:** recursive DFS blows the recursion limit on the deep chain, so everything must be **iterative**: the closure, the ordering and the cycle search. Kahn plus a heap is O((V + E) log V).
- **Trap:** "just raise `sys.setrecursionlimit`". The learner should explain why that's fragile: it can crash the interpreter with a C stack overflow.

## Grading (1–4 each)
| Dimension | 4 looks like |
|---|---|
| Problem solving | spotted the red-herring length check, and chose Kahn plus a heap for determinism with a reason |
| Code quality | closure, ordering and cycle search as separate helpers; no recursion in the final version |
| Verification | added a self-loop case and a cycle-outside-the-targets case before being told |
| Communication | explained the determinism rule and the cycle-report invariant clearly |

Reference solution: `tutor/solution/resolver.py`.
