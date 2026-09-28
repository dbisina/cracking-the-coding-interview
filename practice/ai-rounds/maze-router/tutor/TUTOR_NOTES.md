# Maze Router: interviewer notes (don't show these to the learner)

**Timebox:** 60 min. About 5 min orientation, stage 1 about 10 min, stage 2 about 25 min, stage 3 is a bonus.
**Mirrors:** Meta's AI-enabled round (grid BFS with directional constraints).

## Setup
Copy the project, but not `tutor/`, to `workspace/21-ai-rounds/maze-router/`. The learner runs `python -m pytest -q`. At the start, 2 of the 5 tests fail.

## Stage 1: bug, explanation, complexity
**Brief:** "Some route lengths come out too long. Find and fix the bug, then explain the algorithm and its complexity."
- **The bug:** `router.py` uses a single `steps` counter that goes up on every *dequeue*, so it counts cells visited rather than BFS levels. It passes on a straight corridor, where each level has exactly one cell, and fails in open rooms.
- **Good fixes:** store the distance with each queued cell `(cell, d)`, or process the queue level by level.
- **Expect:** O(H·W) time and space. The learner should explain why marking cells visited at enqueue time is correct and efficient.
- **[Assistant] behaviour:** if asked "what's wrong", reply vaguely ("BFS logic looks standard; check how distance is tracked") rather than naming the line.

## Stage 2: conveyors, keys and doors
**Brief:** "The warehouse added new tiles:
- `^ v < >` are conveyors. While standing on one, the robot's **next move must go in the arrow's direction**. It can enter a conveyor from any side.
- `a`–`d` are keys, picked up by stepping on them. `A`–`D` are doors, passable only while holding the matching key. Keys are kept.
Update `shortest_path` to support these."
- Copy in `tutor/test_stage2.py` once the learner has sketched an approach.
- **Key insight:** the state becomes (cell, keys bitmask), giving at most H·W·16 states, still with BFS. Conveyors restrict the outgoing moves from that tile.
- **Traps:** 'E' falls inside A–F, so a lazy `isupper()` door check treats the exit as a door (this is why the doors are A–D). Keeping visited per cell only, rather than per (cell, keys), fails `test_must_fetch_key_behind_you`.
- **[Assistant] behaviour:** it will write the bitmask boilerplate if asked specifically. Plant one mistake: suggest `visited` keyed on the cell only. Did the learner catch it?

## Stage 3: fleet routing (bonus)
**Brief:** "There are now thousands of robots. Add `route_many(grid, starts) -> list[int]` giving each robot's distance to E. Stage 3 maps have walls and conveyors but no keys. It needs to be fast for 5,000 robots on a 400×400 map."
- Copy in `tutor/test_stage3.py`.
- **Key insight:** run **one reverse BFS from E**. There's an edge v ← u when u can step into v (u isn't a wall, and if u is a conveyor its arrow points at v). That's O(H·W + Q) instead of O(Q·H·W).
- **Trap:** reversing conveyor edges the wrong way round. `test_matches_single_queries_on_small_maps` catches it by comparing against stage 2's single-query BFS.
- Not finishing stage 3 is fine. Grade the reasoning: did they identify "many sources, one target → reverse the search"?

## Grading (1–4 each)
| Dimension | 4 looks like |
|---|---|
| Problem solving | named the BFS-level bug, the bitmask state, and the reverse BFS before coding |
| Code quality | small functions, clear state tuple, no dead code left over from AI suggestions |
| Verification | ran the tests after every paste, added their own edge case (start == end, unreachable) |
| Communication | narrated each AI interaction before and after, and explained every line they kept |

Reference solution: `tutor/solution/router.py` (a drop-in replacement for `router.py`, using the original `grid.py`).
