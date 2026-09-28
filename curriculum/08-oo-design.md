# Module 08: Object-Oriented Design (Ch. 7)

**Book:** concepts on PDF p.137–138 (`book.py section ch7`): approach, Singleton and Factory patterns · questions on p.139–141 · solutions on p.317–353
**Prereqs:** 01 · **Time:** 6–8 h

## Objectives
1. Follow the 4-step approach: **handle ambiguity → define core objects → analyse relationships → investigate actions**.
2. Model classes, fields and methods with sensible inheritance vs. composition choices.
3. Know Singleton and Factory Method, including the drawbacks of Singleton.
4. Talk through a design aloud, making trade-offs explicit.

## How the tutor runs design problems
Nothing is run or tested here. The learner **sketches classes in a code file** (signatures and fields, minimal bodies) and talks through the design. Grade with the rubric below instead of the §6 scores:

| Dimension | 1 | 4 |
|---|---|---|
| Clarifying questions | none | asks about scope, users and constraints before designing |
| Core objects | missing key entities | clean nouns with clear responsibilities |
| Relationships | ad hoc | explicit 1-to-many / is-a / has-a with reasons |
| Actions | vague | walks through 2–3 key flows using the objects |
| Extensibility | rigid | points out where new requirements plug in |

Map the average (rounded) back to a 0–4 score for the problem log.

---

## Concept checks

### C1. Handle ambiguity first
Teach: "Design a coffee maker" might mean an industrial machine or a home appliance. Ask about who uses it, what it does and how it's used (the 6 Ws) before drawing any classes.

**Q:** "Design a parking lot." List 4 clarifying questions.
<details><summary>Answer key</summary>
Examples: multiple levels? Vehicle types (motorcycle, car, bus) and spot sizes? Payment, and if so fixed or hourly? Reservations? Can one vehicle take several spots (e.g. a bus)? Entry and exit gates, and display boards?
</details>

### C2. Core objects and relationships
Teach: Take the nouns from the use case as candidate classes. Then decide on relationships: is-a (inheritance) vs. has-a (composition), and one-to-many vs. many-to-many. Prefer composition unless there's a real substitutable "is-a".

**Q:** For a restaurant (tables, guests, parties, orders, meals, employees, hosts), which relationships are one-to-many?
<details><summary>Answer key</summary>
A party has many guests. A table can host many parties over time, but only one at any moment. A party places many orders, and an order contains many meals. Host is-a Employee.
</details>

### C3. Singleton and Factory
Teach: **Singleton** guarantees exactly one instance (e.g. `Restaurant.getInstance()`). It's easy to misuse, because it's effectively global state and makes testing harder. **Factory Method** is a creation method that decides which concrete class to instantiate (e.g. `CardGame.createCardGame(type)`).

**Q:** Name two problems with Singletons.
<details><summary>Answer key</summary>
They're hidden global state, which couples code together. They're hard to mock in unit tests. Lazy initialisation is tricky under concurrency. They violate the single-responsibility principle by also controlling their own lifecycle.
</details>

---

## Problem ladder

| # | Problem | Tier | Focus |
|---|---|---|---|
| 7.1 | Deck of Cards | ★ | generics / inheritance (`Deck<T extends Card>`, BlackJackHand) |
| 7.2 | Call Center | ★ | escalation chain (respondent → manager → director), queues |
| 7.4 | Parking Lot | ★ | vehicle and spot sizes, levels, finding a spot |
| 7.9 | Circular Array | ★ | rotate via a head offset in O(1); implement an Iterator |
| 7.10 | Minesweeper | ★ | board, cell, expanding blanks with BFS/flood fill |
| 7.12 | Hash Table | ★ | chaining with linked lists, `hash % size`, resize |
| 7.6 | Jigsaw | ☆ | fitting edges; the matching algorithm |
| 7.7 | Chat Server | ☆ | users, conversations, status, a server-side model |
| 7.8 | Othello | ☆ | board, pieces flipping, game loop, players |
| 7.3 | Jukebox | ○ | playlist, CD, song, user |
| 7.5 | Online Book Reader | ○ | users, library, display, active book |
| 7.11 | File System | ○ | Entry → File / Directory (composite pattern) |

**Protocol:** `book.py q 7.x`, then learner clarifies, sketches, and walks through flows. Then compare with `book.py sol 7.x` and discuss. There's no single correct answer in OOD.

## Exit quiz (≥ 3/4)
1. What are the 4 steps of the OOD approach?
2. Inheritance or composition for "a Car has an Engine"? Why?
3. When is the Factory Method useful?
4. How does a circular array rotate in O(1)?

<details><summary>Answer key</summary>

1. Handle ambiguity, define core objects, analyse relationships, investigate actions.
2. Composition. A car is not an engine, and composition lets you swap engines.
3. When the concrete type to create depends on runtime input or configuration, and callers shouldn't depend on the concrete classes.
4. Keep a `head` offset and map index i to `(head + i) % n`. Rotating only moves `head`.
</details>

## Flashcards
- OOD step 1? → **handle ambiguity (who, what, how)**
- Singleton risk? → **global state, hard to test**
- Composite pattern example? → **File / Directory**
- has-a → ? → **composition**
