# Module 09: Recursion & Dynamic Programming (Ch. 8)

**Book:** concepts on PDF p.142–145 (`book.py section ch8`): bottom-up, top-down, half-and-half, recursive vs. iterative, and memoization using Fibonacci · questions on p.146–148 · solutions on p.354–383
**Prereqs:** 00, 05 · **Time:** 10–14 h (the highest-value module for interviews)

## Objectives
1. Recognise recursive problems from wording like "compute all", "list the first n", or "the n-th".
2. Pick an approach: **bottom-up**, **top-down**, or **half-and-half**.
3. Turn exponential recursion into polynomial time with **memoization** (top-down) or **tabulation** (bottom-up), and then cut space where possible.
4. Draw the recursion tree and use it to derive time and space.
5. Write backtracking solutions (permutations, subsets, N-Queens) with clean pruning.

## Diagnostic
1. Naive recursive `fib(n)`: runtime? After memoization?
2. How many subsets does a set of n elements have?

<details><summary>Answer key</summary>

1. O(2ⁿ) naive, O(n) memoized.
2. 2ⁿ.
</details>

---

## Concept checks

### C1. Three ways to think about recursion
Teach: **Bottom-up**: solve for 1 element, then 2, then build n from n−1. **Top-down**: split the problem for n into subproblems, watching out for overlap. **Half-and-half**: split the data in two, as in binary search or merge sort.

**Q:** Which approach fits "count the ways to climb n stairs taking 1, 2 or 3 steps"? Write the recurrence.
<details><summary>Answer key</summary>
Top-down or bottom-up: `ways(n) = ways(n-1) + ways(n-2) + ways(n-3)`, with `ways(0) = 1` and `ways(<0) = 0`.
</details>

### C2. Recursion costs space
Teach: Every recursive call adds a stack frame, so recursion depth d means O(d) space. Any recursion can be rewritten iteratively, usually with an explicit stack. Mention the trade-off in interviews.

**Q:** What's the space complexity of the recursive stairs solution before and after memoization?
<details><summary>Answer key</summary>
O(n) stack depth in both cases. The memo table adds O(n). A bottom-up version that keeps only the last 3 values uses O(1).
</details>

### C3. Memoization (top-down DP)
Teach: If the same subproblem is solved repeatedly, cache it. In the naive Fibonacci recursion tree, `fib(n-2)` is computed twice, `fib(n-3)` three times, and so on. With a cache, each of the n states is computed once.

**Q:** Draw the recursion tree for `fib(5)` and mark the repeated calls. How many distinct calls are needed once you memoize?
<details><summary>Answer key</summary>
The repeats are fib(3) twice, fib(2) three times, fib(1) five times, and so on. With memoization there are 6 distinct states (fib(0) to fib(5)), so O(n).
</details>

### C4. Bottom-up (tabulation)
Teach: Fill a table from the base cases upward in dependency order. There's no recursion, so there's no risk of overflowing the stack. If each state depends only on the last k states, you only need to keep k variables.

**Q:** Convert memoized Fibonacci to O(1) space.
<details><summary>Answer key</summary>
Keep `a, b = 0, 1`, then loop n times doing `a, b = b, a+b` and return `a`.
</details>

### C5. How to define a DP state
Teach: Ask what the smallest description of a subproblem is. Examples: an index into the array; an index together with a remaining amount (for coins); a position (r, c) in a grid. The state space size × the work per state = the runtime.

**Q:** For "number of ways to make n cents from quarters, dimes, nickels and pennies", what's the state, and why isn't just `n` enough?
<details><summary>Answer key</summary>
The state is (amount, index of the coin being considered). With `n` alone you would count orderings: 5+10 and 10+5 would be two different ways. Fixing the order in which coin types are considered prevents that double count.
</details>

### C6. Backtracking
Teach: Build the solution step by step, and **undo** each step on the way back. Prune branches that can't lead to a solution (columns or diagonals already used in N-Queens, or too many closing parens). The cost is bounded by the size of the output, e.g. n! permutations or 2ⁿ subsets.

**Q:** When generating valid parentheses for n pairs, what are the two pruning rules?
<details><summary>Answer key</summary>
You may add "(" only if `left < n`. You may add ")" only if `right < left`.
</details>

---

## Problem ladder

| # | Problem | Tier | Pattern | Target | Key insight |
|---|---|---|---|---|---|
| 8.1 | Triple Step | ★ | memo/dp | O(n) | ways(n) = sum of the previous 3. Mention integer overflow for large n |
| 8.2 | Robot in a Grid | ★ | dfs · memo | O(rc) | Search back from the end, and memoize "failed" cells so they're never retried |
| 8.3 | Magic Index | ★ | binary-search | O(log n) distinct, O(n) worst with duplicates | Compare A[mid] with mid. With duplicates, search both sides but skip to min(mid−1, A[mid]) and max(mid+1, A[mid]) |
| 8.4 | Power Set | ★ | recursion · bit-trick | O(n·2ⁿ) | Subsets of n−1 elements, each with and without the nth element. Or treat the bits of 0..2ⁿ−1 as masks |
| 8.5 | Recursive Multiply | ☆ | divide-conquer | O(log s) | Halve the smaller number: result = 2·half, plus the bigger number if the smaller one is odd |
| 8.6 | Towers of Hanoi | ★ | recursion | O(2ⁿ) | Move n−1 to the buffer, move the bottom disk, move n−1 onto it |
| 8.7 | Permutations without Dups | ★ | backtracking | O(n²·n!) | Insert the first character into every position of each permutation of the rest, or choose each character as the first |
| 8.8 | Permutations with Dups | ★ | backtracking · hash-map | fewer than n! | Build from a frequency map, choosing each distinct character at each level |
| 8.9 | Parens | ★ | backtracking | Catalan | Add "(" if left < n, and ")" if right < left |
| 8.10 | Paint Fill | ★ | dfs | O(pixels) | Flood fill. Recurse in 4 directions only while the colour equals the original |
| 8.11 | Coins | ★ | memo/dp | O(n·coins) | State = (amount, coin index). Memoize |
| 8.12 | Eight Queens | ★ | backtracking | 8! pruned | One queen per row. Check the column and both diagonals |
| 8.13 | Stack of Boxes | ☆ | memo/dp | O(n²) | Sort by one dimension. Memoize the best stack height with each box at the bottom |
| 8.14 | Boolean Evaluation | ☆ | memo/dp | O(n³)-ish | Split at each operator and combine the true/false counts of both sides. Memoize (expression, result) |

**Test prompts:** n = 0 or 1, grids with no path or blocked start/end (8.2), negative numbers and duplicates (8.3), the empty set (8.4), "aab" (8.8), n = 0 (8.9), the new colour equal to the old one (8.10), n = 0 cents (8.11).

## Common pitfalls
- Forgetting the base case, or getting it wrong: is ways(0) 1 or 0?
- Memoizing on a state that doesn't capture everything the answer depends on.
- 8.10: an infinite loop when the new colour equals the old colour.
- Returning shared mutable lists from recursive calls and then mutating them.

## Exit quiz (≥ 5/6)
1. Top-down vs. bottom-up DP: the trade-offs.
2. What's the state for Coins?
3. The runtime of Power Set, and where it comes from.
4. How do you avoid duplicate permutations?
5. The two pruning rules for Parens.
6. Why do you record failed cells in Robot in a Grid?

<details><summary>Answer key</summary>

1. Top-down is natural to write, but it has recursion overhead and a risk of stack overflow. Bottom-up has no stack issues and allows space optimisation, but you must work out the fill order.
2. (remaining amount, index of the current coin).
3. O(n·2ⁿ): there are 2ⁿ subsets, and copying each one costs up to n.
4. Recurse over a frequency map of distinct characters, or sort and skip equal neighbours at the same recursion level.
5. Add "(" if open < n. Add ")" if close < open.
6. So that no cell is explored twice. Without it, the number of paths grows exponentially. With it, the search is O(rc).
</details>

## Flashcards
- DP recipe? → **define state → recurrence → base cases → memo or table → optimise space**
- Hanoi moves? → **2ⁿ − 1**
- Power set size? → **2ⁿ**
- Permutations of n distinct items? → **n!**
- Parens count for n pairs? → **Catalan(n)**
- Recursion space? → **O(depth)**
