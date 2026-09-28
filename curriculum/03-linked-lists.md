# Module 03: Linked Lists (Ch. 2)

**Book:** concepts on PDF p.104–105 (`book.py section ch2`) · questions on p.106–107 · solutions on p.220–238
**Prereqs:** 00–02 · **Time:** 5–7 h

## Objectives
1. Implement a singly linked list node and do insert/delete, handling the head and null cases.
2. Use the **runner technique** (fast/slow pointers) for middle, cycle and k-th-from-end problems.
3. Write recursive list solutions and state their O(n) stack cost.
4. Explain why random access is O(n) and why deletion given a node is O(1).

## Diagnostic
1. How do you find the middle of a singly linked list in one pass?
2. Given only a pointer to a node (not the head), can you delete it?

<details><summary>Answer key</summary>

1. Use a slow pointer that moves 1 step and a fast pointer that moves 2. When fast reaches the end, slow is at the middle.
2. Yes, unless it's the last node: copy `next.data` into this node, then unlink `next`.
</details>

---

## Concept checks

### C1. The structure and its costs
Teach: Each node holds data and `next` (plus `prev` in a doubly linked list). Access by index is O(n). Inserting or deleting at a known position is O(1). There's no contiguous memory, so there's no resizing either.

**Q:** Compare linked lists and arrays for (a) accessing the k-th element, (b) inserting at the front, (c) cache friendliness.
<details><summary>Answer key</summary>
(a) Array O(1), list O(k). (b) Array O(n) (shift everything), list O(1). (c) Arrays win, because the memory is contiguous. List nodes are scattered in memory.
</details>

### C2. Deleting a node, and the head case
Teach: To delete node n, set `prev.next = n.next`. Watch for: deleting the head (you must return a new head, or use a dummy/sentinel node), a null `prev`, and, in C/C++, freeing the memory.

**Q:** Why do many solutions create a dummy node before the head?
<details><summary>Answer key</summary>
It removes the special case for the head. Every real node then has a predecessor, and you return `dummy.next` at the end.
</details>

### C3. Runner technique (fast/slow pointers)
Teach: Move two pointers at different speeds, or with a fixed gap between them. Uses: find the middle, detect a cycle, find the k-th from the end (move one pointer k steps ahead first), and interleave the halves of a list.

**Q:** How do you find the k-th to last element in one pass with O(1) space?
<details><summary>Answer key</summary>
Move p1 k nodes ahead. Then move p1 and p2 together until p1 hits the end. p2 is now k from the end. (Check whether k is 0- or 1-indexed, and handle k > length.)
</details>

### C4. Recursion on lists
Teach: Many list problems have short recursive solutions (reverse, print backwards, compare from the end). Each one costs O(n) stack space, and for long lists that can overflow the stack. Mention this trade-off in interviews.

**Q:** A recursive list reversal is elegant. What's its space complexity, and when does that matter?
<details><summary>Answer key</summary>
O(n) call stack. It matters for very long lists (a stack overflow risk, e.g. Python's default recursion limit of about 1000). The iterative version is O(1).
</details>

### C5. Floyd's cycle detection
Teach: Fast moves 2 steps and slow moves 1. If there's a loop, they meet. To find the **start** of the loop: when they meet, they are k steps before the loop start, where k is the distance from the head to the loop start (taken mod the loop size). Reset one pointer to the head and move both 1 step at a time. They meet at the loop start.

**Q:** Why will fast and slow always meet inside a cycle, rather than fast skipping over slow?
<details><summary>Answer key</summary>
Inside the loop, fast gains exactly 1 node on slow per step. The gap shrinks by 1 each time, so it hits 0 exactly and can never jump past.
</details>

---

## Problem ladder

| # | Problem | Tier | Pattern | Target | Key insight |
|---|---|---|---|---|---|
| 2.1 | Remove Dups | ★ | hash-map · runner | O(n) with a set. O(n²) and O(1) space without a buffer | Set of seen values. No buffer: a current pointer plus a runner that removes later duplicates |
| 2.2 | Return Kth to Last | ★ | runner | O(n), O(1) | Two pointers k apart |
| 2.3 | Delete Middle Node | ★ | in-place | O(1) | Copy the next node's data into this one, then skip next. Can't delete the tail |
| 2.4 | Partition | ★ | two-pointer | O(n) | Build a "before" list and an "after" list and join them, or insert small values at the head and others at the tail |
| 2.5 | Sum Lists | ★ | recursion | O(max(a,b)) | Reverse order: add digit by digit with a carry. Forward order: pad the shorter list, then recurse and return the carry |
| 2.6 | Palindrome | ★ | runner · stack · recursion | O(n) | Push the first half onto a stack (fast/slow), then compare with the second half. Or reverse the second half |
| 2.7 | Intersection | ★ | two-pointer | O(A+B), O(1) | Compare tails by reference (a different tail means no intersection). Advance the longer list by the length difference, then walk together |
| 2.8 | Loop Detection | ★ | runner | O(n), O(1) | Floyd: meet, reset one pointer to the head, step both by 1, and they meet at the loop start |

**Test prompts:** an empty list, one node, two nodes, all duplicates (2.1), k = 0 / k = length / k > length (2.2), a partition value that isn't in the list (2.4), unequal lengths with a final carry such as 9→9 + 1 (2.5), even and odd lengths (2.6), intersection at the head or tail (2.7), and a loop back to the head (2.8).

## Common pitfalls
- Comparing node **values** instead of node **references** in 2.7.
- Losing the rest of the list by overwriting `next` before saving it.
- Forgetting the final carry node in 2.5.
- Null-pointer errors on `fast.next.next`.

## Exit quiz (≥ 4/5)
1. How do you find the middle node in one pass?
2. Prove, informally, why resetting one pointer to the head finds the loop start.
3. How do you detect an intersection by reference in O(A+B) time and O(1) space?
4. What's the space cost of a recursive palindrome check?
5. When can't you use the "copy next into this node" trick?

<details><summary>Answer key</summary>

1. Fast/slow pointers.
2. Let k be the distance from the head to the loop start. When slow enters the loop, fast is k steps into it. They meet LOOP_SIZE − k (mod LOOP_SIZE) steps later, which leaves them k steps short of the loop start. So a pointer from the head and a pointer from the meeting point, both moving at the same speed, meet at the loop start after k steps.
3. Get both lengths and tails. If the tails differ, there's no intersection. Otherwise advance the longer list by the length difference, then walk both until the references match.
4. O(n) stack.
5. When the node is the tail, because there's no next node to copy.
</details>

## Flashcards
- k-th to last? → **two pointers k apart**
- Loop start? → **meet, reset one to the head, both step 1**
- Intersection test? → **same tail node (by reference)**
- Remove the head safely? → **dummy node**
- Recursion on a list? → **O(n) stack; mention it**
