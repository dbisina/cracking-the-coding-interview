# Module 04: Stacks & Queues (Ch. 3)

**Book:** concepts on PDF p.108–109 (`book.py section ch3`) · questions on p.110–111 · solutions on p.239–253
**Prereqs:** 03 · **Time:** 3–5 h

## Objectives
1. Implement a stack (LIFO) and a queue (FIFO) on top of a linked list, with O(1) operations.
2. Know where each is used: stacks for recursion, backtracking and undo; queues for BFS, buffering and caches.
3. Augment a stack to track extra state (such as the min) in O(1).
4. Build one structure out of another (a queue from two stacks) and analyse the amortized cost.

---

## Concept checks

### C1. Stack basics
Teach: A stack supports `push`, `pop`, `peek` and `isEmpty`, all O(1). It's a natural fit for recursive algorithms made iterative, because you push temporary data and pop it when you backtrack.

**Q:** How would you check whether brackets like `([]{})` are balanced?
<details><summary>Answer key</summary>
Push each opening bracket. On a closing bracket, pop and check that it matches. At the end the stack must be empty. O(n).
</details>

### C2. Queue basics
Teach: A queue supports `add`, `remove`, `peek` and `isEmpty`, all O(1) with head and tail pointers. It's the core of **BFS** and of processing items in arrival order. Watch the empty-queue edge case: removing the last element must also clear the tail.

**Q:** In a linked-list queue, what bug happens if `remove()` empties the queue but forgets to reset `last`?
<details><summary>Answer key</summary>
`last` still points to the removed node. The next `add` links the new node onto that stale node while `first` is null, so the new element is lost and the queue is corrupted.
</details>

### C3. Augmenting a stack
Teach: You can store extra information alongside each element, such as "the min at this depth". Because a stack only changes at the top, per-node state stays valid until that node is popped.

**Q:** How do you make `min()` O(1) on a stack?
<details><summary>Answer key</summary>
Either store (value, minSoFar) in each node, or keep a second stack that you push to only when `value <= currentMin` and pop from when the popped value equals the min. The second version saves space when there are many non-min pushes.
</details>

### C4. Amortized analysis with two stacks
Teach: A queue made of two stacks (inbox and outbox): push to the inbox. To pop, if the outbox is empty, move everything from the inbox into it (this reverses the order), then pop the outbox. Each element moves at most once, so operations are O(1) amortized.

**Q:** Why is it important to only move elements when the outbox is empty?
<details><summary>Answer key</summary>
If you moved elements while the outbox still had items, new elements would end up on top of older ones and break FIFO order. Moving lazily also means each element is transferred only once, which is what makes the cost amortized O(1).
</details>

---

## Problem ladder

| # | Problem | Tier | Pattern | Target | Key insight |
|---|---|---|---|---|---|
| 3.1 | Three in One | ☆ | design | O(1) ops | Fixed thirds are simple. A flexible split shifts neighbouring stacks, treating the array as circular |
| 3.2 | Stack Min | ★ | stack (augmented) | O(1) all ops | A second stack of mins |
| 3.3 | Stack of Plates | ☆ | design | O(1) push/pop; popAt may roll over | A list of stacks. With popAt, decide whether to shift bottoms up to keep stacks full |
| 3.4 | Queue via Stacks | ★ | stack · amortized | O(1) amortized | Inbox/outbox with lazy transfer |
| 3.5 | Sort Stack | ★ | stack | O(n²) time, O(n) space | Insertion sort using one temp stack: pop r, move larger items back, place r |
| 3.6 | Animal Shelter | ★ | queue | O(1) | Separate dog and cat queues with an arrival timestamp. dequeueAny compares the two heads |

**Test prompts:** pop or peek on empty, min after popping the min (3.2), popAt on the last stack or a middle one (3.3), interleaved push/pop (3.4), already sorted and reverse sorted input (3.5), and only-cats or only-dogs (3.6).

## Common pitfalls
- 3.2: pushing onto the min stack with `<` instead of `<=`, which breaks duplicate mins.
- 3.4: transferring on every pop.
- Not deciding up front what an empty pop does (throw an exception or return null).

## Exit quiz (≥ 3/4)
1. What does a queue built from two stacks cost per operation, and why?
2. How do you get the min of a stack in O(1)?
3. Which search uses a queue and which uses a stack?
4. What are the time and space costs of sorting a stack using one extra stack?

<details><summary>Answer key</summary>

1. O(1) amortized, because each element is moved at most once.
2. Keep a second stack of mins (push when ≤ the current min, pop when equal to it).
3. BFS uses a queue. DFS uses a stack (or recursion).
4. O(n²) time and O(n) space.
</details>

## Flashcards
- Queue from stacks? → **inbox/outbox, lazy transfer**
- Min stack? → **second stack; push if ≤ min**
- BFS uses? → **a queue**
- Undo/backtracking uses? → **a stack**
