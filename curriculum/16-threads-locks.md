# Module 16: Threads & Locks (Ch. 15)

**Book:** concepts on PDF p.186–190 (`book.py section ch15`): threads in Java (Runnable vs. extending Thread), synchronized methods and blocks, locks, deadlocks and how to prevent them · questions on p.191–192 · solutions on p.459–473
**Prereqs:** 04 · **Time:** 3–4 h

## Language note
The book uses Java. The tutor maps each idea onto the learner's language: Python (`threading.Thread`, `Lock`, `Condition`, `Semaphore`, and the GIL), JS (worker threads and the event loop), C++ (`std::thread`, `std::mutex`, `std::condition_variable`), and Go (goroutines, channels, `sync.Mutex`).

## Objectives
1. Tell a process from a thread, and explain a context switch.
2. Create threads, and protect shared state with locks or synchronized blocks.
3. State the 4 conditions for deadlock and how to break each one.
4. Coordinate threads for ordering (semaphores, conditions) and solve Dining Philosophers.

---

## Concept checks

### C1. Process vs. thread
Teach: A process has its own memory space. Threads within a process share the heap, but each has its own stack and registers. Switching between threads is cheaper than switching between processes. Communicating between processes needs IPC (pipes, sockets, shared memory).

**Q:** Why is sharing data between threads easier but also riskier than sharing it between processes?
<details><summary>Answer key</summary>
It's easier because threads share the heap directly, with no IPC. It's riskier because unsynchronised concurrent access causes race conditions.
</details>

### C2. Synchronization
Teach: A synchronized method or block, or a lock, ensures only one thread at a time runs a critical section *on the same monitor or lock object*. Two different instances have two different locks. A static synchronized method locks the class object.

**Q:** Two threads call a synchronized instance method on **two different objects**. Can they run at the same time?
<details><summary>Answer key</summary>
Yes, because each object has its own monitor. They'd be blocked from running together only if the method were static synchronized, or if both used the same object. (This is 15.6.)
</details>

### C3. Deadlock
Teach: Deadlock requires all 4 of these conditions: **mutual exclusion**, **hold and wait**, **no preemption**, and a **circular wait**. Remove any one to prevent it. The most practical fix is a **global lock ordering**, which removes circular wait.

**Q:** Why does "always acquire locks in increasing ID order" prevent deadlock?
<details><summary>Answer key</summary>
A cycle would need some thread holding a higher-ID lock while waiting for a lower-ID one, which the ordering forbids. With no circular wait, there's no deadlock.
</details>

### C4. Ordering threads
Teach: Use semaphores, condition variables or latches to force an order. For example, "second() runs only after first()": first() releases a semaphore that second() waits on.

**Q:** Three methods must run in the order first, second, third, but they're called from 3 threads in random order. How do you enforce that?
<details><summary>Answer key</summary>
Use two semaphores, s1 and s2, both starting at 0. first() runs, then releases s1. second() acquires s1, runs, then releases s2. third() acquires s2, then runs. (Locks work too, but releasing a lock from a thread that didn't acquire it is illegal in Java, so semaphores are cleaner.)
</details>

## Problem ladder

| # | Problem | Tier | Key insight |
|---|---|---|---|
| 15.1 | Thread vs. Process | ★ | see C1 |
| 15.2 | Context Switch | ★ | measure by ping-ponging between two threads using pipes or signals, and subtract the overhead |
| 15.3 | Dining Philosophers | ★ | lock ordering (pick up the lower-numbered chopstick first), or back off if the second can't be acquired |
| 15.4 | Deadlock-Free Class | ☆ | declare lock needs up front; detect cycles in a lock-order graph before granting |
| 15.5 | Call In Order | ★ | semaphores, see C4 |
| 15.6 | Synchronized Methods | ★ | the same instance blocks, different instances don't, see C2 |
| 15.7 | FizzBuzz | ☆ | 4 threads sharing a counter; each checks its predicate under a lock |

**Workspace:** the learner writes runnable concurrent code for 15.3, 15.5 and 15.7. The tutor writes a stress test that runs it many times to expose races.

## Exit quiz (≥ 4/5)
1. Process vs. thread.
2. The 4 deadlock conditions.
3. The simplest practical way to prevent deadlock.
4. Can two threads run synchronized methods on different instances at the same time?
5. How do you enforce a call order across threads?

<details><summary>Answer key</summary>

1. Separate memory vs. a shared heap. Threads are cheaper to switch and communicate through shared memory.
2. Mutual exclusion, hold and wait, no preemption, circular wait.
3. A global lock ordering.
4. Yes, unless the methods are static or share a lock.
5. Semaphores, conditions or latches.
</details>

## Flashcards
- Deadlock conditions? → **mutual exclusion, hold & wait, no preemption, circular wait**
- Break circular wait? → **global lock order**
- Threads share? → **the heap (not stacks)**
