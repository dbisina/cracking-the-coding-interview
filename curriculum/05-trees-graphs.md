# Module 05: Trees & Graphs (Ch. 4)

**Book:** concepts on PDF p.112–120 (`book.py section ch4`): tree types p.112–115, traversals p.115, heaps p.115–116, tries p.117, graphs p.117–119, BFS/DFS and bidirectional search p.119–120 · questions on p.121–123 · solutions on p.253–287
**Prereqs:** 00–04 · **Time:** 10–14 h (the biggest data-structure module)

## Objectives
1. Tell apart binary tree vs. BST, balanced, complete, full and perfect trees, and ask which one applies.
2. Write in-order, pre-order and post-order traversals recursively, and know what each is used for.
3. Explain min-heap insert and extract (bubble up/down, O(log n)) and trie prefix lookup.
4. Represent a graph as an adjacency list or matrix, and implement BFS and DFS with a visited set.
5. Recognise topological sort, bidirectional BFS and "return information up the recursion" patterns.

## Diagnostic
1. What's the difference between a binary tree and a binary search tree?
2. For shortest path in an unweighted graph, BFS or DFS?

<details><summary>Answer key</summary>

1. A BST requires every node in the left subtree to be ≤ the node and every node in the right subtree to be > it (the exact rule on duplicates varies, so ask). A binary tree has no ordering.
2. BFS. It explores in layers of increasing distance.
</details>

---

## Concept checks

### C1. Tree vocabulary
Teach: A **binary tree** has at most 2 children per node. A **BST** is ordered across whole subtrees, not just between parent and immediate children. A tree is **balanced** when it's roughly O(log n) tall (red-black, AVL). **Complete**: every level full except possibly the last, which fills left to right. **Full**: every node has 0 or 2 children. **Perfect**: both full and complete, with 2^k − 1 nodes.

**Q:** Is this a valid BST? Root 8, left child 4, and 4's right child 10.
<details><summary>Answer key</summary>
No. 10 is in 8's left subtree, so it must be ≤ 8. Checking only parent against child misses this. (It's the trap in 4.5.)
</details>

### C2. Traversals
Teach: **In-order** (left, node, right) visits a BST in sorted order. **Pre-order** (node, then children) is used for copying or serializing a tree. **Post-order** (children, then node) is used for deleting a tree or computing values from the children upward (heights, sizes).

**Q:** You want each subtree's height, and you want to use it to decide whether the tree is balanced. Which traversal order, and why?
<details><summary>Answer key</summary>
Post-order. You need both children's heights before you can compute the node's height and check balance. (This is 4.4.)
</details>

### C3. Binary heaps
Teach: A min-heap is a complete binary tree where each node ≤ its children, stored in an array. **Insert**: add at the bottom-right, then bubble up by swapping with the parent: O(log n). **Extract min**: take the root, move the last element to the root, then bubble down by swapping with the smaller child: O(log n).

**Q:** In an array-backed heap with 0-indexing, where are the children and parent of index i?
<details><summary>Answer key</summary>
The children are at 2i+1 and 2i+2. The parent is at (i−1)/2, using integer division.
</details>

### C4. Tries
Teach: A trie (prefix tree) stores characters on the paths from the root, with a terminator flag marking complete words. Checking whether a prefix exists is O(K) for a K-character string, which is as fast as a hash lookup, and it also answers prefix questions that a hash table can't. Tries are used for autocomplete and word games.

**Q:** Why can a trie beat a hash set when searching a dictionary for words while building them letter by letter?
<details><summary>Answer key</summary>
After each letter you can ask "is this a valid prefix?" in O(1) by stepping one node down, and stop early when it isn't. A hash set would need you to hash every prefix again.
</details>

### C5. Graph representations
Teach: An **adjacency list** gives each node a list of neighbours: space O(V+E), which is best for sparse graphs. An **adjacency matrix** is a V×V boolean table: O(V²) space and an O(1) edge check, but finding a node's neighbours is O(V). Graphs can be disconnected, so loop over every node when you need to search all of them.

**Q:** A social network has 1 billion users with about 200 friends each. Which representation should you use, and why?
<details><summary>Answer key</summary>
An adjacency list. The graph is very sparse (E ≈ 10¹¹ while V² = 10¹⁸), so a matrix would be impossibly large.
</details>

### C6. DFS vs. BFS
Teach: **DFS** goes deep first, using recursion or a stack. It's good for visiting every node and for path existence. **BFS** goes level by level using a queue, which gives shortest paths in unweighted graphs. Both **must mark nodes visited**, otherwise cycles cause infinite loops. **Bidirectional BFS** searches from both ends. With branching factor k and distance d, it explores about k^(d/2) nodes from each side instead of k^d.

**Q:** Where does a missing `visited` check hurt you in graph search but never in tree traversal?
<details><summary>Answer key</summary>
When the graph has cycles, or when several paths lead to the same node. Trees have neither: each node has exactly one parent.
</details>

### C7. Topological sort (preview of 4.7)
Teach: To order the nodes of a directed acyclic graph (DAG) so every edge points forward, either (a) repeatedly take a node with in-degree 0, remove its outgoing edges and repeat (Kahn's algorithm), or (b) run DFS and add each node to the front of the result when it finishes. Either way it's O(V+E). If nodes remain that were never processed, there's a cycle.

**Q:** In Kahn's algorithm, how do you detect a cycle?
<details><summary>Answer key</summary>
If the queue of in-degree-0 nodes empties before every node has been output, the remaining nodes are in a cycle.
</details>

### C8. Returning information up the recursion
Teach: Many tree problems become O(n) instead of O(n log n) or O(n²) when each recursive call **returns several facts at once**: its height together with an "unbalanced" flag, a "found p and found q" pair, or a min/max range. Don't recompute things per node. Return them.

**Q:** A naive balance check calls `height()` at every node. Why is that O(n log n) on a balanced tree, and how do you fix it?
<details><summary>Answer key</summary>
Each node's height is recomputed once for every ancestor, and a balanced tree has log n levels of ancestors, giving O(n log n). Fix it by returning the height, or an error sentinel such as −∞ or −1, from a single post-order pass: O(n).
</details>

---

## Problem ladder

| # | Problem | Tier | Pattern | Target | Key insight |
|---|---|---|---|---|---|
| 4.1 | Route Between Nodes | ★ | bfs/dfs | O(V+E) | BFS from the start with a visited set. Bidirectional BFS is a bonus |
| 4.2 | Minimal Tree | ★ | divide-conquer | O(n) | Make the middle element the root, then recurse on each half |
| 4.3 | List of Depths | ★ | bfs · dfs | O(n) | BFS level by level, or DFS passing the level index |
| 4.4 | Check Balanced | ★ | recursion (return info) | O(n) | Return the height, or an error sentinel that short-circuits |
| 4.5 | Validate BST | ★ | recursion | O(n) | Pass (min, max) bounds down. Or check that the in-order sequence is strictly increasing (careful with duplicates) |
| 4.6 | Successor | ★ | tree nav | O(h) | If there's a right child, take the leftmost node of the right subtree. Otherwise climb until you arrive from a left child |
| 4.7 | Build Order | ★ | topo-sort | O(P+D) | Kahn's algorithm or DFS post-order. Detect cycles |
| 4.8 | First Common Ancestor | ★ | recursion (return info) | O(n) | Recurse and return what was found. The first node where p and q are in different subtrees is the answer |
| 4.9 | BST Sequences | ☆ | backtracking | exponential (output-bound) | Weave the left and right sequences, preserving the relative order within each |
| 4.10 | Check Subtree | ★ | recursion · string | O(n+m) or O(nm) worst | Pre-order strings with null markers plus a substring check, or a recursive match starting at every node whose value equals the root of T2 |
| 4.11 | Random Node | ☆ | augmented tree | O(h) | Store subtree sizes, then choose left, self or right proportionally |
| 4.12 | Paths with Sum | ★ | prefix-sum · hash-map | O(n) | Running sum from the root plus a map of prefix-sum counts. Increment on the way down, decrement on the way back up |

**Test prompts:** an empty tree, a single node, a degenerate tree that's effectively a list, duplicate values (4.5), a node that is its own ancestor (4.8), the last node in in-order (4.6), a dependency cycle (4.7), and negative values (4.12).

## Common pitfalls
- 4.5: checking only against the immediate children (see C1).
- 4.8: assuming both nodes exist in the tree. Handle the case where one is missing.
- 4.7: ignoring projects that have no dependencies at all.
- 4.12: forgetting to decrement the prefix-sum count when backtracking.
- Graph BFS: marking a node visited when it's dequeued instead of when it's enqueued, which queues duplicates.

## Exit quiz (≥ 5/6)
1. Which traversal gives a BST in sorted order?
2. How do you validate a BST in O(n)?
3. What are the costs of heap insert and extract-min, and why?
4. BFS vs. DFS: which do you choose, for what, and what data structure does each use?
5. Topological sort: the algorithm and how it detects a cycle.
6. Paths with Sum in O(n): what's the key idea?

<details><summary>Answer key</summary>

1. In-order.
2. Recurse with (min, max) bounds that tighten as you go down.
3. O(log n) each. You bubble along one root-to-leaf path of a complete tree, whose height is log n.
4. BFS uses a queue and gives shortest paths in unweighted graphs. DFS uses a stack or recursion and is for exhaustive search or path existence.
5. Kahn's algorithm: repeatedly take in-degree-0 nodes. If nodes remain unprocessed, there's a cycle.
6. Keep a running prefix sum and a hash map from prefix sum to count. The number of paths ending at the current node is `count[running - target]`.
</details>

## Flashcards
- In-order of a BST? → **sorted**
- Heap children of i? → **2i+1, 2i+2**
- Shortest path, unweighted? → **BFS**
- Balanced check in O(n)? → **return height or sentinel, post-order**
- Successor with no right child? → **climb until you come from the left**
- Topological sort? → **in-degree 0 queue (Kahn's)**
