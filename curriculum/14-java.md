# Module 14: Java (Ch. 13) *(optional)*

Only do this module if you'll interview in Java.

**Book:** concepts on PDF p.177–178 (`book.py section ch13`): how to approach, overloading vs. overriding, the Collection framework · questions on p.179–180 · solutions on p.445–453
**Prereqs:** none · **Time:** 2–3 h

## Concept checks

### C1. Overloading vs. overriding
Teach: **Overloading** means the same method name with different parameters, resolved at compile time. **Overriding** means a subclass redefines a method with the same signature, resolved at runtime.

**Q:** `computeArea(Circle c)` and `computeArea(Square s)` in the same class. Which is this?
<details><summary>Answer key</summary>
Overloading.
</details>

### C2. The Collection framework
Teach: `ArrayList` is a dynamic array. `Vector` is a synchronised ArrayList. `LinkedList` is doubly linked and also works as a Deque. `HashMap` gives O(1) lookup with no ordering. `TreeMap` is a red-black tree with O(log n) and sorted keys. `LinkedHashMap` preserves insertion (or access) order.

**Q:** Which map would you use to build an LRU cache quickly, and why?
<details><summary>Answer key</summary>
`LinkedHashMap` with `accessOrder = true`, overriding `removeEldestEntry`. It keeps entries in recency order and gives O(1) operations.
</details>

### C3. final, finally, finalize
Teach: `final`: a variable that can't be reassigned, a method that can't be overridden, or a class that can't be subclassed. `finally`: a block that runs after try/catch, even when there's a `return`. `finalize`: the GC hook, now deprecated.

**Q:** Does `finally` run if the `try` block returns?
<details><summary>Answer key</summary>
Yes. It only fails to run if the JVM exits (e.g. `System.exit`) or the thread is killed.
</details>

## Problem ladder

| # | Problem | Tier | Key insight |
|---|---|---|---|
| 13.1 | Private Constructor | ★ | prevents subclassing from outside, enables Singleton or Factory; inner classes can still access it |
| 13.2 | Return from Finally | ★ | finally still runs (unless the JVM exits) |
| 13.3 | Final, etc. | ★ | see C3 |
| 13.4 | Generics vs. Templates | ★ | Java uses type erasure (one compiled class). C++ creates a new copy per type |
| 13.5 | TreeMap, HashMap, LinkedHashMap | ★ | ordering and complexity differences |
| 13.6 | Object Reflection | ☆ | inspect and invoke at runtime: frameworks, debugging, tests |
| 13.7 | Lambda Expressions | ☆ | streams: filter → map → reduce |
| 13.8 | Lambda Random | ☆ | a random subset by flipping a coin per element, using a stream filter |

## Exit quiz (≥ 3/4)
1. Overloading vs. overriding.
2. HashMap vs. TreeMap vs. LinkedHashMap.
3. How do generics differ from C++ templates?
4. When does `finally` not run?

<details><summary>Answer key</summary>

1. Overloading: same name, different parameters, resolved at compile time. Overriding: same signature in a subclass, resolved at runtime.
2. HashMap: O(1) with no order. TreeMap: O(log n) with sorted keys. LinkedHashMap: O(1) with insertion or access order.
3. Java erases type parameters, so there's a single class at runtime and primitives can't be used as type arguments. C++ instantiates separate code for each type.
4. When the JVM exits or the thread is killed.
</details>
