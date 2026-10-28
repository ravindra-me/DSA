def find_anagrams(s: str, p: str) -> list[int]:
    """Return start indices of all anagrams of p in s."""
    n, k = len(s), len(p)
    if n < k:
        return []

    p_count = [0] * 26
    window_count = [0] * 26
    ord_a = ord('a')

    for char in p:
        p_count[ord(char) - ord_a] += 1

    for i in range(k):
        window_count[ord(s[i]) - ord_a] += 1

    matches = sum(1 for i in range(26) if window_count[i] == p_count[i])
    result: list[int] = []

    if matches == 26:
        result.append(0)

    for i in range(k, n):
        in_idx = ord(s[i]) - ord_a
        out_idx = ord(s[i - k]) - ord_a

        if in_idx == out_idx:
            if matches == 26:
                result.append(i - k + 1)
            continue

        # Add incoming character
        if window_count[in_idx] == p_count[in_idx]:
            matches -= 1
        window_count[in_idx] += 1
        if window_count[in_idx] == p_count[in_idx]:
            matches += 1

        # Remove outgoing character
        if window_count[out_idx] == p_count[out_idx]:
            matches -= 1
        window_count[out_idx] -= 1
        if window_count[out_idx] == p_count[out_idx]:
            matches += 1

        if matches == 26:
            result.append(i - k + 1)

    return result
