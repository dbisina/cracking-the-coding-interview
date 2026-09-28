# Module 18: Hard Problems (Ch. 17)

**Book:** questions on PDF p.198–202 · solutions on p.542–639 · no concept section
**Prereqs:** 17 in progress, plus 05 and 09 mastered · **Time:** 14–20 h, spread out

Hard problems reward **patience and a solid brute force first**. Interviewers expect hints on these. How you use the hints is graded.

## How the tutor runs this module
- Same as Module 17: no labels, and recognition is scored first.
- Allow up to 45 minutes. Push for brute force → BUD → optimal, in stages. Each stage that works counts.
- It's normal to reach rung 2 of the hint ladder here. Score 2 is a respectable result on a Hard problem.
- For long solutions (17.17, 17.18, 17.25, 17.26), it's fine to agree on the algorithm and complexity and code only the core function.

## Suggested order
17.10 → 17.2 → 17.1 → 17.5 → 17.21 → 17.16 → 17.19 → 17.20 → 17.14 → 17.11 → 17.8 → 17.7 → 17.15 → 17.22 → 17.3, then the ☆ problems.

## Problem ladder (tutor reference)

| # | Problem | Tier | Pattern | Target | Key insight |
|---|---|---|---|---|---|
| 17.1 | Add Without Plus | ★ | bit-trick | O(bits) | sum = a ^ b, carry = (a & b) << 1. Repeat until the carry is 0. Python needs 32-bit masking |
| 17.2 | Shuffle | ★ | random (Fisher–Yates) | O(n) | For i from n−1 down to 0, swap a[i] with a random index in [0, i] |
| 17.3 | Random Set | ★ | reservoir sampling | O(n) | Keep the first m. For i ≥ m, choose k = rand(0..i) and replace slot k if k < m |
| 17.4 | Missing Number | ☆ | bit-trick · divide-conquer | O(n) | Compare the counts of 0s and 1s in the least significant bit, keep the side that's short, and recurse on the next bit |
| 17.5 | Letters and Numbers | ★ | prefix-sum · hash-map | O(n) | Running (letters − numbers). The longest span between equal values wins |
| 17.6 | Count of 2s | ☆ | math (digit DP) | O(log n) | Per digit position: round down or up depending on whether the digit is <, = or > 2 |
| 17.7 | Baby Names | ★ | union-find · graph | O(B + P) | Synonym pairs form connected components. Sum the frequencies per component and pick a canonical name |
| 17.8 | Circus Tower | ★ | sort-first · LIS | O(n log n) | Sort by height, then find the longest increasing subsequence by weight, handling ties strictly |
| 17.9 | Kth Multiple | ☆ | queue / three pointers | O(k) | Like ugly numbers: merge ×3, ×5, ×7 streams with 3 queues or pointers |
| 17.10 | Majority Element | ★ | Boyer–Moore voting | O(n), O(1) | Keep a candidate and a count. Verify the candidate in a second pass |
| 17.11 | Word Distance | ★ | two-pointer · precompute | O(n) one-off, O(A+B) repeated | For repeated queries, map each word to its sorted positions and merge the two lists |
| 17.12 | BiNode | ☆ | recursion (tree→list) | O(n) | Convert the subtrees in order, returning (head, tail), and link them |
| 17.13 | Re-Space | ☆ | memo/dp · trie | O(n²) | best(i) = the minimum unrecognised characters from i onward. Try each end j and memoize |
| 17.14 | Smallest K | ★ | heap · quickselect | O(n log k) or O(n) avg | A max-heap of size k, or selection rank (quickselect partition) |
| 17.15 | Longest Word | ★ | memo · hash-set | O(n·L²)-ish | Sort by length, descending. canBuild(word) splits it into prefixes that are in the set, recursing with memoization |
| 17.16 | The Masseuse | ★ | dp | O(n), O(1) | best(i) = max(best(i+1), a[i] + best(i+2)). Iterate from the end with two variables |
| 17.17 | Multi Search | ☆ | trie | O(bk) | Build a trie of the smalls and walk it from every index of b (k = length of the longest small) |
| 17.18 | Shortest Supersequence | ☆ | sliding-window · heap | O(B log S) or O(B·S) | Next-occurrence arrays, or a min-heap across the per-element position lists |
| 17.19 | Missing Two | ★ | math | O(N), O(1) | One missing: the expected sum minus the actual sum. Two missing: use the sum and the sum of squares, or split around the midpoint of the pair's sum |
| 17.20 | Continuous Median | ★ | heap (two) | O(log n) add, O(1) median | A max-heap for the lower half and a min-heap for the upper half. Keep their sizes balanced |
| 17.21 | Volume of Histogram | ★ | precompute · two-pointer | O(n) | Water at i = min(maxLeft[i], maxRight[i]) − h[i]. Two pointers give O(1) space |
| 17.22 | Word Transformer | ★ | bfs (bidirectional) | O(words·L) | BFS over one-edit neighbours, using a wildcard map ("b_ll" → words) for fast neighbour lookup |
| 17.23 | Max Black Square | ☆ | precompute · dp | O(N³) | Precompute the run of black cells to the right and below each cell, then check each square size in O(1) |
| 17.24 | Max Submatrix | ☆ | kadane · prefix-sum | O(R²C) | Fix the start and end rows, compress the columns into sums, and run Kadane |
| 17.25 | Word Rectangle | ○ | backtracking · trie | exponential | Group words by length and try the largest areas first. Tries check that each column is still a valid prefix |
| 17.26 | Sparse Similarity | ☆ | hash-map | O(PW + D·W)-ish | An inverted index from word to docs. For each doc, count shared words per other doc, then intersection / union |

## Exit criteria
- All ★ problems scored ≥ 2, and at least half of them ≥ 3.
- Two mock interviews using Hard problems, with Communication and Problem-solving ≥ 3.

## Pattern recognition drill (flashcards)
- "majority / more than half" → **Boyer–Moore voting**
- "running median" → **two heaps**
- "trapped water" → **max-left / max-right**
- "equal count of two types in a subarray" → **prefix difference + first-seen map**
- "choose m of n uniformly" → **reservoir sampling / Fisher–Yates**
- "many small strings inside a big string" → **trie**
- "maximum-sum rectangle" → **fix two rows + Kadane**
- "synonym groups" → **union-find / connected components**
