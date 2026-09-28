# Module 06: Bit Manipulation (Ch. 5)

**Book:** concepts on PDF p.124–126 (`book.py section ch5`) · questions on p.127–128 · solutions on p.288–301
**Prereqs:** 00 · **Time:** 4–6 h

## Objectives
1. Do binary arithmetic by hand, including shifts and XOR.
2. Explain two's complement and the difference between arithmetic (`>>`) and logical (`>>>`) right shifts.
3. Write get, set, clear and update for bit i from memory.
4. Recognise the common tricks: `n & (n-1)`, `x ^ x = 0`, and masks like `0xAAAAAAAA`.

## Language note
In Python, ints have unbounded size and `>>` is arithmetic. There's no `>>>`, so to emulate 32-bit behaviour use `& 0xFFFFFFFF`. JavaScript bitwise operators work on 32-bit signed ints. Java and C++ have fixed widths. **The tutor should adapt examples to the learner's language.**

---

## Concept checks

### C1. By hand
Teach: Practise on paper: `0110 + 0010`, `0011 * 0101`, `0110 >> 1`, `1101 ^ 0101`, `~0 << 2`. XOR is 1 where the bits differ. `x ^ 0s = x`, `x ^ 1s = ~x`, `x ^ x = 0`. `x & 0s = 0`, `x & 1s = x`. `x | 0s = x`, `x | 1s = 1s`.

**Q:** Compute `1101 ^ (~1101)` and `1011 & (~0 << 2)` (4-bit values).
<details><summary>Answer key</summary>
`1101 ^ 0010 = 1111`. `~0 << 2 = 1100`, and `1011 & 1100 = 1000`.
</details>

### C2. Two's complement
Teach: For an N-bit signed int, −K is stored as the complement of K with respect to 2^N, i.e. `~K + 1`. The top bit is the sign. For example, −3 in 4 bits is `1101`.

**Q:** What's −1 in 8-bit two's complement? Why is it convenient?
<details><summary>Answer key</summary>
`11111111`. Adding 1 overflows to `00000000`, so ordinary addition hardware works for negative numbers with no special cases.
</details>

### C3. Arithmetic vs. logical right shift
Teach: An arithmetic shift (`>>`) fills with the sign bit, so it behaves like dividing by 2 and rounding down. A logical shift (`>>>`) fills with 0. Repeated `>>` on −1 stays −1 forever. Repeated `>>>` reaches 0.

**Q:** Why can a loop `while (n != 0) { n >>= 1; }` run forever in Java?
<details><summary>Answer key</summary>
If n is negative, `>>` keeps filling with 1s, so n settles at −1 and never reaches 0. Use `>>>` instead.
</details>

### C4. get, set, clear, update
Teach:
- get: `(num & (1 << i)) != 0`
- set: `num | (1 << i)`
- clear: `num & ~(1 << i)`
- clear bits from the top down to i: `num & ((1 << i) - 1)`
- clear bits i..0: `num & (-1 << (i + 1))`
- update to value v: `(num & ~(1 << i)) | (v << i)`

**Q:** Write (from memory) the expression that sets bits i..j of n to the bits of m (this is problem 5.1).
<details><summary>Answer key</summary>
`mask = ~(((1 << (j - i + 1)) - 1) << i)`, then `(n & mask) | (m << i)`. Alternatively, build the mask as `left | right`, where `left = ~0 << (j + 1)` and `right = (1 << i) - 1`.
</details>

### C5. Signature tricks
Teach: `n & (n-1)` clears the lowest set bit. `n == 0 || (n & (n-1)) == 0` tests for a power of 2 (or 0). `n & -n` isolates the lowest set bit. Counting set bits: repeat `c &= c - 1` and count the iterations.

**Q:** How many iterations does `while c: c &= c-1; count += 1` take for c = 0b10110?
<details><summary>Answer key</summary>
3, one per set bit.
</details>

---

## Problem ladder

| # | Problem | Tier | Pattern | Target | Key insight |
|---|---|---|---|---|---|
| 5.1 | Insertion | ★ | bit-trick | O(1) | Clear bits i..j with a mask, then OR in `m << i` |
| 5.2 | Binary to String | ★ | math | O(32) | Multiply by 2 and take the integer part as the next bit. Print "ERROR" beyond 32 characters |
| 5.3 | Flip Bit to Win | ★ | sliding-window | O(b), O(1) | Track the current and previous run lengths of 1s. At each 0, the candidate is prev + cur + 1 |
| 5.4 | Next Number | ☆ | bit-trick | O(b) | Next larger: flip the rightmost non-trailing 0 and move the 1s after it to the far right. Next smaller: the mirror image |
| 5.5 | Debugger | ★ | bit-trick | explain | `(n & (n-1)) == 0` means n is a power of 2 or 0 |
| 5.6 | Conversion | ★ | bit-trick | O(bits differing) | Count the set bits of `a ^ b` using `c &= c - 1` |
| 5.7 | Pairwise Swap | ★ | bit-trick | O(1) | `((x & 0xAAAAAAAA) >>> 1) \| ((x & 0x55555555) << 1)` |
| 5.8 | Draw Line | ☆ | bit-trick | O(bytes) | Fill whole bytes with 0xFF, then mask the partial first and last bytes. Watch the byte and row offsets |

**Test prompts:** i = 0 or j = 31 (5.1), 0.5 / 0.625 / 0.1 (5.2, where 0.1 must print ERROR), all 1s or all 0s (5.3), a = b (5.6), and negative numbers in your language (5.7).

## Common pitfalls
- Python: forgetting to mask to 32 bits, which gives infinitely long negative numbers.
- Operator precedence: `a & b == 0` parses as `a & (b == 0)` in C, Java and Python. Always add parentheses.
- Shifting by 32 or more in Java or C is undefined behaviour or wraps around.

## Exit quiz (≥ 4/5)
1. The expressions for get, set and clear of bit i.
2. What does `n & (n-1)` do?
3. What's the difference between `>>` and `>>>`?
4. How do you count the bits that differ between a and b?
5. How do you swap the odd and even bits?

<details><summary>Answer key</summary>

1. See C4.
2. It clears the lowest set bit.
3. `>>` fills with the sign bit (arithmetic). `>>>` fills with 0 (logical).
4. Count the set bits of `a ^ b`.
5. Use the 0xAAAAAAAA and 0x55555555 masks and shift each part by 1 in opposite directions.
</details>

## Flashcards
- Clear lowest set bit? → **n & (n-1)**
- Power of 2? → **(n & (n-1)) == 0, n ≠ 0**
- Negative K in two's complement? → **~K + 1**
- Odd-bit mask? → **0xAAAAAAAA**
- Count set bits? → **loop c &= c-1**
