# Module 17: Moderate Problems (Ch. 16)

**Book:** questions on PDF p.193–197 · solutions on p.474–541 · no concept section
**Prereqs:** 02–05, 09, 11 · **Time:** 12–16 h, spread out

These problems are **unlabelled by topic**, just like real interviews. The first skill being trained is working out *which* pattern applies.

## How the tutor runs this module
1. Show the question with `book.py q 16.x`. **Don't reveal the tier or the pattern.**
2. Before any coding, ask: "Which modules or patterns does this remind you of?" Score the recognition separately in the log note, e.g. `recog: yes/partial/no`.
3. Run the full Interview Loop (AGENTS.md §4.3). Aim for 25–30 minutes per problem.
4. Space them out. Don't do the ladder in order, and don't do more than 2 per session. Mix in reviews.
5. From here on, every 3rd session is a **mock interview** (AGENTS.md §5.1) drawing on this module.

## Suggested order
Pattern variety first: 16.17 → 16.5 → 16.24 → 16.6 → 16.10 → 16.21 → 16.16 → 16.19 → 16.25 → 16.26 → 16.11 → 16.2 → 16.1 → 16.8 → 16.15 → 16.20 → 16.23 → 16.4, then the ☆ problems.

## Problem ladder (tutor reference: pattern and target are hidden from the learner until after the attempt)

| # | Problem | Tier | Pattern | Target | Key insight |
|---|---|---|---|---|---|
| 16.1 | Number Swapper | ★ | math · bit-trick | O(1) | `a=a-b; b=a+b; a=b-a`, or three XORs |
| 16.2 | Word Frequencies | ★ | hash-map · precompute | O(1) per query | For repeated queries, precompute a lowercase word → count map once |
| 16.3 | Intersection | ☆ | math | O(1) | Slope and intercept of each segment. Handle parallel lines, collinear overlap and vertical lines. Check the point lies within both segments |
| 16.4 | Tic Tac Win | ★ | design | O(N) per check | If called many times, check only the row, column and diagonals of the last move. Generalise to N×N with iterators |
| 16.5 | Factorial Zeros | ★ | math | O(log n) | Count the factors of 5: n/5 + n/25 + n/125 + … |
| 16.6 | Smallest Difference | ★ | sort-first · two-pointer | O(A log A + B log B) | Sort both arrays and advance the pointer at the smaller value |
| 16.7 | Number Max | ☆ | bit-trick | O(1) | Take the sign bit of a−b. Handle overflow when a and b have different signs |
| 16.8 | English Int | ★ | recursion · chunking | O(digits) | Split into chunks of 3 digits with a scale word (thousand, million, billion). Handle 0 and negatives |
| 16.9 | Operations | ☆ | math | O(n) or O(log) | Negate by adding ±1 repeatedly, with doubling steps for speed. Multiply and divide from add and negate |
| 16.10 | Living People | ★ | prefix-sum | O(P + Y) | +1 at the birth year, −1 at death year + 1, then take a running sum and its max |
| 16.11 | Diving Board | ★ | math | O(k) | There are only k+1 distinct totals: i·longer + (k−i)·shorter. Watch for shorter == longer |
| 16.12 | XML Encoding | ○ | recursion | O(n) | Encode each element recursively: tag, attributes, END, children, END |
| 16.13 | Bisect Squares | ☆ | math | O(1) | The line through both squares' centres. Extend it to the edges of the squares |
| 16.14 | Best Line | ☆ | hash-map · math | O(n²) | Hash each pair's line (slope and intercept, with an epsilon or rational key) and count |
| 16.15 | Master Mind | ★ | hash-map | O(n) | Count exact hits first, then pseudo-hits from the leftover colour frequencies |
| 16.16 | Sub Sort | ★ | two-pointer | O(n) | Find the sorted left prefix and right suffix, take the min and max of the middle, then shrink the prefix and suffix to fit |
| 16.17 | Contiguous Sequence | ★ | dp (Kadane) | O(n), O(1) | Running sum. Reset it when it drops below 0 and track the max. Ask what to return if everything is negative |
| 16.18 | Pattern Matching | ☆ | brute-force + pruning | O(n²) | Try each length for "a", derive b's length, and verify. Swap a and b if the pattern starts with b |
| 16.19 | Pond Sizes | ★ | dfs (flood fill) | O(WH) | Flood-fill the zeros, including diagonal neighbours, and mark them visited |
| 16.20 | T9 | ★ | hash-map · trie | O(1) lookup after precompute | Precompute a digit string → word list map (or walk a trie) |
| 16.21 | Sum Swap | ★ | hash-map · math | O(A+B) | target = (sumA − sumB)/2, which must be an integer. For each a, check whether a − target is in set B |
| 16.22 | Langton's Ant | ☆ | design · hash-set | O(K) | A set of black cells (an infinite grid) and the ant's position and orientation. Print within the bounds seen so far |
| 16.23 | Rand7 from Rand5 | ★ | math · rejection | expected O(1) | `5·rand5() + rand5()` is uniform on 0..24. Reject values ≥ 21 and return the value mod 7 |
| 16.24 | Pairs with Sum | ★ | hash-map · two-pointer | O(n) | A map of unpaired counts, or sort and walk two pointers |
| 16.25 | LRU Cache | ★ | hash-map + linked list | O(1) | A map from key to node, plus a doubly linked list for recency. Evict at the tail |
| 16.26 | Calculator | ★ | stack | O(n) | Two stacks (numbers and operators) that collapse by precedence, or a left-to-right pass that folds * and / immediately |

## Exit criteria (not a quiz)
- All ★ problems scored ≥ 3.
- Pattern recognised before hints in ≥ 70% of attempts.
- At least 2 mock interviews using problems from this module, averaging ≥ 3.

## Pattern recognition drill (flashcards)
When you read a problem, ask which cue it contains:
- "subarray sum / max contiguous" → **Kadane or prefix sums**
- "pairs summing to" → **hash map or two pointers**
- "year ranges / overlapping intervals count" → **delta array + running sum**
- "O(1) get/put with eviction" → **hash map + doubly linked list**
- "generate from a smaller RNG" → **rejection sampling**
- "grid of connected regions" → **flood fill / DFS**
- "sorted order from the edges inward" → **two pointers**
