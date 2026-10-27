# Day 18: Day 18: HashSet Essentials — Membership, Deduplication, and Fast Set Operations

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 18 | 2026-10-27 | Hashing | New topic | progressive | Python 3.12 |

A HashSet is an unordered collection of unique elements engineered for $O(1)$ average-time membership testing, insertions, and deletions. In this lesson, we explore how HashSet leverages hash functions and bucket arrays to eliminate duplicate values, detect cycles, and evaluate set operations. Mastering the HashSet transforms inefficient nested linear scans into clean, high-performance algorithms.

## Topic

**HashSet**: membership tests, deduplication, set operations, seen-before pattern

## Learning Objectives

By the end of this lesson you should be able to:

- Understand the internal mechanism of a HashSet as a key-only hash table
- Identify when to use a HashSet instead of an Array or HashMap
- Apply the seen-before pattern to identify duplicates and cycles in $O(N)$ time
- Implement core mathematical set operations (union, intersection, difference) efficiently
- Analyze average vs. worst-case time and space complexities including collisions and rehashing

## Concept Explanation

### What it is

A **HashSet** is a collection data structure that stores unique items without any guaranteed order. Think of it like a physical pouch: you can reach in and immediately answer 'Is this item in the pouch?' without having to line up or sort everything inside. Internally, a HashSet is essentially a HashMap where we only care about the keys; the values are either ignored or set to a dummy placeholder.

### Why it exists

Checking if an element exists in a standard dynamic array or linked list requires scanning through elements one by one, costing $O(N)$ time. When performed repeatedly (e.g., inside a loop), this yields a quadratic $O(N^2)$ runtime. Sorting the array improves lookups to $O(\log N)$ via binary search, but maintaining sorted order during insertions costs $O(N)$. A HashSet uses hashing to achieve $O(1)$ expected time for insertions, deletions, and membership checks simultaneously.

### When to use it

Reach for a HashSet when you encounter: (1) Membership queries ('does item $X$ exist in the collection?'), (2) Deduplication requirements ('filter out duplicate IDs/characters'), (3) 'Seen-before' patterns (tracking visited elements to detect cycles or matching pairs), or (4) Set operations like finding common elements (intersection), combined elements (union), or missing elements (difference).

### When NOT to use it

Do not use a HashSet when: (1) You need to associate a value with each key (use a **HashMap**), (2) You need to maintain insertion order or sorted order (use a list, OrderedDict, or balanced BST), (3) Elements are not hashable/immutable (e.g., Python lists or dictionaries cannot be set members directly), or (4) You need duplicate frequencies or counts (use a frequency map or multiset/Counter).

### How it works internally

1. **Hash Calculation**: An element is passed through a deterministic hash function `hash(key)`, producing an integer.
2. **Index Mapping**: The integer is mapped to a bucket index, usually using modulo: `index = hash(key) % capacity`.
3. **Collision Handling**: If two different elements hash to the same bucket index, collision resolution is used (either chaining via linked nodes/lists, or open addressing via probing sequences).
4. **Uniqueness Enforcement**: Before insertion, the set checks if the exact element is already present in the bucket (comparing both `hash` equality and equality `==`). If found, the insertion is ignored; if not found, it is added.
5. **Resizing/Rehashing**: When the load factor (number of elements / capacity) exceeds a threshold (e.g., 0.66 to 0.75), the underlying array doubles in capacity, and all elements are re-indexed to prevent long collision chains.

### Common mistakes

- Attempting to add mutable objects (such as Python lists, sets, or dicts) into a set without converting them to immutable equivalents like tuples or frozensets.
- Assuming sets maintain a deterministic sorted order or insertion order across all implementations and operations.
- Modifying an object after it has been inserted into a set, which breaks the invariant that the stored hash matches its current state.
- Iterating through a set while concurrently adding or removing elements from it, which causes runtime errors (e.g., `RuntimeError: Set changed size during iteration`).
- Using `set.intersection()` or other binary operations repeatedly inside a loop without considering that each creates a new set with $O(M)$ time and space.

### Real-world applications

- Web crawlers tracking visited URLs to avoid infinite loops and duplicate scraping.
- Spell checkers storing a dictionary of valid words to provide instant typo verification.
- Database query engines executing `SELECT DISTINCT` operations and anti-joins.
- Network firewalls and routers maintaining IP blocklists and whitelists for microsecond lookup times.

## Example

### Tracing the 'Seen-Before' Pattern

Suppose we want to find the first recurring element in the list `[4, 2, 7, 2, 5]`.

1. Initialize `seen = set()`.
2. Examine `4`: Is `4` in `seen`? False. Add `4` $\to$ `seen = {4}`.
3. Examine `2`: Is `2` in `seen`? False. Add `2` $\to$ `seen = {4, 2}`.
4. Examine `7`: Is `7` in `seen`? False. Add `7` $\to$ `seen = {4, 2, 7}`.
5. Examine `2`: Is `2` in `seen`? **True**! We found the first duplicate: `2`.

Total time: $O(N)$ single pass instead of an $O(N^2)$ nested loop check.

## Visual Explanation

```text
Array: [ 4,  2,  7,  2,  5 ]

Buckets (size 8, index = hash(x) % 8):

Step 1: Insert 4 -> hash(4)%8 = 4
  [0] | [1] | [2] | [3] | [4] -> 4 | [5] | [6] | [7]

Step 2: Insert 2 -> hash(2)%8 = 2
  [0] | [1] | [2] -> 2 | [3] | [4] -> 4 | [5] | [6] | [7]

Step 3: Insert 7 -> hash(7)%8 = 7
  [0] | [1] | [2] -> 2 | [3] | [4] -> 4 | [5] | [6] | [7] -> 7

Step 4: Check 2 -> hash(2)%8 = 2. Bucket 2 contains 2!
  Duplicate detected in O(1) time.
```

## Complexity

- **Time Complexity:** add: O(1) average, O(N) worst-case due to hash collisions. contains (in): O(1) average, O(N) worst-case. remove: O(1) average, O(N) worst-case. union/intersection: O(A + B) or O(min(A, B)) depending on operation.
- **Space Complexity:** O(N) where N is the number of unique elements stored, representing table capacity and collision structures.

Python's built-in `set` uses open addressing with perturbation probing. Worst-case $O(N)$ time per operation only happens in malicious adversarial inputs causing widespread hash collisions. In practice, lookups are reliably $O(1)$ amortized.

## Interview Perspective

1. **What is the difference between a HashSet and a HashMap under the hood?**
   <details><summary>What a strong answer covers</summary>

   Explain that a HashSet is fundamentally implemented using a HashMap's bucket array and hash function, but keys map to null/dummy values. HashSet exposes an interface for uniqueness and membership, whereas HashMap associates keys with values.

   </details>
2. **Why must elements in a HashSet be immutable/hashable?**
   <details><summary>What a strong answer covers</summary>

   Mention that an element's bucket index depends on its hash code. If an object is mutated while in the set, its hash changes, leaving it stuck in the wrong bucket and rendering it unreachable via membership checks, breaking data structure invariants.

   </details>
3. **How does `set` in Python handle hash collisions?**
   <details><summary>What a strong answer covers</summary>

   Describe open addressing with pseudorandom perturbation probing (`j = ((5*j) + 1 + perturb) & mask`). Explain that it avoids separate chaining overhead and maintains cache locality.

   </details>
4. **What are the time complexities for `set.intersection` vs `set.union`?**
   <details><summary>What a strong answer covers</summary>

   Given sets A and B with sizes |A| and |B|: intersection iterates through the smaller set and queries the larger set, taking $O(\min(|A|, |B|))$ average time. Union must add all elements from both sets, taking $O(|A| + |B|)$ average time.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Contains Duplicate](exercises/problem-01.md) | Easy | Basic membership testing and seen-before pattern | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Intersection of Two Arrays](exercises/problem-02.md) | Easy/Medium | Set deduplication and set intersection | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Happy Number](exercises/problem-03.md) | Medium | Cycle detection via a seen-before state set | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Longest Consecutive Sequence](exercises/problem-04.md) | Medium/Hard | O(1) lookups and sequence boundary detection with HashSet | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Minimum Genetic Mutation](exercises/problem-05.md) | Hard | HashSet for graph search state verification and visited tracking | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-018
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: hash-set, membership-testing, deduplication, seen-before-pattern, set-operations*
