# Module 21: The AI-Assisted Coding Round (new; not in the book)

**Source:** not in CtCI 6th ed., which was published in 2015. This module is based on public reporting from 2025–2026 about the AI-enabled interview formats at Meta, Google, Canva and Microsoft. Formats change quickly, so **ask your recruiter for the current format** and treat the details below as a snapshot.
**Prereqs:** 01, 05, 09 and the ★ problems of 17 · **Time:** 6–10 h, including 3 practice projects

## Why this module exists

Interviews now go one of two ways:
1. **AI is banned and enforced.** Several large employers (including Google, Cisco, McKinsey and Deloitte) brought back at least one in-person round after catching candidates reading AI answers during video interviews. Amazon warned that using AI can disqualify a candidate. Everything in modules 00–20 still applies, and you need to be able to do it **without** AI.
2. **AI is allowed and graded.** Meta began piloting an "AI-enabled coding" round in October 2025. It replaces one of the two onsite coding rounds. Google is piloting AI-assisted and code-comprehension rounds for some junior and mid-level US roles, using Gemini. Canva expects candidates to use tools like Copilot, Cursor or Claude. At Meta and Microsoft, using the AI is reported to be optional.

**Rule zero: never use AI in a round where it isn't explicitly allowed.** Getting caught ends the process, and some companies now screen for it.

## The Meta format (as reported, 2025–2026)

| Aspect | Detail |
|---|---|
| Length | 60 min, of which about 5 min is orientation |
| Environment | CoderPad with three panels: file explorer, editor, and AI chat |
| AI | Chat only. It can **read** your code but **cannot edit** files, so you copy and adapt its suggestions yourself. There are several frontier models to choose from |
| Problem | **One multi-file project** that gets harder in stages, not two separate algorithm questions |
| Stage 1 | Find and fix a bug in the existing code, explain the algorithm, and state its complexity |
| Stage 2 | Implement the core feature. It's often harder than a typical LeetCode Medium and can run past 100 lines |
| Stage 3 | Optimise for much larger inputs or new constraints, which may mean switching algorithms |
| Topics seen | BFS/DFS on grids and mazes (sometimes with directional constraints), backtracking with bitmasks (e.g. choosing words to maximise unique characters), tries, greedy, and DP basics |
| Grading | **Problem solving, Code quality, Verification, Communication** |
| Reality | Candidates report the in-interview AI is *less* helpful than in practice. It seems to be limited so it won't simply hand over the fix or the solution. Several candidates got offers **without finishing stage 3** |

Reported interviewer guidance boils down to: use the AI, but show you understand the code; explain what it produced; test before relying on it.

## Google's pilot (as reported, 2026)
- A **code comprehension** round: read, debug and optimise an existing codebase, with Gemini available. Graded on problem solving, understanding the AI's limits, validating its output, ownership and communication.
- The Googleyness & Leadership round now includes a technical design conversation about your past work.
- Junior candidates get an **open-ended engineering** round instead of one traditional technical round.

## Objectives
1. **Read unfamiliar code quickly.** Map a 3–6 file project in 5 minutes: entry point, data model, and the core algorithm. Candidates call this the most important skill for the round.
2. **Decide what to delegate.** You keep the thinking: the algorithm choice, the invariants and the complexity. You hand the AI mechanical work: boilerplate, a test data generator, an idea to check, the syntax of a library call, a second opinion on a bug.
3. **Prompt precisely.** Include context, the constraint and the output shape. Ask for small diffs, not whole files.
4. **Verify everything.** Read every line the AI gives you, run the tests after each paste, and add edge-case tests. Never paste code you can't explain.
5. **Narrate.** Say why you're asking the AI, what you expect back, and what you accepted or rejected, and why.
6. **Degrade gracefully.** If the AI is unhelpful or wrong, drop it and carry on yourself. That's why modules 00–20 still matter.

---

## Concept checks

### C1. Which rounds allow AI?
**Q:** A recruiter says your onsite has "two coding rounds, one AI-enabled". How do you prepare differently for each?
<details><summary>Answer key</summary>
Round A (no AI): classic CtCI preparation, i.e. the 7 steps, from-scratch coding, and finding bugs by hand. Round B (AI): code reading speed, delegation, verification and narration, practised on multi-file projects in the actual tool (CoderPad), ideally with the same model you'd choose on the day. Ask the recruiter which models and languages are available and whether a practice pad exists.
</details>

### C2. Reading code first
Teach: Spend the first 5 minutes reading without the AI. Open the tests first (they tell you the intended behaviour), then the entry point, then the core module. Write a 3-line map: "data flows X → Y → Z, the core algorithm is in `f`, the likely hot spot is `g`."

**Q:** Why not start by asking the AI to "explain this codebase"?
<details><summary>Answer key</summary>
You'd hand over the part that's being graded most (understanding the code) and get a generic summary that might be wrong. Read it yourself first. Then use the AI to *confirm* a specific hypothesis ("does `step()` ever revisit a cell that's already marked?").
</details>

### C3. What to delegate
**Q:** Sort these into "I do it" and "AI can do it": (a) choosing BFS over DFS, (b) writing a random maze generator for tests, (c) proving an optimisation is still correct, (d) Python syntax for a heap of tuples, (e) deciding the bitmask state for memoization, (f) turning a failing test's output into a hypothesis about the bug.
<details><summary>Answer key</summary>
You: a, c, e, and f (you can ask the AI for a second opinion on f after forming your own hypothesis). AI: b and d. The pattern is that **you own decisions and correctness, and the AI does the typing and recall.**
</details>

### C4. Prompt quality
**Q:** Rewrite this prompt: "fix the bug".
<details><summary>Answer key</summary>
Something like: "In `scheduler.py`, `next_slot()` returns 10:30 for the input in `test_overlap`, but 10:00 is free. I suspect the interval merge treats touching intervals (end == start) as overlapping. Show only the changed comparison if you agree, or tell me what else could skip a free slot." A good prompt has context, the evidence, your hypothesis, and a small output shape.
</details>

### C5. Verification loop
Teach: Paste, **read it aloud**, run the tests, then add one new edge-case test. If a suggestion fails twice, stop using the AI for that sub-problem.

**Q:** The AI's optimisation makes all the tests pass in half the time. What do you still do before moving on?
<details><summary>Answer key</summary>
Explain *why* it's correct (the invariant), state its complexity, add tests for edge cases the existing suite doesn't cover (empty input, the maximum size, adversarial layouts), and check it didn't quietly change behaviour, e.g. tie-breaking or the output order.
</details>

### C6. Communication pattern
Teach: Use a three-beat narration for every AI interaction:
- **Before:** "I'm going to ask it for X because Y. I expect Z."
- **After:** "It suggested A. I'll keep B, but C is wrong because D."
- **Verify:** "Running the tests… passes. Adding a case for E."

**Q:** What's the red flag an interviewer is listening for?
<details><summary>Answer key</summary>
Outsourced thinking: pasting code you can't explain, going quiet while the AI "thinks for you", accepting large changes without reading them, or not being able to say why the solution works.
</details>

---

## Practice: AI-round simulations

Three multi-file projects are in `practice/ai-rounds/`. Each one has starter code and tests. Its `tutor/` folder holds `TUTOR_NOTES.md` (the stage briefs, the planted bug and a grading guide), the hidden stage-2 and stage-3 tests, and a reference solution. **The learner must not open `tutor/`.**

| Project | Mirrors | Stage 1 bug | Stage 2 build | Stage 3 scale |
|---|---|---|---|---|
| `maze-router` | grid BFS with directional constraints | BFS over-counts or loops | one-way tiles plus keys and doors | big grids, multiple queries |
| `word-packer` | maximise unique characters | a wrong duplicate check | backtracking with bitmasks | memoization and pruning for large word lists |
| `build-order` | dependency resolution (topological sort) | cycle detection misses a case | install order with optional dependencies | incremental updates on large graphs |

**How the tutor runs one (see AGENTS.md §5.2, "AI mock"):**
1. Copy the project, **without `tutor/`**, to `workspace/21-ai-rounds/<project>/`. The learner works on the copy. Copy in `tutor/test_stageN.py` as each stage starts.
2. Play **two roles**, and label each message clearly:
   - `[Interviewer]`: neutral. Gives the stage briefs from `tutor/TUTOR_NOTES.md` and asks for complexity and reasoning.
   - `[Assistant]`: the in-interview AI. It **answers only what's asked**, won't edit files, won't volunteer the location of the bug, and won't write a whole stage in one go. It makes a realistic mistake about once per stage (an off-by-one error, a missed edge case) so the learner has something to catch.
3. The timebox is 60 minutes. Stage 3 is a bonus.
4. Grade on the 4 Meta dimensions (1–4 each) and log them in `PROGRESS.md → Mock log`. The "Top fix" should be about AI use, e.g. "pasted without reading" or "never tested the AI's patch".

The learner can also practise with a real AI tool (Claude, ChatGPT, Gemini, Copilot) in chat-only mode: no agent editing, and copying by hand, to match the Meta constraint.

## Exit criteria
- 3 AI mocks completed, with Verification ≥ 3 and Communication ≥ 3 in at least 2 of them.
- The learner can say, for every AI-produced line in their final code, what it does and why it's correct.
- One no-AI mock (module 17 or 18) in the same week, to prove the underlying skill hasn't slipped.

## Flashcards
- The Meta AI round's 4 grading dimensions? → **problem solving, code quality, verification, communication**
- The first 5 minutes? → **read the code yourself: tests → entry point → core**
- What to delegate? → **typing and recall, never decisions or correctness**
- AI unhelpful? → **drop it and continue by hand**
- AI allowed? → **only when explicitly stated. Never otherwise**
