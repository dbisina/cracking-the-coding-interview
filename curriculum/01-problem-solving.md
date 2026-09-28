# Module 01: The Problem-Solving Method

**Book:** Ch. VII "Technical Questions", PDF p.72–93 (`book.py section technical-questions`). The problem-solving flowchart is on p.74. The optimize techniques (BUD, DIY, Simplify & Generalize, Base Case & Build, Data Structure Brainstorm, BCR) are on p.79–88. "What Good Coding Looks Like" is on p.89–92.
**Prereqs:** 00 · **Time:** 2–3 h

This module is the **operating system** for every later module. The 7-step Interview Loop in AGENTS.md §4.3 comes straight from here.

## Objectives
1. Recite and follow the 7 steps: Listen → Example → Brute force → Optimize → Walk through → Implement → Test.
2. Apply **BUD** (Bottlenecks, Unnecessary work, Duplicated work) to improve a brute-force solution.
3. Use **DIY** (solve it by hand on a real example, then reverse-engineer what your brain did).
4. Estimate the **Best Conceivable Runtime (BCR)** and use it to decide when to stop optimizing.
5. Test code properly: conceptual walk-through, then suspicious lines, then small cases, then edge cases.

---

## Concept checks

### C1. Listen for the unusual details
Teach: Every detail in a question is usually there for a reason: "sorted", "unique", "runs many times", "in place". If a detail isn't used in your solution, you've probably missed an optimization.

**Q:** "Given two *sorted* arrays, find the elements they have in common." Which detail should shape your approach, and how?
<details><summary>Answer key</summary>
"Sorted". You can walk both arrays with two pointers in O(a+b) and O(1) space, or binary-search one array for each element of the other. You don't need a hash set.
</details>

### C2. Examples: big and not special
Teach: Most examples people draw are too small or are special cases (a perfectly balanced tree, a sorted array). Make the example large enough to show the pattern, and generic.

**Q:** For "find the lowest common ancestor in a binary tree", what's wrong with drawing a 3-node tree as your example?
<details><summary>Answer key</summary>
It's too small and too special. The ancestor is trivially the root, so you can't see how the recursion needs to behave. Use about 8–12 nodes, with the target nodes deep in different subtrees and one case where one target is an ancestor of the other.
</details>

### C3. Brute force first, out loud
Teach: State a brute-force solution and its complexity right away, even if it's terrible. It proves you understand the problem and gives you a baseline to optimize from. Don't code it yet.

**Q:** Why state the brute force at all if you know it isn't good enough?
<details><summary>Answer key</summary>
It shows you understand the problem, gives you and the interviewer a shared baseline, and often exposes the bottleneck to attack. Staying silent while you hunt for the optimal solution looks like being stuck.
</details>

### C4. BUD
Teach: **B**ottlenecks: the step that dominates the runtime (e.g. a one-time sort followed by an O(n) scan, where the sort is the bottleneck). **U**nnecessary work: computing things you never need. **D**uplicated work: recomputing the same thing, which you can cache or precompute. The book's example (p.79–81) is to find all a³+b³ = c³+d³ for 1..1000. Brute force is O(n⁴). Solving for d instead of looping over it gives O(n³). Then a map from sum to pairs gives O(n²).

**Q:** Find the number of pairs in an array that differ by k. Brute force compares all pairs, O(n²). Apply BUD.
<details><summary>Answer key</summary>
The bottleneck is looking for the partner of each element. Put every value in a hash set, then for each x check whether x+k is present: O(n) time and O(n) space. Alternatively, sort in O(n log n) and binary-search or walk two pointers.
</details>

### C5. DIY: solve it with your brain
Teach: Give yourself a large concrete instance and solve it by hand without thinking about algorithms, then notice what you actually did. The book's example (p.81) is finding permutations of a short string s inside a big string b. By hand, you'd slide a window and compare letter counts.

**Q:** Find all anagrams of "abbc" inside "cbabadcbbabbcbabaabccbabc". Before writing any code, describe what your eyes and brain are doing.
<details><summary>Answer key</summary>
You look at 4-letter windows and check whether each has the same letter counts as "abbc", sliding one character at a time. That's a **sliding window with a count map**: O(b) time, versus O(b·s log s) for sorting each window.
</details>

### C6. Simplify & generalize, base case & build, data structure brainstorm
Teach:
- **Simplify & generalize:** solve a simpler version (e.g. characters instead of words), then extend it.
- **Base case & build:** solve for n=1, then n=2, then derive n from n−1. This naturally leads to recursion.
- **Data structure brainstorm:** go through the list: array, hash map, linked list, stack, queue, heap, tree, trie, graph. Ask which one makes the hard step cheap.

**Q:** "Track the median of numbers as they arrive one at a time." Brainstorm data structures. Which ones fit and why?
<details><summary>Answer key</summary>
A sorted array makes insertion O(n). An unsorted array makes the median O(n). A balanced BST works but is complex. **Two heaps** work best: a max-heap for the lower half and a min-heap for the upper half. Insertion is O(log n) and reading the median is O(1). (This is problem 17.20.)
</details>

### C7. Best Conceivable Runtime (BCR)
Teach: BCR is the fastest any solution could possibly be. For example, you must look at each input once, so it's at least O(n); printing k results is at least O(k). If your solution matches the BCR, stop optimizing time and look at space. BCR is a target you know you can't beat, but it isn't always reachable.

**Q:** Two sorted arrays of sizes A and B: find the common elements. What's the BCR? Can you reach it?
<details><summary>Answer key</summary>
The BCR is O(A+B), because you must look at every element. Two pointers reach it with O(1) extra space.
</details>

### C8. Good code and testing
Teach: Interviewers grade correctness, efficiency, **simplicity, readability and maintainability**. Use modular helper functions, validate input only where it's cheap, and pick descriptive names. To test: (1) walk through the code conceptually, (2) look at odd-looking lines (`x = length - 2`), (3) look at hot spots (null nodes, base cases, loop boundaries), (4) try small cases, (5) try special cases (empty, one element, duplicates, extremes).

**Q:** You've written a function that reverses a linked list. List 5 test cases you'd run, in order.
<details><summary>Answer key</summary>
1. A conceptual walk-through on 1→2→3. 2. An empty list (null head). 3. A single node. 4. Two nodes, which catches pointer-order bugs. 5. A long list, checking that the old head's `.next` is null afterwards and there are no cycles.
</details>

### C9. When it goes wrong
Teach: Wrong answers are normal. You're judged relative to other candidates on the same question. If you've heard a question before, say so. Don't give up: interviewers want to see how you handle a hard problem.

**Q:** You realise halfway through coding that your approach is O(n²) and a better one exists. What do you say?
<details><summary>Answer key</summary>
Say it out loud: "I realise this is O(n²). I think there's an O(n) approach using X. Should I switch, or finish this one first?" That shows awareness and lets the interviewer steer.
</details>

---

## Method drills (no book problems in this chapter)

The tutor runs each drill with the learner narrating aloud, focusing on **process, not the final code**:

| Drill | Technique | Source |
|---|---|---|
| D1 | BUD: a³+b³=c³+d³ | the book example, PDF p.79–81 (learner solves before reading) |
| D2 | DIY: find permutations of s in b | PDF p.81–82 |
| D3 | Simplify & generalize: ransom note from magazine words | PDF p.83 |
| D4 | Base case & build: all permutations of a string | PDF p.83 |
| D5 | BCR: common elements of two sorted arrays | PDF p.85–88 |
| D6 | Full 7-step loop on 1.1 Is Unique | preview of module 02 |

## Exit quiz (≥ 4/5)
1. Name the 7 steps in order.
2. What do the letters in BUD stand for? Give an example of each.
3. What's BCR, and when do you stop optimizing?
4. When should you start coding?
5. Name 4 kinds of test case you run after writing code.

<details><summary>Answer key</summary>

1. Listen, Example, Brute force, Optimize, Walk through, Implement, Test.
2. Bottlenecks (e.g. a sort dominating an O(n) scan), Unnecessary work (e.g. continuing to search after finding the answer), Duplicated work (e.g. recomputing sums you could cache).
3. BCR is the Best Conceivable Runtime, the lower bound for any solution. Once you've reached it, stop optimizing time and look at space.
4. Only after you have an optimal (or agreed) algorithm and have walked through it on an example.
5. A conceptual walk-through, odd-looking lines, hot spots (nulls, base cases), small cases, and special or edge cases.
</details>

## Flashcards
- BUD? → **Bottlenecks, Unnecessary, Duplicated**
- The DIY technique? → **Solve a big example by hand, then reverse-engineer what your brain did**
- BCR? → **Best Conceivable Runtime: the floor you can't beat**
- An unused detail in the question? → **A hint you're missing an optimization**
