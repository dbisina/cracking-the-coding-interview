# Module 12: Testing (Ch. 11)

**Book:** concepts on PDF p.164–168 (`book.py section ch11`): what interviewers look for, testing a real-world object, a piece of software, a function, and troubleshooting · questions on p.169 · solutions on p.429–434
**Prereqs:** 01 · **Time:** 2 h

## Objectives
1. Show big-picture thinking: who uses the thing, and what matters most.
2. Organise test cases into categories: normal, extreme, null/illegal, and strange input.
3. Test a function methodically, and troubleshoot a live issue step by step.

---

## Concept checks

### C1. What the interviewer looks for
Teach: Big-picture understanding (who the user is and why it matters), knowing how the pieces fit together, organisation (categories rather than a random list), and practicality (reasonable, prioritised tests).

**Q:** Why do testers need to prioritise their tests?
<details><summary>Answer key</summary>
Time is finite. A crash in the checkout flow matters far more than a cosmetic bug in the settings page, so test by risk × usage.
</details>

### C2. Testing a real-world object (e.g. a pen)
Teach: Ask who uses it, for what, and under what conditions. Then cover **fault tolerance, normal use, and extremes** (temperature, surface, pressure) plus safety (children chewing it).

**Q:** Give 3 test categories for a pen meant for children.
<details><summary>Answer key</summary>
Safety (non-toxic ink, no choking hazard), durability (being dropped or chewed), and usability (washable ink, grip size, working on paper, walls or skin). Also normal writing and the length of its ink supply.
</details>

### C3. Testing software and functions
Teach: Manual vs. automated, and black-box vs. white-box. For a function: define the test cases (normal, extreme, null/illegal, strange input), define the expected result for each, then write the code. Troubleshooting: understand the scenario, break the problem into testable units, then create specific, reproducible tests.

**Q:** Test `sort(int[] array)`. List 6 cases across the categories.
<details><summary>Answer key</summary>
Normal: random values. Extreme: empty array, single element, very large array. Duplicates. Already sorted and reverse sorted. Negative numbers and MIN/MAX int values. Null input.
</details>

---

## Problem ladder

| # | Problem | Tier | Focus |
|---|---|---|---|
| 11.1 | Mistake | ★ | an unsigned counter that can never be negative gives an infinite loop |
| 11.2 | Random Crashes | ★ | form hypotheses: random variables, memory leaks, dependencies, external resources |
| 11.5 | Test a Pen | ★ | clarify first, then categorise |
| 11.6 | Test an ATM | ★ | security, concurrency, network failure, reliability |
| 11.3 | Chess Test | ○ | `canMoveTo`: extreme positions, blocked paths |
| 11.4 | No Test Tools | ○ | load-testing a web page by hand |

Run these as a conversation. The learner answers aloud, then compare with `book.py sol 11.x`.

## Exit quiz (≥ 3/4)
1. The 4 categories of test input.
2. The steps for troubleshooting a random crash.
3. What do you ask before testing a physical object?
4. Black-box vs. white-box testing?

<details><summary>Answer key</summary>

1. Normal, extreme, null/illegal, and strange input.
2. Understand the scenario, isolate the components, form hypotheses (random variables, leaks, dependencies, external resources), then reproduce and test each one.
3. Who uses it, what it's for, and under what conditions.
4. Black-box tests behaviour without looking at the internals. White-box uses the code structure to target paths.
</details>

## Flashcards
- Test categories? → **normal, extreme, null/illegal, strange**
- Random crash causes? → **random variables, memory leaks, dependencies, external resources**
