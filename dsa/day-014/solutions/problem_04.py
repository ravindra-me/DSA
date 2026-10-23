def remove_duplicate_letters(s: str) -> str:
    """Return the lexicographically smallest subsequence containing every unique letter once."""
    last_occurrence = {char: idx for idx, char in enumerate(s)}
    stack: list[str] = []
    seen: set[str] = set()

    for idx, char in enumerate(s):
        if char in seen:
            continue

        while stack and char < stack[-1] and last_occurrence[stack[-1]] > idx:
            removed = stack.pop()
            seen.remove(removed)

        stack.append(char)
        seen.add(char)

    return "".join(stack)
