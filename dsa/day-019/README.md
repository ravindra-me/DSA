# Day 19: Day 19: Frequency Counting

| Day | Date | Phase | Type | Difficulty | Language |
|-----|------|-------|------|------------|----------|
| 19 | 2026-10-28 | Hashing | New topic | progressive | Python 3.12 |

Frequency counting uses hash tables to summarize occurrences of items into key-count mappings in a single pass. Instead of inspecting pairwise relationships across nested loops in $O(n^2)$ time, frequency maps decouple order from multiplicity to enable $O(n)$ time analysis. This foundation enables high-speed operations like anagram validation, streaming majority identification, and linear-time bucket sorting.

## Topic

**Frequency Counting**: counters, anagram grouping, majority element, bucket by frequency

## Learning Objectives

By the end of this lesson you should be able to:

- Construct and query hash-based frequency counters in linear time
- Group equivalent collections using canonical signatures and character-count tuples
- Identify majority and plurality items using hash maps and Boyer-Moore voting
- Sort items by frequency in linear time using the bucket-sort-by-count technique
- Maintain dynamic frequency counts across sliding windows and stream updates

## Concept Explanation

### What it is

Frequency counting is the process of mapping each distinct element in a collection to the number of times it appears. In Python, this is typically represented as a dictionary (`dict`) mapping `{item: count}` or via `collections.Counter`. It converts an ordered sequence of $n$ elements into a compact set of pairs $(x, \text{count}(x))$, collapsing repeated information and allowing instant $O(1)$ lookups of element multiplicities.

### Why it exists

Without frequency counting, answering questions like 'Does string A contain the same characters as string B?' or 'Which element appears most often?' typically requires nested loops ($O(n^2)$ time) or sorting the entire dataset ($O(n \log n)$ time). Frequency counting reduces these problems to linear time ($O(n)$) and enables linear-time bucket sorting on frequencies, which are naturally bounded between $0$ and $n$.

### When to use it

Use frequency counting when the relative order of elements does not matter, but their exact counts do. Common triggers include anagram checking, finding duplicates or missing items, identifying the top-$k$ most frequent items, detecting odd/even character parity (e.g., palindrome permutations), and tracking window statistics where elements enter and leave dynamically.

### When NOT to use it

Do not use frequency counting when the sequence, relative ordering, or spatial adjacency of elements is essential (such as finding the longest contiguous increasing subarray or parsing nested parenthesis). In those scenarios, two pointers, sliding windows tracking raw positions, or stacks are needed. Additionally, if the alphabet size or key domain is strictly bounded and tiny (like ASCII letters), fixed-size arrays (`[0] * 26`) may offer lower overhead than full hash maps.

### How it works internally

1. Initialize an empty hash table (or use `collections.defaultdict(int)` / `collections.Counter`).
2. Iterate through the input sequence. For each item $x$, if $x$ is not present, set `count[x] = 1`; otherwise increment `count[x] += 1`.
3. The result is a mapping where the sum of values equals $n$, and the number of distinct keys $k \le n$.
4. To extract results: query counts directly in $O(1)$, iterate through key-count pairs in $O(k)$, or invert the mapping (group keys by their frequency into buckets from $0$ to $n$) to achieve $O(n)$ sorting without comparison sorts.

### Common mistakes

- Modifying a dictionary while iterating over its keys (use `list(counts.keys())` or iterate over an independent copy).
- Using full string sorting (`''.join(sorted(s))`) inside a hot loop instead of a 26-element tuple or count array as a hashable key.
- Failing to clean up keys when their count reaches zero in dynamic sliding windows (leaving a key with count 0 affects `len(counts)`).
- Using $O(n \log n)$ sorting to find the top $k$ frequent elements when $O(n)$ bucket-by-frequency or $O(n \log k)$ min-heap is required.
- Assuming dict ordering is preserved across all environments or operations, although standard in modern Python, algorithmic invariants should not rely on order unless explicitly intended.

### Real-world applications

- Search engines calculating term frequencies (TF) and inverse document frequencies (IDF) for relevance ranking.
- Network intrusion detection systems (IDS) tracking IP request spikes per minute to mitigate DDoS attacks.
- Compression algorithms like Huffman coding, which build prefix trees directly from symbol frequency distributions.
- Database query planners maintaining histograms of column value distributions to optimize join strategies.

## Example

### Tracing Anagram Grouping with Frequency Signatures

Suppose we want to group strings that are anagrams: `["eat", "tea", "tan", "ate", "nat", "bat"]`.

Instead of sorting each string ($O(L \log L)$ where $L$ is word length), we convert each word into a 26-element count tuple:

1. `"eat"`: count of 'a'=1, 'e'=1, 't'=1, all others 0. Key = `(1, 0, ..., 1, ..., 1)`. Map: `{key1: ["eat"]}`.
2. `"tea"`: produces the exact same count tuple `key1`. Map: `{key1: ["eat", "tea"]}`.
3. `"tan"`: 'a'=1, 'n'=1, 't'=1. Produces `key2`. Map: `{key1: ["eat", "tea"], key2: ["tan"]}`.
4. `"ate"`: matches `key1`. Map: `{key1: ["eat", "tea", "ate"], key2: ["tan"]}`.
5. `"nat"`: matches `key2`. Map: `{key1: ["eat", "tea", "ate"], key2: ["tan", "nat"]}`.
6. `"bat"`: produces `key3`. Map: `{key1: ["eat", "tea", "ate"], key2: ["tan", "nat"], key3: ["bat"]}`.

Collecting values yields: `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]` in $O(N \cdot L)$ total time.

## Visual Explanation

```text
Array: [3, 1, 4, 4, 5, 2, 6, 1, 4, 4]

Pass 1: Frequency Counter
+-----+-----+-----+-----+-----+-----+
| Key |  1  |  2  |  3  |  4  |  5  |  6  |
+-----+-----+-----+-----+-----+-----+
| Cnt |  2  |  1  |  1  |  4  |  1  |  1  |
+-----+-----+-----+-----+-----+-----+

Pass 2: Invert to Frequency Buckets (Index = Frequency, 0 to N=10)
Index (Freq):   0     1        2      3      4     5 ... 10
Buckets:       [ ]  [2,3,5,6] [1]    [ ]    [4]   [ ] ... [ ]

Read from right to left to get Top Elements:
Freq 4 -> [4]
Freq 2 -> [1]
Freq 1 -> [2, 3, 5, 6]
```

## Complexity

- **Time Complexity:** Building counter: O(n) iterating through n elements. Lookup/Update: O(1) average hash table operations. Bucket inversion: O(n + k) where k is the number of distinct keys.
- **Space Complexity:** O(k) auxiliary space, where k is the number of unique elements (bounded by n in the worst case, or by alphabet size |Σ| for strings).

When keys are bounded by a small alphabet (e.g., lowercase English letters, $|\Sigma| = 26$), space is $O(1)$ and count signatures can be compared in $O(|\Sigma|)$ time. For high-entropy keys with hash collisions, lookups degrade to $O(n)$ in the theoretical worst case, but average $O(1)$.

## Interview Perspective

1. **How do you decide between sorting the input vs using a frequency map to check for anagrams?**
   <details><summary>What a strong answer covers</summary>

   Sorting takes $O(L \log L)$ time per string of length $L$ and requires no extra dictionary memory. Frequency mapping takes $O(L + |\Sigma|)$ time and $O(|\Sigma|)$ space. If strings are long ($L \gg |\Sigma|$), counting is strictly faster. If memory is severely constrained or strings are very short ($L \le 4$), sorting avoids hash overhead.

   </details>
2. **Can we find the majority element (appearing > n/2 times) in $O(1)$ extra space?**
   <details><summary>What a strong answer covers</summary>

   Yes, using the Boyer-Moore Voting Algorithm. Maintain a candidate and a counter. Increment when you see the candidate, decrement when you see a different element. If counter drops to 0, pick the current element as the new candidate. It achieves $O(n)$ time and $O(1)$ space.

   </details>
3. **What is the optimal way to find the Top-K Frequent Elements?**
   <details><summary>What a strong answer covers</summary>

   Two primary optimal approaches: 1) Frequency map + Min-Heap of size $K$, which runs in $O(n \log K)$ time. 2) Frequency map + Bucket Sort (an array of lists where index represents frequency), which runs in $O(n)$ time and $O(n)$ space.

   </details>
4. **How do you efficiently check if a substring of length $M$ is a permutation of a pattern of length $M$?**
   <details><summary>What a strong answer covers</summary>

   Use a fixed-size sliding window of length $M$ over the string. Maintain a frequency difference counter or a `matches` variable counting how many of the 26 character counts currently match between pattern and window. Slide by adding one character on the right and removing one from the left in $O(1)$ time.

   </details>

## Exercises

Try each problem yourself before opening its solution.

| # | Problem | Difficulty | Focus | Tests | Solution |
|---|---------|------------|-------|-------|----------|
| 1 | [Valid Anagram Parity](exercises/problem-01.md) | Easy | frequency counting and balance comparison | [tests](tests/test_problem_01.py) | [solution](solutions/problem-01.md) |
| 2 | [Majority Element Identifier](exercises/problem-02.md) | Easy/Medium | majority element counting and Boyer-Moore voting | [tests](tests/test_problem_02.py) | [solution](solutions/problem-02.md) |
| 3 | [Group Anagrams by Count Signature](exercises/problem-03.md) | Medium | canonical frequency signatures as dictionary keys | [tests](tests/test_problem_03.py) | [solution](solutions/problem-03.md) |
| 4 | [Top K Frequent Elements via Bucketing](exercises/problem-04.md) | Medium/Hard | bucket sort by frequency | [tests](tests/test_problem_04.py) | [solution](solutions/problem-04.md) |
| 5 | [Minimum Window Anagram Substring](exercises/problem-05.md) | Hard | dynamic frequency matching over sliding windows | [tests](tests/test_problem_05.py) | [solution](solutions/problem-05.md) |

## How to Practice

1. Read the exercise in `exercises/`.
2. Implement it in `practice/` (a starter file with the signature is already there).
3. Run the tests against your code:

```bash
cd dsa/day-019
# run the reference solutions
python -m unittest discover -s tests -v
# test YOUR solution for problem 01 (edit practice/problem_01.py first)
DSA_SOLUTIONS_DIR=practice python -m unittest discover -s tests -p test_problem_01.py -v
```

4. Compare with the walkthrough in `solutions/`.
5. Commit and push your `practice/` files. In your fork, the **DSA Validation** workflow shows
   which of your solutions pass (see [STUDENTS.md](../../STUDENTS.md)).

---
*Concepts covered: Frequency table construction, Tuple signatures for anagram grouping, Boyer-Moore voting algorithm, Bucket sort by frequency, Sliding window frequency tracking*
