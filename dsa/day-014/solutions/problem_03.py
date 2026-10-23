def find_all_anagrams(s: str, p: str) -> list[int]:
    """Find all start indices in s that form anagrams of p."""
    n, k = len(s), len(p)
    if n < k:
        return []

    p_counts = [0] * 26
    window_counts = [0] * 26
    base = ord('a')

    for char in p:
        p_counts[ord(char) - base] += 1

    for i in range(k):
        window_counts[ord(s[i]) - base] += 1

    result: list[int] = []
    if window_counts == p_counts:
        result.append(0)

    for i in range(k, n):
        window_counts[ord(s[i]) - base] += 1
        window_counts[ord(s[i - k]) - base] -= 1
        if window_counts == p_counts:
            result.append(i - k + 1)

    return result
