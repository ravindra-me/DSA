# Day 16: Day 16: Introduction to HashMaps

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 16 | 2026-10-25 | Hashing | New topic | progressive | Python 3.12 |

Until now, finding an element in an unsorted collection required an $O(n)$ linear scan, or $O(\log n)$ binary search if sorted. A HashMap breaks this trade-off by offering average $O(1)$ insertions, deletions, and lookups using hash functions. Today, we demystify how HashMaps work internally and leverage them to solve fundamental algorithmic patterns like Two-Sum.

## Topic

**HashMap**: hash functions, collisions, load factor, key-value lookup, two-sum pattern

## Learning Objectives

By the end of this lesson you should be able to:

- Explain the internal mechanics of a HashMap: hash functions, bucket indexing, collision resolution, and load factor resizing.
- Analyze the difference between average-case $O(1)$ performance and worst-case $O(n)$ degradation.
- Apply the hash-map lookup pattern (such as the Two-Sum complement technique) to turn $O(n^2)$ search problems into $O(n)$ time.
- Select appropriate immutable key types and avoid common hashing pitfalls in Python.

## Concept Explanation

### What it is

A HashMap (implemented as `dict` in Python) is an associative data structure that stores key-value pairs. Think of an array where instead of indexing via integers $0, 1, \dots, n-1$, you can index using arbitrary immutable keys (strings, tuples, numbers). It converts keys into array indices using a mathematical function called a **hash function**.

### Why it exists

In a standard dynamic array, searching for a value requires checking every element one by one ($O(n)$). If we keep the array sorted, lookup is $O(\log n)$, but insertion costs $O(n)$ due to shifting elements. A HashMap decouples the lookup cost from the collection size, yielding near-instantaneous $O(1)$ average time for read, write, and delete operations.

### When to use it

Use a HashMap whenever you need:
- Instant membership testing or frequency counting (`element -> count`).
- Finding pairs or complements without nested loops (e.g., $A + B = \text{target} \implies B = \text{target} - A$).
- Indexing items by an arbitrary attribute (e.g., group items by ID or signature).
- Caching results of repeated subproblems (memoization).

### When NOT to use it

Do not use a HashMap when:
- You need items ordered by key (use a balanced binary search tree or maintain sorted arrays instead).
- Keys are mutable (like Python `list` or `set`), which cannot be reliably hashed.
- Memory is extremely constrained; HashMaps incur an overhead factor (often 2x-4x) compared to dense arrays.
- You need to perform range queries (e.g., 'find all keys between 10 and 50').

### How it works internally

1. **Hashing**: Given a key $k$, compute integer hash code $h = \text{hash}(k)$.
2. **Bucket Mapping**: Map the hash code to a fixed array index: $\text{index} = h \pmod M$, where $M$ is the capacity of the underlying bucket array.
3. **Collision Handling**: Since two distinct keys can produce the same index (pigeonhole principle), collisions are resolved via:
   - *Separate Chaining*: Each bucket holds a linked list (or small array) of entries.
   - *Open Addressing*: Probe adjacent or pseudorandom buckets until an empty slot is found.
4. **Load Factor & Rehashing**: The load factor is $\alpha = N / M$ (items divided by bucket capacity). When $\alpha$ exceeds a threshold (e.g., $0.66$ to $0.75$), the array is resized (usually doubled), and all existing keys are rehashed into the new bucket array to prevent collision chains from growing long.

### Common mistakes

- Using mutable objects (e.g., lists) as dictionary keys, which raises a `TypeError: unhashable type` in Python.
- Assuming operations are always guaranteed $O(1)$ without considering worst-case hash collisions ($O(n)$).
- Modifying a dictionary's keys while iterating directly over it, causing a `RuntimeError: dictionary changed size during iteration`.
- Neglecting to check whether a key exists before direct indexing, causing an unhandled `KeyError` (use `.get(key, default)` or `in` operator).

### Real-world applications

- Database indexing: Hash indexes for fast point-lookups on primary or foreign keys.
- Compiler symbol tables: Resolving identifiers (variable names, functions) to memory offsets and scope metadata.
- Distributed Caching: In-memory key-value caches like Redis and Memcached.

## Example

### The Two-Sum Pattern

Given an array of numbers `nums = [2, 11, 7, 15]` and `target = 9`, find two indices whose values sum to `9`.

**Naive Approach**: Check every pair $(i, j)$ with nested loops $\to O(n^2)$.

**HashMap Approach ($O(n)$)**:
At each index $i$ with value $x$, the required number is $\text{complement} = \text{target} - x$. If $\text{complement}$ has already been seen in our map, we are done. Otherwise, save $x$ and its index in the map.

1. `i = 0, x = 2`: complement = $9 - 2 = 7$. Map is empty `{}`. Store `2 -> 0`. Map: `{2: 0}`.
2. `i = 1, x = 11`: complement = $9 - 11 = -2$. Not in map. Store `11 -> 1`. Map: `{2: 0, 11: 1}`.
3. `i = 2, x = 7`: complement = $9 - 7 = 2$. $2$ is in map with index $0$! Return `[0, 2]`.

We solved in a single pass with $O(1)$ lookup per item.

## Visual Explanation

```text
Key: "apple" ---> hash("apple") = 4328902842 ---> index = 4328902842 % 8 = 2
Key: "banana" --> hash("banana") = 8291048201 ---> index = 8291048201 % 8 = 1
Key: "cherry" --> hash("cherry") = 1092840986 ---> index = 1092840986 % 8 = 2 (COLLISION with "apple"!)

Underlying Bucket Array (Chaining):
Index
  0: [ Empty ]
  1: [ ("banana", 5) ] -> None
  2: [ ("apple", 3) ]  -> [ ("cherry", 8) ] -> None  <-- Linked List handles collision
  3: [ Empty ]
  4: [ Empty ]
  5: [ Empty ]
  6: [ Empty ]
  7: [ Empty ]
```

## Complexity

- **Time Complexity:** Insert: O(1) amortized; Lookup: O(1) average; Delete: O(1) average. Computing hash and indexing is O(1) assuming constant key length.
- **Space Complexity:** O(N) where N is the number of unique key-value pairs stored.

In the worst case (e.g. all keys produce identical bucket indices or intentional hash-flooding DoS), lookup degrades to O(N). Modern languages mitigate this with randomized seed hashing (SipHash) and tree-ification of buckets.

## Interview Perspective

1. **What happens when two different keys produce the same hash code or map to the same bucket index?**
   <details><summary>What a strong answer covers</summary>

   Explain collision resolution strategies: Separate Chaining (buckets hold linked lists or red-black trees) vs. Open Addressing (probing empty slots via linear, quadratic, or double hashing probing).

   </details>
2. **Why is the load factor important, and what happens when it is exceeded?**
   <details><summary>What a strong answer covers</summary>

   Define load factor as N / capacity. Explain that higher load factor increases collision probability, slowing operations. Resizing allocates a larger array (often 2x) and rehashes keys to maintain O(1) average access.

   </details>
3. **What makes an object 'hashable' in Python?**
   <details><summary>What a strong answer covers</summary>

   An object must have an immutable hash value throughout its lifecycle (implements __hash__) and be comparable to other objects (implements __eq__). Equal objects must have equal hash codes.

   </details>
4. **How does Python's built-in `dict` implement collision resolution and insertion order preservation?**
   <details><summary>What a strong answer covers</summary>

   Python uses open addressing with perturbation probing on a compact array. Since Python 3.6+, it maintains an index table and a dense entry array, preserving insertion order with minimal memory overhead.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Two Sum Target Difference](exercises/problem-01.md) | Easy | Complement lookup via HashMap | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Group Anagrams by Signature](exercises/problem-02.md) | Easy/Medium | Hashing composite keys / canonical representation | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Longest Consecutive Sequence](exercises/problem-03.md) | Medium | O(1) set/map lookup for connected component discovery | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Subarray Sum Divisible by K](exercises/problem-04.md) | Medium/Hard | Prefix sum with modulo hashing | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Design a Chained Hash Map with Dynamic Rehashing](exercises/problem-05.md) | Hard | Internal hash map architecture: buckets, collisions, load factor, rehashing | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-016
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Hash functions and bucket indexing, Collision resolution mechanisms, Load factor and rehashing, Complement lookup / Two-Sum pattern, Frequency counting and grouping with keys*
