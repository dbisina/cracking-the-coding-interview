# Module 10: System Design & Scalability (Ch. 9)

**Book:** concepts on PDF p.149–156 (`book.py section ch9`): handling the questions, the 5-step design process, algorithms that scale, key concepts, considerations, and a worked example · questions on p.156–157 · solutions on p.384–407
**Prereqs:** 05 · **Time:** 6–8 h

## Objectives
1. Run a design discussion: scope → assumptions → major components → key issues → redesign.
2. Use the building blocks: horizontal vs. vertical scaling, load balancers, caching, sharding, denormalization/NoSQL, queues, and MapReduce.
3. Do back-of-envelope estimates for traffic, storage and bandwidth.
4. Talk about failures, availability vs. reliability, read-heavy vs. write-heavy workloads, and security.

## How the tutor runs design problems
The tutor plays the interviewer and **makes the learner drive**. Ask "What would you do next?" and push back with "What happens when X fails?" or "What if traffic grows 100×?". The learner draws an ASCII box diagram in `workspace/10-system-design/<id>.md`. Score each problem with the 1–4 rubric: **Scope**, **Estimation**, **Components**, **Bottlenecks & trade-offs**, **Communication**.

---

## Concept checks

### C1. The 5 steps
Teach: (1) **Scope** the problem: which features, and who uses it? (2) State **reasonable assumptions** and write them down. (3) Draw the **major components**. (4) Identify the **key issues**, i.e. the bottlenecks and hard parts. (5) **Redesign** for those key issues.

**Q:** Why state assumptions explicitly, e.g. "100M URLs a month" for TinyURL?
<details><summary>Answer key</summary>
They drive every later decision, from storage size to the number of servers to caching. Stating them lets the interviewer correct you early, and it shows you're reasoning from numbers rather than guessing.
</details>

### C2. Algorithms that scale
Teach: (1) Ask clarifying questions. (2) Pretend all the data fits on one machine and solve that. (3) Get real: how much data is there, and how do you split it? (4) Solve the problems that splitting creates.

**Q:** "Find all documents containing a list of words" across millions of documents. Outline the single-machine version, then the distributed one.
<details><summary>Answer key</summary>
Single machine: precompute an inverted index from word to a sorted list of document IDs, then intersect the lists for the query words. Distributed: shard the index by word (or by document), send the query to the relevant shards, intersect the partial results, and cache popular queries.
</details>

### C3. Scaling building blocks
Teach:
- **Vertical** scaling: a bigger machine. Simple, but it has a ceiling. **Horizontal** scaling: more machines, which needs load balancing.
- **Load balancer**: spreads requests over stateless front-end servers.
- **Denormalization and NoSQL**: avoid expensive joins at scale.
- **Sharding**: vertical (split by feature), key/hash-based (`hash(key) % N`, which makes adding servers painful; consistent hashing helps), or directory-based (a lookup table, which is flexible but a single point of failure).
- **Caching**: an in-memory key-value store in front of the database. Decide on invalidation and eviction policy.
- **Asynchronous processing and queues**: move slow work off the request path.
- **Networking metrics**: bandwidth (maximum rate), throughput (actual rate), latency (delay).
- **MapReduce**: Map emits (key, value) pairs, then Reduce aggregates each key. It's for large batch jobs.

**Q:** What's the downside of `hash(key) % N` sharding, and what fixes it?
<details><summary>Answer key</summary>
Changing N remaps almost every key, forcing a massive reshuffle. Consistent hashing (or a directory service) means only about 1/N of the keys move.
</details>

### C4. Considerations
Teach: Failures (any component can die, so plan redundancy). Availability (the % of time the system is up) vs. reliability (the probability it works correctly over time). Read-heavy workloads suggest caching and read replicas. Write-heavy workloads suggest queuing writes and sharding. Security: think about abuse.

**Q:** A social feed is read 100× more than it's written. Name 2 design choices that follow from that.
<details><summary>Answer key</summary>
Cache feeds aggressively, precompute them (fan-out on write), and add read replicas. You can accept slightly stale reads.
</details>

### C5. Back-of-envelope numbers
Teach: 1 day is about 86,400 s, roughly 10⁵. 1M requests a day is about 12 requests per second. Units: 1 KB ≈ 10³ bytes, 1 MB ≈ 10⁶, 1 GB ≈ 10⁹, 1 TB ≈ 10¹². Estimate the request rate, then storage (items × size × retention), then bandwidth.

**Q:** 100M new pastes a month, averaging 10 KB each, kept for 5 years. Estimate the storage.
<details><summary>Answer key</summary>
100M × 10 KB = 1 TB a month. Over 60 months that's about 60 TB, before replication.
</details>

---

## Problem ladder

| # | Problem | Tier | Focus |
|---|---|---|---|
| 9.2 | Social Network | ★ | shortest path between people. Bidirectional BFS, sharding users across machines, caching |
| 9.4 | Duplicate URLs | ★ | 10B URLs: estimate (about 4 TB), then split by hash across files or machines and dedupe each part |
| 9.5 | Cache | ★ | caching search results: LRU (hash map + doubly linked list), how to distribute it, invalidation |
| 9.8 | Pastebin | ★ | IDs (hashing vs. random), storage, analytics, expiry |
| 9.1 | Stock Data | ☆ | serving end-of-day prices: flat files vs. SQL vs. XML/API trade-offs |
| 9.3 | Web Crawler | ☆ | avoiding infinite loops: page signatures and priorities |
| 9.6 | Sales Rank | ☆ | best sellers by category: precompute, batch the purchase logs, update periodically |
| 9.7 | Personal Financial Manager | ○ | bank sync, categorisation, alerts, async jobs |

**Protocol:** show `book.py q 9.x` and let the learner drive for 25–35 minutes. Then compare with `book.py sol 9.x`, focusing on what they missed.

## Exit quiz (≥ 4/5)
1. The 5 design steps.
2. Horizontal vs. vertical scaling: the trade-off.
3. The 3 sharding strategies and one downside of each.
4. How an LRU cache gives O(1) get and put.
5. Estimate the QPS for 50M requests a day.

<details><summary>Answer key</summary>

1. Scope, assumptions, major components, key issues, redesign.
2. Vertical is simple but has a hard ceiling and is a single point of failure. Horizontal scales much further but needs load balancing and distributed-state handling.
3. Vertical partitioning: a single feature can still outgrow one machine. Hash-based: changing N reshuffles almost everything. Directory-based: the lookup table is a single point of failure and a bottleneck.
4. A hash map from key to linked-list node, plus a doubly linked list in recency order. Move a node to the front on access, and evict from the tail.
5. 50M / 86,400 ≈ 580 QPS on average. Plan for about 2–3× that at peak.
</details>

## Flashcards
- 1 day in seconds? → **≈ 86,400 (~10⁵)**
- LRU structure? → **hash map + doubly linked list**
- Directory sharding risk? → **single point of failure**
- Read-heavy workload? → **cache + read replicas**
- MapReduce phases? → **Map (emit k,v) → Reduce (aggregate each k)**
