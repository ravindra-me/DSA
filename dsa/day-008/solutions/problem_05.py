def min_window_subsequence(s1: str, s2: str) -> str:
    """Find the shortest contiguous substring of s1 containing s2 as a subsequence."""
    n1, n2 = len(s1), len(s2)
    if n2 > n1:
        return ""

    i = 0
    j = 0
    min_len = float("inf")
    best_start = -1

    while i < n1:
        if s1[i] == s2[j]:
            j += 1
            if j == n2:
                # Full match found ending at i
                end = i
                j -= 1
                # Scan backwards to find the latest valid start for this window
                while j >= 0:
                    if s1[i] == s2[j]:
                        j -= 1
                    i -= 1
                i += 1  # i is now the start index of the window

                window_len = end - i + 1
                if window_len < min_len:
                    min_len = window_len
                    best_start = i

                # Restart search from next character
                j = 0
        i += 1

    if best_start == -1:
        return ""
    return s1[best_start : best_start + int(min_len)]
