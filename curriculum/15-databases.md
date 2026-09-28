# Module 15: Databases (Ch. 14)

**Book:** concepts on PDF p.181–183 (`book.py section ch14`): SQL syntax, normalized vs. denormalized, SQL statements on a sample schema, small and large database design · questions on p.184–185 · solutions on p.453–459
**Prereqs:** none · **Time:** 3 h

## Setup (optional, recommended)
Practise the queries for real with SQLite. Python's standard library includes it, so nothing needs installing. The tutor creates `workspace/15-databases/schema.sql` with the book's Apartments, Buildings, Requests, Complexes, Tenants and AptTenants tables (the schema is on PDF p.185) plus some seed rows. The learner then runs their queries with `sqlite3` or a short Python script.

## Objectives
1. Write SELECT, JOIN (inner, left and right outer, full), GROUP BY, HAVING, subqueries, UPDATE and DELETE.
2. Explain normalization vs. denormalization and when to trade one for the other.
3. Design a small schema: identify entities, choose keys, and resolve many-to-many relationships with a junction table.
4. Explain why joins become expensive at scale and what to do about it.

---

## Concept checks

### C1. Normalization vs. denormalization
Teach: A **normalized** schema minimises redundancy: each fact is stored once and linked by foreign keys. A **denormalized** schema duplicates data to avoid joins, which gives faster reads but makes writes more complex and risks inconsistency.

**Q:** Name one reason a large site would denormalize.
<details><summary>Answer key</summary>
Joins across huge or sharded tables are slow or impossible, so you duplicate the data you read often (for example a username on every post) to serve reads with a single lookup.
</details>

### C2. Join types
Teach: **INNER** joins keep only rows that match on both sides. **LEFT OUTER** keeps every left row, with NULLs where there's no match. **RIGHT OUTER** is the mirror image. **FULL OUTER** keeps all rows from both sides.

**Q:** "List every tenant and the number of apartments they rent, including tenants with 0 apartments." Which join?
<details><summary>Answer key</summary>
A LEFT JOIN from Tenants to AptTenants, then `GROUP BY` tenant with `COUNT(AptTenants.AptID)`. Count a column from the right-hand table so tenants with no apartments get 0.
</details>

### C3. GROUP BY and HAVING
Teach: `WHERE` filters rows before grouping. `HAVING` filters the groups afterwards, so it can use aggregates.

**Q:** "Tenants renting more than one apartment." Write the query shape.
<details><summary>Answer key</summary>
`SELECT TenantID FROM AptTenants GROUP BY TenantID HAVING COUNT(*) > 1`, joined to Tenants for the names.
</details>

### C4. Small database design
Teach: (1) Handle ambiguity: what are the requirements? (2) Define the core objects, which become tables. (3) Analyse the relationships: many-to-many needs a junction table. (4) Investigate the actions and make sure the queries you'll need are easy.

**Q:** Students and courses are many-to-many. How do you model that?
<details><summary>Answer key</summary>
`Students(StudentID, ...)`, `Courses(CourseID, ...)`, and a junction table `CourseEnrollment(StudentID, CourseID, Grade, Term)` with a composite key.
</details>

## Problem ladder

| # | Problem | Tier | Key insight |
|---|---|---|---|
| 14.1 | Multiple Apartments | ★ | GROUP BY TenantID HAVING COUNT > 1, then join for the names |
| 14.2 | Open Requests | ★ | LEFT JOIN Buildings to open Requests, COUNT per building (so 0s show up) |
| 14.3 | Close All Requests | ★ | UPDATE with a subquery on the building's apartments |
| 14.4 | Joins | ★ | explain inner, outer (left, right, full) |
| 14.5 | Denormalization | ★ | pros and cons (see C1) |
| 14.6 | Entity-Relationship Diagram | ☆ | companies, people, professionals, and a many-to-many relationship with attributes |
| 14.7 | Design Grade Database | ☆ | Students, Courses, Enrollment. Query the top 10% by GPA using a ranking or percentile |

## Exit quiz (≥ 3/4)
1. WHERE vs. HAVING.
2. When does a LEFT JOIN give a different result from an INNER JOIN?
3. How do you model a many-to-many relationship?
4. One pro and one con of denormalization.

<details><summary>Answer key</summary>

1. WHERE filters rows before grouping. HAVING filters groups after aggregation.
2. When some left rows have no match: a LEFT JOIN keeps them with NULLs, and an INNER JOIN drops them.
3. With a junction table of two foreign keys, plus any attributes of the relationship.
4. Pro: faster reads with fewer joins. Con: redundant data, harder writes, and a risk of inconsistency.
</details>
