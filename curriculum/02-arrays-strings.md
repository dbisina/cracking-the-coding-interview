# Module 02: Arrays & Strings (Ch. 1)

**Book:** concepts on PDF p.100–101 (`book.py section ch1`) · questions on p.102–103 · solutions on p.204–220
**Prereqs:** 00, 01 · **Time:** 5–7 h

## Objectives
1. Explain how a hash table works internally (hash → index → chain) and when lookup degrades to O(n).
2. Explain dynamic-array amortization and the O(n²) trap of concatenating strings in a loop.
3. Reach for the right array/string tools: count arrays, bit vectors, two pointers, filling from the end in place, and matrix layers.

## Diagnostic
1. How would you check whether a string has duplicate characters in O(n)?
2. Why is `s = s + word` inside a loop slow in Java or C#?

<details><summary>Answer key</summary>

1. Use a set or a boolean[128] array (for ASCII) and return early when a character repeats.
2. Strings are immutable, so each concatenation copies the whole string built so far. That's O(x·n²) for n words of length x. Use a StringBuilder, or join a list in Python.
</details>

---

## Concept checks

### C1. Hash tables under the hood
Teach: A hash table is an array of buckets. To insert: compute `hash(key)`, map it to an index with `hash % capacity`, and store the (key, value) pair in that bucket's linked list. Collisions happen in two ways: different keys can share a hash code, and different hash codes can map to the same index. Lookup is O(1) on average, but O(n) in the worst case when everything collides. The alternative is a balanced BST, which gives O(log n) lookup, uses less space, and keeps keys in order.

**Q:** Why do we store the key as well as the value in each bucket?
<details><summary>Answer key</summary>
Several keys can land in the same bucket. We need the stored key to tell which entry actually matches the key we're looking up.
</details>

**Q2:** When would you choose a BST-backed map (TreeMap, `std::map`) over a hash map?
<details><summary>Answer key</summary>
When you need keys in sorted order, range queries, or floor/ceiling lookups, or when you need a guaranteed O(log n) worst case rather than an expected O(1).
</details>

### C2. Resizable arrays
Teach: A resizable array (ArrayList, Python list, JS array) doubles its capacity when full. The occasional copy is O(n), but appends are O(1) amortized (review Module 00, C6).

**Q:** What's the total copy cost of pushing 16 elements into a list that starts at capacity 1 and doubles?
<details><summary>Answer key</summary>
The resizes happen at sizes 1, 2, 4 and 8, copying 1 + 2 + 4 + 8 = 15 elements. That's under 2·16, so appends are O(1) amortized.
</details>

### C3. StringBuilder
Teach: Building a string by repeated concatenation copies the growing string every time, which adds up to O(x·n²). A StringBuilder (or collecting parts in a list and joining once) makes the whole build O(total length).

**Q:** In Python, what's the idiomatic way to build a long string from many pieces, and why?
<details><summary>Answer key</summary>
Append the pieces to a list, then call `''.join(parts)` once. That's O(total length). (CPython sometimes optimises `+=` in place, but you can't rely on it.)
</details>

### C4. Character counting and bit vectors
Teach: Many string problems reduce to "compare character frequencies". Use an int array sized to the character set (128 for ASCII), or a hash map for Unicode. For yes/no flags on lowercase letters, a single 32-bit int can act as a **bit vector**: bit i means "letter i seen".

**Q:** How do you check whether at most one bit is set in an int `v`?
<details><summary>Answer key</summary>
`(v & (v - 1)) == 0`. Subtracting 1 flips the lowest set bit and every bit below it, so the AND is 0 only when v had zero or one bits set. (This trick is used in 1.4.)
</details>

### C5. Ask about the character set
Teach: Always ask whether the input is ASCII or Unicode, whether case matters, and whether whitespace counts. These change both the space bound (O(1) for a fixed alphabet vs. O(k)) and correctness.

**Q:** For "is unique", why can you immediately return false if the string is longer than 128 characters (ASCII)?
<details><summary>Answer key</summary>
By the pigeonhole principle, there are only 128 distinct ASCII characters, so a longer string must repeat one.
</details>

### C6. In-place from the end, and matrix layers
Teach: When you need to expand text in place (as in URLify), count the final length first and **write backwards from the end** so you never overwrite unread characters. For matrix rotation, work **layer by layer** from the outside in, doing a 4-way swap for each position in the layer.

**Q:** Why write from the end rather than the start when replacing spaces with "%20" in place?
<details><summary>Answer key</summary>
The output is longer than the input. Writing forward would overwrite characters you haven't read yet. Writing backward puts each character into space that's already free.
</details>

---

## Problem ladder

| # | Problem | Tier | Pattern | Target | Key insight (reveal only after the attempt) |
|---|---|---|---|---|---|
| 1.1 | Is Unique | ★ | hash-map · bit-trick | O(n) time, O(1) space | boolean[128] or bit vector. Without extra data structures: sort, then compare neighbours |
| 1.2 | Check Permutation | ★ | hash-map · sort-first | O(n) | Equal lengths plus equal character counts |
| 1.3 | URLify | ★ | in-place | O(n) | Count spaces, then fill from the end |
| 1.4 | Palindrome Permutation | ★ | hash-map · bit-trick | O(n) | At most one character may have an odd count. Toggle bits, then check `v & (v-1) == 0` |
| 1.5 | One Away | ★ | two-pointer | O(n) | Branch on the length difference. One pass allowing a single mismatch |
| 1.6 | String Compression | ★ | StringBuilder | O(n) | Count consecutive runs. Return the original if the result isn't shorter |
| 1.7 | Rotate Matrix | ★ | in-place | O(N²) time, O(1) space | Layer by layer, 4-way swap (top←left←bottom←right←top) |
| 1.8 | Zero Matrix | ★ | in-place | O(MN) time, O(1) space | Record zeros first, then clear. Use row 0 and column 0 as marker storage |
| 1.9 | String Rotation | ★ | math | O(n) | s2 is a rotation of s1 if and only if the lengths match and s2 is a substring of s1+s1 |

**Test-case prompts for the tutor:** the empty string, a single character, all identical characters, Unicode input (1.1/1.2), a 1×1 matrix and a non-square matrix (1.8), trailing spaces (1.3), and "pale"/"ple"/"pales"/"bale"/"bake" (1.5).

## Common pitfalls
- Clearing rows and columns *while* scanning in 1.8, which cascades into wrong zeros.
- Off-by-one errors on layer bounds in 1.7 (`first = layer`, `last = n - 1 - layer`).
- Forgetting to compare lengths first in 1.2 and 1.9.
- Using string concatenation inside loops (1.6).

## Exit quiz (≥ 4/5)
1. The worst-case lookup in a chained hash table, and the reason for it.
2. How do you check "permutation of a palindrome" in O(1) extra space for lowercase letters?
3. Rotate an N×N matrix 90° in place: what's the cost, and what's the idea?
4. What's the one-line test for whether s2 is a rotation of s1?
5. Why must you ask about the character set?

<details><summary>Answer key</summary>

1. O(n). If every key collides into one bucket, the chain is effectively a linked list.
2. Toggle bit (c − 'a') of an int for each character, then check `v == 0 || (v & (v-1)) == 0`.
3. O(N²) time and O(1) space: go layer by layer and do a 4-way swap per element.
4. `len(s1) == len(s2) and s2 in (s1 + s1)`.
5. It changes the space bound (a fixed alphabet gives O(1)), the pigeonhole early exit, and whether an array or a map fits.
</details>

## Flashcards
- In-place expansion? → **fill from the end**
- Palindrome permutation? → **at most one odd count**
- Rotation check? → **s2 ⊂ s1+s1**
- Zero matrix in O(1) space? → **first row and column as flags**
- Hash table worst case? → **O(n), all keys collide**
