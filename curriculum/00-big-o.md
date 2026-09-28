# Module 00: Big O

**Book:** Ch. VI, PDF p.50–71 (`book.py section big-o`). The worked Examples 1–16 are on p.58–66 and the Additional Problems VI.1–VI.12 are on p.67–68, with answers after them.
**Prereqs:** none · **Time:** 4–6 h

## Objectives
By the end, the learner can:
1. State the time and space complexity of any loop, nested loop or recursive function, and justify it.
2. Apply the rules: drop constants, drop non-dominant terms, add vs. multiply.
3. Explain amortized time using the dynamic-array example.
4. Recognise O(log n) and O(branches^depth) patterns on sight.
5. Use the right variables: two different inputs mean two variables, so `O(a·b)`, not `O(n²)`.

## Diagnostic (for onboarding)
1. What's the runtime of looping over an array, and inside that loop, looping over the same array again?
2. What's the runtime of binary search, and why?
3. What does `f(n) = f(n-1) + f(n-1)` with base case `n<=1` cost?

<details><summary>Answer key</summary>

1. O(n²). There are n outer iterations, each doing n inner iterations.
2. O(log n). Each step halves the search space, so it takes k steps where 2^k = n.
3. O(2ⁿ) time, because each call branches twice and the depth is n. Space is O(n), the call-stack depth.
</details>

---

## Concept checks

### C1. What Big O actually measures
Teach: Big O describes **how runtime grows as the input grows**, not how many seconds something takes. Use the book's analogy (PDF p.50): sending a huge file electronically is O(s) in its size s, while flying a hard drive across the country is O(1). For big enough files, the plane wins. Academics distinguish O (upper bound), Ω (lower bound) and Θ (tight bound). In interviews, "Big O" means the tight bound.

**Q:** Why can an O(n) algorithm be slower than an O(n²) one in practice?
<details><summary>Answer key</summary>
Big O hides constants and lower-order terms. For small n, an O(n) algorithm with a huge constant (say 10,000·n) can lose to one that takes n². Big O only promises what happens as n grows large.
</details>

### C2. Best, worst and expected case
Teach: Quicksort is the canonical example: expected O(n log n), worst O(n²) when pivots are bad, and best case isn't a useful measure. Best/worst/expected describe *which input* you're analysing. O/Ω/Θ describe *how tightly you bound* the runtime for that input. The two ideas are independent.

**Q:** Is "the best case of linear search is O(1)" a useful statement in an interview? Why or why not?
<details><summary>Answer key</summary>
Not really. Almost any algorithm is O(1) on a specially chosen input. Interviewers care about worst case and expected case.
</details>

### C3. Space complexity
Teach: Count the memory you allocate plus the depth of the call stack. A recursive `sum(n)` that calls `sum(n-1)` uses O(n) stack space. A loop that calls a helper n times, where each call returns before the next one starts, uses O(1).

**Q:** A recursive function makes n calls in a chain (each one calls the next). A second function makes n calls one after another from a loop. What's the space cost of each?
<details><summary>Answer key</summary>
The chain uses O(n), because all n frames are on the stack at once. The loop uses O(1), because each call finishes before the next begins.
</details>

### C4. Drop constants and non-dominant terms
Teach: O(2n) becomes O(n). O(n² + n) becomes O(n²). But O(n + m) stays as it is, because there are two inputs and you don't know which one dominates.

**Q:** Simplify: (a) O(N + log N) (b) O(5·2ⁿ + 1000·n¹⁰⁰) (c) O(B² + A)
<details><summary>Answer key</summary>
(a) O(N). (b) O(2ⁿ), because an exponential eventually beats any polynomial. (c) It stays O(B² + A), since A and B are independent.
</details>

### C5. Add vs. multiply
Teach: If you do A, *then* B, the cost is O(A + B). If you do B *for each* A, the cost is O(A·B).

**Q:** Loop over array `a`, then loop over array `b`. Now nest the `b` loop inside the `a` loop. What's the Big O of each?
<details><summary>Answer key</summary>
Sequential: O(a + b). Nested: O(a·b). Using a single n for both is a classic mistake.
</details>

### C6. Amortized time
Teach: A dynamic array (ArrayList, Python list) doubles its capacity when it fills up. That one copy costs O(n), but it happens so rarely that X inserts cost X + X/2 + X/4 + … ≤ 2X copies in total, which is **O(1) amortized** per insert.

**Q:** Why doesn't the occasional O(n) resize make appending O(n)?
<details><summary>Answer key</summary>
The copies form a geometric series that sums to at most 2X for X inserts. Spread across all the inserts, that's a constant amount of work per insert. You can also think of each insert as "prepaying" for one future copy.
</details>

### C7. Log n runtimes
Teach: When the problem space **halves** at each step (binary search, a balanced BST lookup), the step count is k where 2^k = n, so k = log₂ n. The base of the log doesn't matter in Big O.

**Q:** What's the runtime of finding an element in a balanced BST with n nodes? What about an unbalanced one?
<details><summary>Answer key</summary>
Balanced: O(log n), because the height is log n. Unbalanced: O(n) in the worst case, since the tree can degenerate into a linked list. In both cases the cost is really O(depth).
</details>

### C8. Recursive runtimes
Teach: A recursive function that makes **b** calls to itself, with depth **d**, often costs **O(b^d)**. For example, `f(n) = f(n-1) + f(n-1)` is O(2ⁿ). Space is only O(d), because at most d frames are live at once. Memoization collapses repeated subproblems (this previews Module 09).

**Q:** Naive recursive Fibonacci: what's the time and space complexity? What does memoization change it to?
<details><summary>Answer key</summary>
Naive: O(2ⁿ) time (the tight bound is about 1.6ⁿ) and O(n) space. With memoization, each of the n subproblems is computed once, so O(n) time and O(n) space.
</details>

### C9. Book worked examples (drill)
Have the learner work through **Examples 1–16** (PDF p.58–66, `book.py pages 58-66`). Show one example's code at a time, **without the explanation that follows it**. The learner states the runtime and justifies it, then you reveal the book's reasoning. Push hardest on these:
- **Ex 3 / 4**: the inner loop starts at `i+1` (still O(n²)), and two different arrays (O(ab)).
- **Ex 8**: sort each string, then sort the array. The answer is O(a·s(log a + log s)). It's the classic trap.
- **Ex 9**: summing a balanced BST is O(n), even though it has "two recursive calls".
- **Ex 12**: permutations are O(n² · n!) (the n! count, times path length, times printing).
- **Ex 13–14**: Fibonacci, all n values with and without memo.

---

## Pattern toolbox
- One loop over n → O(n). Nested loops over the same input → O(n²).
- "Halve each step" → O(log n).
- "b recursive calls, depth d" → O(b^d) time, O(d) space.
- Sorting → O(n log n) unless the values are bounded (counting sort).
- Hash insert/lookup → O(1) expected, O(n) worst.
- Two independent inputs → two variables.

## Problem ladder

| # | Problem | Tier | Focus |
|---|---|---|---|
| VI.1 | Product via loop | ★ | single loop |
| VI.2 | Power via recursion | ★ | linear recursion |
| VI.3 | Mod via loop | ★ | constant work |
| VI.4 | Division via repeated subtraction | ★ | depends on the ratio a/b |
| VI.5 | Integer sqrt by binary search | ★ | log n |
| VI.6 | Integer sqrt by guessing | ★ | √n |
| VI.7 | Worst-case find in an unbalanced BST | ★ | depth vs. n |
| VI.8 | Find a value in a binary tree that isn't a BST | ★ | no ordering means visiting every node |
| VI.9 | Copy-array append | ☆ | hidden O(n²) |
| VI.10 | Sum of digits | ☆ | number of digits = log₁₀ n |
| VI.11 | Print sorted strings of length k | ☆ | c^k · k |
| VI.12 | Intersection count with a sort + binary search | ☆ | b log b + a log b |

The problems are on PDF p.67–69 and the book's answers follow straight after (`book.py pages 67-71`). **Protocol:** show the code only. The learner answers first, then you reveal the book's answer and discuss any gap.

## Common pitfalls
- Using n for two different inputs.
- Treating "two recursive calls" as automatically O(2ⁿ). Check whether the input halves (as in a BST) or shrinks by one.
- Forgetting the cost of string operations: concatenation or comparison is O(length).
- Forgetting the call stack in space complexity.

## Exit quiz (≥ 4/5 to pass)
1. `for i in range(n): for j in range(i, n): ...` → ?
2. Sorting an array of n strings, each of length at most s → ?
3. Space complexity of recursive DFS on a tree of height h → ?
4. Two sorted arrays of sizes a and b: runtime of merging them → ?
5. Why is appending to a dynamic array O(1) amortized?

<details><summary>Answer key</summary>

1. O(n²), because n + (n−1) + … + 1 = n(n+1)/2.
2. O(s · n log n). Each comparison costs O(s).
3. O(h).
4. O(a + b).
5. The resize copies form a geometric series totalling at most 2X for X inserts (see C6).
</details>

## Flashcards
- Rule for a recursive runtime? → **O(branches^depth)**, but check how the input shrinks.
- O(n + m) vs. O(n·m)? → **"then" adds, "for each" multiplies**
- Binary search runtime and why? → **O(log n), halving each step**
- Space of recursion? → **max stack depth**
- Dynamic array append? → **O(1) amortized, O(n) worst**
