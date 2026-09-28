# Module 13: C and C++ (Ch. 12) *(optional)*

Only do this module if you'll interview in C or C++, or if the role is systems-level.

**Book:** concepts on PDF p.170–174 (`book.py section ch12`): classes, constructors and destructors, virtual functions, virtual destructors, default values, operator overloading, pointers and references, templates · questions on p.175–176 · solutions on p.434–445
**Prereqs:** 00 · **Time:** 3–4 h

## Concept checks

### C1. Virtual functions and vtables
Teach: A `virtual` method is dispatched at runtime through the object's **vtable**, a per-class table of function pointers. Without `virtual`, the call is bound at compile time to the static type.

**Q:** `Person* p = new Student(); p->aboutMe();`. Which version runs if `aboutMe` isn't virtual? And if it is?
<details><summary>Answer key</summary>
Not virtual: `Person::aboutMe`, because the static type is used. Virtual: `Student::aboutMe`, because of dynamic dispatch through the vtable.
</details>

### C2. Virtual destructors
Teach: If you delete a derived object through a base pointer and the base destructor isn't virtual, only the base destructor runs, leaking the derived class's resources.

**Q:** When must a destructor be virtual?
<details><summary>Answer key</summary>
Whenever a class is meant to be used polymorphically, i.e. objects may be deleted through a base-class pointer.
</details>

### C3. Pointers vs. references, shallow vs. deep copy
Teach: A reference can't be null and can't be reseated. A pointer can do both. A shallow copy copies the pointer values, so both objects share the same memory. A deep copy duplicates what they point to.

**Q:** Why does shallow-copying an object that owns a heap buffer cause a double free?
<details><summary>Answer key</summary>
Both copies point to the same buffer, and each destructor frees it, so the second `delete` is undefined behaviour.
</details>

### C4. Smart pointers
Teach: A reference-counted smart pointer increments a count when copied, decrements it on destruction, and frees the object when the count reaches 0. That's what `shared_ptr` does. `unique_ptr` has a single owner and can only be moved.

**Q:** What's the weakness of reference counting?
<details><summary>Answer key</summary>
Cycles. Two objects holding shared pointers to each other never reach a count of 0. Break the cycle with `weak_ptr`.
</details>

## Problem ladder

| # | Problem | Tier | Key insight |
|---|---|---|---|
| 12.1 | Last K Lines | ★ | circular buffer of K lines |
| 12.2 | Reverse String | ★ | two pointers on a null-terminated char* |
| 12.3 | Hash Table vs. STL Map | ★ | O(1) unordered vs. O(log n) ordered red-black tree |
| 12.4 | Virtual Functions | ★ | vtable, dynamic dispatch |
| 12.5 | Shallow vs. Deep Copy | ★ | shared vs. duplicated memory |
| 12.6 | Volatile | ☆ | tells the compiler the value may change unexpectedly, so don't optimise away reads |
| 12.7 | Virtual Base Class | ★ | why the base-class destructor must be virtual (see C2) |
| 12.8 | Copy Node | ☆ | deep copy of a node-based structure using a map from old node to new node |
| 12.9 | Smart Pointer | ☆ | reference count, copy constructor, assignment operator, destructor |
| 12.10 | Malloc | ☆ | over-allocate, align, and store the offset just before the returned pointer |
| 12.11 | 2D Alloc | ☆ | one malloc: an array of row pointers followed by the data block |

## Exit quiz (≥ 3/4)
1. How does dynamic dispatch work?
2. Why use a virtual destructor?
3. Name the smart pointer types and what each is for.
4. What does `volatile` do, and what doesn't it guarantee?

<details><summary>Answer key</summary>

1. Each object has a vptr pointing to its class's vtable, and the call goes through the table entry.
2. So that deleting through a base pointer runs the derived destructor.
3. `unique_ptr` for a single owner, `shared_ptr` for reference-counted shared ownership, `weak_ptr` for a non-owning pointer that breaks cycles.
4. It prevents the compiler from caching the value, so every access reads memory. It does **not** provide atomicity or thread synchronisation.
</details>
