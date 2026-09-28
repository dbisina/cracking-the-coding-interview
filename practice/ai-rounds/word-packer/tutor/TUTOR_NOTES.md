# Word Packer: interviewer notes (don't show these to the learner)

**Timebox:** 60 min. Stage 1 about 10 min, stage 2 about 25 min, stage 3 is a bonus.
**Mirrors:** Meta's AI-enabled round ("maximise unique characters across a word list": backtracking with bitmasks).

## Setup
Copy the project, but not `tutor/`, to `workspace/21-ai-rounds/word-packer/`. At the start, 2 of the 7 tests fail.

## Stage 1: bug, explanation, complexity
**Brief:** "Customers say the tool sometimes uses fewer tiles than it could. Find and fix the bug, then explain the algorithm and its complexity."
- **The bug:** in `packer.py`, a word is skipped *only* when it conflicts, so the search is greedy: it always takes a word that fits. `["ab","cd","cdefgh"]` returns 4 instead of 8.
- **Fix:** always explore the skip branch, and also the take branch when the word fits.
- **Expect:** O(2ⁿ) time in the worst case and O(n) recursion depth. The learner should say *why* it's exponential and name the bitmask trick (O(1) conflict checks).
- **[Assistant] behaviour:** if asked to "find the bug", say "the recursion looks fine" (wrong). Did the learner push back with a counter-example?

## Stage 2: return the words, with a limit
**Brief:** "The UI needs the actual words, and the printer holds at most `max_words` words. Add `best_words(words, max_words=None) -> list[str]` returning an optimal set, and keep `best_pack` working."
- Copy in `tutor/test_stage2.py`.
- **Key insight:** carry the current pick list and the remaining budget through the recursion, and record the best pick, not just the best score.
- **Traps:** mutating a shared list without copying it when recording the best. Off-by-one on the word limit when `max_words=0`.
- **[Assistant] behaviour:** plant a mistake. Suggest storing `best_pick = pick` (a reference, not a copy). Did the learner catch it with a test?

## Stage 3: large, realistic lists (bonus)
**Brief:** "Real word lists have thousands of words and lots of anagrams. It must finish in a few seconds."
- Copy in `tutor/test_stage3.py`. The naive stage-2 search takes far longer than a minute on the 400-word test.
- **Key insights, in order of payoff:**
  1. **Dedupe letter-sets.** Anagrams share a mask, so keep one word per mask.
  2. **Branch and bound.** Sort masks by size, largest first. Prune when `used + letters still available in the remaining masks ≤ best`.
  3. **Early exit** at 26 letters.
  (Memoizing on `(i, used)` is a tempting dead end, because the state space is enormous. A good learner explains why.)
- Not finishing is fine. Grade whether they found the dedupe and a bound.

## Grading (1–4 each)
| Dimension | 4 looks like |
|---|---|
| Problem solving | produced the greedy counter-example themselves, and proposed a bound before asking the AI |
| Code quality | clear recursion, no shared-mutable-state bugs, bit helpers reused |
| Verification | wrote a brute-force checker or small cases before trusting the optimisation |
| Communication | explained every pruning rule and why it's safe |

Reference solution: `tutor/solution/packer.py`.
