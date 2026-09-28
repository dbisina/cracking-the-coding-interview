# Module 11: Sorting & Searching (Ch. 10)

**Book:** concepts on PDF p.158–160 (`book.py section ch10`): bubble, selection, merge, quick and radix sort, plus binary search · questions on p.161–163 · solutions on p.408–429
**Prereqs:** 00, 05 · **Time:** 5–7 h

## Objectives
1. State the runtime, space and stability of bubble, selection, merge, quick and radix sort. Implement merge sort and quicksort from memory.
2. Write a bug-free binary search (iterative and recursive) and adapt it to rotated arrays, unknown sizes and sparse data.
3. Think about data that doesn't fit in memory (external sort, bit vectors).

---

## Concept checks

### C1. The sorting table
Teach:

| Sort | Time avg / worst | Space | Stable? | Idea |
|---|---|---|---|---|
| Bubble | O(n²) / O(n²) | O(1) | yes | swap adjacent out-of-order pairs |
| Selection | O(n²) / O(n²) | O(1) | no | select the min, swap it to the front |
| Merge | O(n log n) / O(n log n) | O(n) | yes | split, sort each half, merge |
| Quick | O(n log n) / O(n²) | O(log n) stack | no | partition around a pivot, recurse |
| Radix | O(kn) | O(n+k) | yes (LSD) | sort by each digit, least significant first |

**Q:** Why is quicksort's worst case O(n²), and when does it happen?
<details><summary>Answer key</summary>
When the pivot is always the smallest or largest element (for example, a sorted array with the first element as pivot), each partition removes only one element, giving n levels × O(n) work. Random pivots or median-of-three make this unlikely.
</details>

### C2. Merge sort in detail
Teach: Split into two halves, sort each recursively, then merge using a helper array. Only the left half's remaining elements need copying back, because the right half's leftovers are already in place.

**Q:** Why does merge sort need O(n) extra space, while quicksort needs only O(log n)?
<details><summary>Answer key</summary>
The merge step needs a buffer the size of the subarray being merged. Quicksort partitions in place and only uses space for the recursion stack, which is log n deep on average.
</details>

### C3. Binary search, done right
Teach: `low = 0, high = n-1; while low <= high: mid = low + (high-low)//2`. Compare, then move `low = mid+1` or `high = mid-1`. Writing `low + (high-low)/2` avoids integer overflow. The general version is "find the first index where a predicate becomes true".

**Q:** What's the bug in `while (low < high) { mid = (low+high)/2; if (a[mid] < x) low = mid; else high = mid; }`?
<details><summary>Answer key</summary>
When `high = low + 1` and `a[mid] < x`, mid equals low, so `low = mid` makes no progress and the loop never ends. Also, `(low+high)` can overflow in Java or C.
</details>

### C4. Beyond memory
Teach: If data doesn't fit in RAM, sort chunks that do fit, write them to disk, then do a **k-way merge** (external sort). A bit vector packs 8 flags per byte, so 4 billion flags take 512 MB.

**Q:** 20 GB file, 1 GB of RAM: outline the sort.
<details><summary>Answer key</summary>
Read 1 GB at a time, sort it in memory, and write it out as a sorted run (20 runs). Then do a 20-way merge using a min-heap holding the head of each run, streaming the output to disk.
</details>

---

## Problem ladder

| # | Problem | Tier | Pattern | Target | Key insight |
|---|---|---|---|---|---|
| 10.1 | Sorted Merge | ★ | two-pointer · in-place | O(A+B) | Merge from the back of A so nothing is overwritten |
| 10.2 | Group Anagrams | ★ | hash-map · sort-first | O(n·s log s) | Group by sorted string (or a character-count key), then output the groups |
| 10.3 | Search in Rotated Array | ★ | binary-search | O(log n), O(n) with many dups | One half is always normally ordered. Check whether x lies in that half |
| 10.4 | Sorted Search, No Size | ★ | binary-search | O(log n) | Double the index until you pass x (or hit −1), then binary search |
| 10.5 | Sparse Search | ★ | binary-search | O(log n) usually, O(n) worst | If mid is "", move to the nearest non-empty string |
| 10.6 | Sort Big File | ★ | external sort | — | Chunk, sort each chunk, k-way merge |
| 10.7 | Missing Int | ☆ | bit-trick | O(n) | 4B bits = 512 MB bit vector. With 10 MB: first count per block, then use a bit vector for the sparse block |
| 10.8 | Find Duplicates | ★ | bit-trick | O(n) | 4 KB = 32,000 bits. Use a bit vector over 1..32000 |
| 10.9 | Sorted Matrix Search | ★ | two-pointer | O(M+N) | Start top-right: go left if too big, down if too small |
| 10.10 | Rank from Stream | ☆ | augmented BST | O(log n) balanced | Each node stores the size of its left subtree |
| 10.11 | Peaks and Valleys | ★ | greedy | O(n) | At every other index, swap the middle of each triple with its largest neighbour |

**Test prompts:** empty or duplicate-heavy arrays, rotation by 0 or n (10.3), x absent, all "" except one string (10.5), 1×N and N×1 matrices (10.9), equal values (10.11).

## Exit quiz (≥ 4/5)
1. Which sorts are stable, and which are O(n log n) in the worst case?
2. Write binary search from memory. Where do the off-by-one bugs usually hide?
3. Rotated array search: what's the key observation?
4. How do you search a sorted matrix in O(M+N)?
5. How do you sort a file 20× larger than RAM?

<details><summary>Answer key</summary>

1. Stable: merge, bubble, insertion, radix (LSD). O(n log n) worst case: merge sort (heapsort too).
2. See C3. The usual suspects are the loop condition (`<=`) and the updates (`mid±1`).
3. At least one half around mid is sorted. Check whether x falls inside that sorted range.
4. Start at the top-right corner. Each comparison eliminates a row or a column.
5. External merge sort: sorted runs plus a k-way heap merge.
</details>

## Flashcards
- Merge sort space? → **O(n)**
- Quicksort worst case? → **O(n²), bad pivots**
- Stable O(n log n) sort? → **merge sort**
- Sorted matrix start? → **top-right corner**
- Safe mid? → **low + (high - low) / 2**
