# Solution 3: String Compression (Run-Length Encoding)

> Spoiler warning: try [the exercise](../exercises/problem-03.md) first.

**Difficulty:** Medium | **Concept:** String Building & In-Place Pointer Compacting

## Approach

Use a two-pointer technique (read and write pointers) to inspect consecutive runs of identical characters and overwrite the list in-place. Because a compressed run of length $L \ge 1$ occupies at most $1 + \lfloor \log_{10}(L) \rfloor + 1$ slots—which is always $\le L$—the write pointer never overtakes the read pointer.

## Thought Process

A naive approach creates a new list, scans runs of characters, appends the character and counts, and finally copies the result back. However, the problem strictly prohibits allocating extra arrays and requires an in-place $O(1)$ auxiliary space solution.

To solve this in-place, notice that for any run of $L$ identical characters:
- If $L = 1$, we write $1$ character ('c'). $1 \le 1$.
- If $L \ge 2$, we write $1$ character plus the decimal representation of $L$. For $L \in [2, 9]$, write length is $2 \le L$. For $L \in [10, 99]$, write length is $3 \le 10 \le L$, and so forth.

Since the number of characters written is always less than or equal to the run length consumed, a write index `write_idx` will never exceed the read index `read_idx`. We can safely mutate `chars` in-place as we scan across consecutive segments.

## Algorithm

1. Initialize `write_idx = 0` and `read_idx = 0`.
2. While `read_idx < len(chars)`, record the current character `char = chars[read_idx]` and find the extent of this run: advance a second pointer `run_end` until `run_end == len(chars)` or `chars[run_end] != char`.
3. Compute the run count `count = run_end - read_idx`.
4. Write `chars[write_idx] = char`, then increment `write_idx` by 1.
5. If `count > 1`, convert `count` to string digits and write each digit into `chars[write_idx]`, incrementing `write_idx` for each digit.
6. Advance `read_idx = run_end`.
7. Return `write_idx` as the new length $k$.

## Complexity Analysis

- **Time:** O(N) where N is the length of `chars`. Each character is read at most twice (by `read_idx` and `run_end`), and written at most once.
- **Space:** O(1) auxiliary space. We only use pointer indices and integer counts; the string conversion of the count takes at most 4 digits since N <= 2000.

## Edge Cases

- Single character list: `write_idx` writes the single character and outputs length 1 without adding any count.
- All unique characters: Each run length is 1, so the array is rewritten identically and no digits are appended.
- A single long run (e.g., 12 or 1000 identical characters): The count requires multiple digits ('1', '2' or '1', '0', '0', '0'), which are written sequentially.
- Non-alphabetic characters: Symbols, uppercase letters, and digits are treated uniformly as characters.

## Implementation

Source: [`solutions/problem_03.py`](../solutions/problem_03.py) · Tests: [`tests/test_problem_03.py`](../tests/test_problem_03.py)

```python
def compress_string(chars: list[str]) -> int:
    """Compress consecutive identical characters in-place and return new length."""
    write_idx = 0
    read_idx = 0
    n = len(chars)

    while read_idx < n:
        char = chars[read_idx]
        run_end = read_idx
        while run_end < n and chars[run_end] == char:
            run_end += 1

        count = run_end - read_idx
        chars[write_idx] = char
        write_idx += 1

        if count > 1:
            for digit in str(count):
                chars[write_idx] = digit
                write_idx += 1

        read_idx = run_end

    return write_idx
```
