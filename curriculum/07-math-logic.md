# Module 07: Math & Logic Puzzles (Ch. 6)

**Book:** concepts on PDF p.129–133 (`book.py section ch6`): primes, the Sieve of Eratosthenes, probability, and approaches to brainteasers · questions on p.134–136 · solutions on p.301–316
**Prereqs:** 00 · **Time:** 3–5 h

## Objectives
1. Check primality in O(√n) and generate primes with the Sieve of Eratosthenes.
2. Apply probability rules: P(A and B), P(A or B), independence vs. mutual exclusivity.
3. Attack brainteasers out loud: start talking, find rules and patterns, balance the worst case, and use algorithmic approaches.

---

## Concept checks

### C1. Primes and divisibility
Teach: Every number is a product of primes. x divides y exactly when every prime's exponent in x is ≤ its exponent in y. For a primality check, trying divisors up to √n is enough, because divisors come in pairs around √n.

**Q:** Why is checking divisors up to √n sufficient?
<details><summary>Answer key</summary>
If n = a·b with a > √n, then b < √n. So any divisor above √n pairs with one below √n that you would already have found.
</details>

### C2. Sieve of Eratosthenes
Teach: List 2..max. Take the next unmarked number (it's prime) and cross off all its multiples, starting from p². Repeat until p > √max. It runs in O(n log log n).

**Q:** Why can you start crossing off at p² rather than 2p?
<details><summary>Answer key</summary>
Any smaller multiple k·p with k < p has a prime factor smaller than p, so it was already crossed off when that smaller prime was processed.
</details>

### C3. Probability rules
Teach: P(A and B) = P(B|A)·P(A). P(A or B) = P(A) + P(B) − P(A and B). **Independent** means one event happening says nothing about the other: P(A and B) = P(A)P(B). **Mutually exclusive** means they can't both happen: P(A and B) = 0. Two events with nonzero probability can't be both.

**Q:** Pick a number from 1–10. What's P(even or ≤ 5)?
<details><summary>Answer key</summary>
P(even) = 5/10, P(≤5) = 5/10, and P(even and ≤5) = 2/10 (just 2 and 4). So 5/10 + 5/10 − 2/10 = 8/10.
</details>

### C4. How to approach brainteasers
Teach: (1) **Start talking**: interviewers grade the process. (2) **Develop rules and patterns**: write down what you know for sure. (3) **Balance the worst case**: e.g. in the 9-balls problem, split into three groups of 3. (4) **Algorithmic approaches**: base case and build, DIY.

**Q:** 9 balls, one heavier, a balance scale. What's the minimum number of weighings, and how?
<details><summary>Answer key</summary>
2. Split into three groups of 3 and weigh two of them. The heavier side contains the ball, or if they balance, the third group does. Then weigh 1 vs. 1 from that group the same way. Each weighing has 3 outcomes, so it divides the search space by 3.
</details>

---

## Problem ladder

Puzzles: **the learner must talk through a solution before any hint.** Score the reasoning, not just the final answer.

| # | Problem | Tier | Pattern | Answer (tutor only) |
|---|---|---|---|---|
| 6.1 | The Heavy Pill | ★ | math | Take i pills from bottle i and weigh once. (weight − 210 g) / 0.1 is the heavy bottle's number |
| 6.2 | Basketball | ★ | probability | Game 1 wins with p. Game 2 wins with 3p² − 2p³. Game 1 is better when p < 0.5, and they're equal at p = 0, 0.5 and 1 |
| 6.3 | Dominos | ★ | invariant | Impossible. The two removed corners are the same colour, leaving 32 of one colour and 30 of the other, and every domino covers one of each |
| 6.4 | Ants on a Triangle | ★ | probability | P(collision) = 1 − 2·(1/2)³ = 3/4. For n ants on an n-gon: 1 − (1/2)^(n−1) |
| 6.5 | Jugs of Water | ★ | search | Fill the 5, pour into the 3 (leaving 2), empty the 3, pour the 2 in, fill the 5, top up the 3. That leaves 4 in the 5-quart jug |
| 6.6 | Blue-Eyed Island | ★ | induction | If c people have blue eyes, all of them leave on night c |
| 6.7 | The Apocalypse | ★ | probability | The gender ratio stays 1:1. Each birth is an independent 50/50 event |
| 6.8 | The Egg Drop Problem | ★ | balance worst case | 14 drops. Drop the first egg at 14, 27, 39, … (step sizes shrink by 1), then go linearly with the second egg |
| 6.9 | 100 Lockers | ★ | math | Only perfect squares have an odd number of factors, so 10 lockers are open |
| 6.10 | Poison | ★ | bit-trick | Label the bottles 0–999 in binary and put bottle b on strip i if bit i of b is set. 10 strips, one round of about 7 days |

## Common pitfalls
- Rushing to an answer without explaining the reasoning.
- 6.8: solving with equal step sizes (e.g. every 10 floors) instead of balancing the worst case.
- 6.2: forgetting there are three ways to make exactly 2 of 3 shots.

## Exit quiz (≥ 3/4)
1. Primality check in O(√n): explain why it works.
2. Independent vs. mutually exclusive: define both and give an example of each.
3. Explain the balance-the-worst-case idea using the egg drop.
4. Why do perfect squares have an odd number of factors?

<details><summary>Answer key</summary>

1. Divisors pair up as (a, n/a) around √n.
2. Independent: coin flips, where P(A∧B) = P(A)P(B). Mutually exclusive: one die roll showing both 1 and 2, where P(A∧B) = 0.
3. Choose the first-egg drop points so that (drops with egg 1) + (worst-case drops with egg 2) is the same whichever interval the answer is in. That's why the step size shrinks by 1 each time.
4. Factors pair up as (d, n/d). For a perfect square, √n pairs with itself, so it's counted only once.
</details>

## Flashcards
- Sieve starts crossing off at? → **p²**
- P(A or B)? → **P(A)+P(B)−P(A and B)**
- Egg drop, 100 floors? → **14**
- Open lockers? → **perfect squares**
- Brainteaser rule 1? → **start talking**
