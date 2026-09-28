# Curriculum map

All page numbers are **PDF pages**. The printed book page is the PDF page − 12.

| # | Module | Book source | PDF pages (concepts · questions) | Problems | Est. time |
|---|---|---|---|---|---|
| 00 | [Big O](00-big-o.md) | VI | 50–71 | Book examples + VI.1–VI.12 | 4–6 h |
| 01 | [Problem-Solving Method](01-problem-solving.md) | VII | 72–93 | method drills | 2–3 h |
| 02 | [Arrays & Strings](02-arrays-strings.md) | Ch 1 | 100–101 · 102–103 | 1.1–1.9 | 5–7 h |
| 03 | [Linked Lists](03-linked-lists.md) | Ch 2 | 104–105 · 106–107 | 2.1–2.8 | 5–7 h |
| 04 | [Stacks & Queues](04-stacks-queues.md) | Ch 3 | 108–109 · 110–111 | 3.1–3.6 | 3–5 h |
| 05 | [Trees & Graphs](05-trees-graphs.md) | Ch 4 | 112–120 · 121–123 | 4.1–4.12 | 10–14 h |
| 06 | [Bit Manipulation](06-bit-manipulation.md) | Ch 5 | 124–126 · 127–128 | 5.1–5.8 | 4–6 h |
| 07 | [Math & Logic Puzzles](07-math-logic.md) | Ch 6 | 129–133 · 134–136 | 6.1–6.10 | 3–5 h |
| 08 | [Object-Oriented Design](08-oo-design.md) | Ch 7 | 137–138 · 139–141 | 7.1–7.12 | 6–8 h |
| 09 | [Recursion & DP](09-recursion-dp.md) | Ch 8 | 142–145 · 146–148 | 8.1–8.14 | 10–14 h |
| 10 | [System Design](10-system-design.md) | Ch 9 | 149–156 · 156–157 | 9.1–9.8 | 6–8 h |
| 11 | [Sorting & Searching](11-sorting-searching.md) | Ch 10 | 158–160 · 161–163 | 10.1–10.11 | 5–7 h |
| 12 | [Testing](12-testing.md) | Ch 11 | 164–168 · 169 | 11.1–11.6 | 2 h |
| 13 | [C & C++](13-cpp.md) *(optional)* | Ch 12 | 170–174 · 175–176 | 12.1–12.11 | 3–4 h |
| 14 | [Java](14-java.md) *(optional)* | Ch 13 | 177–178 · 179–180 | 13.1–13.8 | 2–3 h |
| 15 | [Databases](15-databases.md) | Ch 14 | 181–183 · 184–185 | 14.1–14.7 | 3 h |
| 16 | [Threads & Locks](16-threads-locks.md) | Ch 15 | 186–190 · 191–192 | 15.1–15.7 | 3–4 h |
| 17 | [Moderate](17-moderate.md) | Ch 16 | 193–197 | 16.1–16.26 | 12–16 h |
| 18 | [Hard](18-hard.md) | Ch 17 | 198–202 | 17.1–17.26 | 14–20 h |
| 19 | [Advanced Topics](19-advanced-topics.md) | XI–XII | 640–663 | none | 3–4 h |
| 20 | [Behavioral, Process & Offers](20-behavioral-offers.md) | I–V, VIII | 14–49, 94–98 | prep grid + AI-era questions | 2–3 h |
| 21 | [AI-Assisted Coding Round](21-ai-assisted-coding.md) **new** | not in the book | — | 3 practice projects (`practice/ai-rounds/`) | 6–10 h |
| 22 | [GenAI / LLM System Design](22-genai-system-design.md) **new** | not in the book | — | G1–G7 design problems | 6–8 h |

Solutions for Ch 1–17 are on PDF p.204–639 (`book.py sol <id>`). Hints are on PDF p.664–708 (`book.py hint <id> <n>`).

## Paths

**Standard (6–10 weeks, ~1 h/day):**
00 → 01 → 02 → 03 → 04 → 05 → 09 → 11 → 06 → 07 → 08 → 10 → 17 → 18 → **21** → 12 → 15 → 16 → 19 → **22** → 20. Do 13/14 only if you'll interview in that language.

Mix in modules 17 and 18 once 05 and 09 are mastered: one Moderate problem per session is good spacing.

**Fast Track (3 weeks or less):**
00 (skim) → 01 → 02 → 03 → 04 → 05 → 09 → 11 → the ★ problems of 17 → a few 18 ★ → 21 (if your loop has an AI-enabled round) → 20. Skip every ☆/○ problem. Run a mock interview every 3rd session from week 2 onwards.

**AI-era add-ons:**
- Your loop includes an AI-enabled coding round (Meta, Google pilot, Canva…): do Module 21 after 05 and 09, and run one AI mock a week alongside normal mocks.
- AI/ML engineer or product roles building on LLMs: do Module 22 after Module 10.
- Every path: the AI-era behavioral questions in Module 20 (Q11–14).

## Problem tiers

- ★ **Core.** Classic patterns interviewers reuse. Do all of these.
- ☆ **Stretch.** Harder, or a pattern already covered. Do these on the Standard path.
- ○ **Optional.** Niche, or mostly design discussion. Skim the solution.

## Pattern tags (used in every ladder)

`hash-map` · `two-pointer` · `runner(fast/slow)` · `sliding-window` · `prefix-sum` · `sort-first` · `binary-search` · `bfs` · `dfs` · `topo-sort` · `recursion` · `backtracking` · `memo/dp` · `greedy` · `stack` · `queue` · `heap` · `trie` · `union-find` · `bit-trick` · `math` · `in-place` · `design` · `precompute` · `divide-conquer`
