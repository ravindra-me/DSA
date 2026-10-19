def is_valid_brackets(s: str) -> bool:
    """Determine if the string has balanced brackets."""
    if len(s) % 2 != 0:
        return False

    matching_open = {")": "(", "}": "{", "]": "["}
    stack: list[str] = []

    for char in s:
        if char in matching_open:
            if not stack or stack[-1] != matching_open[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0
