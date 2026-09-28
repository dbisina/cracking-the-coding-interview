# Module 19: Advanced Topics & Code Library (XI–XII)

**Book:** PDF p.640–663. Sections for `book.py section <key>`:
`advanced-math` (p.641–644) · `topological-sort` (p.644–645) · `dijkstra` (p.645–647) · `hash-collisions` (p.648) · `rabin-karp` (p.648–649) · `avl-trees` (p.649–651) · `red-black-trees` (p.651–654) · `mapreduce` (p.654–656) · `code-library` (p.657–663)
**Prereqs:** 05, 09 · **Time:** 3–4 h

These topics rarely come up directly, but they deepen your understanding and show up in follow-up questions. The goal is **fluent explanation**, not memorising code, except for topological sort and Dijkstra, which you should be able to code.

---

## Concept checks

### C1. Useful math
Teach: 1 + 2 + … + n = n(n+1)/2. 2⁰ + 2¹ + … + 2ⁿ = 2ⁿ⁺¹ − 1. Logs of any two bases differ only by a constant factor. There are n! permutations, C(n,k) = n!/(k!(n−k)!) combinations, and 2ⁿ subsets. Know how to prove things by induction.

**Q:** Why is `for i in range(n): for j in range(i+1, n)` exactly n(n−1)/2 iterations?
<details><summary>Answer key</summary>
The inner loop runs n−1, n−2, …, 0 times. That's the sum of 0..n−1, which is n(n−1)/2, and that's O(n²).
</details>

### C2. Topological sort (code it)
Teach: This is Kahn's algorithm from Module 05 C7. Implement it from memory: build in-degree counts, queue the zero-in-degree nodes, pop, output, decrement the neighbours' in-degrees, and queue any that reach zero.

**Q:** Code it for `projects=[a..f]`, `deps=[(a,d),(f,b),(b,d),(f,a),(d,c)]`.
<details><summary>Answer key</summary>
One valid order is e, f, a, b, d, c (e has no edges at all and can go anywhere). Verify that every edge (x, y) has x before y.
</details>

### C3. Dijkstra (code it)
Teach: Shortest paths from a source in a graph with **non-negative** weights. Use a min-priority queue of (distance, node). Pop the closest node and relax its edges. The cost is O((V+E) log V) with a binary heap.

**Q:** Why does Dijkstra fail with negative edge weights? What do you use instead?
<details><summary>Answer key</summary>
Once a node is popped, it's treated as final. A negative edge found later could still give it a shorter path. Use Bellman–Ford instead, which is O(VE) and can also detect negative cycles.
</details>

### C4. Hash collision resolution
Teach: **Chaining** stores a linked list (or a BST) per bucket. **Open addressing** probes for the next slot using linear probing (which clusters), quadratic probing, or double hashing.

**Q:** What's the trade-off of chaining with BSTs instead of linked lists?
<details><summary>Answer key</summary>
The worst case improves from O(n) to O(log n), but there's extra overhead that's rarely worth it unless you expect adversarial or uneven keys. Java 8's HashMap switches a bucket to a tree once it gets large.
</details>

### C5. Rabin–Karp substring search
Teach: Use a rolling hash over a window of length m. Compare hashes, and only compare characters when the hashes match. It's O(n + m) expected and O(nm) worst case with many false positives.

**Q:** How does the rolling hash update in O(1) when the window slides?
<details><summary>Answer key</summary>
Subtract the outgoing character's contribution (char × base^(m−1)), multiply by the base, then add the incoming character. Do all of it modulo a prime.
</details>

### C6. Balanced trees: AVL and red-black
Teach: **AVL** stores a height or balance factor and rotates whenever the balance goes outside {−1, 0, 1}. Its balance is stricter, so lookups are faster. **Red-black** trees use colour rules: the root is black, a red node has black children, and every path has the same black height. They're looser, with fewer rotations on insert, which is why they back TreeMap and `std::map`.

**Q:** Which suits a write-heavy workload better, AVL or red-black? Why?
<details><summary>Answer key</summary>
Red-black. It needs fewer rotations per insert or delete. AVL's stricter balance favours read-heavy workloads.
</details>

### C7. MapReduce
Teach: **Map** turns input records into (key, value) pairs. The framework shuffles and groups them by key. **Reduce** aggregates each key's values. The canonical example is word count.

**Q:** Write the map and reduce functions for "average temperature per city".
<details><summary>Answer key</summary>
Map: emit (city, (temp, 1)). Reduce: sum the temps and counts, then emit (city, total / count). Emitting pairs lets a combiner pre-aggregate safely.
</details>

### C8. Code library
Teach: The book's helper classes are HashMapList (a map from key to a list of values), TreeNode, LinkedListNode, and Trie/TrieNode. Have the learner **write their own versions in their language** in `workspace/19-advanced/lib.*` and reuse them in the Module 17 and 18 problems.

## Exit quiz (≥ 4/5)
1. The sum of 1..n and the sum of 2⁰..2ⁿ.
2. Dijkstra's complexity and its limitation.
3. Chaining vs. open addressing.
4. The rolling hash idea.
5. AVL vs. red-black: which suits which workload?

<details><summary>Answer key</summary>

1. n(n+1)/2 and 2ⁿ⁺¹ − 1.
2. O((V+E) log V). It needs non-negative weights.
3. Chaining stores lists (or trees) per bucket. Open addressing probes other slots in the same array.
4. Update the hash in O(1) per slide and compare characters only when the hashes match.
5. AVL for read-heavy workloads, red-black for write-heavy ones.
</details>
